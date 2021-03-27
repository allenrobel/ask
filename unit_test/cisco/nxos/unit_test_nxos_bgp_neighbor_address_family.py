#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_address_family.py
# Status = BETA
our_version = 100
 
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp_neighbor_address_family import NxosBgpNeighborAddressFamily

ansible_module = 'nxos_bgp_neighbor_address_family'
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

def add_task(pb):
    task = NxosBgpNeighborAddressFamily(log)
    task.as_number = '12000.0'
    task.afi = 'ipv4'
    task.safi = 'unicast'
    task.allowas_in_set = True
    task.allowas_in_max_occurences = 2
    task.capability_additional_paths_receive = 'enable'
    task.capability_additional_paths_send = 'disable'
    task.default_originate_route_map = 'DEFAULT_ORIGINATE_RM'
    task.default_originate_set = True
    task.maximum_prefix_max_prefix_limit = 12000
    task.maximum_prefix_generate_warning_threshold = 80
    task.maximum_prefix_restart_interval = 5
    task.maximum_prefix_warning_only = True
    task.next_hop_self_set = True
    task.route_map_inbound = 'INBOUND_RM'
    task.route_map_outbound = 'OUTBOUND_RM'
    task.add_address_family()

    task.afi = 'l2vpn'
    task.safi = 'evpn'
    task.rewrite_evpn_rt_asn = True
    task.add_address_family()

    task.neighbor_address = '10.1.1.1'
    task.add_bgp_neighbor()

    # add AF for one bgp neighbor in vrf VRF_1
    task.afi = 'ipv4'
    task.safi = 'unicast'
    task.add_address_family()

    task.neighbor_address = '10.3.1.0/25'
    task.add_vrf_bgp_neighbor()
    task.vrf = 'VRF_1'
    task.add_vrf()

    # add two bgp neighbors in vrf VRF_2
    task.afi = 'ipv4'
    task.safi = 'unicast'
    task.add_address_family()
    task.neighbor_address = '10.5.1.0/25'
    task.add_vrf_bgp_neighbor()

    task.afi = 'ipv6'
    task.safi = 'unicast'
    task.add_address_family()
    task.neighbor_address = '2001:bbbb::/120'
    task.add_vrf_bgp_neighbor()

    task.vrf = 'VRF_2'
    task.add_vrf()

    # add another bgp neighbor into the global/default vrf
    task.afi = 'ipv6'
    task.safi = 'unicast'
    task.add_address_family()
    task.neighbor_address = '2001:aaaa::1'
    task.add_bgp_neighbor()

    task.state = 'merged'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)


pb = playbook()
add_task(pb)

pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
