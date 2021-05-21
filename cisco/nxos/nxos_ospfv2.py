# NxosOspfV2() - cisco/nxos/nxos_ospfv2.py
our_version = 109
from copy import deepcopy
from ask.common.task import Task
'''
***********************************
NxosOspfV2 - nxos_ospfv2.py
***********************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosOspfV2() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_ospfv2
- These can then be passed to Playbook().add_task()


Ansible Module Documentation
----------------------------
- `cisco.nxos.nxos_ospfv2 <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_ospfv2_module.rst>`_


ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_ospfv2.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_ospfv2.py>`_


Properties
----------

NxosOspfV2() disambiguates property names when they are used in multiple dictionaries by the
cisco.nxos.nxos_ospfv2 module.

The heusistc used for disambiguation is to include the name(s) of the enclosing dictionary(ies) 
in the property name.

For example, Property name ``not_advertise`` is disambiguated into ``ranges_not_advertise``
and ``summary_address_not_advertise`` since this property name appears in both the ``ranges``
and the ``summary_address`` dictionaries.

|

======================================  ==================================================
Property                                Description
======================================  ==================================================
area_id                                 Area ID as an integer or IP Address::

                                            - Type: str()
                                            - Valid values: int() or ipv4 address without prefixlen
                                            - Examples:
                                                - task.area_id = 0 
                                                - task.area_id = '10.0.1.1'

bfd                                     Enable BFD on all OSPF interfaces::

                                            - Type: bool()
                                            - Valid values: False, True

default_cost                            Default cost for default summary LSA::

                                            - Type: int()
                                            - Example: task.default_cost = 10

default_metric                          Default metric for redistributed routes::

                                            - Type: int()
                                            - Example: task.default_metric = 100

distance                                OSPF administrative distance::

                                            - Type: int()
                                            - Example: task.distance = 100

flush_routes                            Flush routes on a non-graceful controlled restart::

                                            - Type: bool()
                                            - Valid values: False, True

isolate                                 Isolate this router from OSPF perspective::

                                            - Type: bool()
                                            - Valid values: False, True

maximum_paths                           Maximum paths per destination::

                                            - Type: int()
                                            - Example: task.maximum_paths = 16

name_lookup                             Display OSPF router ids as DNS names::

                                            - Type: bool()
                                            - Valid values: False, True

process_id                              The OSPF process tag::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-65535
                                            - Example:
                                                task.process_id = 100
                                            - Required

rfc1583compatibility                    Configure RFC1583 compatibility for external path preferences::

                                            - Type: bool()
                                            - Valid values: False, True

router_id                               OSPF process router-id::

                                            - Type: str()
                                            - Valid values: ivp4 address without prefixlen
                                            - Example: task.router_id = '10.0.1.1'

shutdown                                Shutdown the OSPF protocol instance::

                                            - Type: bool()
                                            - Valid values: False, True

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
authentication_message_digest           Use message-digest authentication::

                                            - Type: bool()
                                            - Valid values: False, True

authentication_set                      Set authentication for the area::

                                            - Type: bool()
                                            - Valid values: False, True

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
auto_cost_reference_bandwidth           Reference bandwidth used to assign OSPF cost::

                                            - Type: int()
                                            - Required
                                            - Valid values:
                                                - If auto_cost_unit == 'Mbps'
                                                    - int() range: 1-4000000
                                                    - Default: 40000
                                                - If auto_cost_unit == 'Gbps'
                                                    - int() range: 1-4000
                                                    - Default: 40
                                            - Examples:
                                                - task.auto_cost_reference_bandwidth = 50000 

auto_cost_unit                          auto_cost_reference_bandwidth unit::

                                            - Type: str()
                                            - Required
                                            - Valid values: Gbps, Mbps
                                            - Example: task.auto_cost_unit = 'Mbps'

======================================  ==================================================

|
|

======================================      ==================================================
Property                                    Description
======================================      ==================================================
default_information_originate_always        Always advertise a default route::

                                                - Type: bool()
                                                - Valid values: False, True

default_information_originate_route_map     Policy to control distribution of default routes::

                                                - Type: str()

default_information_originate_set           Enable distribution of default route::

                                                - Type: bool()
                                                - Valid values: False, True

======================================      ==================================================


======================================  ==================================================
Property                                Description
======================================  ==================================================
filter_list_direction                   The direction to apply the route map::

                                            - Type: str()
                                            - Valid values: in, out
                                            - Required
                                            - Dependencies:
                                                Because filter_list is heirarchally located
                                                within [processes][areas], both of the following
                                                must be called:
                                                -   task.add_area()
                                                -   task.add_process()

filter_list_route_map                   Route-map name::

                                            - Type: str()
                                            - Required
                                            - Dependencies:
                                                Because filter_list is heirarchally located
                                                within [processes][areas], both of the following
                                                must be called:
                                                -   task.add_area()
                                                -   task.add_process()

======================================  ==================================================

|

filter_list example
-------------------

::

    def task_nxos_ospfv2_filter_list(pb):
        task = NxosOspfV2(log)
        task.task_name = '{} {}'.format(ansible_host, ansible_module)

        task.filter_list_direction = 'in'
        task.filter_list_route_map = 'FOOBAR_IN'

        task.area_id = 100
        task.add_area()
        task.process_id = 100
        task.add_process()
        task.state = 'merged'
        task.update()
        pb.add_task(task)

|

======================================  ==================================================
Property                                Description
======================================  ==================================================
graceful_restart_grace_period           maximum interval to restart gracefully::

                                            - Type: int()

graceful_restart_helper_disable         Enable/Disable helper mode::

                                            - Type: bool()
                                            - Valid values: False, True

graceful_restart_set                    Enable/Disable graceful-restart::

                                            - Type: bool()
                                            - Valid values: False, True

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
log_adjacency_changes_detail            Notify all state changes::

                                            - Type: bool()
                                            - Valid values: False, True

log_adjacency_changes_log               Enable/disable logging changes in adjacency state::

                                            - Type: bool()
                                            - Valid values: False, True

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
max_lsa_ignore_count                    Set count on how many times adjacencies can be
                                        suppressed::

                                            - Type: int()

max_lsa_ignore_time                     Set count on how many times adjacencies can be
                                        suppressed::

                                            - Type: int()

max_lsa_max_non_self_generated_lsa      Set the maximum number of non self-generated
                                        LSAs::

                                            - Type: int()
                                            - Required

max_lsa_reset_time                      Set number of minutes after which ignore-count is
                                        reset to zero::

                                            - Type: int()

max_lsa_threshold                       Threshold value (%) at which to generate a
                                        warning message::

                                            - Type: int()

max_lsa_warning_only                    Log a warning message when limit is exceeded::

                                            - Type: bool()
                                            - Valid values: False, True

======================================  ==================================================

|
|

====================================================    ==================================================
Property                                                Description
====================================================    ==================================================
max_metric_router_lsa_include_stub                      Advertise Max metric for Stub links as well::

                                                            - Type: bool()
                                                            - Valid values: False, True

max_metric_router_lsa_set                               Set router-lsa attribute::

                                                            - Type: bool()
                                                            - Valid values: False, True

max_metric_router_lsa_external_lsa_max_metric_value     max metric value for external LSAs::

                                                            - Type: int()
                                                            - Valid values: int()

max_metric_router_lsa_external_lsa_set                  Set external-lsa attribute::

                                                            - Type: bool()
                                                            - Valid values: False, True

max_metric_router_lsa_on_startup_set                    Set on-startup attribute:

                                                            - Type: bool()
                                                            - Valid values: False, True

max_metric_router_lsa_on_startup_wait_for_bgp_asn       ASN of BGP to wait for::

                                                            - Type: str()
                                                            - Valid values: An AS number

max_metric_router_lsa_on_startup_wait_period            Wait period in seconds after startup::

                                                            - Type: int()
                                                            - Valid values: int()

max_metric_router_lsa_summary_lsa_set                   Set summary-lsa attribute::

                                                            - Type: bool()
                                                            - Valid values: False, True

max_metric_router_lsa_summary_lsa_max_metric_value      Max metric value for summary LSAs::

                                                            - Type: int()
                                                            - Valid values: int()

====================================================    ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
mpls_traffic_eng_areas                  Python list of area IDs. These will be converted 
                                        to str() in populate_processes_mpls_traffic_eng() before adding
                                        them to the mpls_traffic_eng dictionary::

                                            - Type: list()
                                            - Example: task.mpls_traffic_eng_areas = [100, 120]

mpls_traffic_eng_multicast_intact       MPLS TE multicast support::

                                            - Type: bool()
                                            - Valid values: False, True

mpls_traffic_eng_router_id              Interface used for Router ID associated with TE::

                                            - Type: str()
                                            - Example: task.mpls_traffic_eng_router_id = 'loopback2'
======================================  ==================================================

======================================  ==================================================
Property                                Description
======================================  ==================================================
nssa_default_information_originate      Originate Type-7 default LSA into NSSA area::

                                            - Type: bool()
                                            - Valid values: False, True

nssa_no_redistribution                  Do not send redistributed LSAs into NSSA area::

                                            - Type: bool()
                                            - Valid values: False, True

nssa_no_summary                         Do not send summary LSAs into NSSA area:: 

                                            - Type: bool()
                                            - Valid values: False, True

nssa_set                                Configure area as NSSA::

                                            - Type: bool()
                                            - Valid values: False, True

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
nssa_translate_type7_always             Always translate LSAs::

                                            - Type: bool()
                                            - Valid values: False, True

nssa_translate_type7_never              Never translate LSAs::

                                            - Type: bool()
                                            - Valid values: False, True

nssa_translate_type7_supress_fa         Suppress forwarding address in translated LSAs::

                                            - Type: bool()
                                            - Valid values: False, True

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
passive_interface_default               Interfaces passive by default (Suppress routing 
                                        updates on the interface)::

                                            - Type: bool()
                                            - Valid values: False, True

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
ranges_cost                             Cost to use for the range::

                                            - Type: int()
                                            - Valid values: int()

ranges_not_advertise                    Suppress advertising the specified range::

                                            - Type: bool()
                                            - Valid values: False, True

ranges_prefix                           Range prefix::

                                            - Type: str()
                                            - Valid values: IPv4 prefix with format (x.x.x.x/len)
                                            - Required

======================================  ==================================================

|
|

========================    ===================================================
Property                    Description
========================    ===================================================
redistribute_id             The identifier for the protocol specified::

                                - Type: str()
                                - Example: if "router ospf 3" is configured,
                                  redistribute_id would be 3. 

redistribute_protocol       The name of the protocol::

                                - Type: str()
                                - Valid values: bgp, direct, eigrp, isis, 
                                  lisp, ospf, rip, static
                                - Required

redistribute_route_map      The route map policy to constrain redistribution::

                                - Type: str()
                                - Required

register                    Ansible variable to save output to::

                                - Type: str()
                                - Examples:
                                    task.register = 'result'

running_config              Full path to a file containing the output of
                            ``show running-config | section "^router ospf .*"``.
                            ``running_config`` is mutually-exclusive with
                            every other property except ``state`` and
                            ``register``.  ``state`` must be set to ``parsed``
                            if ``running_config`` is set.::

                                - Type: str()
                                - Examples:
                                    task.state = 'parsed'
                                    task.running_config = '/tmp/running.cfg'
                                    task.register = 'parsed'

========================    ===================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
stub_no_summary                         Do not send summary LSAs into NSSA area::

                                            - Type: bool()
                                            - Valid values: False, True

stub_set                                Configure area as NSSA::

                                            - Type: bool()
                                            - Valid values: False, True

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
summary_address_not_advertise           Supress advertising the specified summary::

                                            - Type: bool()
                                            - Valid values: False, True

summary_address_prefix                  Prefix to summarize::

                                            - Type: str()
                                            - Valid values: IPv4 prefix with format (x.x.x.x/len)
                                            - Required

summary_address_tag                     32-bit tag value for summary::

                                            - Type: int()
                                            - Valid values: int()

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
table_map_filter                        Block the OSPF routes from being sent to RIB::

                                            - Type: bool()
                                            - Valid values: False, True

table_map_name                          Route Map name::

                                            - Type: str()
                                            - Required

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
timers_lsa_arrival                      Minimum interval between arrival of a LSA::

                                            - Type: int()
                                            - Valid values: int()

timers_lsa_group_pacing                 LSA group refresh/maxage interval::

                                            - Type: int()
                                            - Valid values: int()

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
timers_throttle_lsa_hold_interval       The hold interval::

                                            - Type: int()
                                            - Valid values: int()

timers_throttle_lsa_max_interval        The max interval::

                                            - Type: int()
                                            - Valid values: int()

timers_throttle_lsa_start_interval      The start interval::

                                            - Type: int()
                                            - Valid values: int()

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
timers_throttle_spf_initial_spf_delay   Initial SPF schedule delay in milliseconds::

                                            - Type: int()
                                            - Valid values: int()

timers_throttle_spf_max_wait_time       Maximum wait time between SPF calculations::

                                            - Type: int()
                                            - Valid values: int()

timers_throttle_spf_min_hold_time       Minimum hold time between SPF calculations::

                                            - Type: int()
                                            - Valid values: int()

======================================  ==================================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosOspfV2(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_ospfv2'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.config = dict()
        self.config['processes'] = list() # list of self.processes_dict

        self.properties_areas_authentication_set = set()
        self.properties_areas_authentication_set.add('authentication_message_digest')
        self.properties_areas_authentication_set.add('authentication_set')

        self.properties_areas_filter_list_set = set()
        self.properties_areas_filter_list_set.add('filter_list_direction')
        self.properties_areas_filter_list_set.add('filter_list_route_map')

        self.properties_areas_nssa_set = set()
        self.properties_areas_nssa_set.add('nssa_default_information_originate')
        self.properties_areas_nssa_set.add('nssa_no_redistribution')
        self.properties_areas_nssa_set.add('nssa_no_summary')
        self.properties_areas_nssa_set.add('nssa_set')

        self.properties_areas_nssa_translate_type7_set = set()
        self.properties_areas_nssa_translate_type7_set.add('nssa_translate_type7_always')
        self.properties_areas_nssa_translate_type7_set.add('nssa_translate_type7_never')
        self.properties_areas_nssa_translate_type7_set.add('nssa_translate_type7_supress_fa')

        self.properties_areas_ranges_set = set()
        self.properties_areas_ranges_set.add('ranges_cost')
        self.properties_areas_ranges_set.add('ranges_not_advertise')
        self.properties_areas_ranges_set.add('ranges_prefix')

        self.properties_areas_stub_set  = set()
        self.properties_areas_stub_set.add('stub_no_summary')
        self.properties_areas_stub_set.add('stub_set')

        self.properties_areas_top_level_set = set()
        self.properties_areas_top_level_set.add('area_id')
        self.properties_areas_top_level_set.add('default_cost')

        self.properties_processes_auto_cost_set = set()
        self.properties_processes_auto_cost_set.add('auto_cost_reference_bandwidth')
        self.properties_processes_auto_cost_set.add('auto_cost_unit')

        self.properties_processes_default_information_originate_set = set()
        self.properties_processes_default_information_originate_set.add('default_information_originate_always')
        self.properties_processes_default_information_originate_set.add('default_information_originate_route_map')
        self.properties_processes_default_information_originate_set.add('default_information_originate_set')

        self.properties_processes_graceful_restart_set = set()
        self.properties_processes_graceful_restart_set.add('graceful_restart_grace_period')
        self.properties_processes_graceful_restart_set.add('graceful_restart_helper_disable')
        self.properties_processes_graceful_restart_set.add('graceful_restart_set')

        self.properties_processes_passive_interface_set = set()
        self.properties_processes_passive_interface_set.add('passive_interface_default')

        self.properties_processes_table_map_set = set()
        self.properties_processes_table_map_set.add('table_map_filter')
        self.properties_processes_table_map_set.add('table_map_name')

        self.properties_processes_timers_lsa_set = set()
        self.properties_processes_timers_lsa_set.add('timers_lsa_arrival')
        self.properties_processes_timers_lsa_set.add('timers_lsa_group_pacing')

        self.properties_processes_max_lsa_set = set()
        self.properties_processes_max_lsa_set.add('max_lsa_ignore_count')
        self.properties_processes_max_lsa_set.add('max_lsa_ignore_time')
        self.properties_processes_max_lsa_set.add('max_lsa_max_non_self_generated_lsa')
        self.properties_processes_max_lsa_set.add('max_lsa_reset_time')
        self.properties_processes_max_lsa_set.add('max_lsa_threshold')
        self.properties_processes_max_lsa_set.add('max_lsa_warning_only')

        self.properties_processes_max_metric_router_lsa_set = set()
        self.properties_processes_max_metric_router_lsa_set.add('max_metric_router_lsa_include_stub')
        self.properties_processes_max_metric_router_lsa_set.add('max_metric_router_lsa_set')

        self.properties_processes_max_metric_router_lsa_external_lsa_set = set()
        self.properties_processes_max_metric_router_lsa_external_lsa_set.add('max_metric_router_lsa_external_lsa_max_metric_value')
        self.properties_processes_max_metric_router_lsa_external_lsa_set.add('max_metric_router_lsa_external_lsa_set')

        self.properties_processes_max_metric_router_on_startup_set = set()
        self.properties_processes_max_metric_router_on_startup_set.add('max_metric_router_lsa_on_startup_set')
        self.properties_processes_max_metric_router_on_startup_set.add('max_metric_router_lsa_on_startup_wait_for_bgp_asn')
        self.properties_processes_max_metric_router_on_startup_set.add('max_metric_router_lsa_on_startup_wait_period')

        self.properties_processes_max_metric_router_lsa_summary_lsa_set = set()
        self.properties_processes_max_metric_router_lsa_summary_lsa_set.add('max_metric_router_lsa_summary_lsa_max_metric_value')
        self.properties_processes_max_metric_router_lsa_summary_lsa_set.add('max_metric_router_lsa_summary_lsa_set')

        self.properties_processes_mpls_traffic_eng_set = set()
        self.properties_processes_mpls_traffic_eng_set.add('mpls_traffic_eng_multicast_intact')
        self.properties_processes_mpls_traffic_eng_set.add('mpls_traffic_eng_router_id')

        self.properties_processes_log_adjacency_changes_set = set()
        self.properties_processes_log_adjacency_changes_set.add('log_adjacency_changes_detail')
        self.properties_processes_log_adjacency_changes_set.add('log_adjacency_changes_log')

        self.properties_processes_redistribute_set = set()
        self.properties_processes_redistribute_set.add('redistribute_id')
        self.properties_processes_redistribute_set.add('redistribute_protocol')
        self.properties_processes_redistribute_set.add('redistribute_route_map')

        self.properties_processes_timers_throttle_lsa_set = set()
        self.properties_processes_timers_throttle_lsa_set.add('timers_throttle_lsa_hold_interval')
        self.properties_processes_timers_throttle_lsa_set.add('timers_throttle_lsa_max_interval')
        self.properties_processes_timers_throttle_lsa_set.add('timers_throttle_lsa_start_interval')

        self.properties_processes_timers_throttle_spf_set = set()
        self.properties_processes_timers_throttle_spf_set.add('timers_throttle_spf_initial_spf_delay')
        self.properties_processes_timers_throttle_spf_set.add('timers_throttle_spf_max_wait_time')
        self.properties_processes_timers_throttle_spf_set.add('timers_throttle_spf_min_hold_time')

        self.properties_processes_top_level_set = set()
        self.properties_processes_top_level_set.add('bfd')
        self.properties_processes_top_level_set.add('default_metric')
        self.properties_processes_top_level_set.add('distance')
        self.properties_processes_top_level_set.add('flush_routes')
        self.properties_processes_top_level_set.add('isolate')
        self.properties_processes_top_level_set.add('maximum_paths')
        self.properties_processes_top_level_set.add('name_lookup')
        self.properties_processes_top_level_set.add('process_id')
        self.properties_processes_top_level_set.add('rfc1583compatibility')
        self.properties_processes_top_level_set.add('router_id')
        self.properties_processes_top_level_set.add('shutdown')

        self.properties_summary_address_set = set()
        self.properties_summary_address_set.add('summary_address_not_advertise')
        self.properties_summary_address_set.add('summary_address_prefix')
        self.properties_summary_address_set.add('summary_address_tag')

        self.properties_set = set()
        self.properties_set.update(self.properties_areas_authentication_set)
        self.properties_set.update(self.properties_areas_filter_list_set)
        self.properties_set.update(self.properties_areas_nssa_set)
        self.properties_set.update(self.properties_areas_nssa_translate_type7_set)
        self.properties_set.update(self.properties_areas_ranges_set)
        self.properties_set.update(self.properties_areas_stub_set)
        self.properties_set.update(self.properties_areas_top_level_set)
        self.properties_set.update(self.properties_processes_auto_cost_set)
        self.properties_set.update(self.properties_processes_default_information_originate_set)
        self.properties_set.update(self.properties_processes_graceful_restart_set)
        self.properties_set.update(self.properties_processes_log_adjacency_changes_set)
        self.properties_set.update(self.properties_processes_max_lsa_set)
        self.properties_set.update(self.properties_processes_max_metric_router_lsa_set)
        self.properties_set.update(self.properties_processes_max_metric_router_lsa_external_lsa_set)
        self.properties_set.update(self.properties_processes_max_metric_router_on_startup_set)
        self.properties_set.update(self.properties_processes_max_metric_router_lsa_summary_lsa_set)
        self.properties_set.update(self.properties_processes_passive_interface_set)
        self.properties_set.update(self.properties_processes_redistribute_set)
        self.properties_set.update(self.properties_processes_table_map_set)
        self.properties_set.update(self.properties_processes_timers_lsa_set)
        self.properties_set.update(self.properties_processes_timers_throttle_lsa_set)
        self.properties_set.update(self.properties_processes_timers_throttle_spf_set)
        self.properties_set.update(self.properties_processes_top_level_set)
        self.properties_set.update(self.properties_summary_address_set)

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        # map disambiguated property names back into their ambiguous names
        # see the various populate_*() methods
        self.property_map = dict()
        self.property_map['area_id'] = 'area_id'
        self.property_map['authentication_message_digest'] = 'message_digest'
        self.property_map['authentication_set'] = 'set'
        self.property_map['auto_cost_reference_bandwidth'] = 'reference_bandwidth'
        self.property_map['auto_cost_unit'] = 'unit'
        self.property_map['bfd'] = 'bfd'

        self.property_map['default_information_originate_always'] = 'always'
        self.property_map['default_information_originate_route_map'] = 'route_map'
        self.property_map['default_information_originate_set'] = 'set'

        self.property_map['default_cost'] = 'default_cost'
        self.property_map['default_metric'] = 'default_metric'
        self.property_map['distance'] = 'distance'

        self.property_map['graceful_restart_grace_period'] = 'grace_period'
        self.property_map['graceful_restart_helper_disable'] = 'helper_disable'
        self.property_map['graceful_restart_set'] = 'set'

        self.property_map['filter_list_direction'] = 'direction'
        self.property_map['filter_list_route_map'] = 'route_map'

        self.property_map['flush_routes'] = 'flush_routes'
        self.property_map['isolate'] = 'isolate'

        self.property_map['log_adjacency_changes_detail'] = 'detail'
        self.property_map['log_adjacency_changes_log'] = 'log'

        self.property_map['max_lsa_ignore_count'] = 'ignore_count'
        self.property_map['max_lsa_ignore_time'] = 'ignore_time'
        self.property_map['max_lsa_max_non_self_generated_lsa'] = 'max_non_self_generated_lsa'
        self.property_map['max_lsa_reset_time'] = 'reset_time'
        self.property_map['max_lsa_threshold'] = 'threshold'
        self.property_map['max_lsa_warning_only'] = 'warning_only'

        self.property_map['max_metric_router_lsa_include_stub'] = 'include_stub'
        self.property_map['max_metric_router_lsa_set'] = 'set'

        self.property_map['max_metric_router_lsa_external_lsa_max_metric_value'] = 'max_metric_value'
        self.property_map['max_metric_router_lsa_external_lsa_set'] = 'set'

        self.property_map['max_metric_router_lsa_on_startup_set'] = 'set'
        self.property_map['max_metric_router_lsa_on_startup_wait_for_bgp_asn'] = 'wait_for_bgp_asn'
        self.property_map['max_metric_router_lsa_on_startup_wait_period'] = 'wait_period'

        self.property_map['max_metric_router_lsa_summary_lsa_max_metric_value'] = 'max_metric_value'
        self.property_map['max_metric_router_lsa_summary_lsa_set'] = 'set'

        self.property_map['maximum_paths'] = 'maximum_paths'

        self.property_map['mpls_traffic_eng_multicast_intact'] = 'multicast_intact'
        self.property_map['mpls_traffic_eng_router_id'] = 'router_id'

        self.property_map['name_lookup'] = 'name_lookup'

        self.property_map['nssa_default_information_originate'] = 'default_information_originate'
        self.property_map['nssa_no_redistribution'] = 'no_redistribution'
        self.property_map['nssa_no_summary'] = 'no_summary'
        self.property_map['nssa_set'] = 'set'

        self.property_map['nssa_translate_type7_always'] = 'always'
        self.property_map['nssa_translate_type7_never'] = 'never'
        self.property_map['nssa_translate_type7_supress_fa'] = 'supress_fa'

        self.property_map['passive_interface_default'] = 'default'
        self.property_map['process_id'] = 'process_id'

        self.property_map['ranges_cost'] = 'cost'
        self.property_map['ranges_not_advertise'] = 'not_advertise'
        self.property_map['ranges_prefix'] = 'prefix'

        self.property_map['rfc1583compatibility'] = 'rfc1583compatibility'
        self.property_map['router_id'] = 'router_id'

        self.property_map['redistribute_id'] = 'id'
        self.property_map['redistribute_protocol'] = 'protocol'
        self.property_map['redistribute_route_map'] = 'route_map'

        self.property_map['shutdown'] = 'shutdown'

        self.property_map['summary_address_not_advertise'] = 'not_advertise'
        self.property_map['summary_address_prefix'] = 'prefix'
        self.property_map['summary_address_tag'] = 'tag'

        self.property_map['stub_no_summary'] = 'no_summary'
        self.property_map['stub_set'] = 'set'

        self.property_map['table_map_name'] = 'name'
        self.property_map['table_map_filter'] = 'filter'

        self.property_map['timers_lsa_arrival'] = 'lsa_arrival'
        self.property_map['timers_lsa_group_pacing'] = 'lsa_group_pacing'
        self.property_map['timers_throttle_lsa_hold_interval'] = 'hold_interval'
        self.property_map['timers_throttle_lsa_max_interval'] = 'max_interval'
        self.property_map['timers_throttle_lsa_start_interval'] = 'start_interval'
        self.property_map['timers_throttle_spf_initial_spf_delay'] = 'initial_spf_delay'
        self.property_map['timers_throttle_spf_max_wait_time'] = 'max_wait_time'
        self.property_map['timers_throttle_spf_min_hold_time'] = 'min_hold_time'

        self.nxos_ospfv2_valid_auto_cost_unit = set()
        self.nxos_ospfv2_valid_auto_cost_unit.add('Mbps')
        self.nxos_ospfv2_valid_auto_cost_unit.add('Gbps')

        self.nxos_ospfv2_valid_filter_list_direction = set()
        self.nxos_ospfv2_valid_filter_list_direction.add('in')
        self.nxos_ospfv2_valid_filter_list_direction.add('out')

        self.nxos_ospfv2_valid_mpls_traffic_eng_router_id_interfaces = set()
        self.nxos_ospfv2_valid_mpls_traffic_eng_router_id_interfaces.add('ethernet')
        self.nxos_ospfv2_valid_mpls_traffic_eng_router_id_interfaces.add('loopback')
        self.nxos_ospfv2_valid_mpls_traffic_eng_router_id_interfaces.add('port-channel')

        self.nxos_ospfv2_valid_redistribute_protocol = set()
        self.nxos_ospfv2_valid_redistribute_protocol.add('bgp')
        self.nxos_ospfv2_valid_redistribute_protocol.add('direct')
        self.nxos_ospfv2_valid_redistribute_protocol.add('eigrp')
        self.nxos_ospfv2_valid_redistribute_protocol.add('isis')
        self.nxos_ospfv2_valid_redistribute_protocol.add('lisp')
        self.nxos_ospfv2_valid_redistribute_protocol.add('ospf')
        self.nxos_ospfv2_valid_redistribute_protocol.add('rip')
        self.nxos_ospfv2_valid_redistribute_protocol.add('static')

        self.nxos_ospfv2_valid_state = set()
        self.nxos_ospfv2_valid_state.add('merged')
        self.nxos_ospfv2_valid_state.add('replaced')
        self.nxos_ospfv2_valid_state.add('overridden')
        self.nxos_ospfv2_valid_state.add('deleted')
        self.nxos_ospfv2_valid_state.add('gathered')
        self.nxos_ospfv2_valid_state.add('parsed')
        self.nxos_ospfv2_valid_state.add('rendered')

        self.init_properties()

    def running_config_verification(self):
        if self.state != 'parsed':
            self.task_log.error('exiting. if running_config is set, state must be set to parsed')
            exit(1)
        for p in self.properties_set:
            if self.properties[p] != None:
                self.task_log.error('exiting. Cannot mix running_config with other configuration.')
                self.task_log.error('Instantiate a separate NxosOspfV2() instance and configure it solely for running_config.')
                exit(1)

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if self.running_config != None:
            self.running_config_verification()

    def commit(self):
        self.update()
    def update(self):
        '''
        update verifies that mandatory module-specific parameters are set
        '''
        self.final_verification()

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.task_name != None:
             self.ansible_task['name'] = self.task_name
        if self.register != None:
            self.ansible_task['register'] = self.register
        if self.running_config != None:
            self.ansible_task[self.ansible_module]['running_config'] = self.make_running_config()
            return

        self.ansible_task[self.ansible_module]['config'] = self.config.copy()
        self.init_properties()

    def make_running_config(self):
        return r'{{' +  " lookup(" + r'"file"' + ',' + r'"' + self.running_config + r'"' + ')' + r' }}'


    def remove_null_from_dict(self, d):
        return {k: v for k, v in d.items() if v is not None}
    def remove_empty_list_from_dict(self, d):
        new_d = dict()
        for k in d:
            if type(d[k]) == type(list()):
                if len(d[k]) == 0:
                    continue
            new_d[k] = d[k]
        return new_d.copy()

    def populate_areas_authentication(self):
        d = dict()
        for p in self.properties_areas_authentication_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.areas_dict['authentication'] = deepcopy(d)

    def populate_areas_ranges(self):
        d = dict()
        for p in self.properties_areas_ranges_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.areas_dict['ranges'].append(deepcopy(d))

    def verify_area_filter_list(self):
        '''
        called from self.populate_areas_filter_list()
        '''
        if self.filter_list_direction == None and self.filter_list_route_map == None:
            return False
        if self.filter_list_direction != None and self.filter_list_route_map != None:
            return True
        self.task_log.error('exiting. filter_list_direction and filter_list_route_map must both be set, or both be unset (None)')
        exit(1)
    def populate_areas_filter_list(self):
        if self.verify_area_filter_list():
            d = dict()
            for p in self.properties_areas_filter_list_set:
                if self.properties[p] != None:
                    mapped_p = self.property_map[p]
                    d[mapped_p] = self.properties[p]
            self.areas_dict['filter_list'].append(deepcopy(d))

    def verify_nssa_translate_type7(self):
        if self.nssa_translate_type7_always != None and self.nssa_translate_type7_never != None:
            self.task_log.error('exiting. The following are mutually-exclusive. Unset one or the other.')
            self.task_log.error('nssa_translate_type7_always ({})'.format(self.nssa_translate_type7_always))
            self.task_log.error('nssa_translate_type7_never ({})'.format(self.nssa_translate_type7_never))
            exit(1)
        if self.nssa_translate_type7_never == True and self.nssa_translate_type7_supress_fa == True:
            self.task_log.error('exiting. The following are mutually-exclusive. Unset one or the other.')
            self.task_log.error('nssa_translate_type7_never ({})'.format(self.nssa_translate_type7_never))
            self.task_log.error('nssa_translate_type7_supress_fa ({})'.format(self.nssa_translate_type7_supress_fa))
            exit(1)

    def populate_areas_nssa(self):
        nssa_dict = dict()
        for p in self.properties_areas_nssa_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                nssa_dict[mapped_p] = self.properties[p]

        self.verify_nssa_translate_type7()
        nssa_translate_dict = dict()
        nssa_translate_dict['type7'] = dict()
        for p in self.properties_areas_nssa_translate_type7_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                nssa_translate_dict['type7'][mapped_p] = self.properties[p]
        if len(nssa_translate_dict['type7']) > 0:
            nssa_dict['translate'] = deepcopy(nssa_translate_dict)
        if len(nssa_dict) != 0:
            self.areas_dict['nssa'] = deepcopy(nssa_dict)

    def populate_areas_stub(self):
        d = dict()
        for p in self.properties_areas_stub_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.areas_dict['stub'] = deepcopy(d)

    def populate_areas_top_level(self):
        d = dict()
        for p in self.properties_areas_top_level_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                self.areas_dict[mapped_p] = self.properties[p]

    def populate_processes_auto_cost(self):
        d = dict()
        for p in self.properties_processes_auto_cost_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.processes_dict['auto_cost'] = deepcopy(d)

    def populate_processes_default_information_originate(self):
        d = dict()
        for p in self.properties_processes_default_information_originate_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.processes_dict['default_information'] = dict()
            self.processes_dict['default_information']['originate'] = deepcopy(d)

    def populate_processes_graceful_restart(self):
        d = dict()
        for p in self.properties_processes_graceful_restart_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.processes_dict['graceful_restart'] = deepcopy(d)

    def populate_processes_log_adjacency_changes(self):
        d = dict()
        for p in self.properties_processes_log_adjacency_changes_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.processes_dict['log_adjacency_changes'] = deepcopy(d)

    def verify_max_lsa(self):
        if self.max_lsa_warning_only == True:
            if self.max_lsa_ignore_count != None:
                self.task_log.error('exiting.  max_lsa_warning_only ({}) cannot be True if max_lsa_ignore_count ({}) is set.'.format(
                    self.max_lsa_warning_only,
                    self.max_lsa_ignore_count))
                exit(1)
            if self.max_lsa_ignore_time != None:
                self.task_log.error('exiting.  max_lsa_warning_only ({}) cannot be True if max_lsa_ignore_time ({}) is set.'.format(
                    self.max_lsa_warning_only,
                    self.max_lsa_ignore_time))
                exit(1)
            if self.max_lsa_reset_time != None:
                self.task_log.error('exiting.  max_lsa_warning_only ({}) cannot be True if max_lsa_reset_time ({}) is set.'.format(
                    self.max_lsa_warning_only,
                    self.max_lsa_reset_time))
                exit(1)
    def populate_processes_max_lsa(self):
        self.verify_max_lsa()
        d = dict()
        for p in self.properties_processes_max_lsa_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.processes_dict['max_lsa'] = deepcopy(d)

    def populate_processes_max_metric(self):
        '''
        max-metric router-lsa external-lsa 16777215 include-stub on-startup 86400 summary-lsa 16777215
        max-metric router-lsa external-lsa 16777215 include-stub on-startup 86400 wait-for bgp 64432.44323 summary-lsa 16777215
        '''
        d = dict()
        router_lsa  = set()
        router_lsa.add(self.max_metric_router_lsa_include_stub)
        router_lsa.add(self.max_metric_router_lsa_set)
        router_lsa.add(self.max_metric_router_lsa_external_lsa_max_metric_value)
        router_lsa.add(self.max_metric_router_lsa_external_lsa_set)
        router_lsa.add(self.max_metric_router_lsa_on_startup_set)
        router_lsa.add(self.max_metric_router_lsa_on_startup_wait_for_bgp_asn)
        router_lsa.add(self.max_metric_router_lsa_on_startup_wait_period)
        router_lsa.add(self.max_metric_router_lsa_summary_lsa_set)
        router_lsa.add(self.max_metric_router_lsa_summary_lsa_max_metric_value)
        if len(router_lsa) > 1:
            d['router_lsa'] = dict()

        external_lsa = set()
        external_lsa.add(self.max_metric_router_lsa_external_lsa_max_metric_value)
        external_lsa.add(self.max_metric_router_lsa_external_lsa_set)
        if len(external_lsa) > 1:
            d['router_lsa']['external_lsa'] = dict()

        on_startup = set()
        on_startup.add(self.max_metric_router_lsa_on_startup_set)
        on_startup.add(self.max_metric_router_lsa_on_startup_wait_for_bgp_asn)
        on_startup.add(self.max_metric_router_lsa_on_startup_wait_period)
        if len(on_startup) > 1:
            d['router_lsa']['on_startup'] = dict()

        summary_lsa = set()
        summary_lsa.add(self.max_metric_router_lsa_summary_lsa_max_metric_value)
        summary_lsa.add(self.max_metric_router_lsa_summary_lsa_set)
        if len(summary_lsa) > 1:
            d['router_lsa']['summary_lsa'] = dict()


        for p in self.properties_processes_max_metric_router_lsa_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d['router_lsa'][mapped_p] = self.properties[p]

        for p in self.properties_processes_max_metric_router_lsa_external_lsa_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d['router_lsa']['external_lsa'][mapped_p] = self.properties[p]

        for p in self.properties_processes_max_metric_router_on_startup_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d['router_lsa']['on_startup'][mapped_p] = self.properties[p]

        for p in self.properties_processes_max_metric_router_lsa_summary_lsa_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d['router_lsa']['summary_lsa'][mapped_p] = self.properties[p]

        if len(d) != 0:
            self.processes_dict['max_metric'] = deepcopy(d)

    def populate_processes_mpls_traffic_eng(self):
        d = dict()
        if len(self.properties['mpls_traffic_eng_areas']) != 0:
            d['areas'] = list() # of dict()
            for area in self.properties['mpls_traffic_eng_areas']:
                area_dict = dict()
                area_dict['area_id'] = str(area)
                d['areas'].append(deepcopy(area_dict))
        for p in self.properties_processes_mpls_traffic_eng_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.processes_dict['mpls'] = dict()
            self.processes_dict['mpls']['traffic_eng'] = deepcopy(d) 

    def populate_processes_passive_interface(self):
        d = dict()
        for p in self.properties_processes_passive_interface_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.processes_dict['passive_interface'] = deepcopy(d) 

    def populate_processes_table_map(self):
        if self.properties['table_map_name'] == None:
            return
        d = dict()
        for p in self.properties_processes_table_map_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.processes_dict['table_map'] = deepcopy(d)

    def populate_processes_timers(self):
        d_timers = dict()
        for p in self.properties_processes_timers_lsa_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d_timers[mapped_p] = self.properties[p]

        d_throttle_lsa = dict()
        for p in self.properties_processes_timers_throttle_lsa_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d_throttle_lsa[mapped_p] = self.properties[p]
        if len(d_throttle_lsa) > 0 and len(d_throttle_lsa) != 3:
            self.task_log.error('exiting. If one parameter associated with timers_throttle_lsa is set, all parameters must be set.')
            self.task_log.error('Got the following:')
            self.task_log.error('lsa_hold_interval {}'.format(self.timers_throttle_lsa_hold_interval))
            self.task_log.error('lsa_max_interval {}'.format(self.timers_throttle_lsa_max_interval))
            self.task_log.error('lsa_start_interval {}'.format(self.timers_throttle_lsa_start_interval))
            exit(1)

        d_throttle_spf = dict()
        for p in self.properties_processes_timers_throttle_spf_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d_throttle_spf[mapped_p] = self.properties[p]

        if len(d_throttle_spf) > 0 and len(d_throttle_spf) != 3:
            self.task_log.error('exiting. If one parameter associated with timers_throttle_spf is set, all parameters must be set.')
            self.task_log.error('Got the following:')
            self.task_log.error('initial_spf_delay {}'.format(self.timers_throttle_spf_initial_spf_delay))
            self.task_log.error('max_wait_time {}'.format(self.timers_throttle_spf_max_wait_time))
            self.task_log.error('min_hold_time {}'.format(self.timers_throttle_spf_min_hold_time))
            exit(1)

        d_throttle = dict()
        if len(d_throttle_lsa) == 3:
            d_throttle['lsa'] = deepcopy(d_throttle_lsa)
        if len(d_throttle_spf) == 3:
            d_throttle['spf'] = deepcopy(d_throttle_spf)
        if len(d_throttle) != 0:
            d_timers['throttle'] = deepcopy(d_throttle)
        if len(d_timers) != 0:
            self.processes_dict['timers'] = deepcopy(d_timers) 

    def populate_processes_top_level(self):
        d = dict()
        for p in self.properties_processes_top_level_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                self.processes_dict[mapped_p] = self.properties[p]

    def add_range(self):
        self.populate_areas_ranges()
        self.init_areas_ranges()

    def verify_add_area(self):
        if self.area_id == None:
            self.task_log.error('exiting. call instance.area_id before calling instance.add_area()')
            exit(1)

    def add_area(self):
        self.verify_add_area()

        self.populate_areas_authentication()
        self.populate_areas_filter_list()
        self.populate_areas_nssa()
        self.populate_areas_stub()
        self.populate_areas_top_level()
        areas_dict_no_null = self.remove_null_from_dict(deepcopy(self.areas_dict))
        areas_dict_no_null = self.remove_empty_list_from_dict(deepcopy(areas_dict_no_null))
        self.processes_dict['areas'].append(deepcopy(areas_dict_no_null))
        self.init_areas_dict()
        self.init_areas_authentication()
        self.init_areas_filter_list()
        self.init_areas_nssa()
        self.init_areas_nssa_translate_type7()
        self.init_areas_ranges()
        self.init_areas_stub()
        self.init_areas_top_level()

    def add_process(self):
        if self.process_id == None:
            self.task_log.error('exiting. call instance.process_id before calling instance.add_process()')
            exit(1)
        self.populate_processes_auto_cost()
        self.populate_processes_default_information_originate()
        self.populate_processes_graceful_restart()
        self.populate_processes_log_adjacency_changes()
        self.populate_processes_max_lsa()
        self.populate_processes_max_metric()
        self.populate_processes_mpls_traffic_eng()
        self.populate_processes_passive_interface()
        self.populate_processes_table_map()
        self.populate_processes_timers()
        self.populate_processes_top_level()
        d_no_null = self.remove_null_from_dict(self.processes_dict)
        d_no_list = self.remove_empty_list_from_dict(deepcopy(d_no_null))
        if len(self.vrfs) != 0:
            d_no_list['vrfs'] = deepcopy(self.vrfs)
            self.vrfs = list()
        self.config['processes'].append(deepcopy(d_no_list))
        self.init_areas_dict()
        self.init_areas_authentication()
        self.init_areas_filter_list()
        self.init_areas_nssa()
        self.init_areas_nssa_translate_type7()
        self.init_areas_ranges()
        self.init_areas_stub()
        self.init_areas_top_level()
        self.init_processes_dict()

    def verify_add_redistribute(self):
        if self.properties['redistribute_protocol'] == None:
            self.task_log.error('exiting. redistribute_protocol must be set before calling add_redistribute()')
            exit(1)
        if self.properties['redistribute_route_map'] == None:
            self.task_log.error('exiting. redistribute_route_map must be set before calling add_redistribute()')
            exit(1)
    def add_redistribute(self):
        '''
        Create redistribute dict() and append to processes_dict['redistribute']
        '''
        self.verify_add_redistribute()
        d = dict()
        for p in self.properties_processes_redistribute_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.processes_dict['redistribute'].append(deepcopy(d))
        self.init_processes_redistribute()

    def verify_add_summary_address(self):
        if self.properties['summary_address_prefix'] == None:
            self.task_log.error('exiting. summary_address_prefix must be set before calling add_summary_address()')
            exit(1)
    def add_summary_address(self):
        '''
        Create summary_address dict() and append to processes_dict['summary_address']
        '''
        self.verify_add_summary_address()
        d = dict()
        for p in self.properties_summary_address_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.processes_dict['summary_address'].append(deepcopy(d))
        self.init_processes_summary_address()

    def add_vrf(self):
        if self.properties['vrf'] == None:
            self.task_log.error('exiting. vrf must be set before calling add_vrf()')
            exit(1)
        self.processes_dict['vrf'] = self.vrf
        self.populate_processes_auto_cost()
        self.populate_processes_default_information_originate()
        self.populate_processes_graceful_restart()
        self.populate_processes_log_adjacency_changes()
        self.populate_processes_max_lsa()
        self.populate_processes_max_metric()
        self.populate_processes_mpls_traffic_eng()
        self.populate_processes_passive_interface()
        self.populate_processes_table_map()
        self.populate_processes_timers()
        self.populate_processes_top_level()
        d_no_null = self.remove_null_from_dict(self.processes_dict)
        processes_dict = self.remove_empty_list_from_dict(deepcopy(d_no_null))
        if 'vrfs' in processes_dict:
            del processes_dict['vrfs']
        if 'process_id' in processes_dict:
            del processes_dict['process_id']
        self.vrfs.append(deepcopy(processes_dict))
        self.vrf = None
        # save process_id and reinstate it after initializing processes_dict()
        process_id = deepcopy(self.process_id)
        self.init_areas_dict()
        self.init_areas_authentication()
        self.init_areas_filter_list()
        self.init_areas_nssa()
        self.init_areas_nssa_translate_type7()
        self.init_areas_ranges()
        self.init_areas_stub()
        self.init_areas_top_level()
        self.init_processes_dict()
        self.process_id = process_id

    def init_properties(self):
        self.vrfs = list() # cleared in add_process(), appended to in add_vrf()
        self.properties = dict()
        self.properties['state'] = None
        self.properties['task_name'] = None
        self.properties['register'] = None
        self.properties['running_config'] = None
        self.properties['vrf'] = None
        self.init_areas_authentication()
        self.init_areas_dict()
        self.init_areas_filter_list()
        self.init_areas_nssa()
        self.init_areas_nssa_translate_type7()
        self.init_areas_ranges()
        self.init_areas_stub()
        self.init_areas_top_level()
        self.init_processes_dict()
        # self.init_areas_vrf_dict() # TODO: figure out areas['vrfs']

    def init_areas_dict(self):
        '''
        initialize areas top-level properties
        called from:
            self.add_area()
            self.add_process()
            self.add_vrf()
            self.init_properties()
        '''
        self.areas_dict = dict()
        self.areas_dict['filter_list'] = list()
        self.areas_dict['ranges'] = list()

    def init_areas_authentication(self):
        '''
        called from:
            self.add_area()
            self.add_process()
            self.add_vrf()
            self.init_properties()
        '''
        for p in self.properties_areas_authentication_set:
            self.properties[p] = None

    def init_areas_filter_list(self):
        '''
        called from:
            self.add_area()
            self.add_process()
            self.add_vrf()
            self.init_properties()
        '''
        for p in self.properties_areas_filter_list_set:
            self.properties[p] = None

    def init_areas_nssa(self):
        '''
        called from:
            self.add_area()
            self.add_process()
            self.add_vrf()
            self.init_properties()
        '''
        for p in self.properties_areas_nssa_set:
            self.properties[p] = None

    def init_areas_nssa_translate_type7(self):
        '''
        called from:
            self.add_area()
            self.add_process()
            self.add_vrf()
            self.init_properties()
        '''
        for p in self.properties_areas_nssa_translate_type7_set:
            self.properties[p] = None

    def init_areas_ranges(self):
        '''
        Called from:
            init_properties()
            add_range()
            add_area()
            add_process()
        '''
        for p in self.properties_areas_ranges_set:
            self.properties[p] = None

    def init_areas_stub(self):
        '''
        called from
            init_properties()
        '''
        for p in self.properties_areas_stub_set:
            self.properties[p] = None

    def init_areas_top_level(self):
        for p in self.properties_areas_top_level_set:
            self.properties[p] = None

    def init_processes_dict(self):
        self.processes_dict = dict()
        self.processes_dict['areas'] = list()
        self.init_processes_auto_cost()
        self.init_processes_default_information()

        self.init_processes_graceful_restart()
        self.init_processes_log_adjacency_changes()
        self.init_processes_max_lsa()
        self.init_processes_max_metric()
        self.init_processes_mpls_traffic_eng()
        self.init_processes_passive_interface()
        self.init_processes_redistribute()
        self.processes_dict['redistribute'] = list()  # list(), list of self.processes_redistribute_dict

        self.processes_dict['summary_address'] = list() # list of self.processes_summary_address_dict
        self.init_processes_summary_address()
        self.init_processes_table_map()
        self.init_processes_timers_lsa()
        self.init_processes_timers_throttle_lsa()
        self.init_processes_timers_throttle_spf()
        self.init_processes_top_level()
        self.processes_dict['vrfs'] = list() # list of modified self.processes_dict. See add_vrf()

    def init_processes_auto_cost(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_auto_cost_set:
            self.properties[p] = None

    def init_processes_default_information(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_default_information_originate_set:
            self.properties[p] = None


    def init_processes_graceful_restart(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_graceful_restart_set:
            self.properties[p] = None

    def init_processes_log_adjacency_changes(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_log_adjacency_changes_set:
            self.properties[p] = None


    def init_processes_max_lsa(self):
        '''
        called from self.init_processes_dict()
        '''
        self.properties['max_lsa_ignore_count']                 = None  # int(), Set count on how many times adjacencies can be suppressed
        self.properties['max_lsa_ignore_time']                  = None  # int(), Set count on how many times adjacencies can be suppressed
        self.properties['max_lsa_max_non_self_generated_lsa']   = None  # int(), required, Set the maximum number of non self-generated LSAs
        self.properties['max_lsa_reset_time']                   = None  # int(), Set number of minutes after which ignore-count is reset to zero
        self.properties['max_lsa_threshold']                    = None  # int(), Threshold value (%) at which to generate a warning message
        self.properties['max_lsa_warning_only']                 = None  # bool(), False, True, Log a warning message when limit is exceeded

    def init_processes_max_metric(self):
        '''
        called from self.init_processes_dict()
        '''
        self.init_processes_max_metric_router_lsa()
        self.init_processes_max_metric_router_lsa_external_lsa()
        self.init_processes_max_metric_router_lsa_on_startup()
        self.init_processes_max_metric_router_lsa_summary_lsa()

    def init_processes_max_metric_router_lsa(self):
        '''
        called from self.init_processes_max_metric()
        '''
        self.properties['max_metric_router_lsa_include_stub'] = None
        self.properties['max_metric_router_lsa_set'] = None

    def init_processes_max_metric_router_lsa_external_lsa(self):
        '''
        called from: init_processes_max_metric()
        if set, these properties will be added to:
            self.processes_dict['max_metric']['router_lsa']['external_lsa']['max_metric_value']
            self.processes_dict['max_metric']['router_lsa']['external_lsa']['set']
        '''
        self.properties['max_metric_router_lsa_external_lsa_max_metric_value'] = None
        self.properties['max_metric_router_lsa_external_lsa_set'] = None

    def init_processes_max_metric_router_lsa_on_startup(self):
        '''
        called from: init_processes_max_metric()
        if set, these properties will be added to:
            self.processes_dict['max_metric']['router_lsa']['on_startup']['set']
            self.processes_dict['max_metric']['router_lsa']['on_startup']['wait_for_bgp_asn']
            self.processes_dict['max_metric']['router_lsa']['on_startup']['wait_period']
        '''
        self.properties['max_metric_router_lsa_on_startup_set'] = None
        self.properties['max_metric_router_lsa_on_startup_wait_for_bgp_asn'] = None
        self.properties['max_metric_router_lsa_on_startup_wait_period'] = None


    def init_processes_max_metric_router_lsa_summary_lsa(self):
        '''
        called from: init_processes_max_metric()
        if set, these properties will be added to:
            self.processes_dict['max_metric']['router_lsa']['summary_lsa']['set']
            self.processes_dict['max_metric']['router_lsa']['summary_lsa']['max_metric_value']
        '''
        self.properties['max_metric_router_lsa_summary_lsa_set'] = None
        self.properties['max_metric_router_lsa_summary_lsa_max_metric_value'] = None

    def init_processes_mpls_traffic_eng(self):
        '''
        called from self.init_processes_mpls_dict()
        '''
        self.properties['mpls_traffic_eng_areas'] = list()
        for p in self.properties_processes_mpls_traffic_eng_set:
            self.properties[p] = None

    def init_processes_passive_interface(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_passive_interface_set:
            self.properties[p] = None

    def init_processes_redistribute(self):
        '''
        Called from add_redistribute() and init_processes_dict()
        These are appended to self.processes_dict['redistribute'] in add_redistribute()
        '''
        for p in self.properties_processes_redistribute_set:
            self.properties[p] = None

    def init_processes_summary_address(self):
        '''
        Called from add_summary_address()
        These are appended to self.processes_dict['summary_address'] in add_summary_address()
        '''
        for p in self.properties_summary_address_set:
            self.properties[p] = None

    def init_processes_table_map(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_table_map_set:
            self.properties[p] = None

    def init_processes_timers_lsa(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_timers_lsa_set:
            self.properties[p] = None

    def init_processes_timers_throttle_lsa(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_timers_throttle_lsa_set:
            self.properties[p] = None

    def init_processes_timers_throttle_spf(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_timers_throttle_spf_set:
            self.properties[p] = None

    def init_processes_top_level(self):
        '''
        called from self.init_processes_dict()
        '''
        for p in self.properties_processes_top_level_set:
            self.properties[p] = None

    def nxos_ospfv2_verify_auto_cost_unit(self, x, parameter='auto_cost_unit'):
        verify_set = self.nxos_ospfv2_valid_auto_cost_unit
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_auto_cost_unit'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_area_id(self, x, parameter='area_id'):
        if self.is_digits(x):
            return
        if self.is_ipv4_address(x):
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_area_id'
        expectation = 'digits or ipv4 address'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_default_cost(self, x, parameter='default_cost'):
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_default_cost'
        expectation = 'digits'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_graceful_restart_grace_period(self, x, parameter='grace_period'):
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_graceful_restart_grace_period'
        expectation = 'digits'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_filter_list_direction(self, x, parameter='filter_list_direction'):
        verify_set = self.nxos_ospfv2_valid_filter_list_direction
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_filter_list_direction'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_maximum_paths(self, x, parameter='maximum_paths'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
        self.verify_integer_range(x, 1, 64, self.class_name, parameter)

    def nxos_ospfv2_verify_mpls_traffic_eng_router_id_interface(self, x, parameter='router_id'):
        for interface in self.nxos_ospfv2_valid_mpls_traffic_eng_router_id_interfaces:
            if interface in x:
                return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_mpls_traffic_eng_router_id_interface'
        expectation = 'An interface type of either {}'.format(','.join(self.nxos_ospfv2_valid_mpls_traffic_eng_router_id_interfaces))
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_redistribute_protocol(self, x, parameter='redistribute_protocol'):
        verify_set = self.nxos_ospfv2_valid_redistribute_protocol
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_redistribute_protocol'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_router_id(self, x, parameter='router_id'):
        if self.is_ipv4_address(x):
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_router_id'
        expectation = "IPv4 Address without prefixlen. Example: 134.45.1.1"
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_summary_address_prefix(self, x, parameter='summary_address_prefix'):
        if self.is_ipv4_network(x):
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_summary_address_prefix'
        expectation = "IPv4 Network summary with prefixlen. Example: 134.45.1.0/24"
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_summary_address_tag(self, x, parameter='summary_address_tag'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 0, 4294967295, self.class_name, parameter)

    #---------------------------------
    # max_lsa verification START
    #---------------------------------
    def nxos_ospfv2_verify_max_lsa_ignore_count(self, x, parameter='max_lsa_ignore_count'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 4294967295, self.class_name, parameter)
    def nxos_ospfv2_verify_max_lsa_ignore_time(self, x, parameter='max_lsa_ignore_time'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 1440, self.class_name, parameter)
    def nxos_ospfv2_verify_max_lsa_max_non_self_generated_lsa(self, x, parameter='max_lsa_max_non_self_generated_lsa'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 4294967295, self.class_name, parameter)
    def nxos_ospfv2_verify_max_lsa_reset_time(self, x, parameter='max_lsa_reset_time'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 1440, self.class_name, parameter)
    def nxos_ospfv2_verify_max_lsa_threshold(self, x, parameter='max_lsa_threshold'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 100, self.class_name, parameter)
    #---------------------------------
    # max_lsa verification END
    #---------------------------------

    #---------------------------------
    # max_metric verification START
    #---------------------------------
    def nxos_ospfv2_verify_max_metric_router_lsa_external_lsa_max_metric_value(self, x, parameter='max_metric_router_lsa_external_lsa_max_metric_value'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 16777215, self.class_name, parameter) # Range from N9K-C93180YC-FX + 9.3(6) CCO

    def nxos_ospfv2_verify_max_metric_router_lsa_on_startup_wait_for_bgp_asn(self, x, parameter='max_metric_router_lsa_on_startup_wait_for_bgp_asn'):
        self.verify_bgp_asn(x, parameter) # inherited from AnsCommon

    def nxos_ospfv2_verify_max_metric_router_lsa_on_startup_wait_period(self, x, parameter='max_metric_router_lsa_on_startup_wait_period'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 5, 86400, self.class_name, parameter) # Range from N9K-C93180YC-FX + 9.3(6) CCO

    def nxos_ospfv2_verify_max_metric_router_lsa_summary_lsa_max_metric_value(self, x, parameter='max_metric_router_lsa_summary_lsa_max_metric_value'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 16777215, self.class_name, parameter) # Range from N9K-C93180YC-FX + 9.3(6) CCO
    #---------------------------------
    # max_metric verification END
    #---------------------------------

    def nxos_ospfv2_verify_process_id(self, x, parameter='process_id'):
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_process_id'
        expectation = 'digits'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_ospfv2_verify_state(self, x, parameter='state'):
        verify_set = self.nxos_ospfv2_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_ospfv2_verify_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    #---------------------------------
    # timers verification START
    #---------------------------------

    def nxos_ospfv2_verify_timers_lsa_arrival(self, x, parameter='timers_lsa_arrival'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 10, 600000, self.class_name, parameter) #  10-600000 (milliseconds), default 1000

    def nxos_ospfv2_verify_timers_lsa_group_pacing(self, x, parameter='timers_lsa_group_pacing'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 1800, self.class_name, parameter) #  1-1800 (seconds)

    def nxos_ospfv2_verify_timers_throttle_lsa_hold_interval(self, x, parameter='timers_throttle_lsa_hold_interval'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 50, 30000, self.class_name, parameter) #  50-30000 (milliseconds), default 5000

    def nxos_ospfv2_verify_timers_throttle_lsa_max_interval(self, x, parameter='timers_throttle_lsa_max_interval'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 50, 30000, self.class_name, parameter) #  50-30000 (milliseconds), default 5000

    def nxos_ospfv2_verify_timers_throttle_lsa_start_interval(self, x, parameter='timers_throttle_lsa_start_interval'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 0, 5000, self.class_name, parameter) #  0-5000 (milliseconds), default 0

    def nxos_ospfv2_verify_timers_throttle_spf_initial_spf_delay(self, x, parameter='timers_throttle_spf_initial_spf_delay'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 600000, self.class_name, parameter) #  1-600000 (milliseconds), default 200

    def nxos_ospfv2_verify_timers_throttle_spf_max_wait_time(self, x, parameter='timers_throttle_spf_max_wait_time'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 600000, self.class_name, parameter) #  1-600000 (milliseconds), default 5000

    def nxos_ospfv2_verify_timers_throttle_spf_min_hold_time(self, x, parameter='timers_throttle_spf_min_hold_time'):
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 1, 600000, self.class_name, parameter) #  1-600000 (milliseconds), default 1000

    #---------------------------------
    # timers verification END
    #---------------------------------

    #-----------------------------------------------------------------------
    # areas_dict properties
    #-----------------------------------------------------------------------
    @property
    def area_id(self):
        return self.properties['area_id']
    @area_id.setter
    def area_id(self, x):
        parameter = 'area_id'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_area_id(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def authentication_message_digest(self):
        return self.properties['authentication_message_digest']
    @authentication_message_digest.setter
    def authentication_message_digest(self, x):
        parameter = 'authentication_message_digest'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def authentication_set(self):
        return self.properties['authentication_set']
    @authentication_set.setter
    def authentication_set(self, x):
        parameter = 'authentication_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def default_cost(self):
        return self.properties['default_cost']
    @default_cost.setter
    def default_cost(self, x):
        parameter = 'default_cost'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_default_cost(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def filter_list_direction(self):
        return self.properties['filter_list_direction']
    @filter_list_direction.setter
    def filter_list_direction(self, x):
        parameter = 'filter_list_direction'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_filter_list_direction(x, parameter)
        self.properties[parameter] = x

    @property
    def filter_list_route_map(self):
        return self.properties['filter_list_route_map']
    @filter_list_route_map.setter
    def filter_list_route_map(self, x):
        parameter = 'filter_list_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def nssa_default_information_originate(self):
        return self.properties['nssa_default_information_originate']
    @nssa_default_information_originate.setter
    def nssa_default_information_originate(self, x):
        parameter = 'nssa_default_information_originate'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def nssa_no_redistribution(self):
        return self.properties['nssa_no_redistribution']
    @nssa_no_redistribution.setter
    def nssa_no_redistribution(self, x):
        parameter = 'nssa_no_redistribution'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def nssa_no_summary(self):
        return self.properties['nssa_no_summary']
    @nssa_no_summary.setter
    def nssa_no_summary(self, x):
        parameter = 'nssa_no_summary'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def nssa_set(self):
        return self.properties['nssa_set']
    @nssa_set.setter
    def nssa_set(self, x):
        parameter = 'nssa_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def nssa_translate_type7_always(self):
        return self.properties['nssa_translate_type7_always']
    @nssa_translate_type7_always.setter
    def nssa_translate_type7_always(self, x):
        parameter = 'nssa_translate_type7_always'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def nssa_translate_type7_never(self):
        return self.properties['nssa_translate_type7_never']
    @nssa_translate_type7_never.setter
    def nssa_translate_type7_never(self, x):
        parameter = 'nssa_translate_type7_never'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def nssa_translate_type7_supress_fa(self):
        return self.properties['nssa_translate_type7_supress_fa']
    @nssa_translate_type7_supress_fa.setter
    def nssa_translate_type7_supress_fa(self, x):
        parameter = 'nssa_translate_type7_supress_fa'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def register(self):
        return self.properties['register']
    @register.setter
    def register(self, x):
        parameter = 'register'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def running_config(self):
        return self.properties['running_config']
    @running_config.setter
    def running_config(self, x):
        parameter = 'running_config'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def stub_no_summary(self):
        return self.properties['stub_no_summary']
    @stub_no_summary.setter
    def stub_no_summary(self, x):
        parameter = 'stub_no_summary'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def stub_set(self):
        return self.properties['stub_set']
    @stub_set.setter
    def stub_set(self, x):
        parameter = 'stub_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    #-----------------------------------------------------------------------
    # processes_dict properties
    #-----------------------------------------------------------------------

    @property
    def auto_cost_reference_bandwidth(self):
        return self.properties['auto_cost_reference_bandwidth']
    @auto_cost_reference_bandwidth.setter
    def auto_cost_reference_bandwidth(self, x):
        parameter = 'auto_cost_reference_bandwidth'
        if self.set_none(x, parameter):
            return
        # TODO: need better verification in populate_processes_auto_cost() which takes into account auto_cost_unit
        self.verify_integer_range(x, 1, 4000000, self.class_name, parameter)
        self.properties[parameter] = str(x)

    @property
    def auto_cost_unit(self):
        return self.properties['auto_cost_unit']
    @auto_cost_unit.setter
    def auto_cost_unit(self, x):
        parameter = 'auto_cost_unit'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_auto_cost_unit(x, parameter)
        self.properties[parameter] = x

    @property
    def bfd(self):
        return self.properties['bfd']
    @bfd.setter
    def bfd(self, x):
        parameter = 'bfd'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def default_information_originate_always(self):
        return self.properties['default_information_originate_always']
    @default_information_originate_always.setter
    def default_information_originate_always(self, x):
        parameter = 'default_information_originate_always'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def default_information_originate_route_map(self):
        return self.properties['default_information_originate_route_map']
    @default_information_originate_route_map.setter
    def default_information_originate_route_map(self, x):
        parameter = 'default_information_originate_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def default_information_originate_set(self):
        return self.properties['default_information_originate_set']
    @default_information_originate_set.setter
    def default_information_originate_set(self, x):
        parameter = 'default_information_originate_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def default_metric(self):
        return self.properties['default_metric']
    @default_metric.setter
    def default_metric(self, x):
        parameter = 'default_metric'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 16777214, self.class_name, parameter)
        self.properties[parameter] = str(x)

    @property
    def distance(self):
        return self.properties['distance']
    @distance.setter
    def distance(self, x):
        parameter = 'distance'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 255, self.class_name, parameter)
        self.properties[parameter] = str(x)

    @property
    def flush_routes(self):
        return self.properties['flush_routes']
    @flush_routes.setter
    def flush_routes(self, x):
        parameter = 'flush_routes'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def graceful_restart_grace_period(self):
        return self.properties['graceful_restart_grace_period']
    @graceful_restart_grace_period.setter
    def graceful_restart_grace_period(self, x):
        parameter = 'graceful_restart_grace_period'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_graceful_restart_grace_period(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def graceful_restart_helper_disable(self):
        return self.properties['graceful_restart_helper_disable']
    @graceful_restart_helper_disable.setter
    def graceful_restart_helper_disable(self, x):
        parameter = 'graceful_restart_helper_disable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def graceful_restart_set(self):
        return self.properties['graceful_restart_set']
    @graceful_restart_set.setter
    def graceful_restart_set(self, x):
        parameter = 'graceful_restart_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def isolate(self):
        return self.properties['isolate']
    @isolate.setter
    def isolate(self, x):
        parameter = 'isolate'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def log_adjacency_changes_detail(self):
        return self.properties['log_adjacency_changes_detail']
    @log_adjacency_changes_detail.setter
    def log_adjacency_changes_detail(self, x):
        parameter = 'log_adjacency_changes_detail'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def log_adjacency_changes_log(self):
        return self.properties['log_adjacency_changes_log']
    @log_adjacency_changes_log.setter
    def log_adjacency_changes_log(self, x):
        parameter = 'log_adjacency_changes_log'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def max_lsa_ignore_count(self):
        return self.properties['max_lsa_ignore_count']
    @max_lsa_ignore_count.setter
    def max_lsa_ignore_count(self, x):
        parameter = 'max_lsa_ignore_count'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_max_lsa_ignore_count(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def max_lsa_ignore_time(self):
        return self.properties['max_lsa_ignore_time']
    @max_lsa_ignore_time.setter
    def max_lsa_ignore_time(self, x):
        parameter = 'max_lsa_ignore_time'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_max_lsa_ignore_time(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def max_lsa_max_non_self_generated_lsa(self):
        return self.properties['max_lsa_max_non_self_generated_lsa']
    @max_lsa_max_non_self_generated_lsa.setter
    def max_lsa_max_non_self_generated_lsa(self, x):
        parameter = 'max_lsa_max_non_self_generated_lsa'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_max_lsa_max_non_self_generated_lsa(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def max_lsa_reset_time(self):
        return self.properties['max_lsa_reset_time']
    @max_lsa_reset_time.setter
    def max_lsa_reset_time(self, x):
        parameter = 'max_lsa_reset_time'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_max_lsa_reset_time(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def max_lsa_threshold(self):
        return self.properties['max_lsa_threshold']
    @max_lsa_threshold.setter
    def max_lsa_threshold(self, x):
        parameter = 'max_lsa_threshold'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_max_lsa_threshold(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def max_lsa_warning_only(self):
        return self.properties['max_lsa_warning_only']
    @max_lsa_warning_only.setter
    def max_lsa_warning_only(self, x):
        parameter = 'max_lsa_warning_only'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x


    @property
    def max_metric_router_lsa_include_stub(self):
        return self.properties['max_metric_router_lsa_include_stub']
    @max_metric_router_lsa_include_stub.setter
    def max_metric_router_lsa_include_stub(self, x):
        parameter = 'max_metric_router_lsa_include_stub'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def max_metric_router_lsa_set(self):
        return self.properties['max_metric_router_lsa_set']
    @max_metric_router_lsa_set.setter
    def max_metric_router_lsa_set(self, x):
        parameter = 'max_metric_router_lsa_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def max_metric_router_lsa_external_lsa_max_metric_value(self):
        return self.properties['max_metric_router_lsa_external_lsa_max_metric_value']
    @max_metric_router_lsa_external_lsa_max_metric_value.setter
    def max_metric_router_lsa_external_lsa_max_metric_value(self, x):
        parameter = 'max_metric_router_lsa_external_lsa_max_metric_value'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_max_metric_router_lsa_external_lsa_max_metric_value(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def max_metric_router_lsa_external_lsa_set(self):
        return self.properties['max_metric_router_lsa_external_lsa_set']
    @max_metric_router_lsa_external_lsa_set.setter
    def max_metric_router_lsa_external_lsa_set(self, x):
        parameter = 'max_metric_router_lsa_external_lsa_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def max_metric_router_lsa_on_startup_set(self):
        return self.properties['max_metric_router_lsa_on_startup_set']
    @max_metric_router_lsa_on_startup_set.setter
    def max_metric_router_lsa_on_startup_set(self, x):
        parameter = 'max_metric_router_lsa_on_startup_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def max_metric_router_lsa_on_startup_wait_for_bgp_asn(self):
        return self.properties['max_metric_router_lsa_on_startup_wait_for_bgp_asn']
    @max_metric_router_lsa_on_startup_wait_for_bgp_asn.setter
    def max_metric_router_lsa_on_startup_wait_for_bgp_asn(self, x):
        parameter = 'max_metric_router_lsa_on_startup_wait_for_bgp_asn'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_max_metric_router_lsa_on_startup_wait_for_bgp_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def max_metric_router_lsa_on_startup_wait_period(self):
        return self.properties['max_metric_router_lsa_on_startup_wait_period']
    @max_metric_router_lsa_on_startup_wait_period.setter
    def max_metric_router_lsa_on_startup_wait_period(self, x):
        parameter = 'max_metric_router_lsa_on_startup_wait_period'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_max_metric_router_lsa_on_startup_wait_period(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def max_metric_router_lsa_summary_lsa_set(self):
        return self.properties['max_metric_router_lsa_summary_lsa_set']
    @max_metric_router_lsa_summary_lsa_set.setter
    def max_metric_router_lsa_summary_lsa_set(self, x):
        parameter = 'max_metric_router_lsa_summary_lsa_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def max_metric_router_lsa_summary_lsa_set(self):
        return self.properties['max_metric_router_lsa_summary_lsa_set']
    @max_metric_router_lsa_summary_lsa_set.setter
    def max_metric_router_lsa_summary_lsa_set(self, x):
        parameter = 'max_metric_router_lsa_summary_lsa_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def max_metric_router_lsa_summary_lsa_max_metric_value(self):
        return self.properties['max_metric_router_lsa_summary_lsa_max_metric_value']
    @max_metric_router_lsa_summary_lsa_max_metric_value.setter
    def max_metric_router_lsa_summary_lsa_max_metric_value(self, x):
        parameter = 'max_metric_router_lsa_summary_lsa_max_metric_value'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_max_metric_router_lsa_summary_lsa_max_metric_value(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def maximum_paths(self):
        return self.properties['maximum_paths']
    @maximum_paths.setter
    def maximum_paths(self, x):
        parameter = 'maximum_paths'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_maximum_paths(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def mpls_traffic_eng_areas(self):
        return self.properties['mpls_traffic_eng_areas']
    @mpls_traffic_eng_areas.setter
    def mpls_traffic_eng_areas(self, x):
        parameter = 'mpls_traffic_eng_areas'
        if self.set_none(x, parameter):
            return
        if not self.is_digits(x) and not self.is_list(x):
            self.task_log.error('exiting. FF Expected digits or list() of digits for {}. Got {}'.format(parameter, v))
            exit(1)
        if self.is_digits(x):
            self.properties[parameter].append(x)
            return
        if self.is_list(x):
            for v in x:
                if not self.is_digits(v):
                    self.task_log.error('exiting. FF Expected digits or list() of digits for {}. Got {}'.format(parameter, v))
                    exit(1)
            self.properties[parameter] += x

    @property
    def mpls_traffic_eng_multicast_intact(self):
        return self.properties['mpls_traffic_eng_multicast_intact']
    @mpls_traffic_eng_multicast_intact.setter
    def mpls_traffic_eng_multicast_intact(self, x):
        parameter = 'mpls_traffic_eng_multicast_intact'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def mpls_traffic_eng_router_id(self):
        return self.properties['mpls_traffic_eng_router_id']
    @mpls_traffic_eng_router_id.setter
    def mpls_traffic_eng_router_id(self, x):
        '''
        An interface name associated with MPLS TE router-id
        Valid values: loopback, ethernet, port-channel
        Examples: loopback0, ethernet1/1, port-channel201
        '''
        parameter = 'mpls_traffic_eng_router_id'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_mpls_traffic_eng_router_id_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def name_lookup(self):
        return self.properties['name_lookup']
    @name_lookup.setter
    def name_lookup(self, x):
        parameter = 'name_lookup'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def passive_interface_default(self):
        return self.properties['passive_interface_default']
    @passive_interface_default.setter
    def passive_interface_default(self, x):
        parameter = 'passive_interface_default'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def process_id(self):
        return self.properties['process_id']
    @process_id.setter
    def process_id(self, x):
        parameter = 'process_id'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_process_id(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def ranges_cost(self):
        return self.properties['ranges_cost']
    @ranges_cost.setter
    def ranges_cost(self, x):
        parameter = 'ranges_cost'
        if self.set_none(x, parameter):
            return
        # TODO: add_verification
        self.properties[parameter] = x

    @property
    def ranges_not_advertise(self):
        return self.properties['ranges_not_advertise']
    @ranges_not_advertise.setter
    def ranges_not_advertise(self, x):
        parameter = 'ranges_not_advertise'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def ranges_prefix(self):
        return self.properties['ranges_prefix']
    @ranges_prefix.setter
    def ranges_prefix(self, x):
        parameter = 'ranges_prefix'
        if self.set_none(x, parameter):
            return
        # TODO: add_verification
        self.properties[parameter] = x

    @property
    def redistribute_id(self):
        return self.properties['redistribute_id']
    @redistribute_id.setter
    def redistribute_id(self, x):
        parameter = 'redistribute_id'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def redistribute_protocol(self):
        return self.properties['redistribute_protocol']
    @redistribute_protocol.setter
    def redistribute_protocol(self, x):
        parameter = 'redistribute_protocol'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_redistribute_protocol(x, parameter)
        self.properties[parameter] = x

    @property
    def redistribute_route_map(self):
        return self.properties['redistribute_route_map']
    @redistribute_route_map.setter
    def redistribute_route_map(self, x):
        parameter = 'redistribute_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def rfc1583compatibility(self):
        return self.properties['rfc1583compatibility']
    @rfc1583compatibility.setter
    def rfc1583compatibility(self, x):
        parameter = 'rfc1583compatibility'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def router_id(self):
        return self.properties['router_id']
    @router_id.setter
    def router_id(self, x):
        parameter = 'router_id'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_router_id(x, parameter)
        self.properties[parameter] = x

    @property
    def shutdown(self):
        return self.properties['shutdown']
    @shutdown.setter
    def shutdown(self, x):
        parameter = 'shutdown'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_state(x, parameter)
        self.properties[parameter] = x

    @property
    def summary_address_not_advertise(self):
        return self.properties['summary_address_not_advertise']
    @summary_address_not_advertise.setter
    def summary_address_not_advertise(self, x):
        parameter = 'summary_address_not_advertise'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def summary_address_prefix(self):
        return self.properties['summary_address_prefix']
    @summary_address_prefix.setter
    def summary_address_prefix(self, x):
        parameter = 'summary_address_prefix'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_summary_address_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def summary_address_tag(self):
        return self.properties['summary_address_tag']
    @summary_address_tag.setter
    def summary_address_tag(self, x):
        parameter = 'summary_address_tag'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_summary_address_tag(x, parameter)
        self.properties[parameter] = x

    @property
    def table_map_filter(self):
        return self.properties['table_map_filter']
    @table_map_filter.setter
    def table_map_filter(self, x):
        parameter = 'table_map_filter'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def table_map_name(self):
        return self.properties['table_map_name']
    @table_map_name.setter
    def table_map_name(self, x):
        parameter = 'table_map_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def timers_lsa_arrival(self):
        return self.properties['timers_lsa_arrival']
    @timers_lsa_arrival.setter
    def timers_lsa_arrival(self, x):
        parameter = 'timers_lsa_arrival'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_timers_lsa_arrival(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def timers_lsa_group_pacing(self):
        return self.properties['timers_lsa_group_pacing']
    @timers_lsa_group_pacing.setter
    def timers_lsa_group_pacing(self, x):
        parameter = 'timers_lsa_group_pacing'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_timers_lsa_group_pacing(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def timers_throttle_lsa_hold_interval(self):
        return self.properties['timers_throttle_lsa_hold_interval']
    @timers_throttle_lsa_hold_interval.setter
    def timers_throttle_lsa_hold_interval(self, x):
        parameter = 'timers_throttle_lsa_hold_interval'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_timers_throttle_lsa_hold_interval(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def timers_throttle_lsa_max_interval(self):
        return self.properties['timers_throttle_lsa_max_interval']
    @timers_throttle_lsa_max_interval.setter
    def timers_throttle_lsa_max_interval(self, x):
        parameter = 'timers_throttle_lsa_max_interval'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_timers_throttle_lsa_max_interval(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def timers_throttle_lsa_start_interval(self):
        return self.properties['timers_throttle_lsa_start_interval']
    @timers_throttle_lsa_start_interval.setter
    def timers_throttle_lsa_start_interval(self, x):
        parameter = 'timers_throttle_lsa_start_interval'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_timers_throttle_lsa_start_interval(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def timers_throttle_spf_initial_spf_delay(self):
        return self.properties['timers_throttle_spf_initial_spf_delay']
    @timers_throttle_spf_initial_spf_delay.setter
    def timers_throttle_spf_initial_spf_delay(self, x):
        parameter = 'timers_throttle_spf_initial_spf_delay'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_timers_throttle_spf_initial_spf_delay(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def timers_throttle_spf_max_wait_time(self):
        return self.properties['timers_throttle_spf_max_wait_time']
    @timers_throttle_spf_max_wait_time.setter
    def timers_throttle_spf_max_wait_time(self, x):
        parameter = 'timers_throttle_spf_max_wait_time'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_timers_throttle_spf_max_wait_time(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def timers_throttle_spf_min_hold_time(self):
        return self.properties['timers_throttle_spf_min_hold_time']
    @timers_throttle_spf_min_hold_time.setter
    def timers_throttle_spf_min_hold_time(self, x):
        parameter = 'timers_throttle_spf_min_hold_time'
        if self.set_none(x, parameter):
            return
        self.nxos_ospfv2_verify_timers_throttle_spf_min_hold_time(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def vrf(self):
        return self.properties['vrf']
    @vrf.setter
    def vrf(self, x):
        parameter = 'vrf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
