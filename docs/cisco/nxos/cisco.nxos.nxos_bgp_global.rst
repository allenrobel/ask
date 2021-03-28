**************************************
NxosBgpGlobal()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
106

Status
------

- BETA

- This library is in development and not yet complete, nor fully-tested.
- See TODO below for missing functionality.
- Initial vrf support is added as of version 102
- Breaking change to vrf support added as of version 103
    - task.add_bgp_neighbor() adds neighbor into the global/default vrf
    - task.add_vrf_bgp_neighbor() adds neighbor into a non-default vrf

TODO
----

1. Support for states ``parsed`` and ``rendered`` not yet included
    - Hence ``running_config`` property is not yet supported
2. Verification of property mutual-exclusion not complete
3. Verification of required properties not complete
4. Verification of missing/dependent properties not complete

ScriptKit Synopsis
------------------
- NxosBgpGlobal() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp_global
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_global_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp_global.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp_global.py>`_

NOTES
-----

1.  When ``task.add_vrf()`` is called, the following happens:

    a.  All currently-defined neighbors that were added using
        ``instance.add_vrf_bgp_neighbor()`` are added to the vrf specified
        with ``instance.vrf`` and the vrf bgp neighbor list is cleared so
        that a new set of neighbors can be added to another non-default vrf.

    b.  All properties that are currently-set and are supported under
        vrf config are added to the vrf config when add_vrf() is called.
        These properties are then cleared so that they may be set again
        (or not) for another vrf, or the default vrf.

    c.  Properties that are currently-set and are not supported under
        vrf config are not added to the vrf, and are not otherwise 
        altered/cleared when add_vrf() is called.

2.  Based on the above note, below is an example which adds two bgp neighbors
    into the default vrf, one bgp neighbor into vrf VRF_1, and two bgp neighbors
    into vrf VRF_2::

        pb = Playbook(log)
        task = NxosBgpGlobal(log)
        task.as_number = '6202.0'

        # Add a bgp neighbor to VRF_1
        task.neighbor_address = '10.1.1.1'
        task.neighbor_remote_as = '6101.1'
        task.add_vrf_bgp_neighbor()
        task.vrf = 'VRF_1'
        task.add_vrf()

        # Add one bgp neighbor to the global/default vrf
        task.neighbor_address = '10.2.1.1'
        task.neighbor_remote_as = '6201.1'
        task.add_bgp_neighbor()

        # Add two bgp neighbors to VRF_2
        task.neighbor_address = '10.3.1.1'
        task.neighbor_remote_as = '6301.1'
        task.add_vrf_bgp_neighbor()
        task.neighbor_address = '10.3.1.3'
        task.neighbor_remote_as = '6301.1'
        task.add_vrf_bgp_neighbor()
        task.vrf = "VRF_2"
        task.add_vrf()

        # Add another bgp neighbor to the global/default vrf
        task.neighbor_address = '10.1.1.1'
        task.neighbor_remote_as = '6401.1'
        task.add_bgp_neighbor()

        # update the task. This performs a final verification
        # and prepares the task to be added to a playbook
        task.task_name = 'bgp neighbors under default vrf and non-default vrf'
        task.state = 'merged'
        task.update()

        # add the task to the playbook
        pb.add_task(task)

        # Append the playbook (more than one playbook, each
        # with more than one task, can be appended to a
        # given playbook file)
        pb.append_playbook()

        # write the playbook
        pb.file = '/tmp/nxos_bgp_global.yaml'
        pb.write_playbook()

|

================================    ==============================================
Method                              Description
================================    ==============================================
add_bgp_neighbor()                  Add a bgp neighbor into the default/global vrf, and
                                    clear all bgp neighbor properties to make way
                                    for adding the next neighbor::

                                        Example:
                                            task = NxosBgpGlobal(log)
                                            task.as_number = '12000.0'
                                            task.neighbor_address = '10.4.4.0/24'
                                            task.neighbor_inherit_peer = 'TOR_GLOBAL_VRF'
                                            task.neighbor_remote_as = '6201.3'
                                            task.neighbor_update_source = 'Vlan4'
                                            task.add_bgp_neighbor()

add_vrf_bgp_neighbor()              Add a bgp neighbor into a non-default vrf, and
                                    clear all bgp neighbor properties to make way
                                    for adding the next neighbor::

                                        Example:
                                            task = NxosBgpGlobal(log)
                                            task.as_number = '12000.0'
                                            task.neighbor_address = '10.4.4.0/24'
                                            task.neighbor_inherit_peer = 'TOR_VRF_1'
                                            task.neighbor_remote_as = '6201.3'
                                            task.neighbor_update_source = 'Ethernet1/1'
                                            task.add_vrf_bgp_neighbor()
                                            task.vrf = 'VRF_1'
                                            task.add_vrf()

add_vrf()                           Add all currently-set properties, and all bgp 
                                    neighbors added up to this point with
                                    ``add_vrf_bgp_neighbor()``, to the current ``vrf``.
                                    Any properties that are set, but are not supported
                                    under vrf configuration are not added to the vrf
                                    and are not cleared::

                                        Example (add one neighbor and one global property
                                        (bestpath_med_non_deterministic) to vrf VRF_1):

                                            task = NxosBgpGlobal(log)
                                            # as_number is not supported under vrf config,
                                            # so is not added to the vrf and is not otherwise
                                            # altered by add_vrf()
                                            task.as_number = '12000.0'

                                            # bestpath_med_non_deterministic is supported
                                            # under vrf config, so is added to the vrf,
                                            # and is cleared so that it can later be set
                                            # for another vrf, or the default vrf.
                                            task.bestpath_med_non_deterministic = False

                                            task.neighbor_address = '10.4.4.0/24'
                                            task.neighbor_inherit_peer = 'TOR_VRF_1'
                                            task.neighbor_remote_as = '6201.3'
                                            task.neighbor_update_source = 'Ethernet1/1'
                                            task.add_vrf_bgp_neighbor()
                                            task.vrf = 'VRF_1'
                                            task.add_vrf()

================================    ==============================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
affinity_group_group_id             Affinity Group ID::

                                        - Type: int()
                                        - Valid values:
                                            - range 1-4294967295
                                        - Example:
                                            task.affinity_group_group_id = 200

as_number                           BGP autonomous system number of the router::

                                        - Type: int() or str()
                                        - Valid values:
                                            - int() range 1-4294967295
                                            - str() <1-65535>.<0-65535>
                                        - Examples:
                                            task.as_number = 64512
                                            task.as_number = 4200000000
                                            task.as_number = '2301.0'
                                        - NOTES:
                                            - private asn ranges
                                                - 64512 to 65534
                                                - 4200000000 to 4294967294

bestpath_always_compare_med         Enable/Disable MED comparison on paths from 
                                    different autonomous systems::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_always_compare_med = False

bestpath_as_path_ignore             Ignore AS-Path during bestpath selection::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_as_path_ignore = True

bestpath_as_path_multipath_relax    Relax AS-Path restriction when choosing multipaths::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_as_path_multipath_relax = True

bestpath_compare_neighborid         When more paths are available than max path
                                    config, use neighborid as tie-breaker::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_compare_neighborid = True

bestpath_compare_routerid           Compare router-id for identical EBGP paths::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_compare_routerid = True

bestpath_cost_community_ignore      Ignore cost communities in bestpath selection::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_cost_community_ignore = True

bestpath_igp_metric_ignore          Ignore IGP metric for next-hop during
                                    bestpath selection::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_igp_metric_ignore = True

bestpath_med_confed                 Compare MED only from paths originated from
                                    within a confederation::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_med_confed = True

bestpath_med_missing_as_worst       Treat missing MED as highest MED::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_med_missing_as_worst = True

bestpath_med_non_deterministic      Enable/Disable deterministic selection of the 
                                    best MED path from among the paths from the 
                                    same autonomous system::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.bestpath_med_non_deterministic = True

cluster_id                          Route Reflector Cluster-ID::

                                        - Type: int() or str()
                                        - Valid values:
                                            - int() range: 1-4294967295
                                            - str() IPv4 address
                                        - Examples:
                                            task.cluster_id = 12300
                                            task.cluster_id = '10.1.1.45'

confederation_identifier            Routing domain confederation AS::

                                        - Type: int() or str()
                                        - Valid values:
                                            - int() range 1-4294967295
                                            - str() <1-65535>.<0-65535>
                                        - Examples:
                                            task.confederation_identifier = 64512
                                            task.confederation_identifier = 4200000000
                                            task.confederation_identifier = '2301.0'

confederation_peers                 Peer ASs in BGP confederation::

                                        - Type: list()
                                        - Valid values:
                                            - python list() of ASs
                                        Example:
                                            peers = list()
                                            peers.append('64512')
                                            peers.append('64513.0')
                                            peers.append('64523')
                                            task.confederation_peers = peers
                                        NOTES:
                                            - confederation_identifier must be configured first

================================    ==============================================

|

========================================    =========================================
Property                                    Description
========================================    =========================================
disable_policy_batching_set                 Enable/Disable the batching evaluation of
                                            prefix advertisement to all peers::

                                                - Type: bool()
                                                - Valid values:
                                                    - False
                                                    - True
                                                - Example:
                                                    task.disable_policy_batching_set = True

disable_policy_batching_ipv4_prefix_list    Disable batching evaluation of outbound
                                            policy for ipv4 peers in the provided
                                            ip prefix-list::

                                                - Type: str()
                                                - Valid values:
                                                    - An ip prefix-list name
                                                - Example:
                                                    task.disable_policy_batching_ipv4_prefix_list = 'DPB'

disable_policy_batching_ipv6_prefix_list    Disable batching evaluation of outbound
                                            policy for ipv6 peers in the provided 
                                            ipv6 prefix-list::

                                                - Type: str()
                                                - Valid values:
                                                    - An ipv6 prefix-list name
                                                - Example:
                                                    task.disable_policy_batching_ipv6_prefix_list = 'DPB'

disable_policy_batching_nexthop             Batching based on nexthop::

                                                - Type: bool()
                                                - Valid values:
                                                    - False
                                                    - True
                                                - Example:
                                                    task.disable_policy_batching_nexthop = True

========================================    =========================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
dynamic_med_interval                Sets the interval for dampening of med changes::

                                        - Type: int()
                                        - Unit: seconds
                                        - Valid values:
                                            - range: 0-4294967295
                                        - Example:
                                            task.dynamic_med_interval = 10

enforce_first_as                    Enable ``True`` or disable ``False`` enforcement
                                    that the neighbor autonomous system must be the
                                    first AS number listed in the AS path attribute
                                    for eBGP::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.enforce_first_as = True

enhanced_error                      Enable BGP Enhanced error handling::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.enhanced_error = True

fabric_soo                          Fabric site of origin::

                                        - Type: str()
                                        - Example:
                                            task.fabric_soo = '65000:1'

fast_external_fallover              Enable ``True`` or disable ``False``
                                    immediate session reset if the link to a 
                                    directly connected BGP peer goes down::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.fast_external_fallover = True

flush_routes                        Enable ``True`` or disable ``False``  
                                    flush routes in RIB upon controlled restart::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.flush_routes = True

graceful_restart_helper             Enable ``True`` or disable ``False``
                                    graceful restart helper mode::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.graceful_restart_helper = True

graceful_restart_restart_time       Set maximum time for a restart sent to
                                    BGP peers::

                                        - Type: int()
                                        - Units: seconds
                                        - Valid values:
                                            - range: 1-3600
                                        - Default: 120
                                        - Example:
                                            task.graceful_restart_restart_time = 300

graceful_restart_set                Enable ``True`` or disable ``False`` 
                                    graceful restart::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.graceful_restart_set = True

graceful_restart_stalepath_time     Maximum time to keep a restarting peer's
                                    stale routes::

                                        - Type: int()
                                        - Units: seconds
                                        - Valid values:
                                            - range: 1-3600
                                        - Default: 300
                                        - Example:
                                            task.graceful_restart_stalepath_time = 240

================================    ==============================================

|

====================================    ==============================================
graceful_shutdown_activate_route_map    Apply route-map to modify attributes
                                        for outbound::

                                            - Type: str()
                                            - Valid values:
                                                - route-map name
                                            - Example:
                                                task.graceful_shutdown_activate_route_map = 'GS_MAP'

graceful_shutdown_activate_set          Activate graceful shutdown::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.graceful_shutdown_activate_set = True

graceful_shutdown_aware                 Reduce preference of routes carrying graceful-shutdown
                                        community::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.graceful_shutdown_aware = True

====================================    ==============================================

============================    ==============================================
Property                        Description
============================    ==============================================
isolate_include_local           Withdraw both local and remote BGP routes::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.isolate_include_local = False

isolate_set                     Withdraw remote BGP routes to isolate this router::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.isolate_set = False

log_neighbor_changes            Enable ``True`` or disable ``False``
                                message logging for neighbor up/down event::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.log_neighbor_changes = True


maxas_limit                     Specify Maximum number of AS numbers allowed
                                in the AS-path attribute::

                                    - Type: int()
                                    - Valid values:
                                        - int() range 1-512
                                    - Example:
                                        task.maxas_limit = 16

neighbor_down_fib_accelerate    Enable ``True`` or disable ``False``
                                When enabled, withdraws the corresponding next hop
                                from all next-hop groups (ECMP groups and single
                                next-hop routes) whenever a BGP session goes down::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.neighbor_down_fib_accelerate = True
                                    - NOTES:
                                        - Must be used only in a pure BGP environment
                                          where all non-direct routes are installed
                                          by BGP.

============================    ==============================================

|

==============================================  ==============================================
Property                                        Description
==============================================  ==============================================
neighbor_address                                IP address/[prefixlen] of this neighbor::

                                                    - Type: str()
                                                    - Valid values:
                                                        - ipv4 address with/without prefixlen
                                                        - ipv6 address with/without prefixlen
                                                    - Examples:
                                                        task.neighbor_address = '1.2.3.4'
                                                        task.neighbor_address = '1.2.3.0/24'
                                                        task.neighbor_address = '2001:aaaa::1'
                                                        task.neighbor_address = '2001:aaaa::0/126'

neighbor_affinity_group_group_id                Affinity Group ID for this neighbor::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range 1-4294967295
                                                    - Example:
                                                        task.neighbor_affinity_group_group_id = 200

neighbor_bfd_multihop_interval_min_rx_interval  Minimum rx-interval for multi-hop
                                                BFD session with this neighbor::

                                                    - Type: int()
                                                    - Units: milliseconds
                                                    - Default: 250
                                                    - Valid values:
                                                        - range: 250-999
                                                    - Example:
                                                        task.neighbor_bfd_multihop_interval_min_rx_interval = 300

neighbor_bfd_multihop_interval_multiplier       Detect multiplier::

                                                    - Type: int()
                                                    - Default: 3
                                                    - Valid values:
                                                        - range: 1-50
                                                    - Example:
                                                        task.neighbor_bfd_multihop_interval_multiplier = 3

neighbor_bfd_multihop_interval_tx_interval      TX interval::

                                                    - Type: int()
                                                    - Units: milliseconds
                                                    - Default: 250
                                                    - Valid values:
                                                        - range: 250-999
                                                    - Example:
                                                        task.neighbor_bfd_multihop_interval_tx_interval = 100

neighbor_bfd_multihop_set                       Enable ``True`` or disable ``False`` BFD
                                                multihop with this neighbor::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_bfd_multihop_set = False

neighbor_bfd_set                                Enable ``True`` or disable ``False`` BFD
                                                with this neighbor::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_bfd_set = True

neighbor_bfd_singlehop                          Enable ``True`` or disable ``False`` BFD
                                                singlehop session with this neighbor::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_bfd_singlehop = True

neighbor_bmp_activate_server                    Specify server ID for activating BMP 
                                                monitoring for the peer::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 1-2
                                                    - Example:
                                                        task.neighbor_bmp_activate_server = 1

neighbor_capability_suppress_4_byte_as          Suppress 4-byte AS capability with this 
                                                neighbor::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_capability_suppress_4_byte_as = True

neighbor_description                            Neighbor-specific description::

                                                    - Type: str()
                                                    - Example:
                                                        task.neighbor_description = 'my neighbor'

neighbor_disable_connected_check                Disable check for directly connected peer::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_disable_connected_check = False

neighbor_dont_capability_negotiate              Don't negotiate capabilities
                                                with this neighbor::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_dont_capability_negotiate = False

neighbor_dscp                                   Set dscp value for tcp transport
                                                with this neighbor::

                                                    - Type: int() or str()
                                                    - Valid values:
                                                        - range: 1-64
                                                        - af11 (001010)
                                                        - af12 (001100)
                                                        - af13 (001110)
                                                        - af21 (010010)
                                                        - af22 (010100)
                                                        - af23 (010110)
                                                        - af31 (011010)
                                                        - af32 (011100)
                                                        - af33 (011110)
                                                        - af41 (100010)
                                                        - af42 (100100)
                                                        - af43 (100110)
                                                        - cs1 (001000) (precedence 1)
                                                        - cs2 (010000) (precedence 2)
                                                        - cs3 (011000) (precedence 3)
                                                        - cs4 (100000) (precedence 4)
                                                        - cs5 (101000) (precedence 5)
                                                        - cs6 (110000) (precedence 6)
                                                        - cs7 (111000) (precedence 7)
                                                        - default
                                                        - ef
                                                    - Default: cs6
                                                    - Examples:
                                                        task.neighbor_dscp = 61
                                                        task.neighbor_dscp = 'cs5'
                                                        task.neighbor_dscp = 'af11'
                                                        task.neighbor_dscp = 'default'
                                                        task.neighbor_dscp = 'ef'

neighbor_dynamic_capability                     Dynamic Capability::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_dynamic_capability = False

neighbor_ebgp_multihop                          Specify multihop TTL for this neighbor::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 2-255
                                                    - Example:
                                                        task.neighbor_ebgp_multihop = 2

neighbor_graceful_shutdown_activate_route_map   Apply route-map to modify outbound attributes
                                                for this neighbor::

                                                    - Type: str()
                                                    - Valid values:
                                                        - route-map name
                                                    - Example:
                                                        task.neighbor_graceful_shutdown_activate_route_map = 'GS_MAP'

neighbor_graceful_shutdown_activate_set         Activate graceful shutdown for this neighbor::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_graceful_shutdown_activate_set = True

neighbor_inherit_peer                           Peer template to inherit::

                                                    - Type: str()
                                                    - Valid values:
                                                        - bgp peer-template
                                                    - Example:
                                                        task.neighbor_inherit_peer = 'TOR'

neighbor_inherit_peer_session                   Peer template to inherit::

                                                    - Type: str()
                                                    - Valid values:
                                                        - bgp session-template
                                                    - Example:
                                                        task.neighbor_inherit_peer_session = 'TOR_SESSION'

neighbor_local_as                               Specify the local-as number for this
                                                eBGP neighbor in ``ASPLAIN`` or ``ASDOT``
                                                notation::

                                                    - Type: int() or str()
                                                    - Valid values:
                                                        - int() range 1-4294967295
                                                        - <1-65535>.<0-65535>
                                                        - str() Keyword: default (remove local_as config)
                                                    - Examples:
                                                        task.neighbor_local_as = 64512
                                                        task.neighbor_local_as = '64512.45'

neighbor_log_neighbor_changes_disable           Disable message logging for neighbor
                                                up/down event::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_log_neighbor_changes_disable = True

neighbor_log_neighbor_changes_set               Set log-neighbor-changes::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_log_neighbor_changes_set = True

neighbor_low_memory_exempt                      Do not shutdown this peer when under
                                                memory pressure::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_low_memory_exempt = False

neighbor_password_encryption                    Encryption type for ``neighbor_password_key``::

                                                    - Type: int()
                                                    - Valid values:
                                                        - 0 : UNENCRYPTED key
                                                        - 3 : 3DES ENCRYPTED key
                                                        - 7 : Cisco type 7 ENCRYPTED key
                                                    - Example:
                                                        task.neighbor_password_encryption = 3

neighbor_password_encryption                    Encryption type for ``neighbor_password_key``::

                                                    - Type: int()
                                                    - Valid values:
                                                        - 0 : UNENCRYPTED key
                                                        - 3 : 3DES ENCRYPTED key
                                                        - 7 : Cisco type 7 ENCRYPTED key
                                                    - Example:
                                                        task.neighbor_password_encryption = 3

neighbor_password_key                           The unencrypted or encrypted key for this
                                                neighbor.  See also:
                                                ``neighbor_password_encryption``::

                                                    - Type: str()
                                                    - Example:
                                                        task.neighbor_password_key = 'foobar'

neighbor_path_attribute_action                  Action::

                                                    - Type: str()
                                                    - Valid values:
                                                        - discard
                                                        - treat-as-withdraw
                                                    - Example:
                                                        task.neighbor_path_attribute_action = 'discard'

neighbor_path_attribute_range_end               Path attribute range end value::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 1-255
                                                    - Example:
                                                        task.neighbor_path_attribute_range_end = 20
                                                    - Notes:
                                                        - Mutually-exclusive with:
                                                            - neighbor_path_attribute_type

neighbor_path_attribute_range_start             Path attribute range start value::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 1-255
                                                    - Example:
                                                        task.neighbor_path_attribute_range_start = 10
                                                    - Notes:
                                                        - Mutually-exclusive with:
                                                            - neighbor_path_attribute_type

neighbor_path_attribute_type                    Path attribute type::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 1-255
                                                    - Example:
                                                        task.neighbor_path_attribute_type = 10
                                                    - Notes:
                                                        - Mutually-exclusive with:
                                                            - neighbor_path_attribute_range_end
                                                            - neighbor_path_attribute_range_start

neighbor_peer_type                              Neighbor facing::

                                                    - Type: str()
                                                    - Valid values:
                                                        - fabric-border-leaf
                                                        - fabric-external
                                                    - Example:
                                                        task.neighbor_peer_type = 'fabric-external'

neighbor_remote_as                              Autonomous System Number of this neighbor
                                                in ``ASPLAIN``or ``ASDOT`` notation::

                                                    - Type: int() or str()
                                                    - Valid values:
                                                        - range 1-4294967295
                                                        - <1-65535>.<0-65535>
                                                    - Examples:
                                                        task.neighbor_remote_as = 64512
                                                        task.neighbor_remote_as = '64512.45'

neighbor_remove_private_as_all                  Remove all private AS numbers from outbound
                                                updates to this neighbor::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_remove_private_as_all = False

neighbor_remove_private_as_replace_as           Replace private AS numbers in outbound
                                                updates to this neighbor with``as_number``::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_remove_private_as_replace_as = True

neighbor_remove_private_as_set                  Enable / disable remove_private_as for this
                                                neighbor::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_remove_private_as_set = True

neighbor_shutdown                               Administratively shutdown the BGP session with
                                                this neighbor::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_shutdown = False

neighbor_timers_holdtime                        Set BGP holddown timer for this neighbor.
                                                How long before resetting bgp sessions
                                                after keepalives are not received from
                                                this neighbor::

                                                    - Type: int() or str()
                                                    - Valid values:
                                                        - int() range 3-3600
                                                        - str() keyword: default
                                                    - Units: seconds
                                                    - Default: 180
                                                    - Example:
                                                        task.neighbor_timers_holdtime = 60
                                                    - NOTES:
                                                        - While the NXOS CLI claims the valid range
                                                          is 0-3600, the lowest accepted value is 3.

neighbor_timers_keepalive                       Set BGP keepalive timer for this neighbor.
                                                How often to send keepalive messages to this
                                                neighbor::

                                                    - Type: int() or str()
                                                    - Valid values:
                                                        - int() range 1-3599
                                                        - str() keyword: default
                                                    - Units: seconds
                                                    - Default: 60
                                                    - Example:
                                                        task.neighbor_timers_keepalive = 60
                                                    - NOTES:
                                                        - While the NXOS CLI claims the valid range
                                                          is 0-3600, the lowest accepted value is 1
                                                          and the highest accepted value is 3599.

neighbor_transport_connection_mode_passive      Allow passive connection setup only i.e. wait
                                                for this neighbor to initiate the BGP session::

                                                    - Type: bool()
                                                    - Valid values:
                                                        - False
                                                        - True
                                                    - Example:
                                                        task.neighbor_transport_connection_mode_passive = False

neighbor_ttl_security_hops                      Specify hop count for this BGP neighbor::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 1-254
                                                    - Example:
                                                        task.neighbor_ttl_security_hops = 2

neighbor_update_source                          Specify source of BGP session and updates
                                                with this neighbor::

                                                    - Type: str()
                                                    - Valid values:
                                                        - A full interface name
                                                    - Examples:
                                                        task.neighbor_update_source = 'Ethernet1/1'
                                                        task.neighbor_update_source = 'Loopback3'
                                                        task.neighbor_update_source = 'port-channel3'
                                                        task.neighbor_update_source = 'Vlan3'

==============================================  ==============================================

|

====================================    ==============================================
Property                                Description
====================================    ==============================================
nexthop_suppress_default_resolution     Prohibit use of default route for nexthop
                                        address resolution::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.nexthop_suppress_default_resolution = True

rd_dual                                 Generate Secondary RD for all VRFs
                                        and L2VNIs::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.rd_dual = True

rd_id                                   Specify 2 byte value for ID::

                                            - Type: int()
                                            - Valid values:
                                                - int() range 1-65535
                                            - Example:
                                                task.rd_dual = True
                                                task.rd_id = 16
                                            - Notes:
                                                1. If rd_id is set, rd_dual must also be set.

reconnect_interval                      The BGP reconnection interval for dropped
                                        sessions::

                                            - Type: int()
                                            - Valid values:
                                                - int() range 1-60
                                            - Units: seconds
                                            - Default: 60
                                            - Example:
                                                task.reconnect_interval = 15

router_id                               Router Identifier (ID) of the BGP
                                        router instance::

                                            - Type: str()
                                            - Valid values:
                                                - An ipv4 address without prefixlen
                                            - Example:
                                                task.router_id = '10.1.1.3'

shutdown                                Administratively shutdown the BGP
                                        router instance::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.shutdown = False

suppress_fib_pending                    Advertise only routes that are programmed in 
                                        hardware to peers::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.suppress_fib_pending = True

task_name                               Name of the task. Ansible will display this
                                        when the playbook is run::

                                            - Type: str()
                                            - Examples:
                                                - task.task_name = 'my task'

timers_bestpath_limit_always            Specify how advertisment of learned best paths
                                        are handled.  If set to False, wait for 
                                        ``timers_bestpath_timeout`` seconds after a BGP
                                        process restart before advertising learned best
                                        paths.  If set to True, always wait
                                        ``timers_bestpath_timeout`` seconds before advertising
                                        learned best paths::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.timers_bestpath_limit_always = True

timers_bestpath_limit_timeout           The amount of time (in seconds) to wait before
                                        advertising of learned best paths to neighbors::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-3600
                                            - Units: seconds
                                            - Default: 300
                                            - Example:
                                                task.timers_bestpath_limit_timeout = 180

timers_bgp_holdtime                     BGP holddown timer.
                                        How long before resetting bgp sessions
                                        after keepalives are not received from 
                                        a neighbor::

                                            - Type: int() or str()
                                            - Valid values:
                                                - int() range 3-3600
                                                - str() keyword: default
                                            - Units: seconds
                                            - Default: 180
                                            - Example:
                                                task.neighbor_timers_holdtime = 60
                                            - NOTES:
                                                1.  While the NXOS CLI claims the valid
                                                    range for holdtime is 0-3600, it will
                                                    not accept values less than 3, as of
                                                    version 9.3(7)
                                                2.  timers_bgp_holdtime must be greater
                                                    than timers_bgp_keepalive
    
timers_bgp_keepalive                    BGP keepalive interval.
                                        How often to send keepalives to BGP neighbors::

                                            - Type: int()
                                            - Valid values:
                                                - int() range 1-3599
                                            - Units: seconds
                                            - Default: 60
                                            - Example:
                                                task.neighbor_timers_holdtime = 60
                                            - NOTES:
                                                1.  While the NXOS CLI claims the valid
                                                    range for keepalive is 0-3600, it will
                                                    not accept values less than 1 (since keepalive
                                                    cannot be 0 if holddown is non-zero, and
                                                    the CLI down not allow a non-zero holddown),
                                                    and will not accept values greater than 3599
                                                    (since keepalive must be less than holddown).

timers_prefix_peer_timeout              Prefix-peer timeout::

                                            - Type: int()
                                            - Valid values:
                                                - int() range 1-1200
                                            - Units: seconds
                                            - Default: 90
                                            - Example:
                                                task.timers_prefix_peer_timeout = 60

timers_prefix_peer_wait                 Configure wait timer for a prefix peer::

                                            - Type: int()
                                            - Valid values:
                                                - int() range 1-1200
                                            - Units: seconds
                                            - Default: 90
                                            - Example:
                                                task.timers_prefix_peer_wait = 30

====================================    ==============================================

============================    ==============================================
VRF-specific Properties         Description
============================    ==============================================
vrf_allocate_index              Allocate per-vrf label on VPC peers::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-8000
                                    - Example:
                                        task.vrf = 'FOO'
                                        task.vrf_allocate_index = 1

vrf                             Name of VRF to create under the bgp router::

                                    - Type: str()
                                    - Examples:
                                        - task.vrf = 'MY_VRF'

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

