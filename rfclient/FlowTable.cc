#include <iostream>
#include <stdio.h>
#include <netinet/ether.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <sys/socket.h>

#include "ipc/RFProtocol.h"
#include "converter.h"
#include "defs.h"

#include "FlowTable.h"

using namespace std;

#define FULL_IPV4_MASK ((in_addr){ 0xffffffff })
#define FULL_CIDR_MASK 32
#define FULL_IPV6_MASK ((in6_addr){{{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }}})
#define EMPTY_MAC_ADDRESS "00:00:00:00:00:00"

struct rtnl_handle FlowTable::rthNeigh;
struct rtnl_handle FlowTable::rth;
int FlowTable::family = AF_UNSPEC;
unsigned FlowTable::groups = ~0U;
int FlowTable::llink = 0;
int FlowTable::laddr = 0;
int FlowTable::lroute = 0;
boost::thread FlowTable::HTPolling;
boost::thread FlowTable::RTPolling;
map<string, Interface> FlowTable::interfaces;
vector<uint32_t>* FlowTable::down_ports;
IPCMessageService* FlowTable::ipc;
uint64_t FlowTable::vm_id;

list<RouteEntry> FlowTable::routeTable;
list<HostEntry> FlowTable::hostTable;

// TODO: implement a way to pause the flow table updates when the VM is not associated with a valid datapath

void FlowTable::HTPollingCb() {
	rtnl_listen(&rthNeigh, FlowTable::updateHostTable, NULL);
}

void FlowTable::RTPollingCb() {
	rtnl_listen(&rth, FlowTable::updateRouteTable, NULL);
}

void FlowTable::clear() {
    FlowTable::routeTable.clear();
    FlowTable::hostTable.clear();
}

void FlowTable::start(uint64_t vm_id, map<string, Interface> interfaces, IPCMessageService* ipc, vector<uint32_t>* down_ports) {
	FlowTable::vm_id = vm_id;
	FlowTable::interfaces = interfaces;
	FlowTable::ipc = ipc;
    FlowTable::down_ports = down_ports;

	rtnl_open(&rth, RTMGRP_IPV4_MROUTE | RTMGRP_IPV4_ROUTE | RTMGRP_IPV6_MROUTE | RTMGRP_IPV6_ROUTE);
	rtnl_open(&rthNeigh, RTMGRP_NEIGH);

	HTPolling = boost::thread(&FlowTable::HTPollingCb);
	RTPolling = boost::thread(&FlowTable::RTPollingCb);
	HTPolling.detach();
	RTPolling.detach();
}

int FlowTable::updateHostTable(const struct sockaddr_nl *who, struct nlmsghdr *n, void *arg) {
	struct ndmsg *ndmsg_ptr = (struct ndmsg *) NLMSG_DATA(n);
	struct rtattr *rtattr_ptr;

	char intf[IF_NAMESIZE + 1];
	memset(intf, 0, IF_NAMESIZE + 1);

	if (if_indextoname((unsigned int) ndmsg_ptr->ndm_ifindex, (char *) intf) == NULL) {
		return 0;
	}

    /*
	if (ndmsg_ptr->ndm_state != NUD_REACHABLE) {
	    cout << "ndm_state: " << (uint16_t) ndmsg_ptr->ndm_state << endl;
		return 0;
	}
	*/

	char ip[INET_ADDRSTRLEN];
	char mac[2 * IFHWADDRLEN + 5 + 1];

	memset(ip, 0, INET_ADDRSTRLEN);
	memset(mac, 0, 2 * IFHWADDRLEN + 5 + 1);

	rtattr_ptr = (struct rtattr *) RTM_RTA(ndmsg_ptr);
	int rtmsg_len = RTM_PAYLOAD(n);

	for (; RTA_OK(rtattr_ptr, rtmsg_len); rtattr_ptr = RTA_NEXT(rtattr_ptr, rtmsg_len)) {
		switch (rtattr_ptr->rta_type) {
		case RTA_DST:
			if (inet_ntop(AF_INET, RTA_DATA(rtattr_ptr), ip, 128) == NULL)
				return 0;
			break;
		case NDA_LLADDR:
			if (strncpy(mac, ether_ntoa(((ether_addr *) RTA_DATA(rtattr_ptr))), sizeof(mac)) == NULL)
				return 0;
			break;
		default:
			break;
		}
	}

	HostEntry hentry;
	map<string, Interface>::iterator it;

	hentry.address = IPAddress(IPV4, ip);
	hentry.hwaddress = MACAddress(mac);

	it = interfaces.find(intf);
	if (it != interfaces.end())
		hentry.interface = it->second;
	if (not hentry.interface.active)
		return 0;

	switch (n->nlmsg_type) {
	    case RTM_NEWNEIGH:
		    std::cout << "netlink->RTM_NEWNEIGH: ip=" << ip << ", mac=" << mac << std::endl;
		    FlowTable::addFlowToHw(hentry);
		    // TODO: Shouldn't we check for a duplicate?
		    FlowTable::hostTable.push_back(hentry);
		    break;
	    /* TODO: enable this? It is causing serious problems. Why?
	    case RTM_DELNEIGH:
		    std::cout << "netlink->RTM_DELNEIGH: ip=" << ip << ", mac=" << mac << std::endl;
		    FlowTable::delFlowFromHw(hentry);
		    // TODO: delete from hostTable
		    break;
	    */
	}

	return 0;
}

int FlowTable::updateRouteTable(const struct sockaddr_nl *who, struct nlmsghdr *n, void *arg) {
	struct rtmsg *rtmsg_ptr = (struct rtmsg *) NLMSG_DATA(n);

	if (!((n->nlmsg_type == RTM_NEWROUTE || n->nlmsg_type == RTM_DELROUTE) && rtmsg_ptr->rtm_table == RT_TABLE_MAIN)) {
		return 0;
	}

        std::cout << "flags " << n->nlmsg_flags << "\n";

	char net[INET_ADDRSTRLEN];
	char gw[INET_ADDRSTRLEN];
	char intf[IF_NAMESIZE + 1];

	memset(net, 0, INET_ADDRSTRLEN);
	memset(gw, 0, INET_ADDRSTRLEN);
	memset(intf, 0, IF_NAMESIZE + 1);

	struct rtattr *rtattr_ptr;
	rtattr_ptr = (struct rtattr *) RTM_RTA(rtmsg_ptr);
	int rtmsg_len = RTM_PAYLOAD(n);

	for (; RTA_OK(rtattr_ptr, rtmsg_len); rtattr_ptr = RTA_NEXT(rtattr_ptr, rtmsg_len)) {
		switch (rtattr_ptr->rta_type) {
		case RTA_DST:
			inet_ntop(AF_INET, RTA_DATA(rtattr_ptr), net, 128);
			break;
		case RTA_GATEWAY:
			inet_ntop(AF_INET, RTA_DATA(rtattr_ptr), gw, 128);
			break;
		case RTA_OIF:
			if_indextoname(*((int *) RTA_DATA(rtattr_ptr)), (char *) intf);
			break;
		case RTA_MULTIPATH: {
			struct rtnexthop *rtnhp_ptr = (struct rtnexthop *) RTA_DATA(
					rtattr_ptr);
			int rtnhp_len = RTA_PAYLOAD(rtattr_ptr);

			if (rtnhp_len < (int) sizeof(*rtnhp_ptr)) {
				break;
			}

			if (rtnhp_ptr->rtnh_len > rtnhp_len) {
				break;
			}

			if_indextoname(rtnhp_ptr->rtnh_ifindex, (char *) intf);

			int attrlen = rtnhp_len - sizeof(struct rtnexthop);

			if (attrlen) {
				struct rtattr *attr = RTNH_DATA(rtnhp_ptr);

				for (; RTA_OK(attr, attrlen); attr = RTA_NEXT(attr, attrlen))
					if ((attr->rta_type == RTA_GATEWAY)) {
						inet_ntop(AF_INET, RTA_DATA(attr), gw, 128);
						break;
					}
			}
		}
			break;
		default:
			break;
		}
	}

	struct in_addr convmask;
	convmask.s_addr = htonl(~((1 << (32 - rtmsg_ptr->rtm_dst_len)) - 1));
	char mask[INET_ADDRSTRLEN];
	snprintf(mask, sizeof(mask), "%s", inet_ntoa(convmask));

	RouteEntry rentry;
	map<string, Interface>::iterator it;
	list<RouteEntry>::iterator itRoutes;

        /* Skipping routes to directly attached networks (next-hop field is blank) */
        {
                struct in_addr gwAddr;
                if (inet_aton(gw, &gwAddr) == 0)
                {
			std::cout << "discarding " << " net=" << net << ", mask=" << mask << " because no gateway\n";
                        return 0;
                }
        }

	switch (n->nlmsg_type) {
	case RTM_NEWROUTE:
		std::cout << "netlink->RTM_NEWROUTE: net=" << net << ", mask=" << mask << ", gw=" << gw << std::endl;

		// Discard if there's no gateway
		if (inet_addr(gw) == INADDR_NONE) {
                        std::cout << "discarding " << " net=" << net << ", mask=" << mask << " because no gateway\n";
			return 0;
		}

		rentry.address = IPAddress(IPV4, net);
		rentry.gateway = IPAddress(IPV4, gw);
		rentry.netmask = IPAddress(IPV4, mask);

		it = interfaces.find(intf);
		if (it != interfaces.end())
			rentry.interface = it->second;

		if (not rentry.interface.active) {
			std::cout << "discarding " << " net=" << net << ", mask=" << mask << " because interface not active\n";
			return 0;
		}

		for (itRoutes = FlowTable::routeTable.begin(); itRoutes != FlowTable::routeTable.end(); itRoutes++) {
			if (rentry == (*itRoutes)) {
				std::cout << "Duplicate route add request.\n";
				return 0;
			}
		}

		FlowTable::addFlowToHw(rentry);
		FlowTable::routeTable.push_back(rentry);
		break;
	case RTM_DELROUTE:
		std::cout << "netlink->RTM_DELROUTE: net=" << net << ", mask=" << mask << ", gw=" << gw << std::endl;

		rentry.address = IPAddress(IPV4, net);
		rentry.gateway = IPAddress(IPV4, gw);
		rentry.netmask = IPAddress(IPV4, mask);

		it = interfaces.find(intf);
		if (it != interfaces.end())
			rentry.interface = it->second;

		if (not rentry.interface.active) {
                        std::cout << "discarding " << " net=" << net << ", mask=" << mask << " because interface not active";
			return 0;
		}

		for (itRoutes = FlowTable::routeTable.begin(); itRoutes != FlowTable::routeTable.end(); itRoutes++) {
			if (rentry == (*itRoutes)) {
				FlowTable::delFlowFromHw(rentry);
				FlowTable::routeTable.remove(*itRoutes);
				return 0;
			}
		}
		break;
	}

	return 0;
}

void FlowTable::fakeReq(const char *hostAddr, const char *intf) {
	int s;
	struct arpreq req;
	struct hostent *hp;
	struct sockaddr_in *sin;

	bzero((caddr_t) & req, sizeof(req));

	sin = (struct sockaddr_in *) &req.arp_pa;
	sin->sin_family = AF_INET;
	sin->sin_addr.s_addr = inet_addr(hostAddr);

    // Cast to eliminate warning. in_addr.s_addr is uint32_t (netinet/in.h:141)
	if (sin->sin_addr.s_addr == (uint32_t) -1) {
		if (!(hp = gethostbyname(hostAddr))) {
			fprintf(stderr, "ARP: %s ", hostAddr);
			herror((char *) NULL);
			return;
		}
		bcopy((char *) hp->h_addr, (char *) &sin->sin_addr,
				sizeof(sin->sin_addr));
	}

	if ((s = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		perror("socket() failed.");
		return;
	}

	connect(s, (struct sockaddr *) sin, sizeof(struct sockaddr));
	close(s);
}

bool FlowTable::is_port_down(uint32_t port) {
    vector<uint32_t>::iterator it;
    for (it=down_ports->begin() ; it < down_ports->end(); it++)
        if (*it == port)
            return true;
    return false;
}

void FlowTable::addFlowToHw(const RouteEntry& rentry) {
    if (is_port_down(rentry.interface.port))
        return;

	list<HostEntry>::iterator iter;
	MACAddress dstMac;

	uint8_t tries = 0;
    bool found = false;

	// We need to resolve the gateway's IP in order to install a route flow.
	// The MAC address of the next-hop is required as it is used to re-write
	// the layer 2 header before forwarding the packet.
	while (tries < 50 and not found) {
		for (iter = FlowTable::hostTable.begin(); iter != FlowTable::hostTable.end(); iter++) {
			if (iter->address == rentry.gateway) {
				found = true;
				dstMac = iter->hwaddress;
				break;
			}
		}

		if (not found) {
			FlowTable::fakeReq(rentry.gateway.toString().c_str(), rentry.interface.name.c_str());
			usleep(20000);
		}
		tries++;
	}

	if (not found)
		return;

	RouteMod msg;
	msg.set_mod(RMT_ADD);
	msg.set_id(FlowTable::vm_id);

	boost::scoped_ptr<Match> ipdst;

	if(rentry.address.getVersion() == IPV6) {
		ip6_match_t ipmatch;
		ipmatch.addr = *((in6_addr*) rentry.address.toInAddr());
		ipmatch.mask = *((in6_addr*) rentry.netmask.toInAddr());

		ipdst.reset(new Match(RFMT_IPV6, &ipmatch));
	} else {
		ip_match_t ipmatch;
		ipmatch.addr = *((in_addr*) rentry.address.toInAddr());
		ipmatch.mask = *((in_addr*) rentry.netmask.toInAddr());

		ipdst.reset(new Match(RFMT_IPV4, &ipmatch));
	}

	msg.add_match(*(ipdst.get()));

	Action outport = Action(RFAT_OUTPUT, rentry.interface.port);

	uint8_t srcaddr[IFHWADDRLEN];
	rentry.interface.hwaddress.toArray(srcaddr);
	Action setdlsrc = Action(RFAT_SET_ETH_SRC, srcaddr);

	uint8_t dstaddr[IFHWADDRLEN];
	dstMac.toArray(dstaddr);
	Action setdldst = Action(RFAT_SET_ETH_DST, dstaddr);

	msg.add_action(setdlsrc);
	msg.add_action(setdldst);
	msg.add_action(outport);

	uint16_t pri = DEFAULT_PRIORITY + rentry.netmask.toCIDRMask();
	Option priority(RFOT_PRIORITY, pri);
	msg.add_option(priority);

	// Send
	FlowTable::ipc->send(RFCLIENT_RFSERVER_CHANNEL, RFSERVER_ID, msg);
}

void FlowTable::addFlowToHw(const HostEntry& hentry) {
	if (is_port_down(hentry.interface.port))
		return;

	RouteMod msg;
	msg.set_mod(RMT_ADD);
	msg.set_id(FlowTable::vm_id);

	boost::scoped_ptr<Match> ipdst;
	boost::scoped_ptr<Option> idle;

	if(hentry.address.getVersion() == IPV6) {
		ip6_match_t ipmatch;
		ipmatch.addr = *((in6_addr*) hentry.address.toInAddr());
		ipmatch.mask = FULL_IPV6_MASK;

		ipdst.reset(new Match(RFMT_IPV6, &ipmatch));
	} else {
		// RFC1122 specifies that ARP entries should timeout in ~60 seconds
		idle.reset(new Option(RFOT_IDLE_TIMEOUT, (uint16_t)60));
		msg.add_option(*(idle.get()));

		ip_match_t ipmatch;
		ipmatch.addr = *((in_addr*) hentry.address.toInAddr());
		ipmatch.mask = FULL_IPV4_MASK;

		ipdst.reset(new Match(RFMT_IPV4, &ipmatch));
	}

	msg.add_match(*(ipdst.get()));

	Action outport = Action(RFAT_OUTPUT, hentry.interface.port);

	uint8_t srcaddr[IFHWADDRLEN];
	hentry.interface.hwaddress.toArray(srcaddr);
	Action setdlsrc = Action(RFAT_SET_ETH_SRC, srcaddr);

	uint8_t dstaddr[IFHWADDRLEN];
	hentry.hwaddress.toArray(dstaddr);
	Action setdldst = Action(RFAT_SET_ETH_DST, dstaddr);

	msg.add_action(setdlsrc);
	msg.add_action(setdldst);
	msg.add_action(outport);

	uint16_t pri = DEFAULT_PRIORITY + FULL_CIDR_MASK;
	Option priority(RFOT_PRIORITY, pri);
	msg.add_option(priority);

    // Send
    FlowTable::ipc->send(RFCLIENT_RFSERVER_CHANNEL, RFSERVER_ID, msg);
}

void FlowTable::delFlowFromHw(const RouteEntry& rentry) {
	// We don't need to resolve the gateway's IP on route flow deletion.
	// The MAC address of the next-hop is useless when deleting flows.
    if (is_port_down(rentry.interface.port))
        return;

	RouteMod msg;
	msg.set_mod(RMT_DELETE);
	msg.set_id(FlowTable::vm_id);

	boost::scoped_ptr<Match> ipdst;
	if(rentry.address.getVersion() == IPV6) {
		ip6_match_t ipmatch;
		ipmatch.addr = *((in6_addr*) rentry.address.toInAddr());
		ipmatch.mask = *((in6_addr*) rentry.netmask.toInAddr());

		ipdst.reset(new Match(RFMT_IPV6, &ipmatch));
	} else {
		ip_match_t ipmatch;
		ipmatch.addr = *((in_addr*) rentry.address.toInAddr());
		ipmatch.mask = *((in_addr*) rentry.netmask.toInAddr());

		ipdst.reset(new Match(RFMT_IPV4, &ipmatch));
	}
	msg.add_match(*(ipdst.get()));

	uint8_t dstaddr[IFHWADDRLEN];
	rentry.interface.hwaddress.toArray(dstaddr);

	Action outport = Action(RFAT_OUTPUT, rentry.interface.port);

	msg.add_action(outport);

	uint16_t pri = DEFAULT_PRIORITY + rentry.netmask.toCIDRMask();
	Option priority(RFOT_PRIORITY, pri);
	msg.add_option(priority);

    // Send
    FlowTable::ipc->send(RFCLIENT_RFSERVER_CHANNEL, RFSERVER_ID, msg);
}

void FlowTable::delFlowFromHw(const HostEntry& hentry) {
    if (is_port_down(hentry.interface.port))
        return;

	RouteMod msg;
	msg.set_mod(RMT_DELETE);
	msg.set_id(FlowTable::vm_id);

	boost::scoped_ptr<Match> ipdst;
	if(hentry.address.getVersion() == IPV6) {
		ip6_match_t ipmatch;
		ipmatch.addr = *((in6_addr*) hentry.address.toInAddr());
		ipmatch.mask = FULL_IPV6_MASK;

		ipdst.reset(new Match(RFMT_IPV6, &ipmatch));
	} else {
		ip_match_t ipmatch;
		ipmatch.addr = *((in_addr*) hentry.address.toInAddr());
		ipmatch.mask = FULL_IPV4_MASK;

		ipdst.reset(new Match(RFMT_IPV4, &ipmatch));
	}
	msg.add_match(*(ipdst.get()));

	uint8_t dstaddr[IFHWADDRLEN];
	hentry.interface.hwaddress.toArray(dstaddr);

	Action outport = Action(RFAT_OUTPUT, hentry.interface.port);

	msg.add_action(outport);

	uint16_t pri = DEFAULT_PRIORITY + FULL_CIDR_MASK;
	Option priority(RFOT_PRIORITY, pri);
	msg.add_option(priority);

    // Send
    FlowTable::ipc->send(RFCLIENT_RFSERVER_CHANNEL, RFSERVER_ID, msg);
}
