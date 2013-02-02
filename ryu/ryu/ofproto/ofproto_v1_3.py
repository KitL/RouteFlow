# Copyright (C) 2012 Nippon Telegraph and Telephone Corporation.
# Copyright (C) 2012 Isaku Yamahata <yamahata at valinux co jp>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from struct import calcsize

# struct ofp_header
OFP_HEADER_PACK_STR = '!BBHI'
OFP_HEADER_SIZE = 8
assert calcsize(OFP_HEADER_PACK_STR) == OFP_HEADER_SIZE

# enum ofp_type
OFPT_HELLO = 0    # Symmetric message
OFPT_ERROR = 1    # Symmetric message
OFPT_ECHO_REQUEST = 2    # Symmetric message
OFPT_ECHO_REPLY = 3    # Symmetric message
OFPT_EXPERIMENTER = 4    # Symmetric message

OFPT_FEATURES_REQUEST = 5    # Controller/switch message
OFPT_FEATURES_REPLY = 6    # Controller/switch message
OFPT_GET_CONFIG_REQUEST = 7    # Controller/switch message
OFPT_GET_CONFIG_REPLY = 8    # Controller/switch message
OFPT_SET_CONFIG = 9    # Controller/switch message

OFPT_PACKET_IN = 10    # Async message
OFPT_FLOW_REMOVED = 11    # Async message
OFPT_PORT_STATUS = 12    # Async message

OFPT_PACKET_OUT = 13    # Controller/switch message
OFPT_FLOW_MOD = 14    # Controller/switch message
OFPT_GROUP_MOD = 15    # Controller/switch message
OFPT_PORT_MOD = 16    # Controller/switch message
OFPT_TABLE_MOD = 17    # Controller/switch message

OFPT_MULTIPART_REQUEST = 18    # Controller/switch message
OFPT_MULTIPART_REPLY = 19    # Controller/switch message

OFPT_BARRIER_REQUEST = 20    # Controller/switch message
OFPT_BARRIER_REPLY = 21    # Controller/switch message
OFPT_QUEUE_GET_CONFIG_REQUEST = 22    # Controller/switch message
OFPT_QUEUE_GET_CONFIG_REPLY = 23    # Controller/switch message

OFPT_ROLE_REQUEST = 24    # Controller/switch message
OFPT_ROLE_REPLY = 25    # Controller/switch message

OFPT_GET_ASYNC_REQUEST = 26    # Controller/switch message
OFPT_GET_ASYNC_REPLY = 27    # Controller/switch message
OFPT_SET_ASYNC = 28    # Controller/switch message

OFPT_METER_MOD = 29    # Controller/switch message

# struct ofp_port
OFP_MAX_PORT_NAME_LEN = 16
OFP_ETH_ALEN = 6
OFP_ETH_ALEN_STR = str(OFP_ETH_ALEN)
_OFP_PORT_PACK_STR = 'I4x' + OFP_ETH_ALEN_STR + 'B' + '2x' + \
                     str(OFP_MAX_PORT_NAME_LEN) + 's' + 'IIIIIIII'
OFP_PORT_PACK_STR = '!' + _OFP_PORT_PACK_STR
OFP_PORT_SIZE = 64
assert calcsize(OFP_PORT_PACK_STR) == OFP_PORT_SIZE

# enum ofp_port_config
OFPPC_PORT_DOWN = 1 << 0    # Port is administratively down.
OFPPC_NO_RECV = 1 << 2        # Drop all packets recieved by port.
OFPPC_NO_FWD = 1 << 5        # Drop packets forwarded to port.
OFPPC_NO_PACKET_IN = 1 << 6    # Do not send packet-in msgs for port.

# enum ofp_port_state
OFPPS_LINK_DOWN = 1 << 0    # No physical link present.
OFPPS_BLOCKED = 1 << 1        # Port is blocked.
OFPPS_LIVE = 1 << 2        # Live for Fast Failover Group.

# enum ofp_port_no
OFPP_MAX = 0xffffff00
OFPP_IN_PORT = 0xfffffff8       # Send the packet out the input port. This
                                # virtual port must be explicitly used
                                # in order to send back out of the input
                                # port.
OFPP_TABLE = 0xfffffff9         # Perform actions in flow table.
                                # NB: This can only be the destination
                                # port for packet-out messages.
OFPP_NORMAL = 0xfffffffa        # Process with normal L2/L3 switching.
OFPP_FLOOD = 0xfffffffb         # All physical ports except input port and
                                # those disabled by STP.
OFPP_ALL = 0xfffffffc           # All physical ports except input port.
OFPP_CONTROLLER = 0xfffffffd    # Send to controller.
OFPP_LOCAL = 0xfffffffe         # Local openflow "port".
OFPP_ANY = 0xffffffff 	        # Not associated with a physical port.

# All ones is used to indicate all queues in a port (for stats retrieval).
OFPQ_ALL = 0xffffffff

# enum ofp_port_features
OFPPF_10MB_HD = 1 << 0    # 10 Mb half-duplex rate support.
OFPPF_10MB_FD = 1 << 1    # 10 Mb full-duplex rate support.
OFPPF_100MB_HD = 1 << 2    # 100 Mb half-duplex rate support.
OFPPF_100MB_FD = 1 << 3    # 100 Mb full-duplex rate support.
OFPPF_1GB_HD = 1 << 4    # 1 Gb half-duplex rate support.
OFPPF_1GB_FD = 1 << 5    # 1 Gb full-duplex rate support.
OFPPF_10GB_FD = 1 << 6    # 10 Gb full-duplex rate support.
OFPPF_40GB_FD = 1 << 7    # 40 Gb full-duplex rate support.
OFPPF_100GB_FD = 1 << 8    # 100 Gb full-duplex rate support.
OFPPF_1TB_FD = 1 << 9    # 1 Tb full-duplex rate support.
OFPPF_OTHER = 1 << 10    # Other rate, not in the list.
OFPPF_COPPER = 1 << 11    # Copper medium.
OFPPF_FIBER = 1 << 12    # Fiber medium.
OFPPF_AUTONEG = 1 << 13    # Auto-negotiation.
OFPPF_PAUSE = 1 << 14    # Pause.
OFPPF_PAUSE_ASYM = 1 << 15    # Asymmetric pause.

# struct ofp_packet_queue
OFP_PACKET_QUEUE_PACK_STR = '!IIH6x'
OFP_PACKET_QUEUE_SIZE = 16
assert calcsize(OFP_PACKET_QUEUE_PACK_STR) == OFP_PACKET_QUEUE_SIZE

# enum ofp_queue_properties
OFPQT_MIN_RATE = 1    # Minimum datarate guaranteed.
OFPQT_MAX_RATE = 2    # Maximum datarate.
OFPQT_EXPERIMENTER = 0xffff    # Experimenter defined property.

# struct ofp_queue_prop_header
OFP_QUEUE_PROP_HEADER_PACK_STR = '!HH4x'
OFP_QUEUE_PROP_HEADER_SIZE = 8
assert calcsize(OFP_QUEUE_PROP_HEADER_PACK_STR) == OFP_QUEUE_PROP_HEADER_SIZE

# struct ofp_queue_prop_min_rate
OFP_QUEUE_PROP_MIN_RATE_PACK_STR = '!H6x'
OFP_QUEUE_PROP_MIN_RATE_SIZE = 16
assert (calcsize(OFP_QUEUE_PROP_MIN_RATE_PACK_STR) +
        OFP_QUEUE_PROP_HEADER_SIZE) == OFP_QUEUE_PROP_MIN_RATE_SIZE

# struct ofp_queue_prop_max_rate
OFP_QUEUE_PROP_MAX_RATE_PACK_STR = '!H6x'
OFP_QUEUE_PROP_MAX_RATE_SIZE = 16
assert (calcsize(OFP_QUEUE_PROP_MAX_RATE_PACK_STR) +
        OFP_QUEUE_PROP_HEADER_SIZE) == OFP_QUEUE_PROP_MAX_RATE_SIZE

# struct ofp_queue_prop_experimenter
OFP_QUEUE_PROP_EXPERIMENTER_PACK_STR = '!I4x'
OFP_QUEUE_PROP_EXPERIMENTER_SIZE = 16
assert (calcsize(OFP_QUEUE_PROP_EXPERIMENTER_PACK_STR) +
        OFP_QUEUE_PROP_HEADER_SIZE) == OFP_QUEUE_PROP_EXPERIMENTER_SIZE

# struct ofp_match
_OFP_MATCH_PACK_STR = 'HHBBBB'
OFP_MATCH_PACK_STR = '!' + _OFP_MATCH_PACK_STR
OFP_MATCH_SIZE = 8
assert calcsize(OFP_MATCH_PACK_STR) == OFP_MATCH_SIZE

# enum ofp_match_type
OFPMT_STANDARD = 0  # Deprecated
OFPMT_OXM = 1  # OpenFlow Extensible Match

# enum ofp_oxm_class
OFPXMC_NXM_0 = 0x0000  # Backward compatibility with NXM
OFPXMC_NXM_1 = 0x0001  # Backward compatibility with NXM
OFPXMC_OPENFLOW_BASIC = 0x8000  # Basic class for OpenFlow
OFPXMC_EXPERIMENTER = 0xFFFF  # Experimenter class

# enmu oxm_ofb_match_fields
OFPXMT_OFB_IN_PORT = 0  # Switch input port.
OFPXMT_OFB_IN_PHY_PORT = 1  # Switch physical input port.
OFPXMT_OFB_METADATA = 2  # Metadata passed between tables.
OFPXMT_OFB_ETH_DST = 3  # Ethernet destination address.
OFPXMT_OFB_ETH_SRC = 4  # Ethernet source address.
OFPXMT_OFB_ETH_TYPE = 5  # Ethernet frame type.
OFPXMT_OFB_VLAN_VID = 6  # VLAN id.
OFPXMT_OFB_VLAN_PCP = 7  # VLAN priority.
OFPXMT_OFB_IP_DSCP = 8  # IP DSCP (6 bits in ToS field).
OFPXMT_OFB_IP_ECN = 9  # IP ECN (2 bits in ToS field).
OFPXMT_OFB_IP_PROTO = 10  # IP protocol.
OFPXMT_OFB_IPV4_SRC = 11  # IPv4 source address.
OFPXMT_OFB_IPV4_DST = 12  # IPv4 destination address.
OFPXMT_OFB_TCP_SRC = 13  # TCP source port.
OFPXMT_OFB_TCP_DST = 14  # TCP destination port.
OFPXMT_OFB_UDP_SRC = 15  # UDP source port.
OFPXMT_OFB_UDP_DST = 16  # UDP destination port.
OFPXMT_OFB_SCTP_SRC = 17  # SCTP source port.
OFPXMT_OFB_SCTP_DST = 18  # SCTP destination port.
OFPXMT_OFB_ICMPV4_TYPE = 19  # ICMP type.
OFPXMT_OFB_ICMPV4_CODE = 20  # ICMP code.
OFPXMT_OFB_ARP_OP = 21  # ARP opcode.
OFPXMT_OFB_ARP_SPA = 22  # ARP source IPv4 address.
OFPXMT_OFB_ARP_TPA = 23  # ARP target IPv4 address.
OFPXMT_OFB_ARP_SHA = 24  # ARP source hardware address.
OFPXMT_OFB_ARP_THA = 25  # ARP target hardware address.
OFPXMT_OFB_IPV6_SRC = 26  # IPv6 source address.
OFPXMT_OFB_IPV6_DST = 27  # IPv6 destination address.
OFPXMT_OFB_IPV6_FLABEL = 28  # IPv6 Flow Label
OFPXMT_OFB_ICMPV6_TYPE = 29  # ICMPv6 type.
OFPXMT_OFB_ICMPV6_CODE = 30  # ICMPv6 code.
OFPXMT_OFB_IPV6_ND_TARGET = 31  # Target address for ND.
OFPXMT_OFB_IPV6_ND_SLL = 32  # Source link-layer for ND.
OFPXMT_OFB_IPV6_ND_TLL = 33  # Target link-layer for ND.
OFPXMT_OFB_MPLS_LABEL = 34  # MPLS label.
OFPXMT_OFB_MPLS_TC = 35  # MPLS TC.
OFPXMT_OFB_MPLS_BOS = 36  # MPLS BoS bit.
OFPXMT_OFB_PBB_ISID = 37  # PBB I-SID.
OFPXMT_OFB_TUNNEL_ID = 38  # Logical Port Metadata.
OFPXMT_OFB_IPV6_EXTHDR = 39  # IPv6 Extension Header pseudo-field

# enum ofp_vlan_id
OFPVID_PRESENT = 0x1000  # bit that indicate that a VLAN id is set.
OFPVID_NONE = 0x0000  # No VLAN id was set.

# enum ofp_ipv6exthdr_flags
OFPIEH_NONEXT = 1 << 0    # "No next header" encountered.
OFPIEH_ESP = 1 << 1    # Encrypted Sec Payload header present.
OFPIEH_AUTH = 1 << 2    # Authentication header present.
OFPIEH_DEST = 1 << 3    # 1 or 2 dest headers present.
OFPIEH_FRAG = 1 << 4    # Fragment header present.
OFPIEH_ROUTER = 1 << 5    # Router header present.
OFPIEH_HOP = 1 << 6    # Hop-by-hop header present.
OFPIEH_UNREP = 1 << 7    # Unexpected repeats encountered.
OFPIEH_UNSEQ = 1 << 8    # Unexpected sequencing encountered.

# ofp_oxm_experimenter_header
OFP_OXM_EXPERIMENTER_HEADER_PACK_STR = '!II'
OFP_OXM_EXPERIMENTER_HEADER_SIZE = 8
assert (calcsize(OFP_OXM_EXPERIMENTER_HEADER_PACK_STR) ==
        OFP_OXM_EXPERIMENTER_HEADER_SIZE)

# enum ofp_instruction_type
OFPIT_GOTO_TABLE = 1  # Setup the next table in the lookup pipeline.
OFPIT_WRITE_METADATA = 2  # Setup the metadata field for use later in
                          # pipeline.
OFPIT_WRITE_ACTIONS = 3  # Write the action(s) onto the datapath
                         # action set
OFPIT_APPLY_ACTIONS = 4  # Applies the action(s) immediately
OFPIT_CLEAR_ACTIONS = 5  # Clears all actions from the datapath action
                         # set
OFPIT_METER = 6  # Apply meter (rate limiter)
OFPIT_EXPERIMENTER = 0xFFFF   # Experimenter instruction

# struct ofp_instruction_goto_table
OFP_INSTRUCTION_GOTO_TABLE_PACK_STR = '!HHB3x'
OFP_INSTRUCTION_GOTO_TABLE_SIZE = 8
assert (calcsize(OFP_INSTRUCTION_GOTO_TABLE_PACK_STR) ==
        OFP_INSTRUCTION_GOTO_TABLE_SIZE)

# struct ofp_instruction_write_metadata
OFP_INSTRUCTION_WRITE_METADATA_PACK_STR = '!HH4xQQ'
OFP_INSTRUCTION_WRITE_METADATA_SIZE = 24
assert (calcsize(OFP_INSTRUCTION_WRITE_METADATA_PACK_STR) ==
        OFP_INSTRUCTION_WRITE_METADATA_SIZE)

# struct ofp_instruction_actions
OFP_INSTRUCTION_ACTIONS_PACK_STR = '!HH4x'
OFP_INSTRUCTION_ACTIONS_SIZE = 8
assert (calcsize(OFP_INSTRUCTION_ACTIONS_PACK_STR) ==
        OFP_INSTRUCTION_ACTIONS_SIZE)

# struct ofp_instruction_meter
OFP_INSTRUCTION_METER_PACK_STR = '!HHI'
OFP_INSTRUCTION_METER_SIZE = 8
assert calcsize(OFP_INSTRUCTION_METER_PACK_STR) == OFP_INSTRUCTION_METER_SIZE

# enum ofp_action_type
OFPAT_OUTPUT = 0    # Output to switch port.
OFPAT_COPY_TTL_OUT = 11  # Copy TTL "outwards" -- from
                         # next-to-outermost to outermost
OFPAT_COPY_TTL_IN = 12  # Copy TTL "inwards" -- from outermost to
                        # next-to-outermost
OFPAT_SET_MPLS_TTL = 15  # MPLS TTL.
OFPAT_DEC_MPLS_TTL = 16  # Decrement MPLS TTL
OFPAT_PUSH_VLAN = 17  # Push a new VLAN tag
OFPAT_POP_VLAN = 18  # Pop the outer VLAN tag
OFPAT_PUSH_MPLS = 19  # Push a new MPLS tag
OFPAT_POP_MPLS = 20  # Pop the outer MPLS tag
OFPAT_SET_QUEUE = 21  # Set queue id when outputting to a port
OFPAT_GROUP = 22  # Apply group
OFPAT_SET_NW_TTL = 23  # IP TTL.
OFPAT_DEC_NW_TTL = 24  # Decrement IP TTL.
OFPAT_SET_FIELD = 25  # Set a header field using OXM TLV format.
OFPAT_PUSH_PBB = 26  # Push a new PBB service tag (I-TAG)
OFPAT_POP_PBB = 27  # Pop the outer PBB service tag (I-TAG)
OFPAT_EXPERIMENTER = 0xffff

# struct ofp_action_header
OFP_ACTION_HEADER_PACK_STR = '!HH4x'
OFP_ACTION_HEADER_SIZE = 8
assert calcsize(OFP_ACTION_HEADER_PACK_STR) == OFP_ACTION_HEADER_SIZE

# struct ofp_action_output
OFP_ACTION_OUTPUT_PACK_STR = '!HHIH6x'
OFP_ACTION_OUTPUT_SIZE = 16
assert calcsize(OFP_ACTION_OUTPUT_PACK_STR) == OFP_ACTION_OUTPUT_SIZE

# enum ofp_controller_max_len
OFPCML_MAX = 0xffe5  # maximum max_len value which can be used to
                     # request a specific byte length.
OFPCML_NO_BUFFER = 0xffff  # indicates that no buffering should be
                           # applied and the whole packet is to be
                           # sent to the controller.

# struct ofp_action_group
OFP_ACTION_GROUP_PACK_STR = '!HHI'
OFP_ACTION_GROUP_SIZE = 8
assert calcsize(OFP_ACTION_GROUP_PACK_STR) == OFP_ACTION_GROUP_SIZE

# struct ofp_action_set_queue
OFP_ACTION_SET_QUEUE_PACK_STR = '!HHI'
OFP_ACTION_SET_QUEUE_SIZE = 8
assert calcsize(OFP_ACTION_SET_QUEUE_PACK_STR) == OFP_ACTION_SET_QUEUE_SIZE

# struct ofp_action_mpls_ttl
OFP_ACTION_MPLS_TTL_PACK_STR = '!HHB3x'
OFP_ACTION_MPLS_TTL_SIZE = 8
assert calcsize(OFP_ACTION_MPLS_TTL_PACK_STR) == OFP_ACTION_MPLS_TTL_SIZE

# struct ofp_action_nw_ttl
OFP_ACTION_NW_TTL_PACK_STR = '!HHB3x'
OFP_ACTION_NW_TTL_SIZE = 8
assert calcsize(OFP_ACTION_NW_TTL_PACK_STR) == OFP_ACTION_NW_TTL_SIZE

# struct ofp_action_push
OFP_ACTION_PUSH_PACK_STR = '!HHH2x'
OFP_ACTION_PUSH_SIZE = 8
assert calcsize(OFP_ACTION_PUSH_PACK_STR) == OFP_ACTION_PUSH_SIZE

# struct ofp_action_pop_mpls
OFP_ACTION_POP_MPLS_PACK_STR = '!HHH2x'
OFP_ACTION_POP_MPLS_SIZE = 8
assert calcsize(OFP_ACTION_POP_MPLS_PACK_STR) == OFP_ACTION_POP_MPLS_SIZE

# struct ofp_action_set_field
OFP_ACTION_SET_FIELD_PACK_STR = '!HH4x'
OFP_ACTION_SET_FIELD_SIZE = 8
assert calcsize(OFP_ACTION_SET_FIELD_PACK_STR) == OFP_ACTION_SET_FIELD_SIZE

# struct ofp_action_experimenter_header
OFP_ACTION_EXPERIMENTER_HEADER_PACK_STR = '!HHI'
OFP_ACTION_EXPERIMENTER_HEADER_SIZE = 8
assert (calcsize(OFP_ACTION_EXPERIMENTER_HEADER_PACK_STR) ==
        OFP_ACTION_EXPERIMENTER_HEADER_SIZE)

# ofp_switch_features
OFP_SWITCH_FEATURES_PACK_STR = '!QIBB2xII'
OFP_SWITCH_FEATURES_SIZE = 32
assert (calcsize(OFP_SWITCH_FEATURES_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_SWITCH_FEATURES_SIZE)

# enum ofp_capabilities
OFPC_FLOW_STATS = 1 << 0    # Flow statistics.
OFPC_TABLE_STATS = 1 << 1    # Table statistics.
OFPC_PORT_STATS = 1 << 2    # Port statistics.
OFPC_GROUP_STATS = 1 << 3    # 802.1d spanning tree.
OFPC_IP_REASM = 1 << 5        # Can reassemble IP fragments.
OFPC_QUEUE_STATS = 1 << 6    # Queue statistics.
OFPC_PORT_BLOCKED = 1 << 8    # Match IP addresses in ARP pkts.

# struct ofp_switch_config
OFP_SWITCH_CONFIG_PACK_STR = '!HH'
OFP_SWITCH_CONFIG_SIZE = 12
assert (calcsize(OFP_SWITCH_CONFIG_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_SWITCH_CONFIG_SIZE)

# enum ofp_config_flags
OFPC_FRAG_NORMAL = 0    # No special handling for fragments.
OFPC_FRAG_DROP = 1      # Drop fragments.
OFPC_FRAG_REASM = 2     # Reassemble (only if OFPC_IP_REASM set).
OFPC_FRAG_MASK = 3

# enum ofp_table
OFPTT_MAX = 0xfe
OFPTT_ALL = 0xff

# struct ofp_table_mod
OFP_TABLE_MOD_PACK_STR = '!B3xI'
OFP_TABLE_MOD_SIZE = 16
assert (calcsize(OFP_TABLE_MOD_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_TABLE_MOD_SIZE)

_OFP_FLOW_MOD_PACK_STR0 = 'QQBBHHHIIIH2x'
OFP_FLOW_MOD_PACK_STR = '!' + _OFP_FLOW_MOD_PACK_STR0 + _OFP_MATCH_PACK_STR
OFP_FLOW_MOD_PACK_STR0 = '!' + _OFP_FLOW_MOD_PACK_STR0
OFP_FLOW_MOD_SIZE = 56
assert (calcsize(OFP_FLOW_MOD_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_FLOW_MOD_SIZE)

# enum ofp_flow_mod_command
OFPFC_ADD = 0    # New flow.
OFPFC_MODIFY = 1    # Modify all matching flows.
OFPFC_MODIFY_STRICT = 2    # Modify entry strictly matching wildcards
OFPFC_DELETE = 3    # Delete all matching flows.
OFPFC_DELETE_STRICT = 4    # Strictly match wildcards and priority.

# enum ofp_flow_mod_flags
OFPFF_SEND_FLOW_REM = 1 << 0    # Send flow removed message when flow
                                # expires or is deleted.
OFPFF_CHECK_OVERLAP = 1 << 1    # Check for overlapping entries first.
OFPFF_RESET_COUNT = 1 << 2    # Reset flow packet and byte counts.
OFPFF_NO_PKT_COUNTS = 1 << 3    # Don't keep track of packet count.
OFPFF_NO_BYT_COUNTS = 1 << 4    # Don't keep track of byte count.

# struct ofp_group_mod
OFP_GROUP_MOD_PACK_STR = '!HBBI'
OFP_GROUP_MOD_SIZE = 16
assert (calcsize(OFP_GROUP_MOD_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_GROUP_MOD_SIZE)

# enum ofp_group_mod_command
OFPGC_ADD = 0  # New group.
OFPGC_MODIFY = 1  # Modify all matching groups.
OFPGC_DELETE = 2  # Delete all matching groups.

# enum ofp_group_type
OFPGT_ALL = 0  # All (multicast/broadcast) group.
OFPGT_SELECT = 1  # Select group.
OFPGT_INDIRECT = 2  # Indirect group.
OFPGT_FF = 3  # Fast failover group.

# struct ofp_bucket
OFP_BUCKET_PACK_STR = '!HHII4x'
OFP_BUCKET_SIZE = 16
assert calcsize(OFP_BUCKET_PACK_STR) == OFP_BUCKET_SIZE

# struct ofp_port_mod
OFP_PORT_MOD_PACK_STR = '!I4x' + OFP_ETH_ALEN_STR + 'B2xIII4x'
OFP_PORT_MOD_SIZE = 40
assert (calcsize(OFP_PORT_MOD_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_PORT_MOD_SIZE)

# struct ofp_meter_mod
OFP_METER_MOD_PACK_STR = '!HHI'
OFP_METER_MOD_SIZE = 16
assert (calcsize(OFP_METER_MOD_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_METER_MOD_SIZE)

# enum ofp_meter
OFPM_MAX = 0xffff0000
OFPM_SLOWPATH = 0xfffffffd  # Meter for slow datapath, if any.
OFPM_CONTROLLER = 0xfffffffe  # Meter for controller connection.
OFPM_ALL = 0xffffffff  # Represents all meters for stat requests commands.

# enum ofp_meter_mod_command
OFPMC_ADD = 0  # New meter.
OFPMC_MODIFY = 1  # Modify specified meter.
OFPMC_DELETE = 2  # Delete specified meter.

# enum ofp_meter_flags
OFPMF_KBPS = 1 << 0  # Rate value in kb/s (kilo-bit per second).
OFPMF_PKTPS = 1 << 1  # Rate value in packet/sec.
OFPMF_BURST = 1 << 2  # Do burst size.
OFPMF_STATS = 1 << 3  # Collect statistics.

# struct ofp_meter_band_header
OFP_METER_BAND_HEADER_PACK_STR = '!HHII'
OFP_METER_BAND_HEADER_SIZE = 12
assert (calcsize(OFP_METER_BAND_HEADER_PACK_STR) ==
        OFP_METER_BAND_HEADER_SIZE)

# enum ofp_meter_band_type
OFPMBT_DROP = 1  # Drop packet.
OFPMBT_DSCP_REMARK = 2  # Remark DSCP in the IP header.
OFPMBT_EXPERIMENTER = 0xFFFF  # Experimenter meter band.

# struct ofp_meter_band_drop
OFP_METER_BAND_DROP_PACK_STR = '!HHII4x'
OFP_METER_BAND_DROP_SIZE = 16
assert (calcsize(OFP_METER_BAND_DROP_PACK_STR) ==
        OFP_METER_BAND_DROP_SIZE)

# struct ofp_meter_band_dscp_remark
OFP_METER_BAND_DSCP_REMARK_PACK_STR = '!HHIIB3x'
OFP_METER_BAND_DSCP_REMARK_SIZE = 16
assert (calcsize(OFP_METER_BAND_DSCP_REMARK_PACK_STR) ==
        OFP_METER_BAND_DSCP_REMARK_SIZE)

# struct ofp_meter_band_experimenter
OFP_METER_BAND_EXPERIMENTER_PACK_STR = '!HHIII'
OFP_METER_BAND_EXPERIMENTER_SIZE = 16
assert (calcsize(OFP_METER_BAND_EXPERIMENTER_PACK_STR) ==
        OFP_METER_BAND_EXPERIMENTER_SIZE)

# struct ofp_multipart_request
OFP_MULTIPART_REQUEST_PACK_STR = '!HH4x'
OFP_MULTIPART_REQUEST_SIZE = 16
assert (calcsize(OFP_MULTIPART_REQUEST_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_MULTIPART_REQUEST_SIZE)

# enum ofp_multipart_request_flags
OFPMPF_REQ_MORE = 1 << 0  # More requests to follow.

# struct ofp_multipart_reply
OFP_MULTIPART_REPLY_PACK_STR = '!HH4x'
OFP_MULTIPART_REPLY_SIZE = 16
assert (calcsize(OFP_MULTIPART_REPLY_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_MULTIPART_REPLY_SIZE)

# enum ofp_multipart_reply_flags
OFPMPF_REPLY_MORE = 1 << 0  # More replies to follow.

# enum ofp_multipart_types
OFPMP_DESC = 0
OFPMP_FLOW = 1
OFPMP_AGGREGATE = 2
OFPMP_TABLE = 3
OFPMP_PORT_STATS = 4
OFPMP_QUEUE = 5
OFPMP_GROUP = 6
OFPMP_GROUP_DESC = 7
OFPMP_GROUP_FEATURES = 8
OFPMP_METER = 9
OFPMP_METER_CONFIG = 10
OFPMP_METER_FEATURES = 11
OFPMP_TABLE_FEATURES = 12
OFPMP_PORT_DESC = 13
OFPMP_EXPERIMENTER = 0xffff

# struct ofp_desc
DESC_STR_LEN = 256
DESC_STR_LEN_STR = str(DESC_STR_LEN)
SERIAL_NUM_LEN = 32
SERIAL_NUM_LEN_STR = str(SERIAL_NUM_LEN)
OFP_DESC_PACK_STR = '!' + \
                    DESC_STR_LEN_STR + 'c' + \
                    DESC_STR_LEN_STR + 'c' + \
                    DESC_STR_LEN_STR + 'c' + \
                    SERIAL_NUM_LEN_STR + 'c' + \
                    DESC_STR_LEN_STR + 'c'
OFP_DESC_SIZE = 1056
assert calcsize(OFP_DESC_PACK_STR) == OFP_DESC_SIZE


# struct ofp_flow_stats_request
_OFP_FLOW_STATS_REQUEST_0_PACK_STR = 'B3xII4xQQ'
OFP_FLOW_STATS_REQUEST_0_PACK_STR = '!' + _OFP_FLOW_STATS_REQUEST_0_PACK_STR
OFP_FLOW_STATS_REQUEST_0_SIZE = 32
assert (calcsize(OFP_FLOW_STATS_REQUEST_0_PACK_STR) ==
        OFP_FLOW_STATS_REQUEST_0_SIZE)
OFP_FLOW_STATS_REQUEST_PACK_STR = (OFP_FLOW_STATS_REQUEST_0_PACK_STR +
                                   _OFP_MATCH_PACK_STR)
OFP_FLOW_STATS_REQUEST_SIZE = 40
assert (calcsize(OFP_FLOW_STATS_REQUEST_PACK_STR) ==
        OFP_FLOW_STATS_REQUEST_SIZE)

# struct ofp_flow_stats
_OFP_FLOW_STATS_0_PACK_STR = 'HBxIIHHHH4xQQQ'
OFP_FLOW_STATS_0_PACK_STR = '!' + _OFP_FLOW_STATS_0_PACK_STR
OFP_FLOW_STATS_0_SIZE = 48
assert calcsize(OFP_FLOW_STATS_0_PACK_STR) == OFP_FLOW_STATS_0_SIZE
OFP_FLOW_STATS_PACK_STR = (OFP_FLOW_STATS_0_PACK_STR +
                           _OFP_MATCH_PACK_STR)
OFP_FLOW_STATS_SIZE = 56
assert calcsize(OFP_FLOW_STATS_PACK_STR) == OFP_FLOW_STATS_SIZE

# struct ofp_flow_stats_request
_OFP_AGGREGATE_STATS_REQUEST_0_PACK_STR = 'B3xII4xQQ'
OFP_AGGREGATE_STATS_REQUEST_0_PACK_STR = '!' + \
    _OFP_AGGREGATE_STATS_REQUEST_0_PACK_STR
OFP_AGGREGATE_STATS_REQUEST_0_SIZE = 32
assert (calcsize(OFP_AGGREGATE_STATS_REQUEST_0_PACK_STR) ==
        OFP_AGGREGATE_STATS_REQUEST_0_SIZE)
OFP_AGGREGATE_STATS_REQUEST_PACK_STR = \
    OFP_AGGREGATE_STATS_REQUEST_0_PACK_STR + _OFP_MATCH_PACK_STR
OFP_AGGREGATE_STATS_REQUEST_SIZE = 40
assert (calcsize(OFP_AGGREGATE_STATS_REQUEST_PACK_STR) ==
        OFP_AGGREGATE_STATS_REQUEST_SIZE)

# struct ofp_aggregate_stats_request
OFP_AGGREGATE_STATS_REQUEST_PACK_STR = '!B3xII4xQQ' + _OFP_MATCH_PACK_STR
OFP_AGGREGATE_STATS_REQUEST_SIZE = 40
assert (calcsize(OFP_AGGREGATE_STATS_REQUEST_PACK_STR) ==
        OFP_AGGREGATE_STATS_REQUEST_SIZE)

# struct ofp_aggregate_stats_reply
OFP_AGGREGATE_STATS_REPLY_PACK_STR = '!QQI4x'
OFP_AGGREGATE_STATS_REPLY_SIZE = 24
assert (calcsize(OFP_AGGREGATE_STATS_REPLY_PACK_STR) ==
        OFP_AGGREGATE_STATS_REPLY_SIZE)

# struct ofp_table_stats
OFP_TABLE_STATS_PACK_STR = '!B3xIQQ'
OFP_TABLE_STATS_SIZE = 24
assert calcsize(OFP_TABLE_STATS_PACK_STR) == OFP_TABLE_STATS_SIZE

# struct ofp_table_features
OFP_MAX_TABLE_NAME_LEN = 32
OFP_MAX_TABLE_NAME_LEN_STR = str(OFP_MAX_TABLE_NAME_LEN)
OFP_TABLE_FEATURES_PACK_STR = '!HB5x' + OFP_MAX_TABLE_NAME_LEN_STR + \
                              'c' + 'QQII'
OFP_TABLE_FEATURES_SIZE = 64
assert (calcsize(OFP_TABLE_FEATURES_PACK_STR) ==
        OFP_TABLE_FEATURES_SIZE)

# enum ofp_table_feature_prop_type
OFPTFPT_INSTRUCTIONS = 0
OFPTFPT_INSTRUCTIONS_MISS = 1
OFPTFPT_NEXT_TABLES = 2
OFPTFPT_NEXT_TABLES_MISS = 3
OFPTFPT_WRITE_ACTIONS = 4
OFPTFPT_WRITE_ACTIONS_MISS = 5
OFPTFPT_APPLY_ACTIONS = 6
OFPTFPT_APPLY_ACTIONS_MISS = 7
OFPTFPT_MATCH = 8
OFPTFPT_WILDCARDS = 10
OFPTFPT_WRITE_SETFIELD = 12
OFPTFPT_WRITE_SETFIELD_MISS = 13
OFPTFPT_APPLY_SETFIELD = 14
OFPTFPT_APPLY_SETFIELD_MISS = 15
OFPTFPT_EXPERIMENTER = 0xFFFE
OFPTFPT_EXPERIMENTER_MISS = 0xFFFF

# struct ofp_table_feature_prop_instructions
OFP_TABLE_FEATURE_PROP_INSTRUCTIONS_PACK_STR = '!HH'
OFP_TABLE_FEATURE_PROP_INSTRUCTIONS_SIZE = 4
assert (calcsize(OFP_TABLE_FEATURE_PROP_INSTRUCTIONS_PACK_STR) ==
        OFP_TABLE_FEATURE_PROP_INSTRUCTIONS_SIZE)

# struct ofp_table_feature_prop_next_tables
OFP_TABLE_FEATURE_PROP_NEXT_TABLES_PACK_STR = '!HH'
OFP_TABLE_FEATURE_PROP_NEXT_TABLES_SIZE = 4
assert (calcsize(OFP_TABLE_FEATURE_PROP_NEXT_TABLES_PACK_STR) ==
        OFP_TABLE_FEATURE_PROP_NEXT_TABLES_SIZE)

# struct ofp_table_feature_prop_actions
OFP_TABLE_FEATURE_PROP_ACTIONS_PACK_STR = '!HH'
OFP_TABLE_FEATURE_PROP_ACTIONS_SIZE = 4
assert (calcsize(OFP_TABLE_FEATURE_PROP_ACTIONS_PACK_STR) ==
        OFP_TABLE_FEATURE_PROP_ACTIONS_SIZE)

# struct ofp_table_feature_prop_oxm
OFP_TABLE_FEATURE_PROP_OXM_PACK_STR = '!HH'
OFP_TABLE_FEATURE_PROP_OXM_SIZE = 4
assert (calcsize(OFP_TABLE_FEATURE_PROP_OXM_PACK_STR) ==
        OFP_TABLE_FEATURE_PROP_OXM_SIZE)

# struct ofp_port_stats_reuqest
OFP_PORT_STATS_REQUEST_PACK_STR = '!I4x'
OFP_PORT_STATS_REQUEST_SIZE = 8
assert (calcsize(OFP_PORT_STATS_REQUEST_PACK_STR) ==
        OFP_PORT_STATS_REQUEST_SIZE)

# struct ofp_port_stats
OFP_PORT_STATS_PACK_STR = '!I4xQQQQQQQQQQQQII'
OFP_PORT_STATS_SIZE = 112
assert calcsize(OFP_PORT_STATS_PACK_STR) == OFP_PORT_STATS_SIZE

# struct ofp_queue_stats_request
OFP_QUEUE_STATS_REQUEST_PACK_STR = '!II'
OFP_QUEUE_STATS_REQUEST_SIZE = 8
assert (calcsize(OFP_QUEUE_STATS_REQUEST_PACK_STR) ==
        OFP_QUEUE_STATS_REQUEST_SIZE)

# struct ofp_queue_stats
OFP_QUEUE_STATS_PACK_STR = '!IIQQQII'
OFP_QUEUE_STATS_SIZE = 40
assert calcsize(OFP_QUEUE_STATS_PACK_STR) == OFP_QUEUE_STATS_SIZE

# struct ofp_group_stats_request
OFP_GROUP_STATS_REQUEST_PACK_STR = '!I4x'
OFP_GROUP_STATS_REQUEST_SIZE = 8
assert (calcsize(OFP_GROUP_STATS_REQUEST_PACK_STR) ==
        OFP_GROUP_STATS_REQUEST_SIZE)

# struct ofp_group_stats
OFP_GROUP_STATS_PACK_STR = '!H2xII4xQQII'
OFP_GROUP_STATS_SIZE = 40
assert calcsize(OFP_GROUP_STATS_PACK_STR) == OFP_GROUP_STATS_SIZE

# struct ofp_bucket_counter
OFP_BUCKET_COUNTER_PACK_STR = '!QQ'
OFP_BUCKET_COUNTER_SIZE = 16
assert calcsize(OFP_BUCKET_COUNTER_PACK_STR) == OFP_BUCKET_COUNTER_SIZE

# struct ofp_group_desc_stats
OFP_GROUP_DESC_STATS_PACK_STR = '!HBBI'
OFP_GROUP_DESC_STATS_SIZE = 8
assert calcsize(OFP_GROUP_DESC_STATS_PACK_STR) == OFP_GROUP_DESC_STATS_SIZE

# struct ofp_group_features
OFP_GROUP_FEATURES_PACK_STR = '!II4I4I'
OFP_GROUP_FEATURES_SIZE = 40
assert calcsize(OFP_GROUP_FEATURES_PACK_STR) == OFP_GROUP_FEATURES_SIZE

# enum ofp_group_capabilities
OFPGFC_SELECT_WEIGHT = 1 << 0  # Support weight for select groups.
OFPGFC_SELECT_LIVENESS = 1 << 1  # Support liveness for select groups.
OFPGFC_CHAINING = 1 << 2  # Support chaining groups.
OFPGFC_CHAINING_CHECKS = 1 << 3  # Check chaining for loops and delete

# struct ofp_meter_multipart_request
OFP_METER_MULTIPART_REQUEST_PACK_STR = '!I4B'
OFP_METER_MULTIPART_REQUEST_SIZE = 8
assert (calcsize(OFP_METER_MULTIPART_REQUEST_PACK_STR) ==
        OFP_METER_MULTIPART_REQUEST_SIZE)

# struct ofp_meter_stats
OFP_METER_STATS_PACK_STR = '!IH6xIQQII'
OFP_METER_STATS_SIZE = 40
assert calcsize(OFP_METER_STATS_PACK_STR) == OFP_METER_STATS_SIZE

# struct ofp_meter_band_stats
OFP_METER_BAND_STATS_PACK_STR = '!QQ'
OFP_METER_BAND_STATS_SIZE = 16
assert (calcsize(OFP_METER_BAND_STATS_PACK_STR) ==
        OFP_METER_BAND_STATS_SIZE)

# struct ofp_meter_config
OFP_METER_CONFIG_PACK_STR = '!HHI'
OFP_METER_CONFIG_SIZE = 8
assert calcsize(OFP_METER_CONFIG_PACK_STR) == OFP_METER_CONFIG_SIZE

# struct ofp_meter_features
OFP_METER_FEATURES_PACK_STR = '!IIIBB2x'
OFP_METER_FEATURES_SIZE = 16
assert (calcsize(OFP_METER_FEATURES_PACK_STR) ==
        OFP_METER_FEATURES_SIZE)

# struct ofp_experimenter_multipart_header
OFP_EXPERIMENTER_MULTIPART_HEADER_PACK_STR = '!II'
OFP_EXPERIMENTER_MULTIPART_HEADER_SIZE = 8
assert (calcsize(OFP_EXPERIMENTER_MULTIPART_HEADER_PACK_STR) ==
        OFP_EXPERIMENTER_MULTIPART_HEADER_SIZE)

# struct ofp_queue_get_config_request
OFP_QUEUE_GET_CONFIG_REQUEST_PACK_STR = '!I4x'
OFP_QUEUE_GET_CONFIG_REQUEST_SIZE = 16
assert (calcsize(OFP_QUEUE_GET_CONFIG_REQUEST_PACK_STR) +
        OFP_HEADER_SIZE) == OFP_QUEUE_GET_CONFIG_REQUEST_SIZE

# struct ofp_queue_get_config_reply
OFP_QUEUE_GET_CONFIG_REPLY_PACK_STR = '!I4x'
OFP_QUEUE_GET_CONFIG_REPLY_SIZE = 16
assert (calcsize(OFP_QUEUE_GET_CONFIG_REPLY_PACK_STR) +
        OFP_HEADER_SIZE) == OFP_QUEUE_GET_CONFIG_REPLY_SIZE

# struct ofp_packet_out
OFP_PACKET_OUT_PACK_STR = '!IIH6x'
OFP_PACKET_OUT_SIZE = 24
assert (calcsize(OFP_PACKET_OUT_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_PACKET_OUT_SIZE)

# struct ofp_role_request
OFP_ROLE_REQUEST_PACK_STR = '!I4xQ'
OFP_ROLE_REQUEST_SIZE = 24
assert (calcsize(OFP_ROLE_REQUEST_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_ROLE_REQUEST_SIZE)

# enum ofp_controller_role
OFPCR_ROLE_NOCHANGE = 0  # Don't change current role.
OFPCR_ROLE_EQUAL = 1  # Default role, full access.
OFPCR_ROLE_MASTER = 2  # Full access, at most one master.
OFPCR_ROLE_SLAVE = 3  # Read-only access.

# struct ofp_async_config
OFP_ASYNC_CONFIG_PACK_STR = '!2I2I2I'
OFP_ASYNC_CONFIG_SIZE = 32
assert (calcsize(OFP_ASYNC_CONFIG_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_ASYNC_CONFIG_SIZE)

# struct ofp_packet_in
OFP_PACKET_IN_PACK_STR = '!IHBBQ' + _OFP_MATCH_PACK_STR
OFP_PACKET_IN_SIZE = 32
OFP_PACKET_IN_DATA_OFFSET = 18
assert (calcsize(OFP_PACKET_IN_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_PACKET_IN_SIZE)

# enum ofp_packet_in_reason
OFPR_NO_MATCH = 0    # No matching flow.
OFPR_ACTION = 1        # Action explicitly output to controller.
OFPR_INVALID_TTL = 2    # Packet has invalid TTL.

# struct ofp_flow_removed
_OFP_FLOW_REMOVED_PACK_STR0 = 'QHBBIIHHQQ'
OFP_FLOW_REMOVED_PACK_STR = '!' + _OFP_FLOW_REMOVED_PACK_STR0 + \
                            _OFP_MATCH_PACK_STR
OFP_FLOW_REMOVED_PACK_STR0 = '!' + _OFP_FLOW_REMOVED_PACK_STR0
OFP_FLOW_REMOVED_SIZE = 56
assert (calcsize(OFP_FLOW_REMOVED_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_FLOW_REMOVED_SIZE)

# enum ofp_flow_removed_reason
OFPRR_IDLE_TIMEOUT = 0    # Flow idle time exceeded idle_timeout.
OFPRR_HARD_TIMEOUT = 1    # Time exceeded hard_timeout.
OFPRR_DELETE = 2    # Evicted by a DELETE flow mod.
OFPRR_GROUP_DELETE = 3  # Group was removed.

# struct ofp_port_status
OFP_PORT_STATUS_PACK_STR = '!B7x' + _OFP_PORT_PACK_STR
OFP_PORT_STATUS_DESC_OFFSET = OFP_HEADER_SIZE + 8
OFP_PORT_STATUS_SIZE = 80
assert (calcsize(OFP_PORT_STATUS_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_PORT_STATUS_SIZE)

# enum ofp_port_reason
OFPPR_ADD = 0    # The port was added.
OFPPR_DELETE = 1    # The port was removed.
OFPPR_MODIFY = 2    # Some attribute of the port has changed.

# struct ofp_error_msg
OFP_ERROR_MSG_PACK_STR = '!HH'
OFP_ERROR_MSG_SIZE = 12
assert (calcsize(OFP_ERROR_MSG_PACK_STR) + OFP_HEADER_SIZE ==
        OFP_ERROR_MSG_SIZE)

# enum ofp_error_type
OFPET_HELLO_FAILED = 0        # Hello protocol failed.
OFPET_BAD_REQUEST = 1        # Request was not understood.
OFPET_BAD_ACTION = 2        # Error in action description.
OFPET_BAD_INSTRUCTION = 3    # Error in instruction list.
OFPET_BAD_MATCH = 4        # Error in match.
OFPET_FLOW_MOD_FAILED = 5    # Problem modifying flow entry.
OFPET_GROUP_MOD_FAILED = 6    # Problem modifying group entry.
OFPET_PORT_MOD_FAILED = 7    # OFPT_PORT_MOD failed.
OFPET_TABLE_MOD_FAILED = 8    # Table mod request failed.
OFPET_QUEUE_OP_FAILED = 9    # Queue operation failed.
OFPET_SWITCH_CONFIG_FAILED = 10    # Switch config request failed.
OFPET_ROLE_REQUEST_FAILED = 11    # Controller Role request failed.
OFPET_METER_MOD_FAILED = 12    # Error in meter.
OFPET_TABLE_FEATURES_FAILED = 13    # Setting table features failed.
OFPET_EXPERIMENTER = 0xffff    # Experimenter error messages.

# enum ofp_hello_failed_code
OFPHFC_INCOMPATIBLE = 0        # No compatible version.
OFPHFC_EPERM = 1        # Permissions error.

# enum ofp_bad_request_code
OFPBRC_BAD_VERSION = 0        # ofp_header.version not supported.
OFPBRC_BAD_TYPE = 1        # ofp_header.type not supported.
OFPBRC_BAD_MULTIPART = 2        # ofp_stats_msg.type not supported.
OFPBRC_BAD_EXPERIMENTER = 3    # Experimenter id not supported
                               # (in ofp_experimenter_header
                               # or ofp_stats_request or
                               # ofp_stats_reply).
OFPBRC_BAD_EXP_TYPE = 4        # Experimenter type not supported.
OFPBRC_EPERM = 5        # Permissions error.
OFPBRC_BAD_LEN = 6        # Wrong request length for type.
OFPBRC_BUFFER_EMPTY = 7        # Specified buffer has already been used.
OFPBRC_BUFFER_UNKNOWN = 8    # Specified buffer does not exist.
OFPBRC_BAD_TABLE_ID = 9        # Specified table-id invalid or does not exist.
OFPBRC_IS_SLAVE = 10        # Denied because controller is slave.
OFPBRC_BAD_PORT = 11        # Invalid port.
OFBRC_BAD_PACKET = 12        # Invalid packet in packet-out
OFPBRC_MULTIPART_BUFFER_OVERFLOW = 13       # ofp_multipart_request
                                            # overflowed the assigned buffer.

# enum ofp_bad_action_code
OFPBAC_BAD_TYPE = 0        # Unknown action type.
OFPBAC_BAD_LEN = 1        # Length problem in actions.
OFPBAC_BAD_EXPERIMENTER = 2    # Unknown experimenter id specified.
OFPBAC_BAD_EXP_TYPE = 3        # Unknown action type for experimenter id.
OFPBAC_BAD_OUT_PORT = 4        # Problem validating output action.
OFPBAC_BAD_ARGUMENT = 5        # Bad action argument.
OFPBAC_EPERM = 6        # Permissions error.
OFPBAC_TOO_MANY = 7        # Can't handle this many actions.
OFPBAC_BAD_QUEUE = 8        # Problem validating output queue.
OFPBAC_BAD_OUT_GROUP = 9    # Invalid group id in forward action.
OFPBAC_MATCH_INCONSISTENT = 10    # Action can't apply for this match,
                                  # or Set-Field missing prerequisite.
OFPBAC_UNSUPPORTED_ORDER = 11    # Action order is unsupported for
                                 # the action list in an Apply-Actions
                                 # instruction
OFPBAC_BAD_TAG = 12        # Actions uses an unsupported tag/encap.
OFBAC_BAD_SET_TYPE = 13        # Unsupported type in SET_FIELD action.
OFPBAC_BAD_SET_LEN = 14        # Length problem in SET_FIELD action.
OFPBAC_BAD_SET_ARGUMENT = 15    # Bad arguement in SET_FIELD action.

# enum ofp_bad_instruction_code
OFPBIC_UNKNOWN_INST = 0        # Unknown instruction.
OFPBIC_UNSUP_INST = 1        # Switch or table does not support
                             # the instruction.
OFPBIC_BAD_TABLE_ID = 2        # Invalid Table-Id specified
OFPBIC_UNSUP_METADATA = 3    # Metadata value unsupported by datapath.
OFPBIC_UNSUP_METADATA_MASK = 4    # Metadata mask value unsupported by
                                  # datapath.
OFPBIC_BAD_EXPERIMENTER = 5    # Unknown experimenter id specified.
OFPBIC_BAD_EXP_TYPE = 6        # Unknown instruction for experimenter id.
OFPBIC_BAD_EXP_LEN = 7        # Length problem in instrucitons.
OFPBIC_EPERM = 8        # Permissions error.

# enum ofp_bad_match_code
OFPBMC_BAD_TYPE = 0        # Unsupported match type apecified by
                           # the match.
OFPBMC_BAD_LEN = 1        # Length problem in math.
OFPBMC_BAD_TAG = 2        # Match uses an unsupported tag/encap.
OFPBMC_BAD_DL_ADDR_MASK = 3    # Unsupported datalink addr mask -
                                # switch does not support arbitrary
                                # datalink address mask.
OFPBMC_BAD_NW_ADDR_MASK = 4    # Unsupported network addr mask -
                                # switch does not support arbitrary
                                # network addres mask.
OFPBMC_BAD_WILDCARDS = 5    # Unsupported combination of fields
                                # masked or omitted in the match.
OFPBMC_BAD_FIELD = 6        # Unsupported field type in the match.
OFPBMC_BAD_VALUE = 7        # Unsupported value in a match field.
OFPBMC_BAD_MASK = 8        # Unsupported mask specified in the
                                # match.
OFPBMC_BAD_PREREQ = 9        # A prerequisite was not met.
OFPBMC_DUP_FIELD = 10        # A field type was duplicated.
OFPBMC_EPERM = 11         # Permissions error.

# enum ofp_flow_mod_failed_code
OFPFMFC_UNKNOWN = 0        # Unspecified error.
OFPFMFC_TABLES_FULL = 1        # Flow not added because table was full.
OFPFMFC_BAD_TABLE_ID = 2    # Table does not exist
OFPFMFC_OVERLAP = 3        # Attempted to add overlapping flow
                                # with CHECK_OVERLAP flag set.
OFPFMFC_EPERM = 4        # Permissions error.
OFPFMFC_BAD_TIMEOUT = 5        # Flow not added because of
                                # unsupported idle/hard timeout.
OFPFMFC_BAD_COMMAND = 6        # Unsupported or unknown command.
OFPFMFC_BAD_FLAGS = 7        # Unsupported or unknown flags.

# enum ofp_group_mod_failed_code
OFPGMFC_GROUP_EXISTS = 0
OFPGMFC_INVALID_GROUP = 1
OFPGMFC_WEIGHT_UNSUPPORTED = 2    # Switch does not support unequal load
                                  # sharing with select groups.
OFPGMFC_OUT_OF_GROUPS = 3         # The group table is full.
OFPGMFC_OUT_OF_BUCKETS = 4        # The maximum number of action buckets
                                  # for a group has been exceeded.
OFPGMFC_CHAINING_UNSUPPORTED = 5  # Switch does not support groups that
                                  # forward to groups.
OFPGMFC_WATCH_UNSUPPORTED = 6     # This group cannot watch the
                                  # watch_port or watch_group specified.
OFPGMFC_LOOP = 7                  # Group entry would cause a loop.
OFPGMFC_UNKNOWN_GROUP = 8         # Group not modified because a group
                                  # MODIFY attempted to modify a
                                  # non-existent group.
OFPGMFC_CHAINED_GROUP = 9         # Group not deleted because another
                                  # group is forwarding to it.
OFPGMFC_BAD_TYPE = 10             # Unsupported or unknown group type.
OFPGMFC_BAD_COMMAND = 11          # Unsupported or unknown command.
OFPGMFC_BAD_BUCKET = 12           # Error in bucket.
OFPGMFC_BAD_WATCH = 13            # Error in watch port/group.
OFPGMFC_EPERM = 14                # Permissions error.

# enum ofp_port_mod_failed_code
OFPPMFC_BAD_PORT = 0        # Specified port does not exist.
OFPPMFC_BAD_HW_ADDR = 1        # Specified hardware address does not
                                # match the port number.
OFPPMFC_BAD_CONFIG = 2        # Specified config is invalid.
OFPPMFC_BAD_ADVERTISE = 3    # Specified advertise is invalid.
OFPPMFC_EPERM = 4        # Permissions error.

# enum ofp_table_mod_failed_code
OFPTMFC_BAD_TABLE = 0        # Specified table does not exist.
OFPTMFC_BAD_CONFIG = 1        # Specified config is invalid.
OFPTMFC_EPERM = 2        # Permissions error

# enum ofp_queue_op_failed_code
OFPQOFC_BAD_PORT = 0        # Invalid port (or port does not exist).
OFPQOFC_BAD_QUEUE = 1        # Queue does not exist.
OFPQOFC_EPERM = 2        # Permissions error.

# enum ofp_switch_config_failed_code
OFPSCFC_BAD_FLAGS = 0        # Specified flags is invalid.
OFPSCFC_BAD_LEN = 1        # Specified len is invalid.
OFPQCFC_EPERM = 2        # Permissions error.

# enum ofp_role_request_failed_code
OFPRRFC_STALE = 0        # Stale Message: old generation_id.
OFPRRFC_UNSUP = 1        # Controller role change unsupported.
OFPRRFC_BAD_ROLE = 2        # Invalid role.

# enum ofp_meter_mod_failed_code
OFPMMFC_UNKNOWN = 0        # Unspecified error.
OFPMMFC_METER_EXISTS = 1        # Meter not added because a Meter ADD
                                # attempted to replace an existing Meter.
OFPMMFC_INVALID_METER = 2        # Meter not added because Meter specified
                                # is invalid.
OFPMMFC_UNKNOWN_METER = 3        # Meter not modified because a Meter
                                 # MODIFY attempted to modify a non-existent
                                 # Meter.
OFPMMFC_BAD_COMMAND = 4        # Unsupported or unknown command.
OFPMMFC_BAD_FLAGS = 5        # Flag configuration unsupported.
OFPMMFC_BAD_RATE = 6        # Rate unsupported.
OFPMMFC_BAD_BURST = 7        # Burst size unsupported.
OFPMMFC_BAD_BAND = 8        # Band unsupported.
OFPMMFC_BAD_BAND_VALUE = 9        # Band value unsupported.
OFPMMFC_OUT_OF_METERS = 10        # No more meters availabile.
OFPMMFC_OUT_OF_BANDS = 11        # The maximum number of properties
                                 # for a meter has been exceeded.

# enum ofp_table_features_failed_code
OFPTFFC_BAD_TABLE = 0        # Specified table does not exist.
OFPTFFC_BAD_METADATA = 1        # Invalid metadata mask.
OFPTFFC_BAD_TYPE = 2        # Unknown property type.
OFPTFFC_BAD_LEN = 3        # Length problem in properties.
OFPTFFC_BAD_ARGUMENT = 4        # Unsupported property value.
OFPTFFC_EPERM = 5        # Permissions error.

# struct ofp_error_experimenter_msg
OFP_ERROR_EXPERIMENTER_MSG_PACK_STR = '!HHI'
OFP_ERROR_EXPERIMENTER_MSG_SIZE = 16
assert (calcsize(OFP_ERROR_EXPERIMENTER_MSG_PACK_STR) +
        OFP_HEADER_SIZE) == OFP_ERROR_EXPERIMENTER_MSG_SIZE

# struct ofp_experimenter_header
OFP_EXPERIMENTER_HEADER_PACK_STR = '!II'
OFP_EXPERIMENTER_HEADER_SIZE = 16
assert (calcsize(OFP_EXPERIMENTER_HEADER_PACK_STR) + OFP_HEADER_SIZE
        == OFP_EXPERIMENTER_HEADER_SIZE)

# OXM


def _oxm_tlv_header(class_, field, hasmask, length):
    return (class_ << 16) | (field << 9) | (hasmask << 8) | length


def oxm_tlv_header(field, length):
    return _oxm_tlv_header(OFPXMC_OPENFLOW_BASIC, field, 0, length)


def oxm_tlv_header_w(field, length):
    return _oxm_tlv_header(OFPXMC_OPENFLOW_BASIC, field, 1, length * 2)


OXM_OF_IN_PORT = oxm_tlv_header(OFPXMT_OFB_IN_PORT, 4)
OXM_OF_IN_PHY_PORT = oxm_tlv_header(OFPXMT_OFB_IN_PHY_PORT, 4)
OXM_OF_METADATA = oxm_tlv_header(OFPXMT_OFB_METADATA, 8)
OXM_OF_METADATA_W = oxm_tlv_header_w(OFPXMT_OFB_METADATA, 8)
OXM_OF_ETH_DST = oxm_tlv_header(OFPXMT_OFB_ETH_DST, 6)
OXM_OF_ETH_DST_W = oxm_tlv_header_w(OFPXMT_OFB_ETH_DST, 6)
OXM_OF_ETH_SRC = oxm_tlv_header(OFPXMT_OFB_ETH_SRC, 6)
OXM_OF_ETH_SRC_W = oxm_tlv_header_w(OFPXMT_OFB_ETH_SRC, 6)
OXM_OF_ETH_TYPE = oxm_tlv_header(OFPXMT_OFB_ETH_TYPE, 2)
OXM_OF_VLAN_VID = oxm_tlv_header(OFPXMT_OFB_VLAN_VID, 2)
OXM_OF_VLAN_VID_W = oxm_tlv_header_w(OFPXMT_OFB_VLAN_VID, 2)
OXM_OF_VLAN_PCP = oxm_tlv_header(OFPXMT_OFB_VLAN_PCP, 1)
OXM_OF_IP_DSCP = oxm_tlv_header(OFPXMT_OFB_IP_DSCP, 1)
OXM_OF_IP_ECN = oxm_tlv_header(OFPXMT_OFB_IP_ECN, 1)
OXM_OF_IP_PROTO = oxm_tlv_header(OFPXMT_OFB_IP_PROTO, 1)
OXM_OF_IPV4_SRC = oxm_tlv_header(OFPXMT_OFB_IPV4_SRC, 4)
OXM_OF_IPV4_SRC_W = oxm_tlv_header_w(OFPXMT_OFB_IPV4_SRC, 4)
OXM_OF_IPV4_DST = oxm_tlv_header(OFPXMT_OFB_IPV4_DST, 4)
OXM_OF_IPV4_DST_W = oxm_tlv_header_w(OFPXMT_OFB_IPV4_DST, 4)
OXM_OF_TCP_SRC = oxm_tlv_header(OFPXMT_OFB_TCP_SRC, 2)
OXM_OF_TCP_DST = oxm_tlv_header(OFPXMT_OFB_TCP_DST, 2)
OXM_OF_UDP_SRC = oxm_tlv_header(OFPXMT_OFB_UDP_SRC, 2)
OXM_OF_UDP_DST = oxm_tlv_header(OFPXMT_OFB_UDP_DST, 2)
OXM_OF_SCTP_SRC = oxm_tlv_header(OFPXMT_OFB_SCTP_SRC, 2)
OXM_OF_SCTP_DST = oxm_tlv_header(OFPXMT_OFB_SCTP_DST, 2)
OXM_OF_ICMPV4_TYPE = oxm_tlv_header(OFPXMT_OFB_ICMPV4_TYPE, 1)
OXM_OF_ICMPV4_CODE = oxm_tlv_header(OFPXMT_OFB_ICMPV4_CODE, 1)
OXM_OF_ARP_OP = oxm_tlv_header(OFPXMT_OFB_ARP_OP, 2)
OXM_OF_ARP_SPA = oxm_tlv_header(OFPXMT_OFB_ARP_SPA, 4)
OXM_OF_ARP_SPA_W = oxm_tlv_header_w(OFPXMT_OFB_ARP_SPA, 4)
OXM_OF_ARP_TPA = oxm_tlv_header(OFPXMT_OFB_ARP_TPA, 4)
OXM_OF_ARP_TPA_W = oxm_tlv_header_w(OFPXMT_OFB_ARP_TPA, 4)
OXM_OF_ARP_SHA = oxm_tlv_header(OFPXMT_OFB_ARP_SHA, 6)
OXM_OF_ARP_SHA_W = oxm_tlv_header_w(OFPXMT_OFB_ARP_SHA, 6)
OXM_OF_ARP_THA = oxm_tlv_header(OFPXMT_OFB_ARP_THA, 6)
OXM_OF_ARP_THA_W = oxm_tlv_header_w(OFPXMT_OFB_ARP_THA, 6)
OXM_OF_IPV6_SRC = oxm_tlv_header(OFPXMT_OFB_IPV6_SRC, 16)
OXM_OF_IPV6_SRC_W = oxm_tlv_header_w(OFPXMT_OFB_IPV6_SRC, 16)
OXM_OF_IPV6_DST = oxm_tlv_header(OFPXMT_OFB_IPV6_DST, 16)
OXM_OF_IPV6_DST_W = oxm_tlv_header_w(OFPXMT_OFB_IPV6_DST, 16)
OXM_OF_IPV6_FLABEL = oxm_tlv_header(OFPXMT_OFB_IPV6_FLABEL, 4)
OXM_OF_IPV6_FLABEL_W = oxm_tlv_header_w(OFPXMT_OFB_IPV6_FLABEL, 4)
OXM_OF_ICMPV6_TYPE = oxm_tlv_header(OFPXMT_OFB_ICMPV6_TYPE, 1)
OXM_OF_ICMPV6_CODE = oxm_tlv_header(OFPXMT_OFB_ICMPV6_CODE, 1)
OXM_OF_IPV6_ND_TARGET = oxm_tlv_header(OFPXMT_OFB_IPV6_ND_TARGET, 16)
OXM_OF_IPV6_ND_SLL = oxm_tlv_header(OFPXMT_OFB_IPV6_ND_SLL, 6)
OXM_OF_IPV6_ND_TLL = oxm_tlv_header(OFPXMT_OFB_IPV6_ND_TLL, 6)
OXM_OF_MPLS_LABEL = oxm_tlv_header(OFPXMT_OFB_MPLS_LABEL, 4)
OXM_OF_MPLS_TC = oxm_tlv_header(OFPXMT_OFB_MPLS_TC, 1)
OXM_OF_MPLS_BOS = oxm_tlv_header(OFPXMT_OFB_MPLS_BOS, 1)
OXM_OF_PBB_ISID = oxm_tlv_header(OFPXMT_OFB_PBB_ISID, 3)
OXM_OF_PBB_ISID_W = oxm_tlv_header_w(OFPXMT_OFB_PBB_ISID, 3)
OXM_OF_TUNNEL_ID = oxm_tlv_header(OFPXMT_OFB_TUNNEL_ID, 8)
OXM_OF_TUNNEL_ID_W = oxm_tlv_header_w(OFPXMT_OFB_TUNNEL_ID, 8)
OXM_OF_IPV6_EXTHDR = oxm_tlv_header(OFPXMT_OFB_IPV6_EXTHDR, 2)
OXM_OF_IPV6_EXTHDR_W = oxm_tlv_header_w(OFPXMT_OFB_IPV6_EXTHDR, 2)

# define constants
OFP_VERSION = 0x04
OFP_TCP_PORT = 6633
MAX_XID = 0xffffffff
