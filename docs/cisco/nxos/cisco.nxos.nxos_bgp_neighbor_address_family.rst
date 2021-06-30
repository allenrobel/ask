**************************************
NxosBgpNeighborAddressFamily()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
102

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
- NxosBgpNeighborAddressFamily() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp_neighbor_address_family
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp_neighbor_address_family <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_neighbor_address_family_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_address_family.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_address_family.py>`_

NOTES
-----

1.  When ``task.add_vrf()`` is called, the following happens:

    a.  All currently-defined neighbor address-families that were added using
        ``instance.add_address_family()`` followed by ``instance.add_vrf_bgp_neighbor()``
        are added to the vrf specified with ``instance.vrf`` and the vrf bgp neighbor
        list is cleared so that a new set of neighbor address-families can be added
        to another non-default vrf.

2.  Based on the above note, below is an example which adds two bgp neighbors
    into the default vrf, one bgp neighbor into vrf VRF_1, and two bgp neighbors
    into vrf VRF_2::

        pb = Playbook(log)
        task = NxosBgpNeighborAddressFamily(log)
        task.as_number = '6202.0'

        # Add two AF to a neighbor in VRF_1
        task.afi = 'ipv4'
        task.safi = 'unicast'
        task.add_address_family()

        task.afi = 'ipv6'
        task.safi = 'unicast'
        task.add_address_family()

        task.neighbor_address = '10.1.1.1'
        task.add_vrf_bgp_neighbor()
        task.vrf = 'VRF_1'
        task.add_vrf()

        # Add an AF to a neighbor in the global/default vrf
        task.afi = 'ipv6'
        task.safi = 'unicast'
        task.add_address_family()
        task.neighbor_address = '10.2.1.1'
        task.add_bgp_neighbor()

        # Add an AF to two neighbors in VRF_2
        task.afi = 'ipv4'
        task.safi = 'multicast'
        task.neighbor_address = '10.3.1.1'
        task.add_address_family()
        task.add_vrf_bgp_neighbor()

        task.afi = 'ipv4'
        task.safi = 'unicast'
        task.add_address_family()
        task.neighbor_address = '10.3.1.3'
        task.add_vrf_bgp_neighbor()
        task.vrf = "VRF_2"
        task.add_vrf()

        # Add another bgp neighbor to the global/default vrf
        task.afi = 'ipv4'
        task.safi = 'unicast'
        task.add_address_family()
        task.neighbor_address = '10.1.1.1'
        task.add_bgp_neighbor()

        # Commit the task. This performs a final verification
        # and prepares the task to be added to a playbook
        task.task_name = 'bgp neighbor AFs under default vrf and non-default vrf'
        task.state = 'merged'
        task.commit()

        # add the task to the playbook
        pb.add_task(task)

        # Append the playbook (more than one playbook, each
        # with more than one task, can be appended to a
        # given playbook file)
        pb.append_playbook()

        # write the playbook
        pb.file = '/tmp/nxos_bgp_neighbor_address_family.yaml'
        pb.write_playbook()

|

========================    ==============================================
Method                      Description
========================    ==============================================
add_address_family()        Add an address-family to the address-family
                            list.::

                                Example:
                                    task = NxosBgpNeighborAddressFamily(log)
                                    task.as_number = '12000.0'
                                    task.afi = 'ipv4'
                                    task.safi = 'unicast'
                                    task.add_address_family()
                                    task.afi = 'ipv6'
                                    task.safi = 'unicast'
                                    task.add_address_family()

add_bgp_neighbor()          Add a bgp neighbor, along with the currrent
                            address-family list, to the default/global vrf::

                                Example:
                                    task = NxosBgpNeighborAddressFamily(log)
                                    task.as_number = '12000.0'
                                    task.afi = 'ipv4'
                                    task.safi = 'multicast'
                                    task.add_address_family()
                                    task.neighbor_address = '10.4.4.0/24'
                                    task.add_bgp_neighbor()

add_vrf_bgp_neighbor()      Add a bgp neighbor, along with the currrent
                            address-family list, to a non-default vrf::

                                Example:
                                    task = NxosBgpNeighborAddressFamily(log)
                                    task.as_number = '12000.0'
                                    task.afi = 'ipv4'
                                    task.safi = 'multicast'
                                    task.add_address_family()
                                    task.neighbor_address = '10.4.4.0/24'
                                    task.add_vrf_bgp_neighbor()
                                    task.vrf = 'MY_VRF'
                                    task.add_vrf()

add_vrf()                   Add all bgp neighbors onfigured up to this
                            point with ``add_vrf_bgp_neighbor()``,
                            to the current ``vrf``.::

                                Example (add one neighbor with one
                                address family to vrf VRF_1):

                                    task = NxosBgpNeighborAddressFamily(log)
                                    task.as_number = '12000.0'
                                    task.afi = 'ipv4'
                                    task.safi = 'unicast'
                                    task.next_hop_self_all_routes = True
                                    task.next_hop_self_set = True
                                    task.as_override = True
                                    task.add_address_family()
                                    task.neighbor_address = '10.4.4.0/24'
                                    task.add_vrf_bgp_neighbor()
                                    task.vrf = 'VRF_1'
                                    task.add_vrf()

commit()                    Perform final verification and prepare the task
                            to be added to a playbook::

                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See NOTE 2 above, or
                                    See ScriptKit Example link above

========================    ==============================================

|

=================================== ==============================================
Property                            Description
=================================== ==============================================
advertise_map_exist_map             Condition route-map to advertise only when
                                    prefix in condition exists::

                                        - Type: str()
                                        - Example:
                                            task.advertise_map_exist_map = 'RM_EXIST'

advertise_map_non_exist_map         Condition route-map to advertise only when
                                    prefix in condition does not exist::

                                        - Type: str()
                                        - Example:
                                            task.advertise_map_non_exist_map = 'RM_NON_EXIST'

advertise_map_route_map             Route-map name::

                                        - Type: str()
                                        - Required if other advertise_map_* are set
                                        - Example:
                                            task.advertise_map_route_map = 'AM_RM'

advertisement_interval              Minimum interval between sending BGP routing updates::

                                        - Type: int()
                                        - Valid values:
                                            - range 1-600
                                        - Units: seconds
                                        - Example:
                                            task.advertisement_interval = 10

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

allowas_in_max_occurences           Number of occurrences of AS number to allow in
                                    inbound updates::

                                        - Type: int()
                                        - Valid values:
                                            - range 1-10
                                        - Default: 3
                                        - Example:
                                            task.allowas_in_max_occurences = 10

allowas_in_set                      Activate allowas-in property::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.allowas_in_set = True

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

as_override                         Override matching AS-number while sending update.::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.as_override = False

capability_additional_paths_receive Enable additional paths receive capability::

                                        - Type: str()
                                        - Valid values:
                                            - disable
                                            - enable
                                        - Example:
                                            task.capability_additional_paths_receive = 'disable'

capability_additional_paths_send    Enable additional paths send capability::

                                        - Type: str()
                                        - Valid values:
                                            - disable
                                            - enable
                                        - Example:
                                            task.capability_additional_paths_send = 'disable'

default_originate_route_map         Route-map to specify criteria for originating
                                    default::

                                        - Type: str()
                                        - Example:
                                            task.default_originate_route_map = 'DO_RM'

default_originate_set               Set default-originate attribute::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.allowas_in_set = True

disable_peer_as_check               Disable checking of peer AS-number while
                                    advertising::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.disable_peer_as_check = True

filter_list_inbound                 Apply policy to incoming routes::

                                        - Type: str()
                                        - Example:
                                            task.filter_list_inbound = 'FL_IN'

filter_list_outbound                 Apply policy to outgoing routes::

                                        - Type: str()
                                        - Example:
                                            task.filter_list_inbound = 'FL_OUT'

inherit_sequence                    Sequence number::

                                        - Type: int()
                                        - Example:
                                            task.inherit_sequence = 10

inherit_template                    Template name::

                                        - Type: str()
                                        - Example:
                                            task.inherit_template = 'TOR_TEMPLATE'

=================================== ==============================================

|

============================================    =========================================
Property                                        Description
============================================    =========================================
maximum_prefix_generate_warning_threshold       Threshold percentage of 
                                                ``maximum_prefix_max_prefix_limit`` at
                                                which to generate a warning::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 1-100
                                                    - Example:
                                                        task.maximum_prefix_generate_warning_threshold = 75

============================================    =========================================

====================================    =========================================
Property                                Description
====================================    =========================================
maximum_prefix_max_prefix_limit         Maximum prefix limit::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-4294967295
                                            - Example:
                                                task.maximum_prefix_max_prefix_limit = 12000

maximum_prefix_restart_interval         Restart bgp connection after limit is exceeded::

                                            - Type: int()
                                            - Units: minutes
                                            - Valid values:
                                                - range: 1-65535
                                            - Example:
                                                task.maximum_prefix_restart_interval = 5

maximum_prefix_warning_only             Only give a warning message when limit
                                        is exceeded::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.maximum_prefix_warning_only = True

next_hop_self_all_routes                Set our address as nexthop (non-reflected)
                                        for all routes::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.next_hop_self_all_routes = True

next_hop_self_set                       Set next-hop-self attribute::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.next_hop_self_set = True

next_hop_third_party                    Compute a third-party nexthop if possible::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.next_hop_third_party = True

prefix_list_inbound                     Apply policy to incoming routes via
                                        prefix-list::

                                            - Type: str()
                                            - Example:
                                                task.prefix_list_inbound = 'PL_IN'

prefix_list_outbound                    Apply policy to outgoing routes via::
                                        prefix-list::

                                            - Type: str()
                                            - Example:
                                                task.prefix_list_outbound = 'PL_OUT'

rewrite_evpn_rt_asn                     Auto generate RTs for EBGP neighbor::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.rewrite_evpn_rt_asn = False

route_map_inbound                       Apply policy to incoming routes via
                                        route-map::

                                            - Type: str()
                                            - Example:
                                                task.prefix_list_inbound = 'PL_IN'

route_map_outbound                      Apply policy to outgoing routes via
                                        route-map::

                                            - Type: str()
                                            - Example:
                                                task.prefix_list_outbound = 'PL_OUT'

route_reflector_client                  Configure a neighbor as Route reflector
                                        client::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.route_reflector_client = False

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

send_community_both                     Send Standard and Extended Community 
                                        attributes::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.send_community_both = False

send_community_extended                 Send only Extended Community attributes::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.send_community_extended = False

send_community_set                      Set send-community attribute::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.send_community_set = False
                                            - NOTES:
                                                1. mutually-exclusive with send_community_standard

send_community_standard                 Send only Standard Community attributes::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.send_community_standard = False
                                            - NOTES:
                                                1. mutually-exclusive with send_community_set

soft_reconfiguration_inbound_always     Always perform inbound soft reconfiguration::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.soft_reconfiguration_inbound_always = True

soft_reconfiguration_inbound_set        Set soft-reconfiguration inbound attribute::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.soft_reconfiguration_inbound_set = True

soo                                     Site-of-origin extcommunity::

                                            - Type: str()
                                            - Valid values:
                                                - ASN2:NN
                                                - ASN4:NN
                                                - IPV4:NN
                                            - Examples:
                                                task.soo = '65000:40'
                                                task.soo = '1055423144:40`
                                                task.soo = '10.167.1.4:40`

suppress_inactive                       Advertise only active routes to peer::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.suppress_inactive = True

unsuppress_map                          Route-map to selectively unsuppress
                                        suppressed routes::

                                            - Type: str()
                                            - Example:
                                                task.unsuppress_map = 'US_RM'

weight                                  Set default weight for routes from this
                                        neighbor in this address-family::

                                            - Type: int()
                                            - Valid values:
                                                - range 0-65535
                                            - Example:
                                                task.weight = 1200

neighbor_address                        IP address/[prefixlen] of this neighbor::

                                            - Type: str()
                                            - Valid values:
                                                - ipv4 address without prefixlen
                                                - ipv4 address with prefixlen
                                                - ipv6 address without prefixlen
                                                - ipv6 address with prefixlen
                                            - Examples:
                                                task.neighbor_address = '1.2.3.4'
                                                task.neighbor_address = '1.2.3.0/24'
                                                task.neighbor_address = '2001:aaaa::1'
                                                task.neighbor_address = '2001:aaaa::0/126'


task_name                               Name of the task. Ansible will display this
                                        when the playbook is run::

                                            - Type: str()
                                            - Examples:
                                                - task.task_name = 'my task'

vrf                                     Name of VRF in which bgp neighbor resides::

                                            - Type: str()
                                            - Examples:
                                                - task.vrf = 'MY_VRF'

====================================    =========================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

