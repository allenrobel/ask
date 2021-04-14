#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_address_family.py
# Status = BETA
our_version = 103
 
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

def asn(task):
     task.as_number = '12000.0'
def ipv4_additional_paths(task):
    task.additional_paths_install_backup = True
    task.additional_paths_receive = True
    task.additional_paths_selection_route_map = 'ADD_PATH_MAP'
    task.additional_paths_send = False
def ipv4_aggregates(task):
    for aggregate in ['10.50.3.0/25', '10.50.4.0/25']:
        task.aggregate_address_advertise_map = 'AGG_IPV4_ADV_MAP'
        task.aggregate_address_as_set = False
        task.aggregate_address_attribute_map = 'AGG_IPV4_ATTR_MAP'
        task.aggregate_address_prefix = aggregate
        task.aggregate_address_summary_only = False
        task.aggregate_address_suppress_map = 'AGG_IPV4_SUPP_MAP'
        task.add_aggregate_address()
def ipv4_dampening(task):
    '''
    comment any of these for negative test
    '''
    task.dampening_decay_half_life = 45
    task.dampening_max_suppress_time = 120
    task.dampening_start_reuse_route = 120
    task.dampening_start_suppress_route = 60
def ipv4_distance(task):
    '''
    comment any of these for negative test
    '''
    task.distance_ebgp_routes = 10
    task.distance_ibgp_routes = 20
    task.distance_local_routes = 30
def ipv4_unicast_afi_safi(task):
    task.afi = 'ipv4'
    task.safi = 'unicast'
    task.append_to_task_name('{}/{}'.format(task.afi, task.safi))
def ipv4_networks(task):
    for prefix in ['10.3.1.1/32', '10.3.4.0/25']:
        task.networks_prefix = prefix
        task.networks_route_map = 'IPV4_ORIGINATE'
        task.add_network()
def ipv4_nexthop(task):
    task.nexthop_route_map = 'NEXTHOP_MAP'
    task.nexthop_trigger_delay_critical_delay = 100
    task.nexthop_trigger_delay_non_critical_delay = 3000
def ipv4_maximum_paths(task):
    task.maximum_paths_eibgp_parallel_paths = 32
def ipv4_redistribute(task):
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
def ipv4_timers(task):
    task.timers_bestpath_defer_defer_time = 600
    task.timers_bestpath_defer_maximum_defer_time = 1200
def ipv4_vrf(task):
    #task.vrf = 'default' # uncomment for negative test (vrf cannot be 'default')
    task.vrf = 'FOO' # comment for negative test (maximum_paths_eibgp_parallel_paths requires vrf)
def ipv4_address_family(task):
    ipv4_additional_paths(task)
    ipv4_aggregates(task)
    ipv4_unicast_afi_safi(task)
    asn(task)
    ipv4_dampening(task)
    ipv4_distance(task)
    task.advertise_pip = True
    task.default_information_originate = True
    task.default_metric = 100
    ipv4_networks(task)
    ipv4_nexthop(task)
    ipv4_maximum_paths(task)
    ipv4_redistribute(task)
    ipv4_timers(task)
    ipv4_vrf(task)
    task.add_address_family()

def l2vpn_evpn_afi_safi(task):
    task.afi = 'l2vpn'
    task.safi = 'evpn'
    task.append_to_task_name('{}/{}'.format(task.afi, task.safi))
def l2vpn_evpn_address_family(task):
    l2vpn_evpn_afi_safi(task)
    task.advertise_system_mac =  True
    task.add_address_family()

def ipv6_unicast_afi_safi(task):
    task.afi = 'ipv6'
    task.safi = 'unicast'
    task.append_to_task_name('{}/{}'.format(task.afi, task.safi))
def ipv6_networks(task):
    for prefix in ['2001::1/128', '2001:aaaa:bbbb::/48']:
        task.networks_prefix = prefix
        task.networks_route_map = 'IPV6_ORIGINATE'
        task.add_network()
def ipv6_maximum_paths(task):
    task.maximum_paths_parallel_paths = 32
def ipv6_unicast_address_family(task):
    ipv6_networks(task)
    ipv6_maximum_paths(task)
    ipv6_unicast_afi_safi(task)
    task.add_address_family()

def add_task(pb):
    task = NxosBgpAddressFamily(log)
    task.append_to_task_name('v.{}'.format(our_version))
    task.append_to_task_name(ansible_host)
    ipv4_address_family(task)
    l2vpn_evpn_address_family(task)
    ipv6_unicast_address_family(task)
    task.state = 'merged'
    task.commit()
    pb.add_task(task)


pb = playbook()
add_task(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
