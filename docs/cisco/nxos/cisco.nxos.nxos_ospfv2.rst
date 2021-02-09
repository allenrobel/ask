***********************************
NxosOspfv2 - nxos_ospfv2.py
***********************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosOspfv2() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_ospfv2
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
and ``summary_address_not_advertise`` since this property name appears in both the ranges
and the summary_address dictionaries.

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
                                            - Valid values: no, yes

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
                                            - Valid values: no, yes

isolate                                 Isolate this router from OSPF perspective::

                                            - Type: bool()
                                            - Valid values: no, yes

maximum_paths                           Maximum paths per destination::

                                            - Type: int()
                                            - Example: task.maximum_paths = 16

name_lookup                             Display OSPF router ids as DNS names::

                                            - Type: bool()
                                            - Valid values: no, yes

process_id                              The OSPF process tag::

                                            - Type: str()
                                            - Example: task.process_id = 0
                                            - Required

rfc1583compatibility                    Configure RFC1583 compatibility for external path preferences::

                                            - Type: bool()
                                            - Valid values: no, yes

router_id                               OSPF process router-id::

                                            - Type: str()
                                            - Valid values: ivp4 address without prefixlen
                                            - Example: task.router_id = '10.0.1.1'

shutdown                                Shutdown the OSPF protocol instance::

                                            - Type: bool()
                                            - Valid values: no, yes

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
authentication_message_digest           Use message-digest authentication::

                                            - Type: bool()
                                            - Valid values: no, yes

authentication_set                      Set authentication for the area::

                                            - Type: bool()
                                            - Valid values: no, yes

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
                                                - Valid values: no, yes

default_information_originate_route_map     Policy to control distribution of default routes::

                                                - Type: str()

default_information_originate_set           Enable distribution of default route::

                                                - Type: bool()
                                                - Valid values: no, yes

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
                                            - Valid values: no, yes

graceful_restart_set                    Enable/Disable graceful-restart::

                                            - Type: bool()
                                            - Valid values: no, yes

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
log_adjacency_changes_detail            Notify all state changes::

                                            - Type: bool()
                                            - Valid values: no, yes

log_adjacency_changes_log               Enable/disable logging changes in adjacency state::

                                            - Type: bool()
                                            - Valid values: no, yes

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
                                            - Valid values: no, yes

======================================  ==================================================

|
|

====================================================    ==================================================
Property                                                Description
====================================================    ==================================================
max_metric_router_lsa_include_stub                      Advertise Max metric for Stub links as well::

                                                            - Type: bool()
                                                            - Valid values: no, yes

max_metric_router_lsa_set                               Set router-lsa attribute::

                                                            - Type: bool()
                                                            - Valid values: no, yes

max_metric_router_lsa_external_lsa_max_metric_value     max metric value for external LSAs::

                                                            - Type: int()
                                                            - Valid values: int()

max_metric_router_lsa_external_lsa_set                  Set external-lsa attribute::

                                                            - Type: bool()
                                                            - Valid values: no, yes

max_metric_router_lsa_on_startup_set                    Set on-startup attribute:

                                                            - Type: bool()
                                                            - Valid values: no, yes

max_metric_router_lsa_on_startup_wait_for_bgp_asn       ASN of BGP to wait for::

                                                            - Type: str()
                                                            - Valid values: An AS number

max_metric_router_lsa_on_startup_wait_period            Wait period in seconds after startup::

                                                            - Type: int()
                                                            - Valid values: int()

max_metric_router_lsa_summary_lsa_set                   Set summary-lsa attribute::

                                                            - Type: bool()
                                                            - Valid values: no, yes

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
                                            - Valid values: no, yes

mpls_traffic_eng_router_id              Interface used for Router ID associated with TE::

                                            - Type: str()
                                            - Example: task.mpls_traffic_eng_router_id = 'loopback2'
======================================  ==================================================

======================================  ==================================================
Property                                Description
======================================  ==================================================
nssa_default_information_originate      Originate Type-7 default LSA into NSSA area::

                                            - Type: bool()
                                            - Valid values: no, yes

nssa_no_redistribution                  Do not send redistributed LSAs into NSSA area::

                                            - Type: bool()
                                            - Valid values: no, yes

nssa_no_summary                         Do not send summary LSAs into NSSA area:: 

                                            - Type: bool()
                                            - Valid values: no, yes

nssa_set                                Configure area as NSSA::

                                            - Type: bool()
                                            - Valid values: no, yes

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
nssa_translate_type7_always             Always translate LSAs::

                                            - Type: bool()
                                            - Valid values: no, yes

nssa_translate_type7_never              Never translate LSAs::

                                            - Type: bool()
                                            - Valid values: no, yes

nssa_translate_type7_supress_fa         Suppress forwarding address in translated LSAs::

                                            - Type: bool()
                                            - Valid values: no, yes

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
passive_interface_default               Interfaces passive by default (Suppress routing 
                                        updates on the interface)::

                                            - Type: bool()
                                            - Valid values: no, yes

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
                                            - Valid values: no, yes

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

========================    ===================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
stub_no_summary                         Do not send summary LSAs into NSSA area::

                                            - Type: bool()
                                            - Valid values: no, yes

stub_set                                Configure area as NSSA::

                                            - Type: bool()
                                            - Valid values: no, yes

======================================  ==================================================

|
|

======================================  ==================================================
Property                                Description
======================================  ==================================================
summary_address_not_advertise           Supress advertising the specified summary::

                                            - Type: bool()
                                            - Valid values: no, yes

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
                                            - Valid values: no, yes

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
