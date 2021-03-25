**************************************
NxosBgpNeighborAf()
**************************************

.. contents::
   :local:
   :depth: 1

Deprecation
-----------

- Status: ``DEPRECATED``
- Alternative: `nxos_bgp_neighbor_address_family <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_neighbor_address_family.rst>`_
- 2021-02-24, deprecation date
- 2023-02-24, removal date (module may be removed after this date)

ScriptKit Synopsis
------------------
- NxosBgpNeighborAf() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp_neighbor_af
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp_neighbor_af <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_neighbor_af_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_af.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_af.py>`_


|

=============================   ==============================================
Property                        Description
=============================   ==============================================
additional_paths_receive        Advertise the capability to receive additional
                                paths from the neighbors under this
                                address family ``afi`` for which the capability
                                has not been disabled::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_receive = True

additional_paths_send           Advertise the capability to send additional
                                paths to all of the neighbors under this
                                address family ``afi`` for which the capability
                                has not been disabled::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_send = False

advertise_map_exist             Conditional route advertisement. This property
                                requires two route maps, an ``advertise-map``
                                and an ``exist-map``. Valid values are an array
                                specifying both the ``advertise-map`` name and
                                the ``exist-map`` name, or simply the keyword
                                ``default``.  This property is mutually-exclusive
                                with ``advertise_map_non_exist``::

                                    - Type: list() or str()
                                        - str() if 'default' keyword is used
                                        - list() otherwise
                                    - Valid values:
                                        - 2-element list() containing:
                                            - a route-map name -> advertise-map
                                            - a route-map name -> exist-map
                                        - Keyword: default
                                    - Examples:
                                        - list()
                                            ame = list()
                                            ame.append('my_advertise_map')
                                            ame.append('my_exist_map')
                                            task.advertise_map_exist = ame.copy()
                                        - str()
                                            task.advertise_map_exist = 'default'
                                    - NOTES:
                                        - Mutually-exclusive with: advertise_map_non_exist

advertise_map_non_exist         Conditional route advertisement. This property
                                requires two route maps, an ``advertise-map``
                                and a ``non-exist-map``. Valid values are an array
                                specifying both the ``advertise-map name`` and
                                the ``non-exist-map`` name, or simply the keyword
                                ``default``. This property is mutually-exclusive
                                with ``advertise_map_exist``::

                                    - Type: list() or str()
                                        - str() if 'default' keyword is used
                                        - list() otherwise
                                    - Valid values:
                                        - 2-element list() containing:
                                            - a route-map name -> advertise-map
                                            - a route-map name -> non-exist-map
                                        - Keyword: default
                                    - Examples:
                                        - list()
                                            amne = list()
                                            amne.append('my_advertise_map')
                                            amne.append('my_exist_map')
                                            task.advertise_map_non_exist = amne.copy()
                                        - str()
                                            task.advertise_map_non_exist = 'default'
                                    - NOTES:
                                        - Mutually-exclusive with: advertise_map_exist

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

allowas_in                      Accept advertisements with our AS in the AS path.
                                Mutually-exclusive with allowas_in_max::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.allowas_in = False

allowas_in_max                  Max-occurrences value for allowas_in.
                                Mutually-exclusive with allowas_in::

                                    - Type: int()
                                    - Valid values:
                                        - int() range: 1-10
                                        - Keyword: default
                                    - Example:
                                        task.allowas_in_max = 2

as_override                     Activate the as-override feature::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.as_override = False


asn                             BGP autonomous system number, in ``ASPLAIN`` or ``ASDOT`` notation::

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

default_originate               Advertise the default route to this neighbor, regardless
                                of whether it is present in the routing table::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.default_originate = True

default_originate_route_map     Route-map for the ``default_originate`` property. 
                                Mutually-exclusive with ``default_originate``::

                                    - Valid values:
                                        - str() defining a route-map name
                                        - Keyword: default

disable_peer_as_check           Disable checking of peer AS-number while advertising::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.disable_peer_as_check = True

filter_list_in                  Inbound filter-list applied to this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - filter-list name
                                        - Keyword: default
                                    - Examples:
                                        task.filter_list_in = 'FILTER_IN'
                                        task.filter_list_in = 'default'

filter_list_out                 Outbound filter-list applied to this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - filter-list name
                                        - Keyword: default
                                    - Examples:
                                        task.filter_list_out = 'FILTER_OUT'
                                        task.filter_list_out = 'default'

max_prefix_interval             When the maximum number of prefixes is received from this
                                neighbor, restart the BGP connection after this interval::

                                    - Type: int()
                                    - Valid values: range 1-65535
                                    - Units: seconds
                                    - Example:
                                        task.max_prefix_interval = 300
                                    - NOTES:
                                        - Requires max_prefix_limit to be configured
                                        - Mutually-exclusive with max_prefix_warning

max_prefix_limit                Maximum number of prefixes allowed from this neighbor::

                                    - Type: int()
                                    - Example:
                                        task.max_prefix_limit = 12000

max_prefix_threshold            Optional threshold percentage at which to generate a warning::

                                    - Type: int()
                                    - Example:
                                        task.max_prefix_threshold = 85
                                    NOTES:
                                        - Requires max_prefix_limit to be configured

max_prefix_warning              Warn (via syslog) if the number of prefixes received
                                from this neighbor exceeds ``max_prefix_limit``::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.max_prefix_warning = True
                                    NOTES:
                                        - Requires max_prefix_limit to be configured
                                        - Mutually-exclusive with max_prefix_interval

neighbor                        IPv4 or IPv6 address of the neighbor.  May 
                                include a prefixlen for prefix-peering
                                scenarios::

                                    - Type: str()
                                    - Valid values:
                                        - IPv4 address
                                        - IPv4 address with prefixlen
                                        - IPv6 address
                                        - IPv6 address with prefixlen
                                    - Examples:
                                        task.neighbor = '10.1.1.1'
                                        task.neighbor = '10.1.1.0/24'
                                        task.neighbor = '2011:aaaa::1'
                                        task.neighbor = '2011:aaaa::/126'
                                    - Required

next_hop_self                   Advertise prefixes to this neighbor with our peering
                                interface as the next-hop::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.next_hop_self = True

next_hop_third_party            If the neighbor and the next-hop for a given prefix are both
                                on a common shared network (e.g. an L2 internet peering point
                                where the neighbor address falls within the same subnet as a
                                prefix's next-hop), ``next_hop_third_party`` determines whether
                                we advertise the prefix with the unaltered (3rd-party) next-hop
                                of the prefix, or no.  See RFC2283::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.next_hop_third_party = False

prefix_list_in                  Inbound prefix-list influencing acceptance of
                                prefixes from this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - prefix-list name
                                        - Keyword: default
                                    - Examples:
                                        task.prefix_list_in = 'PREFIX_IN'
                                        task.prefix_list_in = 'default'

prefix_list_out                 Outbound prefix-list influencing advertisement of
                                prefixes to this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - prefix-list name
                                        - Keyword: default
                                    - Examples:
                                        task.prefix_list_out = 'PREFIX_OUT'
                                        task.prefix_list_out = 'default'

rewrite_evpn_rt_asn             Auto generate route targets for EBGP neighbor::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.rewrite_evpn_rt_asn = True

route_map_in                    Inbound route-map for this neighbor which permits
                                and/or denies acceptance of prefixes from neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - route-map name
                                        - Keyword: default
                                    - Examples:
                                        task.route_map_in = 'TO_TOR'
                                        task.route_map_in = 'default'

route_map_out                   Outbound route-map for this neighbor which permits
                                and/or denies advertisement of prefixes::

                                    - Type: str()
                                    - Valid values:
                                        - route-map name
                                        - Keyword: default
                                    - Examples:
                                        task.route_map_out = 'TO_TOR'
                                        task.route_map_out = 'default'

route_reflector_client          Specify whether this neighbor is a route-reflector
                                client::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.route_reflector_client = True

safi                            Sub Address Family Identifier::

                                    - Type: str()
                                    - Valid values:
                                        - unicast
                                        - multicast
                                        - evpn
                                    - Example:
                                        - task.safi = 'unicast'
                                    - Required

send_community                  Send the BGP community attribute to this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - none
                                        - both
                                        - extended
                                        - standard
                                        - default
                                    - Example:
                                        task.send_community = 'both'

soft_reconfiguration_in         Configure inbound soft-reconfiguration::

                                    - Type: str()
                                    - Valid values:
                                        - enable  (issues: soft-reconfiguration inbound)
                                        - always  (issues: soft-reconfiguration inbound always)
                                        - inherit (remove from neighbor config and inherit,
                                                   if present, from a template)
                                    - Example:
                                        task.soft_reconfiguration_in = 'always'

soo                             Site-of-origin::

                                    - Type: str()
                                    - Valid values:
                                        - str() defining a VPN extcommunity
                                        - str() Keyword: default
                                    - Examples:
                                        - task.soo = '65000:0'
                                        - task.soo = 'default'

state                           Determines whether the config should be present or
                                not on the remote device::

                                    - Type: str()
                                    - Valid values:
                                        - absent
                                        - present
                                    - Examples:
                                        - task.state = 'present'
                                    - Required

suppress_inactive               Advertise only active routes to peers::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.suppress_inactive = True

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Examples:
                                        - task.task_name = 'my task'

unsuppress_map                  In addition to active routes (see ``suppress_inactive``) advertise these
                                inactive routes::

                                    - Type: str()
                                    - Valid values:
                                        - A route-map name
                                        - Keyword: default
                                    - Examples:
                                        - task.unsuppress_map = 'DO_NOT_SUPPRESS_THESE'
                                        - task.unsuppress_map = 'default'

vrf                             Name of the VRF. The name ``default`` is a valid VRF representing
                                the global bgp table.::

                                    - Type: str()
                                    - Default: 'default'
                                    - Examples:
                                        - task.vrf = 'default'
                                        - task.vrf = 'PROD'

weight                          ``weight`` is a Cisco proprietary property and is not exchanged
                                with BGP neighbors.  Weight takes precedence over other BGP path
                                selection attributes (assuming all other attributes are equal 
                                between two or more neighbors). To prefer one neighbor over others
                                (again, assuming their other next-hop selection criteria are equal)
                                set the weight for that neighbor higher than the other neighbors)::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range: 0-65535
                                        - str() Keyword: default
                                    - Examples:
                                        - task.weight = 400
                                        - task.weight = 'default'

=============================   ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)


