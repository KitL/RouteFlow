import logging

from rflib.defs import *
from binascii import *
from rflib.types.Match import * 
from rflib.types.Action import *
from rflib.types.Option import *

log = logging.getLogger('ryu.app.rfproxy')

def create_default_flow_mod(dp, cookie=0, cookie_mask=0, table_id=0,
                            command=None, idle_timeout=0, hard_timeout=0,
                            priority=PRIORITY_LOWEST,
                            buffer_id=0xffffffff, match=None, actions=None,
                            inst_type=None, out_port=None, out_group=None,
                            flags=0, inst=[]):

  if command is None:
    command = dp.ofproto.OFPFC_ADD

  if inst is []:
    if inst_type is None:
      inst_type = dp.ofproto.OFPIT_APPLY_ACTIONS

    if actions is not None:
      inst = [dp.ofproto_parser.OFPInstructionActions(inst_type, actions)]

  if match is None:
    match = dp.ofproto_parser.OFPMatch()

  if out_port is None:
    out_port = dp.ofproto.OFPP_ANY

  if out_group is None:
    out_group = dp.ofproto.OFPG_ANY

  return dp.ofproto_parser.OFPFlowMod(dp, cookie, cookie_mask,
                                      table_id, command,
                                      idle_timeout, hard_timeout,
                                      priority, buffer_id,
                                      out_port, out_group,
                                      flags, match, inst)

def create_flow_mod(dp, mod, matches, actions, options):
  flow_mod = create_default_flow_mod(dp)
  add_command(flow_mod, mod)
  add_matches(flow_mod, matches)
  add_actions(flow_mod, actions)
  add_options(flow_mod, options)
  return flow_mod

def add_command(flow_mod, mod):
  if mod == RMT_ADD:
    pass
  elif mod == RMT_DELETE:
    flow_mod.command = flow_mod.datapath.ofproto.OFPFC_DELETE_STRICT
  elif mod == RMT_MODIFY:
    flow_mod.command = flow_mod.datapath.ofproto.OFPFC_MODIFY_STRICT

def add_matches(flow_mod, matches):
  for match in matches:
    if match['type'] == RFMT_IPV4:
      value = bin_to_int(match['value'])
      addr = value >> 32
      mask = value & ((1 << 32) - 1)
      flow_mod.match.set_dl_type(ETHERTYPE_IP)
      flow_mod.match.set_ipv4_dst_masked(addr, mask)
    elif match['type'] == RFMT_IPV6:
      v = match['value']
      #convert to tuples of 2 byte values
      addr = tuple((ord(v[i]) << 8) | ord(v[i + 1]) for i in range(0, 16, 2))
      mask = tuple((ord(v[i]) << 8) | ord(v[i + 1]) for i in range(16, 32, 2))
      flow_mod.match.set_dl_type(ETHERTYPE_IPV6)
      flow_mod.match.set_ipv6_dst_masked(addr, mask)
    elif match['type'] == RFMT_ETHERNET:
      flow_mod.match.set_dl_dst(match['value'])
    elif match['type'] == RFMT_ETHERTYPE:
      flow_mod.match.set_dl_type(bin_to_int(match['value']))
    elif match['type'] == RFMT_NW_PROTO:
      flow_mod.match.set_ip_proto(bin_to_int(match['value']))
    elif match['type'] == RFMT_TP_SRC:
      flow_mod.match.set_ip_proto(IPPROTO_TCP)
      flow_mod.match.set_tcp_src(bin_to_int(match['value']))
    elif match['type'] == RFMT_TP_DST:
      flow_mod.match.set_ip_proto(IPPROTO_TCP)
      flow_mod.match.set_tcp_dst(bin_to_int(match['value']))
    elif match['type'] == RFMT_IN_PORT:
      flow_mod.match.set_in_port(bin_to_int(match['value']))
    elif TLV.optional(Match.from_dict(match)):
        log.info("Dropping unsupported Match (type: %s)" % match['type'])
    else:
        log.warning("Failed to serialise Match (type: %s)" % match['type'])
        return

def add_actions(flow_mod, action_tlvs):
  parser = flow_mod.datapath.ofproto_parser
  ofproto = flow_mod.datapath.ofproto
  actions = []
  for action in action_tlvs:
    if action['type'] == RFAT_OUTPUT:
      port = bin_to_int(action['value'])
      a = parser.OFPActionOutput(port, ofproto.OFPCML_MAX)
      actions.append(a)
    elif action['type'] == RFAT_SET_ETH_SRC:
      srcMac = action['value']
      src = parser.OFPMatchField.make(ofproto.OXM_OF_ETH_SRC, srcMac)
      actions.append(parser.OFPActionSetField(src))
    elif action['type'] == RFAT_SET_ETH_DST:
      dstMac = action['value']
      dst = parser.OFPMatchField.make(ofproto.OXM_OF_ETH_DST, dstMac)
      actions.append(parser.OFPActionSetField(dst))
    elif TLV.optional(Action.from_dict(action)):
        log.info("Dropping unsupported Action (type: %s)" % action['type'])
    else:
        log.warning("Failed to serialise Action (type: %s)" % action['type'])
        return
  inst = parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)
  flow_mod.instructions = [inst]

def add_options(flow_mod, options):
  for option in options:
    if option['type'] == RFOT_PRIORITY:
      flow_mod.priority = bin_to_int(option['value'])
    elif option['type'] == RFOT_IDLE_TIMEOUT:
      flow_mod.idle_timeout = bin_to_int(option['value'])
    elif option['type'] == RFOT_HARD_TIMEOUT:
      flow_mod.hard_timeout = bin_to_int(option['value'])
    elif option['type'] == RFOT_CT_ID:
      pass
    elif option.optional():
        log.info("Dropping unsupported Option (type: %s)" % option['type'])
    else:
        log.warning("Failed to serialise Option (type: %s)" % option['type'])
        return

def send_pkt_out(dp, port, msg):
  actions = [dp.ofproto_parser.OFPActionOutput(port, len(msg)), ]
  dp.send_packet_out(buffer_id=0xffffffff, in_port=dp.ofproto.OFPP_ANY,
                     actions=actions, data=msg)
