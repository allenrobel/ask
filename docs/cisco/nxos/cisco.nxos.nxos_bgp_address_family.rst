**************************************
NxosBgpAddressFamily()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
100

Status
------

- BETA

- This library is in development and not yet complete, nor fully-tested.
- See TODO below for missing functionality.

TODO
----

1. Support for states ``parsed`` and ``rendered`` not yet included
    - Hence ``running_config`` property is not yet supported
2. Verification of property mutual-exclusion not complete
3. Verification of required properties not complete
4. Verification of missing/dependent properties not complete

ScriptKit Synopsis
------------------
- NxosBgpAddressFamily() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp_address_family
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp_address_family <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_address_family_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp_address_family.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp_address_family.py>`_

NOTES
-----

|

========================    ==============================================
Method                      Description
========================    ==============================================
add_address_family()        Add an address-family to the address-family
                            list::

                                - Type: function()
                                - Example:
                                    task = NxosBgpAddressFamily(log)
                                    task.as_number = '12000.0'
                                    task.afi = 'ipv4'
                                    task.safi = 'unicast'
                                    task.add_address_family()
                                    task.afi = 'ipv6'
                                    task.safi = 'unicast'
                                    task.add_address_family()

add_aggregate_address()     Add an aggregate prefix to the aggregate list::

                                - Type: function()
                                - Example:
                                    task.aggregate_address_advertise_map = 'AGGR_MAP1'
                                    task.aggregate_address_as_set = True
                                    task.aggregate_address_attribute_map = 'ATTR_MAP1'
                                    task.aggregate_address_prefix = '10.251.0.0/16'
                                    task.aggregate_address_summary_only = False
                                    task.aggregate_address_suppress_map = 'SUPP_MAP1'
                                    task.add_aggregate_address()
                                    task.aggregate_address_advertise_map = 'AGGR_MAP2'
                                    task.aggregate_address_as_set = True
                                    task.aggregate_address_attribute_map = 'ATTR_MAP2'
                                    task.aggregate_address_prefix = '10.252.0.0/16'
                                    task.aggregate_address_summary_only = True
                                    task.add_aggregate_address()

add_inject_map()            Add an inject_map to the inject_map list::

                                - Type: function()
                                - Example:
                                    TODO

add_network()               Add a prefix to the networks list::

                                - Type: function()
                                - Example:
                                    task.afi = 'ipv4'
                                    task.safi = 'unicast'
                                    route_map = 'IPV4_ORIGINATE'
                                    for prefix in ['10.3.1.1/32', '10.3.4.0/25']:
                                        task.networks_prefix = prefix
                                        task.networks.route_map = route_map
                                        task.add_network()
                                    task.add_address_family()
                                    task.afi = 'ipv6'
                                    task.safi = 'unicast'
                                    route_map = 'IPV6_ORIGINATE'
                                    for prefix in ['2020::1/128', '2020:3:2::/48']
                                        task.networks_prefix = prefix
                                        task.networks.route_map = route_map
                                        task.add_network()
                                    task.add_address_family()

add_redistribute()          Add a protocol redistribution to the redistribute list::

                                - Type: function()
                                - Example:
                                    task.redistribute_id = 100
                                    task.redistribute_protocol = 'ospf'
                                    task.redistribute_route_map = 'REDIST_OSPF'
                                    task.add_redistribute()
                                    task.redistribute_id = 'Enterprise'
                                    task.redistribute_protocol = 'isis'
                                    task.redistribute_route_map = 'REDIST_ISIS'
                                    task.add_redistribute()

commit()                    Perform final verification and prepare the task
                            to be added to a playbook::

                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See ScriptKit Example link above

========================    ==============================================

|

====================================    ==============================================
Property                                Description
====================================    ==============================================
additional_paths_install_backup         Install backup path::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.additional_paths_install_backup = False

additional_paths_receive                Additional paths Receive capability::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.additional_paths_receive = True

additional_paths_selection_route_map    Additional paths receive capability::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.additional_paths_receive = True

additional_paths_send                   Additional paths send capability::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.additional_paths_send = True

====================================    ==============================================

|

================================    ==============================================
advertise_pip                       Advertise physical ip for type-5 route::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.advertise_pip = True

advertise_system_mac                Advertise extra EVPN RT-2 with system MAC::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.advertise_system_mac = False

afi                                 Address Family indicator::

                                        - Type: str()
                                        - Valid values:
                                            - ipv4
                                            - ipv6
                                            - link-state
                                            - vpnv4
                                            - vpnv6
                                            - l2vpn
                                        - Required
                                        - Example:
                                            task.afi = 'ipv4'

aggregate_address_advertise_map     Select attribute information from specific 
                                    routes::

                                        - Type: str()
                                        - Example:
                                            See add_aggregate_address()

aggregate_address_as_set            Generate AS-SET information::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            See add_aggregate_address()

aggregate_address_attribute_map     Set attribute information of aggregate::

                                        - Type: str()
                                        - Required if other advertise_map_* are set
                                        - Example:
                                            See add_aggregate_address()

aggregate_address_prefix            Aggregate prefix::

                                        - Type: str()
                                        - Required if other advertise_map_* are set
                                        - Example:
                                            See add_aggregate_address()

aggregate_address_summary_only      Do not advertise more specifics::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            See add_aggregate_address()

aggregate_address_suppress_map      Conditionally filter more specific routes::

                                        - Type: str()
                                        - Required if other advertise_map_* are set
                                        - Example:
                                            See add_aggregate_address()

allow_vni_in_ethertag               Allow VNI in Ethernet Tag field in EVPN route::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.allow_vni_in_ethertag = False

as_number                           BGP autonomous system number of the router::

                                        - Type: int() or str()
                                        - Valid values:
                                            - int() range 1-4294967295
                                            - str() <1-65535>.<0-65535>
                                        - Required
                                        - Examples:
                                            task.as_number = 64512
                                            task.as_number = 4200000000
                                            task.as_number = '2301.0'
                                        - NOTES:
                                            - private asn ranges
                                                - 64512 to 65534
                                                - 4200000000 to 4294967294

client_to_client_no_reflection      Reflection of routes permitted::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.client_to_client_no_reflection = True

dampen_igp_metric                   Dampen IGP metric-related changes::

                                        - Type: int()
                                        - Valid values: range: 20-3600
                                        - Default: 600
                                        - Units: seconds
                                        - Example:
                                            task.dampen_igp_metric = 300

dampening_decay_half_life           Decay half life::

                                        - Type: int()
                                        - Valid values: range: 1-45
                                        - Units: seconds
                                        - Example:
                                            task.dampening_decay_half_life = 30
                                        - NOTES
                                            - If one of these is set, ALL must be set
                                                - dampening_decay_half_life
                                                - dampening_max_suppress_time
                                                - dampening_start_reuse_route
                                                - dampening_start_suppress_route

dampening_max_suppress_time         Maximum suppress time for stable route::

                                        - Type: int()
                                        - Valid values: range: 1-255
                                        - Units: seconds
                                        - Example:
                                            task.dampening_max_suppress_time = 30
                                        - NOTES
                                            - If one of these is set, ALL must be set
                                                - dampening_decay_half_life
                                                - dampening_max_suppress_time
                                                - dampening_start_reuse_route
                                                - dampening_start_suppress_route

dampening_route_map                 Apply route-map to specify dampening criteria::

                                        - Type: str()
                                        - Example:
                                            task.dampening_route_map = 'DAMPEN_RM'

dampening_set                       Set route flap dampening::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.dampening_set = True

dampening_start_reuse_route         When the accumulated penalty decreases until
                                    the penalty drops to the ``dampening_start_reuse_route``
                                    threshold, the route is unsuppressed and made
                                    available to other devices in the network::

                                        - Type: int()
                                        - Valid values: range: 1-20000
                                        - Default: 1000
                                        - Units: accumulated penalty
                                        - Example:
                                            task.dampening_start_reuse_route = 2000
                                        - NOTES
                                            - If one of these is set, ALL must be set
                                                - dampening_decay_half_life
                                                - dampening_max_suppress_time
                                                - dampening_start_reuse_route
                                                - dampening_start_suppress_route

dampening_start_suppress_route      When the accumulated penalty exceeds the value of
                                    ``dampening_start_suppress_route`` the route is
                                    suppressed until the accumulated penalty falls below
                                    ``dampening_start_reuse_route``::

                                        - Type: int()
                                        - Valid values: range: 1-20000
                                        - Units: accumulated penalty
                                        - Example:
                                            task.dampening_start_suppress_route = 12000
                                        - NOTES
                                            - If one of these is set, ALL must be set
                                                - dampening_decay_half_life
                                                - dampening_max_suppress_time
                                                - dampening_start_reuse_route
                                                - dampening_start_suppress_route

default_information_originate       Originate and distribute a default route::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.default_information_originate = False

default_metric                      Set metric of redistributed routes::

                                        - Type: int()
                                        - Valid values: range: 0-4294967295
                                        - Example:
                                            task.default_metric = 300

distance_ebgp_routes                Administrative distance for EBGP routes::

                                        - Type: int()
                                        - Valid values: range: 1-255
                                        - Default: 20
                                        - Example:
                                            task.distance_ebgp_routes = 30
                                        - NOTES
                                            - If one of these is set, ALL must be set
                                                - distance_ebgp_routes
                                                - distance_ibgp_routes
                                                - distance_local_routes

distance_ibgp_routes                Administrative distance for IBGP routes::

                                        - Type: int()
                                        - Valid values: range: 1-255
                                        - Default: 200
                                        - Example:
                                            task.distance_ibgp_routes = 150
                                        - NOTES
                                            - If one of these is set, ALL must be set
                                                - distance_ebgp_routes
                                                - distance_ibgp_routes
                                                - distance_local_routes

distance_local_routes               Administrative distance for local routes::

                                        - Type: int()
                                        - Valid values: range: 1-255
                                        - Default: 220
                                        - Example:
                                            task.distance_local_routes = 210
                                        - NOTES
                                            - If one of these is set, ALL must be set
                                                - distance_ebgp_routes
                                                - distance_ibgp_routes
                                                - distance_local_routes

export_gateway_ip                   Export Gateway IP to Type-5 EVPN routes for VRF::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.export_gateway_ip = True

inject_map_copy_attributes          Copy attributes from aggregate::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.inject_map_copy_attributes = True

inject_map_exist_map                route-map which specifies exist condition::

                                        - Type: str()
                                        - Example:
                                            task.inject_map_exist_map = 'EXIST_MAP'

inject_map_route_map                route-map name::

                                        - Type: str()
                                        - Example:
                                            task.inject_map_route_map = 'INJECT_MAP'

================================    ==============================================

|


====================================    =========================================
Property                                Description
====================================    =========================================
maximum_paths_eibgp_parallel_paths      Number of parallel paths for both EBGP 
                                        and IBGP next-hops::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-64
                                            - Example:
                                                task.maximum_paths_eibgp_parallel_paths = 8

maximum_paths_ibgp_parallel_paths       Number of parallel paths for IBGP next-hops::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-64
                                            - Example:
                                                task.maximum_paths_ibgp_parallel_paths = 8

maximum_paths_local_parallel_paths      Number of parallel paths for local next-hops::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-64
                                            - Example:
                                                task.maximum_paths_local_parallel_paths = 8

maximum_paths_mixed_parallel_paths      Number of parallel paths for local and remote
                                        next-hops::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-64
                                            - Example:
                                                task.maximum_paths_mixed_parallel_paths = 8

maximum_paths_parallel_paths            Number of parallel paths::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-64
                                            - Example:
                                                task.maximum_paths_parallel_paths = 8

networks_prefix                         Prefix to advertise::

                                            - Type: str()
                                            - Valid values:
                                                - ipv4 prefix in CIDR format
                                                - ipv6 prefix in CIDR format
                                            - Example:
                                                task.afi = 'ipv4'
                                                task.safi = 'unicast'
                                                route_map = 'IPV4_ORIGINATE'
                                                for prefix in ['10.3.1.1/32', '10.3.4.0/25']:
                                                    task.networks_prefix = prefix
                                                    task.networks.route_map = route_map
                                                    task.add_network()
                                                task.add_address_family()
                                                task.afi = 'ipv6'
                                                task.safi = 'unicast'
                                                route_map = 'IPV6_ORIGINATE'
                                                for prefix in ['2020::1/128', '2020:3:2::/48']
                                                    task.networks_prefix = prefix
                                                    task.networks.route_map = route_map
                                                    task.add_network()
                                                task.add_address_family()
                                            NOTES:
                                                - Prefix must match address-family AFI/SAFI

networks_route_map                      route-map for ``networks_prefix``::

                                            - Type: str()
                                            - Valid values:
                                                - A route-map name
                                            - Example:
                                                - See networks_prefix

====================================    =========================================

|

============================================    =========================================
Property                                        Description
============================================    =========================================
nexthop_route_map                               Nexthop tracking route-map name::

                                                    - Type: str()
                                                    - Example:
                                                        task.nexthop_route_map = 'NEXTHOP_RM'

nexthop_trigger_delay_critical_delay            Set the delay to trigger nexthop tracking
                                                for changes affecting reachability::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 1-4294967295
                                                    - Default: 3000
                                                    - Units: milliseconds
                                                    - Example:
                                                        task.nexthop_trigger_delay_critical_delay = 4000
                                                    - NOTES:
                                                        - If one of these is set, all must be set
                                                            - nexthop_trigger_delay_critical_delay
                                                            - nexthop_trigger_delay_non_critical_delay

nexthop_trigger_delay_non_critical_delay        Set the delay to trigger nexthop tracking
                                                for other next-hop changes::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 1-4294967295
                                                    - Default: 10000
                                                    - Units: milliseconds
                                                    - Example:
                                                        task.nexthop_trigger_delay_non_critical_delay = 12000
                                                        - NOTES:
                                                            - If one of these is set, all must be set
                                                                - nexthop_trigger_delay_critical_delay
                                                                - nexthop_trigger_delay_non_critical_delay

============================================    =========================================

|

====================================    =========================================
Property                                Description
====================================    =========================================
redistribute_id                         The identifier for the specified protocol::

                                            - Type: int() or str()
                                            - Example:
                                                task.redistribute_id = 100
                                                task.redistribute_protocol = 'ospf'
                                                task.redistribute_route_map = 'REDIST_OSPF'
                                                task.add_redistribute()
                                                task.redistribute_id = 'Enterprise'
                                                task.redistribute_protocol = 'isis'
                                                task.redistribute_route_map = 'REDIST_ISIS'
                                                task.add_redistribute()

redistribute_protocol                   The name of the protocol::

                                            - Type: str()
                                            - Valid values:
                                                - am
                                                - direct
                                                - eigrp
                                                - isis
                                                - lisp
                                                - ospf
                                                - ospfv3
                                                - rip
                                                - static
                                            - Example:
                                                See redistribute_id

redistribute_route_map                  The route map policy to constrain
                                        redistribution::

                                            - Type: str()
                                            - Example:
                                                See redistribute_id

retain_route_target_retain_all          Retain all routes regardless of
                                        Target-VPN community::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.retain_route_target_retain_all = True

retain_route_target_route_map            Apply route-map to filter routes::

                                            - Type: str()
                                            - Example:
                                                task.retain_route_target_route_map = 'RETAIN_RT_MAP'

safi                                    Sub Address Family indicator::

                                            - Type: str()
                                            - Valid values:
                                                - evpn
                                                - multicast
                                                - mvpn
                                                - unicast
                                            - Required
                                            - Example:
                                                task.safi = 'unicast'

suppress_inactive                       Advertise only active routes to peers::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.suppress_inactive = True

table_map_filter                        Block the OSPF routes from being sent to RIB::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.table_map_filter = True

table_map_name                          route-map name defining policy for
                                        filtering/modifying OSPF routes before
                                        sending them to RIB::

                                            - Type: str()
                                            - Examples:
                                                - task.table_map_name = 'TABLE_MAP_RM'

task_name                               Name of the task. Ansible will display this
                                        when the playbook is run::

                                            - Type: str()
                                            - Examples:
                                                - task.task_name = 'my task'

====================================    =========================================

============================================    =========================================
Property                                        Description
============================================    =========================================
timers_bestpath_defer_defer_time                Bestpath defer time for batch prefix processing::

                                                    - Type: int()
                                                    - Valid values:
                                                        range: 100-3000
                                                    - Units: milliseconds
                                                    - Example:
                                                        task.timers_bestpath_defer_defer_time = 700
                                                    - NOTES:
                                                        - If one of these is set, all must be set
                                                            - timers_bestpath_defer_defer_time
                                                            - timers_bestpath_defer_maximum_defer_time

timers_bestpath_defer_maximum_defer_time        Bestpath defer time for batch prefix processing::

                                                    - Type: int()
                                                    - Valid values:
                                                        range: 300-300000
                                                    - Units: milliseconds
                                                    - Example:
                                                        task.timers_bestpath_defer_maximum_defer_time = 7000
                                                    - NOTES:
                                                        - If one of these is set, all must be set
                                                            - timers_bestpath_defer_defer_time
                                                            - timers_bestpath_defer_maximum_defer_time

============================================    =========================================

====================================    =========================================
Property                                Description
====================================    =========================================
vrf                                     Name of VRF in which bgp neighbor resides::

                                            - Type: str()
                                            - Examples:
                                                - task.vrf = 'MY_VRF'

wait_igp_convergence                    Delay initial bestpath until redistributed
                                        IGPs have converged::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.wait_igp_convergence = True

====================================    =========================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

