#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_ospfv2.py
our_version = 111
'''
=================================
unit_test_ans_task_nxos_ospfv2.py
=================================

Description
-----------

Example script and half-hearted unit test for Ansible module: nxos_ospfv2

Usage
-----

Uncomment one or more of the def calls at the bottom of the script.

'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_ospfv2 import NxosOspfV2

ansible_module = 'nxos_ospfv2'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.ansible_connection = 'httpapi' # httpapi, network_cli
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_task_name(task):
    task.append_to_task_name('v.{}'.format(our_version))
    task.append_to_task_name(ansible_host)
    for key in sorted(task.properties_set):
        task.append_to_task_name(key)

def task_nxos_ospfv2_vrf_example(pb):
    task = NxosOspfV2(log)
    task.process_id = 3

    task.auto_cost_reference_bandwidth = '30'
    task.auto_cost_unit = 'Gbps'
    task.vrf = 'foo'
    task.add_vrf()

    task.default_metric = 1111
    task.vrf = 'bar'
    task.add_vrf()

    # At this point you can add non-vrf parameters directly under process 3
    task.default_information_originate_always = 'no'
    task.default_information_originate_set = 'yes'
    task.default_information_originate_route_map = 'DEFAULT_INFORMATION_ORIGINATE_ROUTE_MAP'

    # Since add_process() resets parameters to None, we call task.task_name first
    # so that the parameters we've set are reflected in the playbook's task_name
    task.task_name = add_task_name(task)
    # Now, add the process, which also adds the VRFs
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_auto_cost(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.auto_cost_reference_bandwidth = '30'
    task.auto_cost_unit = 'Gbps'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_auto_cost_vrf(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.auto_cost_reference_bandwidth = '30'
    task.auto_cost_unit = 'Gbps'
    task.task_name = add_task_name(task)
    task.vrf = 'foo'
    task.add_vrf()
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_default_metric(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.default_metric = 1111
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_default_information_originate(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.default_information_originate_always = 'no'
    task.default_information_originate_set = 'yes'
    task.default_information_originate_route_map = 'DEFAULT_INFORMATION_ORIGINATE_ROUTE_MAP'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_distance(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.distance = 100
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_flush_routes(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.flush_routes = 'yes'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_isolate(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.isolate = 'yes'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_log_adjacency_changes(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.log_adjacency_changes_detail = 'yes'
    task.log_adjacency_changes_log = 'yes'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_max_lsa(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.max_lsa_ignore_count = 50
    task.max_lsa_ignore_time = 51
    task.max_lsa_max_non_self_generated_lsa = 54
    task.max_lsa_reset_time = 52
    task.max_lsa_threshold = 53
    task.max_lsa_warning_only = 'no'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_max_metric(pb):
    task = NxosOspfV2(log)
    task.process_id = 3

    task.max_metric_router_lsa_include_stub = 'yes'
    task.max_metric_router_lsa_set = 'yes'

    task.max_metric_router_lsa_external_lsa_max_metric_value = 1111
    task.max_metric_router_lsa_external_lsa_set = 'yes'

    task.max_metric_router_lsa_on_startup_set = 'yes'
    task.max_metric_router_lsa_on_startup_wait_for_bgp_asn = '65134'
    task.max_metric_router_lsa_on_startup_wait_period = '1200'

    task.max_metric_router_lsa_summary_lsa_max_metric_value = '10'
    task.max_metric_router_lsa_summary_lsa_set = 'yes'

    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_maximum_paths(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.maximum_paths = 64
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_mpls_traffic_eng(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.mpls_traffic_eng_areas = [1,2,3]
    task.mpls_traffic_eng_multicast_intact = 'no'
    task.mpls_traffic_eng_router_id = 'loopback0'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_name_lookup(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.name_lookup = 'yes'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_passive_interface(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.passive_interface_default = 'yes'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_redistribute(pb):
    task = NxosOspfV2(log)
    task.process_id = 3

    task.redistribute_id = '1'
    task.redistribute_protocol = 'bgp'
    task.redistribute_route_map = "REDISTRIBUTE_BGP_1_ROUTE_MAP"
    add_task_name(task)
    task.add_redistribute()

    task.redistribute_id = '0'
    task.redistribute_protocol = 'ospf'
    task.redistribute_route_map = "REDISTRIBUTE_OSPF_0_ROUTE_MAP"
    add_task_name(task)
    task.add_redistribute()

    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_rfc1583compatibility(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.rfc1583compatibility = 'yes'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_router_id(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.router_id = '10.10.10.10'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_shutdown(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.shutdown = 'yes'
    task.task_name = add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_summary_address(pb):
    task = NxosOspfV2(log)

    task.summary_address_prefix = '3.0.0.0/8'
    task.summary_address_not_advetise = 'no'
    task.summary_address_tag = 3
    add_task_name(task)
    task.add_summary_address()

    task.summary_address_prefix = '4.3.2.0/24'
    task.summary_address_not_advetise = 'yes'
    task.summary_address_tag = 4
    add_task_name(task)
    task.add_summary_address()

    task.summary_address_prefix = '10.20.30.0/24'
    add_task_name(task)
    task.add_summary_address()

    task.process_id = 3
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_table_map(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.table_map_name = 'TABLE_MAP_ROUTE_MAP'
    task.table_map_filter = 'yes'
    add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_timers_lsa(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.timers_lsa_arrival = 2000
    task.timers_lsa_group_pacing = 200
    add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_timers_throttle_lsa(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.timers_throttle_lsa_hold_interval = 6000
    task.timers_throttle_lsa_max_interval = 7000
    task.timers_throttle_lsa_start_interval = 3000
    add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_timers_throttle_spf(pb):
    task = NxosOspfV2(log)
    task.process_id = 3
    task.timers_throttle_spf_initial_spf_delay = 6000
    task.timers_throttle_spf_max_wait_time = 7000
    task.timers_throttle_spf_min_hold_time = 3000
    add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)


def task_nxos_ospfv2_authentication(pb):
    task = NxosOspfV2(log)
    task.task_name = '{} {}'.format(ansible_host, ansible_module)
    task.area_id = 2
    task.authentication_message_digest = 'yes'
    task.authentication_set = 'yes'
    task.add_area()
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_areas_ranges(pb):
    task = NxosOspfV2(log)
    task.task_name = '{} {}'.format(ansible_host, ansible_module)
    task.process_id = 200
    task.area_id = 200

    task.ranges_cost = 10
    task.ranges_not_advertise = 'yes'
    task.ranges_prefix = '13.13.13.13/32'
    add_task_name(task)
    task.add_range()

    task.ranges_cost = 20
    task.ranges_not_advertise = 'no'
    task.ranges_prefix = '14.14.14.14/32'
    add_task_name(task)
    task.add_range()

    task.add_area()
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)


def task_nxos_ospfv2_areas_nssa(pb):
    task = NxosOspfV2(log)
    task.process_id = 100
    task.area_id = 100
    task.nssa_default_information_originate = 'yes'
    task.nssa_no_redistribution = 'yes'
    task.nssa_no_summary = 'yes'
    task.nssa_set = 'yes'
    #task.nssa_translate_type7_always = 'yes'
    #task.nssa_translate_type7_never = 'yes'
    task.nssa_translate_type7_supress_fa = 'yes'
    add_task_name(task)
    task.add_area()
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_areas_filter_list(pb):
    task = NxosOspfV2(log)
    task.filter_list_direction = 'in'
    task.filter_list_route_map = 'FOOBAR_IN'
    task.area_id = 100
    add_task_name(task)
    task.add_area()
    task.process_id = 100
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_areas_authentication(pb):
    task = NxosOspfV2(log)
    task.area_id = 3
    task.authentication_message_digest = 'yes'
    task.authentication_set = 'yes'
    add_task_name(task)
    task.add_area()
    task.process_id = 0
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_areas_authentication_vrf(pb):
    task = NxosOspfV2(log)
    task.area_id = 3
    task.authentication_message_digest = 'yes'
    task.authentication_set = 'yes'
    add_task_name(task)
    task.add_area()
    task.vrf = 'foo'
    task.add_vrf()
    task.process_id = 0
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_areas_stub(pb):
    task = NxosOspfV2(log)
    task.area_id = 3
    task.stub_no_summary = 'yes'
    task.stub_set = 'yes'
    add_task_name(task)
    task.add_area()
    task.process_id = 0
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_areas_default_cost(pb):
    task = NxosOspfV2(log)
    task.area_id = 0
    task.default_cost = 100
    add_task_name(task)
    task.add_area()
    task.process_id = 0
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_bfd(pb):
    task = NxosOspfV2(log)
    task.process_id = 99
    task.bfd = 'yes'
    add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospfv2_processes_graceful_restart(pb):
    task = NxosOspfV2(log)
    task.graceful_restart_helper_disable = 'yes'
    task.graceful_restart_set = 'no'
    task.graceful_restart_grace_period = 120
    task.process_id = 99
    add_task_name(task)
    task.add_process()
    task.state = 'merged'
    task.update()
    pb.add_task(task)

pb = playbook()

#task_nxos_ospfv2_areas_authentication(pb)
task_nxos_ospfv2_areas_authentication_vrf(pb)
#task_nxos_ospfv2_areas_default_cost(pb)
#task_nxos_ospfv2_areas_filter_list(pb)
#task_nxos_ospfv2_areas_nssa(pb)
#task_nxos_ospfv2_areas_ranges(pb)
#task_nxos_ospfv2_areas_stub(pb)
#task_nxos_ospfv2_processes_auto_cost(pb)
#task_nxos_ospfv2_processes_auto_cost_vrf(pb)
#task_nxos_ospfv2_processes_bfd(pb)
#task_nxos_ospfv2_processes_default_information_originate(pb)
#task_nxos_ospfv2_processes_default_metric(pb)
#task_nxos_ospfv2_processes_distance(pb)
#task_nxos_ospfv2_processes_flush_routes(pb)
#task_nxos_ospfv2_processes_graceful_restart(pb)
#task_nxos_ospfv2_processes_isolate(pb)
#task_nxos_ospfv2_processes_log_adjacency_changes(pb)
#task_nxos_ospfv2_processes_max_lsa(pb)
#task_nxos_ospfv2_processes_max_metric(pb)
#task_nxos_ospfv2_processes_maximum_paths(pb)
#task_nxos_ospfv2_processes_mpls_traffic_eng(pb)
#task_nxos_ospfv2_processes_name_lookup(pb)
#task_nxos_ospfv2_processes_passive_interface(pb)
#task_nxos_ospfv2_processes_redistribute(pb)
#task_nxos_ospfv2_processes_rfc1583compatibility(pb)
#task_nxos_ospfv2_processes_router_id(pb)
#task_nxos_ospfv2_processes_shutdown(pb)
#task_nxos_ospfv2_processes_summary_address(pb)
#task_nxos_ospfv2_processes_table_map(pb)
#task_nxos_ospfv2_processes_timers_lsa(pb)
#task_nxos_ospfv2_processes_timers_throttle_lsa(pb)
#task_nxos_ospfv2_processes_timers_throttle_spf(pb)
#task_nxos_ospfv2_vrf_example(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
