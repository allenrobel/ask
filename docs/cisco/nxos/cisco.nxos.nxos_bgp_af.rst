**************************************
NxosBgpAf()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosBgpAf() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp_af
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp_af <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_af_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp_af.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp_af.py>`_


|

=============================   ==============================================
Property                        Description
=============================   ==============================================
additional_paths_install        Install a backup path into the forwarding table::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_install = False

additional_paths_receive        Advertise the capability to receive additional
                                paths from the neighbors under this
                                address family (afi) for which the capability
                                has not been disabled::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_receive = True

additional_paths_selection      Determines which prefix(es) are eligible for installation
                                of additional paths::

                                    - Type: str()
                                    - Valid values: route-map name
                                    - Example:
                                        task.additional_paths_selection = 'ADD_PATH_SEL'

additional_paths_send           Advertise the capability to send additional
                                paths to all of the neighbors under this
                                address family (afi) for which the capability
                                has not been disabled::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_send = False

advertise_l2vpn_evpn            Advertise L2 EVPN routes::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.advertise_l2vpn_evpn = False

afi                             Address Family Identifier::

                                    - Type: str()
                                    - Valid values:
                                        - ipv4
                                        - ipv6
                                        - vpnv4
                                        - vpnv6
                                        - l2vpn
                                    - Example:
                                        task.afi = 'ipv4'
                                    - Required

asn                             BGP autonomous system number, in ASPLAIN or ASDOT notation::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-4294967295
                                        - <1-65535>.<0-65535>
                                    - Examples:
                                        task.asn = 64512
                                        task.asn = 4200000000
                                        task.asn = '2301.0'
                                    - NOTES:
                                        - private asn ranges
                                            - 64512 to 65534
                                            - 4200000000 to 4294967294
                                    - Required

client_to_client                Configure client-to-client route reflection::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.client_to_client = False

dampen_igp_metric               Duration, in seconds, to dampen IGP
                                metric-related changes::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 20-3600
                                        - keyword: 'default'
                                    - Default: 600
                                    - Units: seconds
                                    - Example:
                                        task.dampen_igp_metric = 1200

dampening_half_time             Decay half life::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-45
                                        - keyword: 'default'
                                    - Units: minutes
                                    - Examples:
                                        task.dampening_half_time = 2

dampening_max_suppress_time     Maximum suppress time for stable route::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-255
                                        - keyword: 'default'
                                    - Units: minutes
                                    - NOTES:
                                        - higher values require higher dampening_half_time values
                                    - Examples:
                                        task.dampening_max_suppress_time = 10

dampening_reuse_time            Value to start reusing a route::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-20000
                                        - keyword: 'default'
                                    - Units: int()
                                    - Examples:
                                        task.dampening_reuse_time = 20
                                    - NOTES:
                                        - dampening_reuse_time must be less than dampening_suppress_time

dampening_routemap              Specify which prefix(es) are subject to route-flap dampening::

                                    - Type: str()
                                    - Example:
                                        task.dampening_routemap = 'DAMPEN_THESE'

dampening_state                 Enable/disable route-flap dampening::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.dampening_state = True

dampening_suppress_time         Value to start suppressing a route::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Units: int()
                                    - NOTES:
                                        - dampening_suppress_time must be greater than dampening_reuse_time
                                    - Examples:
                                        task.dampening_suppress_time = 40
                                        task.dampening_suppress_time = 'default'

default_information_originate   Generate and inject the default route into the
                                BGP RIB, regardless of whether it is present in
                                the routing table::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.default_information_originate = True

default_metric                  Sets default metrics for routes redistributed into BGP::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Examples:
                                        task.default_metric = 400
                                        task.default_metric = 'default'

distance_ebgp                   Sets the administrative distance for eBGP routes::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Examples:
                                        task.distance_ebgp = 300
                                        task.distance_ebgp = 'default'

distance_ibgp                   Sets the administrative distance for iBGP routes::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Examples:
                                        task.distance_ibgp = 200
                                        task.distance_ibgp = 'default'

distance_local                  Sets the administrative distance for local BGP routes::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Examples:
                                        task.distance_local = 100
                                        task.distance_local = 'default'

inject_map                      An array of route-map names which will specify
                                prefixes to inject. Each array entry must first
                                specify the ``inject-map`` name, secondly an ``exist-map``
                                name, and optionally the ``copy-attributes`` keyword,
                                which indicates that attributes should be copied from
                                the aggregate::

                                    - Type: list() of list()
                                    - Example:
                                        inject_map_list = list()
                                        inject_map_list.append(['INJECT_1', 'EXIST_1', 'copy-attributes'])
                                        inject_map_list.append(['INJECT_2', 'EXIST_2'])
                                        task.inject_map = inject_map_list.copy()

maximum_paths                   Maximum number of equal-cost paths for load sharing::

                                    - Type: int()
                                    - Valid values: int() range: 1-64
                                    - Example:
                                        task.maximum_paths = 16

maximum_paths_ibgp              Maximum number of ibgp equal-cost paths for load sharing::

                                    - Type: int()
                                    - Valid values: int() range: 1-64
                                    - Example:
                                        task.maximum_paths_ibgp = 16

networks                        Networks to configure.  Specified as a list() of list().
                                Each list contains network/prefix and, optionally, a 
                                route-map name::

                                    - Type: list() of list()
                                    - Example:
                                        network_list = list()
                                        network_list.append(['10.0.0.0/16', 'routemap_LA'])
                                        network_list.append(['192.168.2.0/24'])
                                        task.networks = network_list.copy()

next_hop_route_map              A route-map which specifies/selects valid nexthops::

                                    - Type: str()
                                    - Examples:
                                        - task.next_hop_route_map = 'NEXT_HOP_RM'

redistribute                    A list of redistribute directives.
                                Multiple redistribute entries are allowed.
                                The list must be in the form of a nested array.
                                The first element of each array specifies the 
                                source-protocol from which to redistribute.
                                The second element specifies a route-map name.
                                A route-map is advised but may be optional
                                on some platforms, in which case it may be
                                omitted from the list::

                                    - Type: list() of list()
                                    - Example:
                                        redistribute_list = list()
                                        redistribute_list.append(['direct'])
                                        redistribute_list.append(['ospf', 'ROUTE_MAP_OSPF'])
                                        task.redistribute = redistribute_list.copy()

retain_route_target             Retains all of the routes or the routes which are
                                part of configured route-map::

                                    - Valid values:
                                        - route-map name
                                            - selectively retain routes
                                            - route-map name cannot be 'all' or 'default'
                                        - keyword: all
                                            -  retain all routes regardless of
                                               Target-VPN community
                                        - keyword: default
                                            - disable the retain route target option
                                        - Examples:
                                            task.retain_route_target = 'RRT_RMAP'
                                            task.retain_route_target = 'all'
                                            task.retain_route_target = 'default'

safi                            Sub Address Family Identifier::

                                    - Type: str()
                                    - Valid values: unicast, multicast, evpn
                                    - Examples:
                                        - task.safi = 'unicast'
                                    - Required

state                           Determines whether the config should be present or
                                not on the remote device::

                                    - Type: str()
                                    - Valid values: absent, present
                                    - Examples:
                                        - task.state = 'present'
                                    - Required

suppress_inactive               Advertise only active routes to peers::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.suppress_inactive = True

table_map                       Apply table-map to filter routes downloaded into URIB::

                                    - Type: str()
                                    - Examples:
                                        - task.table_map = 'PRIO_1'

table_map_filter                Filters routes rejected by the route-map and
                                does not download them to the RIB::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.table_map_filter = True

vrf                             VRF name::

                                    - Type: str()
                                    - Default: 'default'
                                    - Examples:
                                        - task.vrf = 'default'
                                        - task.vrf = 'PROD'

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Examples:
                                        - task.task_name = 'my task'

=============================   ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
