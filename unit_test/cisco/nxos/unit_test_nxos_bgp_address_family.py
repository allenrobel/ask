#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_address_family.py
# Status = BETA
our_version = 102
 
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp_address_family import NxosBgpAddressFamily

ansible_module = 'nxos_bgp_address_family'
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

def add_task(pb):
    task = NxosBgpAddressFamily(log)
    task.append_to_task_name('v.{}'.format(our_version))
    task.append_to_task_name(ansible_host)
    task.as_number = '12000.0'
    task.afi = 'ipv4'
    task.safi = 'unicast'
    #task.vrf = 'default' # uncomment for negative test
    task.append_to_task_name('{}/{}'.format(task.afi, task.safi))
    task.additional_paths_install_backup = True
    task.additional_paths_receive = True
    task.additional_paths_selection_route_map = 'ADD_PATH_MAP'
    task.additional_paths_send = False
    task.advertise_pip = True
    for aggregate in ['10.50.3.0/25', '10.50.4.0/25']:
        task.aggregate_address_advertise_map = 'AGG_IPV4_ADV_MAP'
        task.aggregate_address_as_set = False
        task.aggregate_address_attribute_map = 'AGG_IPV4_ATTR_MAP'
        task.aggregate_address_prefix = aggregate
        task.aggregate_address_summary_only = False
        task.aggregate_address_suppress_map = 'AGG_IPV4_SUPP_MAP'
        task.add_aggregate_address()
    task.default_information_originate = True
    task.default_metric = 100
    task.maximum_paths_eibgp_parallel_paths = 32
    for prefix in ['10.3.1.1/32', '10.3.4.0/25']:
        task.networks_prefix = prefix
        task.networks_route_map = 'IPV4_ORIGINATE'
        task.add_network()
    task.nexthop_route_map = 'NEXTHOP_MAP'
    task.nexthop_trigger_delay_critical_delay = 100
    task.nexthop_trigger_delay_non_critical_delay = 3000
    task.redistribute_id = 100
    task.redistribute_protocol = 'ospf'  # comment for negative test
    task.redistribute_route_map = 'REDISTRIBUTE_OSPF_MAP'
    task.add_redistribute()
    task.redistribute_id = 'Enterprise'  # comment for negative test
    task.redistribute_protocol = 'isis'
    task.redistribute_route_map = 'REDISTRIBUTE_ISIS_MAP'
    task.add_redistribute()
    # task.redistribute_id = 200 # uncomment for negative test
    task.redistribute_protocol = 'direct'
    task.redistribute_route_map = 'DIRECT'
    task.add_redistribute()
    task.timers_bestpath_defer_defer_time = 600
    task.timers_bestpath_defer_maximum_defer_time = 1200
    task.vrf = 'FOO' # comment for negative test (maximum_paths_eibgp_parallel_paths requires vrf)
    task.add_address_family()

    task.afi = 'l2vpn'
    task.safi = 'evpn'
    task.append_to_task_name('{}/{}'.format(task.afi, task.safi))
    task.advertise_system_mac =  True
    task.add_address_family()

    task.afi = 'ipv6'
    task.safi = 'unicast'
    task.append_to_task_name('{}/{}'.format(task.afi, task.safi))
    task.maximum_paths_parallel_paths = 32
    for prefix in ['2001::1/128', '2001:aaaa:bbbb::/48']:
        task.networks_prefix = prefix
        task.networks_route_map = 'IPV6_ORIGINATE'
        task.add_network()
    task.add_address_family()
    task.state = 'merged'
    task.commit()
    pb.add_task(task)


pb = playbook()
add_task(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
