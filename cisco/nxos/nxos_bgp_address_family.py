# NxosBgpAddressFamily() - cisco/nxos/nxos_bgp_address_family.py
our_version = 100
from copy import deepcopy
from ask.common.task import Task
'''
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

'''

class NxosBgpAddressFamily(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp_address_family'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.address_family_list = list()
        self.aggregate_address_list = list()
        self.inject_map_list = list()
        self.networks_list = list()
        self.redistribute_list = list()

        # The set of ansible module properties that should be written
        # when the user calls instance.commit().
        self.ansible_module_set = set()
        self.ansible_module_set.add('state')
        self.ansible_module_set.add('running_config')

        # Used in init_address_family() to clear all address
        # family properties
        self.address_family_set = set()
        self.address_family_set.add('additional_paths_install_backup')
        self.address_family_set.add('additional_paths_receive')
        self.address_family_set.add('additional_paths_selection_route_map')
        self.address_family_set.add('additional_paths_send')
        self.address_family_set.add('advertise_pip')
        self.address_family_set.add('advertise_system_mac')
        self.address_family_set.add('afi')
        self.address_family_set.add('aggregate_address_advertise_map')
        self.address_family_set.add('aggregate_address_as_set')
        self.address_family_set.add('aggregate_address_attribute_map')
        self.address_family_set.add('aggregate_address_prefix')
        self.address_family_set.add('aggregate_address_summary_only')
        self.address_family_set.add('aggregate_address_suppress_map')
        self.address_family_set.add('allow_vni_in_ethertag')
        self.address_family_set.add('client_to_client_no_reflection')
        self.address_family_set.add('dampen_igp_metric')
        self.address_family_set.add('dampening_decay_half_life')
        self.address_family_set.add('dampening_max_suppress_time')
        self.address_family_set.add('dampening_route_map')
        self.address_family_set.add('dampening_set')
        self.address_family_set.add('dampening_start_reuse_route')
        self.address_family_set.add('dampening_start_suppress_route')
        self.address_family_set.add('default_information_originate')
        self.address_family_set.add('default_metric')
        self.address_family_set.add('distance_ebgp_routes')
        self.address_family_set.add('distance_ibgp_routes')
        self.address_family_set.add('distance_local_routes')
        self.address_family_set.add('export_gateway_ip')
        self.address_family_set.add('inject_map_copy_attributes')
        self.address_family_set.add('inject_map_exist_map')
        self.address_family_set.add('inject_map_route_map')
        self.address_family_set.add('maximum_paths_eibgp_parallel_paths')
        self.address_family_set.add('maximum_paths_ibgp_parallel_paths')
        self.address_family_set.add('maximum_paths_local_parallel_paths')
        self.address_family_set.add('maximum_paths_mixed_parallel_paths')
        self.address_family_set.add('networks_prefix')
        self.address_family_set.add('networks_route_map')
        self.address_family_set.add('nexthop_route_map')
        self.address_family_set.add('nexthop_trigger_delay_critical_delay')
        self.address_family_set.add('nexthop_trigger_delay_non_critical_delay')
        self.address_family_set.add('redistribute_id')
        self.address_family_set.add('redistribute_protocol')
        self.address_family_set.add('redistribute_route_map')
        self.address_family_set.add('retain_route_target_retain_all')
        self.address_family_set.add('retain_route_target_route_map')
        self.address_family_set.add('safi')
        self.address_family_set.add('suppress_inactive')
        self.address_family_set.add('table_map_filter')
        self.address_family_set.add('table_map_name')
        self.address_family_set.add('timers_bestpath_defer_defer_time')
        self.address_family_set.add('timers_bestpath_defer_maximum_defer_time')
        self.address_family_set.add('vrf')
        self.address_family_set.add('wait_igp_convergence')

        # The set of atomic -- not members of a dict() -- 
        # properties.  Written when the user calls
        # instance.add_address_family().
        self.address_family_atomic_properties = set()
        self.address_family_atomic_properties.add('advertise_pip')
        self.address_family_atomic_properties.add('advertise_system_mac')
        self.address_family_atomic_properties.add('afi')
        self.address_family_atomic_properties.add('allow_vni_in_ethertag')
        self.address_family_atomic_properties.add('dampen_igp_metric')
        self.address_family_atomic_properties.add('default_metric')
        self.address_family_atomic_properties.add('export_gateway_ip')
        self.address_family_atomic_properties.add('safi')
        self.address_family_atomic_properties.add('suppress_inactive')
        self.address_family_atomic_properties.add('vrf')
        self.address_family_atomic_properties.add('wait_igp_convergence')

        # The set of atomic -- not members of a dict() --
        # aggregate address properties.
        # Written when the user calls instance.add_aggregate_address().
        # These will be written to the top-level of d dict()
        # before it is appended to self.aggregate_address_list
        self.aggregate_address_atomic_properties = set()
        self.aggregate_address_atomic_properties.add('aggregate_address_advertise_map')
        self.aggregate_address_atomic_properties.add('aggregate_address_as_set')
        self.aggregate_address_atomic_properties.add('aggregate_address_attribute_map')
        self.aggregate_address_atomic_properties.add('aggregate_address_prefix')
        self.aggregate_address_atomic_properties.add('aggregate_address_summary_only')
        self.aggregate_address_atomic_properties.add('aggregate_address_suppress_map')

        # Used in init_aggregate_address()
        self.aggregate_address_set = set()
        self.aggregate_address_set.add('aggregate_address_advertise_map')
        self.aggregate_address_set.add('aggregate_address_as_set')
        self.aggregate_address_set.add('aggregate_address_attribute_map')
        self.aggregate_address_set.add('aggregate_address_prefix')
        self.aggregate_address_set.add('aggregate_address_summary_only')
        self.aggregate_address_set.add('aggregate_address_suppress_map')

        # The set of atomic -- not members of a dict() --
        # inject_map properties.
        # Written when the user calls instance.add_inject_map().
        # These will be written to the top-level of d dict()
        # before it is appended to self.inject_map_list
        self.inject_map_atomic_properties = set()
        self.inject_map_atomic_properties.add('inject_map_copy_attributes')
        self.inject_map_atomic_properties.add('inject_map_exist_map')
        self.inject_map_atomic_properties.add('inject_map_route_map')

        # Used in init_inject_map()
        self.inject_map_set = set()
        self.inject_map_set.add('inject_map_copy_attributes')
        self.inject_map_set.add('inject_map_exist_map')
        self.inject_map_set.add('inject_map_route_map')

        # The set of atomic -- not members of a dict() --
        # networks properties.
        # Written when the user calls instance.add_network().
        # These will be written to the top-level of d dict()
        # before it is appended to self.networks_list
        self.networks_atomic_properties = set()
        self.networks_atomic_properties.add('networks_prefix')
        self.networks_atomic_properties.add('networks_route_map')

        # Used in init_networks()
        self.networks_set = set()
        self.networks_set.add('networks_prefix')
        self.networks_set.add('networks_route_map')

        # The set of atomic -- not members of a dict() --
        # redistribute properties.
        # Written when the user calls instance.add_redistribute().
        # These will be written to the top-level of d dict()
        # before it is appended to self.redistribute_list
        self.redistribute_atomic_properties = set()
        self.redistribute_atomic_properties.add('redistribute_id')
        self.redistribute_atomic_properties.add('redistribute_protocol')
        self.redistribute_atomic_properties.add('redistribute_route_map')

        # Used in init_redistribute()
        self.redistribute_set = set()
        self.redistribute_set.add('redistribute_id')
        self.redistribute_set.add('redistribute_protocol')
        self.redistribute_set.add('redistribute_route_map')

        # used to populate self.properties_set
        self.config_set = set()
        self.config_set.add('as_number')

        # The set of atomic -- not members of a dict() --
        # properties that should be written when 
        # the caller calls instance.commit()
        self.config_atomic = set()
        self.config_atomic.add('as_number')

        # propery_map is used to convert the disambiguated property
        # names that users access, to the (potentially) ambiguous 
        # property names that nxos_bgp_address_family uses.
        self.property_map = dict()
        self.property_map['as_number'] = 'as_number'
        self.property_map['additional_paths_install_backup'] = 'install_backup'
        self.property_map['additional_paths_receive'] = 'receive'
        self.property_map['additional_paths_selection_route_map'] = 'route_map'
        self.property_map['additional_paths_send'] = 'send'
        self.property_map['advertise_pip'] = 'advertise_pip'
        self.property_map['advertise_system_mac'] = 'advertise_system_mac'
        self.property_map['afi'] = 'afi'
        self.property_map['aggregate_address_advertise_map'] = 'advertise_map'
        self.property_map['aggregate_address_as_set'] = 'as_set'
        self.property_map['aggregate_address_attribute_map'] = 'attribute_map'
        self.property_map['aggregate_address_prefix'] = 'prefix'
        self.property_map['aggregate_address_summary_only'] = 'summary_only'
        self.property_map['aggregate_address_suppress_map'] = 'suppress_map'
        self.property_map['allow_vni_in_ethertag'] = 'allow_vni_in_ethertag'
        self.property_map['client_to_client_no_reflection'] = 'no_reflection'
        self.property_map['dampen_igp_metric'] = 'dampen_igp_metric'
        self.property_map['dampening_decay_half_life'] = 'decay_half_life'
        self.property_map['dampening_max_suppress_time'] = 'max_suppress_time'
        self.property_map['dampening_route_map'] = 'route_map'
        self.property_map['dampening_set'] = 'set'
        self.property_map['dampening_start_reuse_route'] = 'start_reuse_route'
        self.property_map['dampening_start_suppress_route'] = 'start_suppress_route'
        self.property_map['default_information_originate'] = 'originate'
        self.property_map['default_metric'] = 'default_metric'
        self.property_map['distance_ebgp_routes'] = 'ebgp_routes'
        self.property_map['distance_ibgp_routes'] = 'ibgp_routes'
        self.property_map['distance_local_routes'] = 'local_routes'
        self.property_map['export_gateway_ip'] = 'export_gateway_ip'
        self.property_map['inject_map_copy_attributes'] = 'copy_attributes'
        self.property_map['inject_map_exist_map'] = 'exist_map'
        self.property_map['inject_map_route_map'] = 'route_map'
        self.property_map['maximum_paths_eibgp_parallel_paths'] = 'parallel_paths'
        self.property_map['maximum_paths_ibgp_parallel_paths'] = 'parallel_paths'
        self.property_map['maximum_paths_local_parallel_paths'] = 'parallel_paths'
        self.property_map['maximum_paths_mixed_parallel_paths'] = 'parallel_paths'
        self.property_map['networks_prefix'] = 'prefix'
        self.property_map['networks_route_map'] = 'route_map'
        self.property_map['nexthop_route_map'] = 'route_map'
        self.property_map['nexthop_trigger_delay_critical_delay'] = 'critical_delay'
        self.property_map['nexthop_trigger_delay_non_critical_delay'] = 'non_critical_delay'
        self.property_map['redistribute_id'] = 'id'
        self.property_map['redistribute_protocol'] = 'protocol'
        self.property_map['redistribute_route_map'] = 'route_map'
        self.property_map['retain_route_target_retain_all'] = 'retain_all'
        self.property_map['retain_route_target_route_map'] = 'route_map'
        self.property_map['running_config'] = 'running_config'
        self.property_map['safi'] = 'safi'
        self.property_map['state'] = 'state'
        self.property_map['suppress_inactive'] = 'suppress_inactive'
        self.property_map['table_map_filter'] = 'filter'
        self.property_map['table_map_name'] = 'name'
        self.property_map['timers_bestpath_defer_defer_time'] = 'defer_time'
        self.property_map['timers_bestpath_defer_maximum_defer_time'] = 'maximum_defer_time'
        self.property_map['vrf'] = 'vrf'
        self.property_map['wait_igp_convergence'] = 'wait_igp_convergence'

        self.valid_afi = set()
        self.valid_afi.add('ipv4')
        self.valid_afi.add('ipv6')
        self.valid_afi.add('l2vpn')
        self.valid_afi.add('link-state')
        self.valid_afi.add('vpnv4')
        self.valid_afi.add('vpnv6')

        self.valid_safi = set()
        self.valid_safi.add('evpn')
        self.valid_safi.add('multicast')
        self.valid_safi.add('mvpn')
        self.valid_safi.add('unicast')

        self.valid_state = set()
        self.valid_state.add('deleted')
        self.valid_state.add('gathered')
        self.valid_state.add('merged')
        self.valid_state.add('overridden')
        self.valid_state.add('parsed')
        self.valid_state.add('rendered')
        self.valid_state.add('replaced')

        # properties_set is the full set of disambiguated property
        # names found in nxos_bgp_address_family module.  This includes all
        # global, neighbor, vrf, and ansible properties.
        self.properties_set = set()
        self.properties_set.update(self.address_family_set)
        self.properties_set.update(self.aggregate_address_set)
        self.properties_set.update(self.ansible_module_set)
        self.properties_set.update(self.config_set)
        self.properties_set.update(self.networks_set)
        self.properties_set.update(self.redistribute_set)

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.dampen_igp_metric_min = 20
        self.dampen_igp_metric_max = 3600

        self.dampening_decay_half_life_min = 1
        self.dampening_decay_half_life_max = 45
        self.dampening_max_suppress_time_min = 1
        self.dampening_max_suppress_time_max = 255
        self.dampening_start_reuse_route_min = 1
        self.dampening_start_reuse_route_max = 20000
        self.dampening_start_suppress_route_min = 1
        self.dampening_start_suppress_route_max = 20000
        self.default_metric_min = 1
        self.default_metric_max = 4294967295
        self.distance_ebgp_routes_min = 1
        self.distance_ebgp_routes_max = 255
        self.distance_ibgp_routes_min = 1
        self.distance_ibgp_routes_max = 255
        self.maximum_paths_eibgp_parallel_paths_min = 1
        self.maximum_paths_eibgp_parallel_paths_max = 64
        self.maximum_paths_ibgp_parallel_paths_min = 1
        self.maximum_paths_ibgp_parallel_paths_max = 64
        self.maximum_paths_local_parallel_paths_min = 1
        self.maximum_paths_local_parallel_paths_max = 64
        self.maximum_paths_mixed_parallel_paths_min = 1
        self.maximum_paths_mixed_parallel_paths_max = 64
        self.nexthop_trigger_delay_critical_delay_min = 1
        self.nexthop_trigger_delay_critical_delay_max = 4294967295
        self.nexthop_trigger_delay_non_critical_delay_min = 1
        self.nexthop_trigger_delay_non_critical_delay_max = 4294967295
        self.valid_redistribute_protocol = set()
        self.valid_redistribute_protocol.add('am')
        self.valid_redistribute_protocol.add('direct')
        self.valid_redistribute_protocol.add('eigrp')
        self.valid_redistribute_protocol.add('isis')
        self.valid_redistribute_protocol.add('lisp')
        self.valid_redistribute_protocol.add('ospf')
        self.valid_redistribute_protocol.add('ospfv3')
        self.valid_redistribute_protocol.add('rip')
        self.valid_redistribute_protocol.add('static')
        self.timers_bestpath_defer_defer_time_min = 100
        self.timers_bestpath_defer_defer_time_max = 3000
        self.timers_bestpath_defer_maximum_defer_time_min = 300
        self.timers_bestpath_defer_maximum_defer_time_max = 300000

        # Keyed on feature, value is a pointer to the verification
        # method for the feature
        self.verification_dispatch_table = dict()
        #self.verification_dispatch_table[''] = self.verify_maximum_prefix

        # See update_property_group()
        # properties whose structure is a single-level dict() and
        # are not an element of a list() e.g. this eliminates
        # aggregate_address, inject_map, networks, redistribute
        self.address_family_property_groups = set()
        self.address_family_property_groups.add('client_to_client')
        self.address_family_property_groups.add('dampening')
        self.address_family_property_groups.add('default_information')
        self.address_family_property_groups.add('distance')
        self.address_family_property_groups.add('table_map')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def init_address_family(self):
        self.address_family_dict = dict()
        for p in self.address_family_set:
            self.properties[p] = None

    def init_aggregate_address(self):
        for p in self.aggregate_address_set:
            self.properties[p] = None

    def init_inject_map(self):
        for p in self.inject_map_set:
            self.properties[p] = None

    def init_networks(self):
        for p in self.networks_set:
            self.properties[p] = None

    def init_redistribute(self):
        for p in self.redistribute_set:
            self.properties[p] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if self.as_number == None:
            self.task_log.error('exiting. call instance.as_number before calling instance.commit()')
            exit(1)

    def update_config_atomic(self):
        '''
        Update all atomic (not member of a dictionary) properties at
        the top-level of self.config
        '''
        for p in self.config_atomic:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                self.config[mapped_p] = self.properties[p]

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        self.config = dict()

        self.update_config_atomic()
        if len(self.address_family_list) != 0:
            self.config['address_family'] = deepcopy(self.address_family_list)
        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['config'] = deepcopy(self.config)
        self.ansible_task[self.ansible_module]['state'] = self.state

    def update_address_family_atomic(self):
        '''
        Update all atomic (not member of a dictionary) address-family
        properties
        '''
        for p in self.address_family_atomic_properties:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                self.address_family_dict[mapped_p] = self.properties[p]

    def update_address_family_additional_paths(self):
        d = dict()
        selection = dict()
        for p in self.address_family_set:
            if not p.startswith('additional_paths_'):
                continue
            if 'selection' in p:
                continue
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        p = 'additional_paths_selection_route_map'
        if self.properties[p] != None:
            mapped_p = self.property_map[p]
            selection[mapped_p] = self.properties[p]
        if len(selection) != 0:
            d['selection'] = deepcopy(selection)
        if len(d) != 0:
            self.address_family_dict['additional_paths'] = deepcopy(d)

    def update_address_family_maximum_paths(self):
        d = dict()
        if self.maximum_paths_eibgp_parallel_paths != None:
            d['eibgp'] = dict()
            d['eibgp']['parallel_paths'] = self.maximum_paths_eibgp_parallel_paths
        if self.maximum_paths_ibgp_parallel_paths != None:
            d['ibgp'] = dict()
            d['ibgp']['parallel_paths'] = self.maximum_paths_ibgp_parallel_paths
        if self.maximum_paths_local_parallel_paths != None:
            d['local'] = dict()
            d['local']['parallel_paths'] = self.maximum_paths_local_parallel_paths
        if self.maximum_paths_mixed_parallel_paths != None:
            d['mixed'] = dict()
            d['mixed']['parallel_paths'] = self.maximum_paths_mixed_parallel_paths
        if len(d) != 0:
            self.address_family_dict['maximum_paths'] = deepcopy(d)

    def update_address_family_nexthop(self):
        d = dict()
        trigger_delay = dict()
        if self.nexthop_route_map != None:
            d['route_map'] = self.nexthop_route_map
        if self.nexthop_trigger_delay_critical_delay != None:
            trigger_delay['critical_delay'] = self.nexthop_trigger_delay_critical_delay
        if self.nexthop_trigger_delay_non_critical_delay != None:
            trigger_delay['non_critical_delay'] = self.nexthop_trigger_delay_non_critical_delay
        if len(trigger_delay) != 0:
            d['trigger_delay'] = deepcopy(trigger_delay)
        if len(d) != 0:
            self.address_family_dict['nexthop'] = deepcopy(d)

    def update_address_family_timers(self):
        d = dict()
        bestpath_defer = dict()
        if self.timers_bestpath_defer_defer_time != None:
            bestpath_defer['defer_time'] = self.timers_bestpath_defer_defer_time
        if self.timers_bestpath_defer_maximum_defer_time != None:
            bestpath_defer['maximum_defer_time'] = self.timers_bestpath_defer_maximum_defer_time
        if len(bestpath_defer) != 0:
            d['bestpath_defer'] = deepcopy(bestpath_defer)
        if len(d) != 0:
            self.address_family_dict['timers'] = deepcopy(d)

    def update_property_group(self, pg):
        '''
        update address family properties whose structure is
        a single-level dictionary
        '''
        d = dict()
        for p in self.address_family_set:
            if not p.startswith(pg):
                continue
            if pg in self.verification_dispatch_table:
                self.verification_dispatch_table[pg]()
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.address_family_dict[pg] = deepcopy(d)

    def verify_address_family(self):
        if self.afi == None:
            self.task_log.error('exiting. afi is a mandatory property but is not set.')
            exit(1)
        if self.safi == None:
            self.task_log.error('exiting. safi is a mandatory property but is not set.')
            exit(1)
    def add_address_family(self):
        '''
        Add an address-family to self.address_family_list

        Example: Add ipv4 unicast and evpn l2vpn address-families

        instance.afi = 'ipv4'
        instance.safi = 'unicast'
        instance.add_address_family()

        instance.afi = 'l2vpn'
        instance.safi = 'evpn'
        instance.add_address_family()

        '''
        self.verify_address_family()
        self.address_family_dict = dict()
        self.update_address_family_atomic()
        for pg in self.address_family_property_groups:
            self.update_property_group(pg)

        self.update_address_family_additional_paths()
        self.update_address_family_maximum_paths()
        self.update_address_family_nexthop()
        self.update_address_family_timers()

        if len(self.address_family_dict) == 0:
            self.task_log.error('exiting. One or more address-family properties must be set before calling add_address_family()')
            exit(1)
        self.address_family_list.append(deepcopy(self.address_family_dict))
        self.init_address_family()

    def verify_aggregate_address(self):
        if self.aggregate_address_prefix == None:
            self.task_log.error('exiting. Set instance.aggregate_address_prefix before calling instance.add_aggregate_address()')
            exit(1)
    def add_aggregate_address(self):
        '''
        Add an aggregate address to self.aggregate_address_list
        '''
        self.verify_aggregate_address()
        d = dict()
        for p in self.aggregate_address_atomic_properties:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.aggregate_address_list.append(deepcopy(d))
        self.init_aggregate_address()

    def verify_inject_map(self):
        if self.inject_map_route_map == None:
            self.task_log.error('exiting. Set instance.inject_map_route_map before calling instance.add_inject_map()')
            exit(1)
        if self.inject_map_exist_map == None:
            self.task_log.error('exiting. Set instance.inject_map_exist_map before calling instance.add_inject_map()')
            exit(1)
    def add_inject_map(self):
        '''
        Add an inject-map to self.inject_map_list
        '''
        self.verify_inject_map()
        d = dict()
        for p in self.inject_map_atomic_properties:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.inject_map_list.append(deepcopy(d))
        self.init_inject_map()

    def verify_network(self):
        if self.networks_prefix == None:
            self.task_log.error('exiting. Set instance.networks_prefix before calling instance.add_network()')
            exit(1)
    def add_network(self):
        '''
        Add a network prefix to self.networks_list
        '''
        self.verify_network()
        d = dict()
        for p in self.networks_atomic_properties:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.networks_list.append(deepcopy(d))
        self.init_networks()

    def verify_redistribute(self):
        if self.redistribute_protocol == None:
            self.task_log.error('exiting. Set instance.redistribute_protocol before calling instance.add_redistribute()')
            exit(1)
        if self.redistribute_id == None:
            self.task_log.error('exiting. Set instance.redistribute_id before calling instance.add_redistribute()')
            exit(1)
        if self.redistribute_route_map == None:
            self.task_log.error('exiting. Set instance.redistribute_route_map before calling instance.add_redistribute()')
            exit(1)
    def add_redistribute(self):
        '''
        Add a redistribution to self.redistribute_list
        '''
        self.verify_redistribute()
        d = dict()
        for p in self.redistribute_atomic_properties:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.redistribute_list.append(deepcopy(d))
        self.init_redistribute()

    def verify_afi(self, x, parameter='afi'):
        verify_set = self.valid_afi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_afi'
        expectation = ','.join(sorted([str(x) for x in verify_set]))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_aggregate_address_prefix(self, x, parameter='aggregate_address_prefix'):
        # NX-OS allows this to be entered as prefix + mask e.g. 1.1.1.0 0.0.0.255
        # but nxos_bgp_address_family does not include a mask property.  Hence, 
        # we accept only prefix/prefixlen
        if self.is_ipv4_address_with_prefix(x):
            return
        if self.is_ipv6_address_with_prefix(x):
            return
        source_class = self.class_name
        source_method = 'verify_aggregate_address_prefix'
        expectation = '[ipv4/ipv6 address with prefixlen]'
        self.fail(source_class, source_method, x, parameter, expectation)


    def verify_dampen_igp_metric(self, x, parameter='dampen_igp_metric'):
        source_class = self.class_name
        range_min = self.dampen_igp_metric_min
        range_max = self.dampen_igp_metric_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_dampening_decay_half_life(self, x, parameter='dampening_decay_half_life'):
        source_class = self.class_name
        range_min = self.dampening_decay_half_life_min
        range_max = self.dampening_decay_half_life_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_dampening_max_suppress_time(self, x, parameter='dampening_max_suppress_time'):
        source_class = self.class_name
        range_min = self.dampening_max_suppress_time_min
        range_max = self.dampening_max_suppress_time_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_dampening_start_reuse_route(self, x, parameter='dampening_start_reuse_route'):
        source_class = self.class_name
        range_min = self.dampening_start_reuse_route_min
        range_max = self.dampening_start_reuse_route_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_dampening_start_suppress_route(self, x, parameter='dampening_start_suppress_route'):
        source_class = self.class_name
        range_min = self.dampening_start_suppress_route_min
        range_max = self.dampening_start_suppress_route_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)



    def verify_default_metric(self, x, parameter='default_metric'):
        source_class = self.class_name
        range_min = self.default_metric_min
        range_max = self.default_metric_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_distance_ebgp_routes(self, x, parameter='distance_ebgp_routes'):
        source_class = self.class_name
        range_min = self.distance_ebgp_routes_min
        range_max = self.distance_ebgp_routes_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_distance_ibgp_routes(self, x, parameter='distance_ibgp_routes'):
        source_class = self.class_name
        range_min = self.distance_ibgp_routes_min
        range_max = self.distance_ibgp_routes_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_distance_local_routes(self, x, parameter='distance_local_routes'):
        source_class = self.class_name
        # TODO_ADD_RANGE
        range_min = self.distance_local_routes_min
        range_max = self.distance_local_routes_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_maximum_paths_eibgp_parallel_paths(self, x, parameter='maximum_paths_eibgp_parallel_paths'):
        source_class = self.class_name
        range_min = self.maximum_paths_eibgp_parallel_paths_min
        range_max = self.maximum_paths_eibgp_parallel_paths_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_maximum_paths_ibgp_parallel_paths(self, x, parameter='maximum_paths_ibgp_parallel_paths'):
        source_class = self.class_name
        range_min = self.maximum_paths_ibgp_parallel_paths_min
        range_max = self.maximum_paths_ibgp_parallel_paths_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_maximum_paths_local_parallel_paths(self, x, parameter='maximum_paths_local_parallel_paths'):
        source_class = self.class_name
        range_min = self.maximum_paths_local_parallel_paths_min
        range_max = self.maximum_paths_local_parallel_paths_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_maximum_paths_mixed_parallel_paths(self, x, parameter='maximum_paths_mixed_parallel_paths'):
        source_class = self.class_name
        range_min = self.maximum_paths_mixed_parallel_paths_min
        range_max = self.maximum_paths_mixed_parallel_paths_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_networks_prefix(self, x, parameter='networks_prefix'):
        # NX-OS allows this to be entered as prefix + mask e.g. 1.1.1.0 0.0.0.255
        # but nxos_bgp_address_family does not include a mask property.  Hence, 
        # we accept only prefix/prefixlen
        if self.is_ipv4_address_with_prefix(x):
            return
        if self.is_ipv6_address_with_prefix(x):
            return
        source_class = self.class_name
        source_method = 'verify_networks_prefix'
        expectation = '[ipv4/ipv6 address with prefixlen]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nexthop_trigger_delay_critical_delay(self, x, parameter='nexthop_trigger_delay_critical_delay'):
        source_class = self.class_name
        range_min = self.nexthop_trigger_delay_critical_delay_min
        range_max = self.nexthop_trigger_delay_critical_delay_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nexthop_trigger_delay_non_critical_delay(self, x, parameter='nexthop_trigger_delay_non_critical_delay'):
        source_class = self.class_name
        range_min = self.nexthop_trigger_delay_non_critical_delay_min
        range_max = self.nexthop_trigger_delay_non_critical_delay_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_redistribute_protocol(self, x, parameter='redistribute_protocol'):
        verify_set = self.valid_redistribute_protocol
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_redistribute_protocol'
        expectation = ','.join(sorted([str(x) for x in verify_set]))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_safi(self, x, parameter='safi'):
        verify_set = self.valid_safi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_safi'
        expectation = ','.join(sorted([str(x) for x in verify_set]))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_state(self, x, parameter='state'):
        verify_set = self.valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_timers_bestpath_defer_defer_time(self, x, parameter='timers_bestpath_defer_defer_time'):
        source_class = self.class_name
        range_min = self.timers_bestpath_defer_defer_time_min
        range_max = self.timers_bestpath_defer_defer_time_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_timers_bestpath_defer_maximum_defer_time(self, x, parameter='timers_bestpath_defer_maximum_defer_time'):
        source_class = self.class_name
        range_min = self.timers_bestpath_defer_maximum_defer_time_min
        range_max = self.timers_bestpath_defer_maximum_defer_time_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    @property
    def additional_paths_install_backup(self):
        return self.properties['additional_paths_install_backup']
    @additional_paths_install_backup.setter
    def additional_paths_install_backup(self, x):
        parameter = 'additional_paths_install_backup'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def additional_paths_receive(self):
        return self.properties['additional_paths_receive']
    @additional_paths_receive.setter
    def additional_paths_receive(self, x):
        parameter = 'additional_paths_receive'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def additional_paths_selection_route_map(self):
        return self.properties['additional_paths_selection_route_map']
    @additional_paths_selection_route_map.setter
    def additional_paths_selection_route_map(self, x):
        parameter = 'additional_paths_selection_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def additional_paths_send(self):
        return self.properties['additional_paths_send']
    @additional_paths_send.setter
    def additional_paths_send(self, x):
        parameter = 'additional_paths_send'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def advertise_pip(self):
        return self.properties['advertise_pip']
    @advertise_pip.setter
    def advertise_pip(self, x):
        parameter = 'advertise_pip'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def advertise_system_mac(self):
        return self.properties['advertise_system_mac']
    @advertise_system_mac.setter
    def advertise_system_mac(self, x):
        parameter = 'advertise_system_mac'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.verify_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def aggregate_address_advertise_map(self):
        return self.properties['aggregate_address_advertise_map']
    @aggregate_address_advertise_map.setter
    def aggregate_address_advertise_map(self, x):
        parameter = 'aggregate_address_advertise_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def aggregate_address_as_set(self):
        return self.properties['aggregate_address_as_set']
    @aggregate_address_as_set.setter
    def aggregate_address_as_set(self, x):
        parameter = 'aggregate_address_as_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def aggregate_address_attribute_map(self):
        return self.properties['aggregate_address_attribute_map']
    @aggregate_address_attribute_map.setter
    def aggregate_address_attribute_map(self, x):
        parameter = 'aggregate_address_attribute_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def aggregate_address_prefix(self):
        return self.properties['aggregate_address_prefix']
    @aggregate_address_prefix.setter
    def aggregate_address_prefix(self, x):
        parameter = 'aggregate_address_prefix'
        if self.set_none(x, parameter):
            return
        self.verify_aggregate_address_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def aggregate_address_summary_only(self):
        return self.properties['aggregate_address_summary_only']
    @aggregate_address_summary_only.setter
    def aggregate_address_summary_only(self, x):
        parameter = 'aggregate_address_summary_only'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def aggregate_address_suppress_map(self):
        return self.properties['aggregate_address_suppress_map']
    @aggregate_address_suppress_map.setter
    def aggregate_address_suppress_map(self, x):
        parameter = 'aggregate_address_suppress_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def allow_vni_in_ethertag(self):
        return self.properties['allow_vni_in_ethertag']
    @allow_vni_in_ethertag.setter
    def allow_vni_in_ethertag(self, x):
        parameter = 'allow_vni_in_ethertag'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def as_number(self):
        return self.properties['as_number']
    @as_number.setter
    def as_number(self, x):
        parameter = 'as_number'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def client_to_client_no_reflection(self):
        return self.properties['client_to_client_no_reflection']
    @client_to_client_no_reflection.setter
    def client_to_client_no_reflection(self, x):
        parameter = 'client_to_client_no_reflection'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def dampen_igp_metric(self):
        return self.properties['dampen_igp_metric']
    @dampen_igp_metric.setter
    def dampen_igp_metric(self, x):
        parameter = 'dampen_igp_metric'
        if self.set_none(x, parameter):
            return
        self.verify_dampen_igp_metric(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_decay_half_life(self):
        return self.properties['dampening_decay_half_life']
    @dampening_decay_half_life.setter
    def dampening_decay_half_life(self, x):
        parameter = 'dampening_decay_half_life'
        if self.set_none(x, parameter):
            return
        self.verify_dampening_decay_half_life(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_max_suppress_time(self):
        return self.properties['dampening_max_suppress_time']
    @dampening_max_suppress_time.setter
    def dampening_max_suppress_time(self, x):
        parameter = 'dampening_max_suppress_time'
        if self.set_none(x, parameter):
            return
        self.verify_dampening_max_suppress_time(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_route_map(self):
        return self.properties['dampening_route_map']
    @dampening_route_map.setter
    def dampening_route_map(self, x):
        parameter = 'dampening_route_map'
        if self.set_none(x, parameter):
            return
        self.dampening_route_map(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_set(self):
        return self.properties['dampening_set']
    @dampening_set.setter
    def dampening_set(self, x):
        parameter = 'dampening_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_start_reuse_route(self):
        return self.properties['dampening_start_reuse_route']
    @dampening_start_reuse_route.setter
    def dampening_start_reuse_route(self, x):
        parameter = 'dampening_start_reuse_route'
        if self.set_none(x, parameter):
            return
        self.verify_dampening_start_reuse_route(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_start_suppress_route(self):
        return self.properties['dampening_start_suppress_route']
    @dampening_start_suppress_route.setter
    def dampening_start_suppress_route(self, x):
        parameter = 'dampening_start_suppress_route'
        if self.set_none(x, parameter):
            return
        self.verify_dampening_start_suppress_route(x, parameter)
        self.properties[parameter] = x

    @property
    def default_information_originate(self):
        return self.properties['default_information_originate']
    @default_information_originate.setter
    def default_information_originate(self, x):
        parameter = 'default_information_originate'
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
        self.verify_default_metric(x, parameter)
        self.properties[parameter] = x

    @property
    def distance_ebgp_routes(self):
        return self.properties['distance_ebgp_routes']
    @distance_ebgp_routes.setter
    def distance_ebgp_routes(self, x):
        parameter = 'distance_ebgp_routes'
        if self.set_none(x, parameter):
            return
        self.verify_distance_ebgp_routes(x, parameter)
        self.properties[parameter] = x

    @property
    def distance_ibgp_routes(self):
        return self.properties['distance_ibgp_routes']
    @distance_ibgp_routes.setter
    def distance_ibgp_routes(self, x):
        parameter = 'distance_ibgp_routes'
        if self.set_none(x, parameter):
            return
        self.verify_distance_ibgp_routes(x, parameter)
        self.properties[parameter] = x

    @property
    def distance_local_routes(self):
        return self.properties['distance_local_routes']
    @distance_local_routes.setter
    def distance_local_routes(self, x):
        parameter = 'distance_local_routes'
        if self.set_none(x, parameter):
            return
        self.verify_distance_local_routes(x, parameter)
        self.properties[parameter] = x

    @property
    def export_gateway_ip(self):
        return self.properties['export_gateway_ip']
    @export_gateway_ip.setter
    def export_gateway_ip(self, x):
        parameter = 'export_gateway_ip'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def inject_map_copy_attributes(self):
        return self.properties['inject_map_copy_attributes']
    @inject_map_copy_attributes.setter
    def inject_map_copy_attributes(self, x):
        parameter = 'inject_map_copy_attributes'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def inject_map_exist_map(self):
        return self.properties['inject_map_exist_map']
    @inject_map_exist_map.setter
    def inject_map_exist_map(self, x):
        parameter = 'inject_map_exist_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def inject_map_route_map(self):
        return self.properties['inject_map_route_map']
    @inject_map_route_map.setter
    def inject_map_route_map(self, x):
        parameter = 'inject_map_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def maximum_paths_eibgp_parallel_paths(self):
        return self.properties['maximum_paths_eibgp_parallel_paths']
    @maximum_paths_eibgp_parallel_paths.setter
    def maximum_paths_eibgp_parallel_paths(self, x):
        parameter = 'maximum_paths_eibgp_parallel_paths'
        if self.set_none(x, parameter):
            return
        self.verify_maximum_paths_eibgp_parallel_paths(x, parameter)
        self.properties[parameter] = x

    @property
    def maximum_paths_ibgp_parallel_paths(self):
        return self.properties['maximum_paths_ibgp_parallel_paths']
    @maximum_paths_ibgp_parallel_paths.setter
    def maximum_paths_ibgp_parallel_paths(self, x):
        parameter = 'maximum_paths_ibgp_parallel_paths'
        if self.set_none(x, parameter):
            return
        self.verify_maximum_paths_ibgp_parallel_paths(x, parameter)
        self.properties[parameter] = x

    @property
    def maximum_paths_local_parallel_paths(self):
        return self.properties['maximum_paths_local_parallel_paths']
    @maximum_paths_local_parallel_paths.setter
    def maximum_paths_local_parallel_paths(self, x):
        parameter = 'maximum_paths_local_parallel_paths'
        if self.set_none(x, parameter):
            return
        self.verify_maximum_paths_local_parallel_paths(x, parameter)
        self.properties[parameter] = x

    @property
    def maximum_paths_mixed_parallel_paths(self):
        return self.properties['maximum_paths_mixed_parallel_paths']
    @maximum_paths_mixed_parallel_paths.setter
    def maximum_paths_mixed_parallel_paths(self, x):
        parameter = 'maximum_paths_mixed_parallel_paths'
        if self.set_none(x, parameter):
            return
        self.verify_maximum_paths_mixed_parallel_paths(x, parameter)
        self.properties[parameter] = x

    @property
    def networks_prefix(self):
        return self.properties['networks_prefix']
    @networks_prefix.setter
    def networks_prefix(self, x):
        parameter = 'networks_prefix'
        if self.set_none(x, parameter):
            return
        self.verify_networks_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def networks_route_map(self):
        return self.properties['networks_route_map']
    @networks_route_map.setter
    def networks_route_map(self, x):
        parameter = 'networks_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def nexthop_route_map(self):
        return self.properties['nexthop_route_map']
    @nexthop_route_map.setter
    def nexthop_route_map(self, x):
        parameter = 'nexthop_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def nexthop_trigger_delay_critical_delay(self):
        return self.properties['nexthop_trigger_delay_critical_delay']
    @nexthop_trigger_delay_critical_delay.setter
    def nexthop_trigger_delay_critical_delay(self, x):
        parameter = 'nexthop_trigger_delay_critical_delay'
        if self.set_none(x, parameter):
            return
        self.verify_nexthop_trigger_delay_critical_delay(x, parameter)
        self.properties[parameter] = x

    @property
    def nexthop_trigger_delay_non_critical_delay(self):
        return self.properties['nexthop_trigger_delay_non_critical_delay']
    @nexthop_trigger_delay_non_critical_delay.setter
    def nexthop_trigger_delay_non_critical_delay(self, x):
        parameter = 'nexthop_trigger_delay_non_critical_delay'
        if self.set_none(x, parameter):
            return
        self.verify_nexthop_trigger_delay_non_critical_delay(x, parameter)
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
        self.verify_redistribute_protocol(x, parameter)
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
    def retain_route_target_retain_all(self):
        return self.properties['retain_route_target_retain_all']
    @retain_route_target_retain_all.setter
    def retain_route_target_retain_all(self, x):
        parameter = 'retain_route_target_retain_all'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def retain_route_target_route_map(self):
        return self.properties['retain_route_target_route_map']
    @retain_route_target_route_map.setter
    def retain_route_target_route_map(self, x):
        parameter = 'retain_route_target_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def safi(self):
        return self.properties['safi']
    @safi.setter
    def safi(self, x):
        parameter = 'safi'
        if self.set_none(x, parameter):
            return
        self.verify_safi(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_inactive(self):
        return self.properties['suppress_inactive']
    @suppress_inactive.setter
    def suppress_inactive(self, x):
        parameter = 'suppress_inactive'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
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
    def timers_bestpath_defer_defer_time(self):
        return self.properties['timers_bestpath_defer_defer_time']
    @timers_bestpath_defer_defer_time.setter
    def timers_bestpath_defer_defer_time(self, x):
        parameter = 'timers_bestpath_defer_defer_time'
        if self.set_none(x, parameter):
            return
        self.verify_timers_bestpath_defer_defer_time(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_bestpath_defer_maximum_defer_time(self):
        return self.properties['timers_bestpath_defer_maximum_defer_time']
    @timers_bestpath_defer_maximum_defer_time.setter
    def timers_bestpath_defer_maximum_defer_time(self, x):
        parameter = 'timers_bestpath_defer_maximum_defer_time'
        if self.set_none(x, parameter):
            return
        self.verify_timers_bestpath_defer_maximum_defer_time(x, parameter)
        self.properties[parameter] = x

    @property
    def vrf(self):
        return self.properties['vrf']
    @vrf.setter
    def vrf(self, x):
        parameter = 'vrf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def wait_igp_convergence(self):
        return self.properties['wait_igp_convergence']
    @wait_igp_convergence.setter
    def wait_igp_convergence(self, x):
        parameter = 'wait_igp_convergence'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x
