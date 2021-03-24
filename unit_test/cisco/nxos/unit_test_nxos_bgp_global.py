#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_global.py
# Status = BETA
our_version = 103
 
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp_global import NxosBgpGlobal

ansible_module = 'nxos_bgp_global'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.profile_nxos()
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_task_name(task):
    task.append_to_task_name('v.{}'.format(our_version))
    task.append_to_task_name(ansible_host)
    for key in sorted(task.scriptkit_properties):
        task.append_to_task_name(key)

def ipv4_neighbors(pb):
    task = NxosBgpGlobal(log)
    task.as_number = '12000.0'

    # Since disable_policy_batching_* is not supported
    # under vrf config, it will not be cleared by
    # task.add_vrf(), and will be added to the global
    # bgp config when task.update() is called.
    task.disable_policy_batching_ipv4_prefix_list = 'IPV4_DPB'
    task.disable_policy_batching_nexthop = True

    # Since bestpath_* is supported under vrf config, it
    # will be cleared by task.add_vrf() after it has
    # been added to the vrf. The same holds for all other
    # properties that are supported under vrf config.
    # Hence, it's probably better when structuring your
    # script, to group vrf-supported properties separately
    # from vrf-non-supported properties.
    task.bestpath_med_non_deterministic = False
    task.confederation_identifier = 65000
    task.confederation_peers = [65001, 65002]
    task.neighbor_down_fib_accelerate = True
    task.timers_prefix_peer_timeout = 10
    task.timers_prefix_peer_wait = 30

    # add a bgp neighbor in the global/default vrf
    task.neighbor_affinity_group_group_id = 200
    task.neighbor_bfd_singlehop = True
    task.neighbor_bfd_set = True
    task.neighbor_bfd_multihop_set = True
    task.neighbor_bfd_multihop_interval_tx_interval = 300
    task.neighbor_bfd_multihop_interval_min_rx_interval = 300
    task.neighbor_bfd_multihop_interval_multiplier = 6
    task.neighbor_address = '10.1.1.1'
    task.neighbor_graceful_shutdown_activate_route_map = 'SHUTDOWN_RM'
    task.neighbor_graceful_shutdown_activate_set = False
    task.neighbor_log_neighbor_changes_disable = True
    task.neighbor_log_neighbor_changes_set = True
    task.neighbor_low_memory_exempt = True
    task.neighbor_password_encryption = 0
    task.neighbor_password_key = 'wings'
    task.neighbor_remote_as = '6201.1'
    task.neighbor_remove_private_as_all = True
    task.neighbor_remove_private_as_replace_as = True
    task.neighbor_remove_private_as_set = True
    task.neighbor_timers_holdtime = 20
    task.neighbor_timers_keepalive = 5
    task.neighbor_transport_connection_mode_passive = False
    task.neighbor_ttl_security_hops = 1
    task.neighbor_update_source = 'Vlan2'
    task.add_bgp_neighbor()

    # add one bgp neighbor in vrf VRF_1
    task.neighbor_address = '10.3.1.0/25'
    task.neighbor_inherit_peer = 'TOR_VRF_1'
    task.neighbor_inherit_peer_session = 'TOR_SESSION_VRF_1'
    task.neighbor_remote_as = '6201.3'
    task.neighbor_update_source = 'port-channel33'
    task.neighbor_capability_suppress_4_byte_as = True
    task.add_vrf_bgp_neighbor()
    task.vrf = 'VRF_1'
    task.add_vrf()

    # add two bgp neighbors in vrf VRF_2
    task.neighbor_address = '10.5.1.0/25'
    task.neighbor_inherit_peer = 'TOR_VRF_2'
    task.neighbor_inherit_peer_session = 'TOR_SESSION_VRF_2'
    task.neighbor_remote_as = '6501.3'
    task.neighbor_update_source = 'Ethernet1/5.5'
    task.add_vrf_bgp_neighbor()

    task.neighbor_address = '10.5.2.0/25'
    task.neighbor_inherit_peer = 'TOR_VRF_2'
    task.neighbor_inherit_peer_session = 'TOR_SESSION_VRF_2'
    task.neighbor_remote_as = '6501.4'
    task.neighbor_update_source = 'Ethernet1/20'
    task.add_vrf_bgp_neighbor()

    task.vrf = 'VRF_2'
    task.add_vrf()

    # add another bgp neighbor into the global/default vrf
    task.neighbor_address = '10.4.4.0/24'
    task.neighbor_inherit_peer = 'TOR'
    task.neighbor_inherit_peer_session = 'TOR_SESSION'
    task.neighbor_remote_as = '6201.3'
    task.neighbor_update_source = 'Vlan4'
    task.add_bgp_neighbor()

    task.state = 'merged'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def ipv6_neighbors(pb):
    task = NxosBgpGlobal(log)
    task.as_number = '12000.0'
    task.neighbor_address = '2001:aaaa::1'
    task.neighbor_remote_as = 4700000001
    task.add_bgp_neighbor()

    task.as_number = '12000.0'
    task.neighbor_address = '2001:bbbb::/120'
    task.neighbor_remote_as = 4700000001
    task.add_bgp_neighbor()

    task.state = 'merged'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)


pb = playbook()
ipv4_neighbors(pb)
ipv6_neighbors(pb)

pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
