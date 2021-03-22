# NxosBgpGlobal() - cisco/nxos/nxos_bgp_global.py
our_version = 100
from copy import deepcopy
import re
from ask.common.task import Task
'''
**************************************
NxosBgpGlobal()
**************************************

.. contents::
   :local:
   :depth: 1

Status
------

- BETA

- This library is in development and not yet complete, nor fully-tested.  See TODO below for missing functionality.

TODO
----
1. Support for vrf not included yet
2. Support for states running_config, rendered not included yet
3. Verification of property mutual-exclusion not complete
4. Verification of required properties not complete
5. Verification of missing/dependent properties not complete

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

1. If ``vrf`` is set, all other properties will be applied to
   the vrf when ``task.add_vrf()`` is called.
2. Calling ``task.add_vrf()`` adds the vrf (along with all properties
   set in #1) and resets all properties.

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
                                            - <1-65535>.<0-65535>
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

disable_policy_batching_ipv4_prefix_list    Enable ``True`` or Disable ``False``
                                            batching evaluation of outbound
                                            policy for ipv4 peers in the provided
                                            ip prefix-list::

                                                - Type: str()
                                                - Valid values:
                                                    - An ip prefix-list name
                                                - Example:
                                                    task.disable_policy_batching_ipv4_prefix_list = 'DPB'

disable_policy_batching_ipv6_prefix_list    Enable ``True`` or Disable ``False``
                                            batching evaluation of outbound
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

'''

class NxosBgpGlobal(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp_global'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.bgp_neighbor_path_attribute_list = list()
        self.bgp_neighbors_list  = list()

        # The set of ansible module properties that should be written
        # when the user calls instance.update().
        # TODO: VERIFY these are written to the ansible_task
        self.ansible_module_set = set()
        self.ansible_module_set.add('state')
        self.ansible_module_set.add('running_config')

        # The set of atomic -- not members of a dict() -- 
        # bgp global (non-neighbor, non-vrf) properties.
        # Written when the user calls instance.update().
        # These will be written to the top-level of
        # self.config
        self.bgp_global_atomic_properties = set()
        self.bgp_global_atomic_properties.add('as_number')
        self.bgp_global_atomic_properties.add('cluster_id')
        self.bgp_global_atomic_properties.add('dynamic_med_interval')
        self.bgp_global_atomic_properties.add('enforce_first_as')
        self.bgp_global_atomic_properties.add('enhanced_error')
        self.bgp_global_atomic_properties.add('fabric_soo')
        self.bgp_global_atomic_properties.add('fast_external_fallover')
        self.bgp_global_atomic_properties.add('flush_routes')
        self.bgp_global_atomic_properties.add('log_neighbor_changes')
        self.bgp_global_atomic_properties.add('maxas_limit')
        self.bgp_global_atomic_properties.add('reconnect_interval')
        self.bgp_global_atomic_properties.add('router_id')
        self.bgp_global_atomic_properties.add('shutdown')
        self.bgp_global_atomic_properties.add('suppress_fib_pending')

        # The set of all bgp global (non-neighbor, non-vrf) properties
        # Used in init_bgp_global()
        self.bgp_global_set = set()
        self.bgp_global_set.add('affinity_group_group_id')
        self.bgp_global_set.add('as_number')
        self.bgp_global_set.add('bestpath_always_compare_med')
        self.bgp_global_set.add('bestpath_as_path_ignore')
        self.bgp_global_set.add('bestpath_as_path_multipath_relax')
        self.bgp_global_set.add('bestpath_compare_neighborid')
        self.bgp_global_set.add('bestpath_compare_routerid')
        self.bgp_global_set.add('bestpath_cost_community_ignore')
        self.bgp_global_set.add('bestpath_igp_metric_ignore')
        self.bgp_global_set.add('bestpath_med_confed')
        self.bgp_global_set.add('bestpath_med_non_deterministic')
        self.bgp_global_set.add('bestpath_med_missing_as_worst')
        self.bgp_global_set.add('cluster_id')
        self.bgp_global_set.add('confederation_identifier')
        self.bgp_global_set.add('confederation_peers')
        self.bgp_global_set.add('disable_policy_batching_ipv4_prefix_list')
        self.bgp_global_set.add('disable_policy_batching_ipv6_prefix_list')
        self.bgp_global_set.add('disable_policy_batching_nexthop')
        self.bgp_global_set.add('disable_policy_batching_set')
        self.bgp_global_set.add('dynamic_med_interval')
        self.bgp_global_set.add('enforce_first_as')
        self.bgp_global_set.add('enhanced_error')
        self.bgp_global_set.add('fabric_soo')
        self.bgp_global_set.add('fast_external_fallover')
        self.bgp_global_set.add('flush_routes')
        self.bgp_global_set.add('graceful_restart')
        self.bgp_global_set.add('graceful_restart_helper')
        self.bgp_global_set.add('graceful_restart_timers_restart')
        self.bgp_global_set.add('graceful_restart_timers_stalepath_time')
        self.bgp_global_set.add('graceful_shutdown_activate_route_map')
        self.bgp_global_set.add('graceful_shutdown_activate_set')
        self.bgp_global_set.add('graceful_shutdown_aware')
        self.bgp_global_set.add('isolate_include_local')
        self.bgp_global_set.add('isolate_set')
        self.bgp_global_set.add('log_neighbor_changes')
        self.bgp_global_set.add('maxas_limit')
        self.bgp_global_set.add('neighbor_down_fib_accelerate')
        self.bgp_global_set.add('nexthop_suppress_default_resolution')
        self.bgp_global_set.add('rd_dual')
        self.bgp_global_set.add('rd_id')
        self.bgp_global_set.add('reconnect_interval')
        self.bgp_global_set.add('router_id')
        self.bgp_global_set.add('shutdown')
        self.bgp_global_set.add('suppress_fib_pending')
        self.bgp_global_set.add('timers_bestpath_limit_always')
        self.bgp_global_set.add('timers_bestpath_limit_timeout')
        self.bgp_global_set.add('timers_bgp_holdtime')
        self.bgp_global_set.add('timers_bgp_keepalive')
        self.bgp_global_set.add('timers_prefix_peer_timeout')
        self.bgp_global_set.add('timers_prefix_peer_wait')

        # The set of atomic -- not members of a dict() -- 
        # bgp neighbor properties.
        # Written when the user calls instance.add_bgp_neighbor().
        # These will be written to the top-level of self.bgp_neighbor_dict
        # before it is appended to self.bgp_neighbor_list
        self.bgp_neighbor_atomic_properties = set()
        self.bgp_neighbor_atomic_properties.add('neighbor_address')
        self.bgp_neighbor_atomic_properties.add('neighbor_bmp_activate_server')
        self.bgp_neighbor_atomic_properties.add('neighbor_description')
        self.bgp_neighbor_atomic_properties.add('neighbor_disable_connected_check')
        self.bgp_neighbor_atomic_properties.add('neighbor_dont_capability_negotiate')
        self.bgp_neighbor_atomic_properties.add('neighbor_dscp')
        self.bgp_neighbor_atomic_properties.add('neighbor_dynamic_capability')
        self.bgp_neighbor_atomic_properties.add('neighbor_ebgp_multihop')
        self.bgp_neighbor_atomic_properties.add('neighbor_local_as')
        self.bgp_neighbor_atomic_properties.add('neighbor_low_memory_exempt')
        self.bgp_neighbor_atomic_properties.add('neighbor_peer_type')
        self.bgp_neighbor_atomic_properties.add('neighbor_remote_as')
        self.bgp_neighbor_atomic_properties.add('neighbor_shutdown')
        self.bgp_neighbor_atomic_properties.add('neighbor_update_source')

        # The set of properties that should be written if 
        # the caller has set vrf and calls instance.add_vrf().
        # These will be written to the top-level of config dict, 
        # after disambiguation, which is then appended to vrfs list()
        self.bgp_neighbor_set = set()
        self.bgp_neighbor_set.add('neighbor_address')
        self.bgp_neighbor_set.add('neighbor_affinity_group_group_id')
        self.bgp_neighbor_set.add('neighbor_bfd_multihop_interval_min_rx_interval')
        self.bgp_neighbor_set.add('neighbor_bfd_multihop_interval_multiplier')
        self.bgp_neighbor_set.add('neighbor_bfd_multihop_interval_tx_interval')
        self.bgp_neighbor_set.add('neighbor_bfd_multihop_set')
        self.bgp_neighbor_set.add('neighbor_bfd_set')
        self.bgp_neighbor_set.add('neighbor_bfd_singlehop')
        self.bgp_neighbor_set.add('neighbor_bmp_activate_server')
        self.bgp_neighbor_set.add('neighbor_capability_suppress_4_byte_as')
        self.bgp_neighbor_set.add('neighbor_description')
        self.bgp_neighbor_set.add('neighbor_disable_connected_check')
        self.bgp_neighbor_set.add('neighbor_dont_capability_negotiate')
        self.bgp_neighbor_set.add('neighbor_dscp')
        self.bgp_neighbor_set.add('neighbor_dynamic_capability')
        self.bgp_neighbor_set.add('neighbor_ebgp_multihop')
        self.bgp_neighbor_set.add('neighbor_graceful_shutdown_activate_route_map')
        self.bgp_neighbor_set.add('neighbor_graceful_shutdown_activate_set')
        self.bgp_neighbor_set.add('neighbor_inherit_peer')
        self.bgp_neighbor_set.add('neighbor_inherit_peer_session')
        self.bgp_neighbor_set.add('neighbor_local_as')
        self.bgp_neighbor_set.add('neighbor_log_neighbor_changes_disable')
        self.bgp_neighbor_set.add('neighbor_log_neighbor_changes_set')
        self.bgp_neighbor_set.add('neighbor_low_memory_exempt')
        self.bgp_neighbor_set.add('neighbor_password_encryption')
        self.bgp_neighbor_set.add('neighbor_password_key')
        # TODO make sure to add the following list()
        # to neighbor dict() prior to appending neighbor_dict()
        # to vrf_list
        # self.bgp_neighbor_path_attribute_list.
        self.bgp_neighbor_set.add('neighbor_path_attribute_action')
        self.bgp_neighbor_set.add('neighbor_path_attribute_range_end')
        self.bgp_neighbor_set.add('neighbor_path_attribute_range_start')
        self.bgp_neighbor_set.add('neighbor_path_attribute_type')
        self.bgp_neighbor_set.add('neighbor_peer_type')
        self.bgp_neighbor_set.add('neighbor_remote_as')
        self.bgp_neighbor_set.add('neighbor_remove_private_as_all')
        self.bgp_neighbor_set.add('neighbor_remove_private_as_replace_as')
        self.bgp_neighbor_set.add('neighbor_remove_private_as_set')
        self.bgp_neighbor_set.add('neighbor_shutdown')
        self.bgp_neighbor_set.add('neighbor_timers_holdtime')
        self.bgp_neighbor_set.add('neighbor_timers_keepalive')
        self.bgp_neighbor_set.add('neighbor_transport_connection_mode_passive')
        self.bgp_neighbor_set.add('neighbor_ttl_security_hops')
        self.bgp_neighbor_set.add('neighbor_update_source')

        # Used in self.add_bgp_neighbor_path_attribute()
        self.neighbor_path_attribute_set = set()
        self.neighbor_path_attribute_set.add('neighbor_path_attribute_action')
        self.neighbor_path_attribute_set.add('neighbor_path_attribute_range_end')
        self.neighbor_path_attribute_set.add('neighbor_path_attribute_range_start')
        self.neighbor_path_attribute_set.add('neighbor_path_attribute_type')

        # The set of properties that should be written if 
        # the caller has set vrf and calls instance.add_vrf().
        # These will be written to the top-level of config dict, 
        # after disambiguation, which is then appended to vrfs list()
        self.vrf_set = set()
        self.vrf_set.add('vrf_allocate_index')
        self.vrf_set.add('bestpath_always_compare_med')
        self.vrf_set.add('bestpath_as_path_ignore')
        self.vrf_set.add('bestpath_as_path_multipath_relax')
        self.vrf_set.add('bestpath_compare_neighborid')
        self.vrf_set.add('bestpath_compare_routerid')
        self.vrf_set.add('bestpath_cost_community_ignore')
        self.vrf_set.add('bestpath_igp_metric_ignore')
        self.vrf_set.add('bestpath_med_confed')
        self.vrf_set.add('bestpath_med_non_deterministic')
        self.vrf_set.add('bestpath_med_missing_as_worst')
        self.vrf_set.add('cluster_id')
        self.vrf_set.add('confederation_identifier')
        self.vrf_set.add('confederation_peers')
        self.vrf_set.add('graceful_restart_helper')
        self.vrf_set.add('graceful_restart_restart_time')
        self.vrf_set.add('graceful_restart_set')
        self.vrf_set.add('graceful_restart_stalepath_time')
        self.vrf_set.add('local_as')
        self.vrf_set.add('log_neighbor_changes')
        self.vrf_set.add('maxas_limit')
        self.vrf_set.add('neighbor_down_fib_accelerate')
        self.vrf_set.add('neighbor_bfd_multihop_interval_min_rx_interval')
        self.vrf_set.add('neighbor_bfd_multihop_interval_multiplier')
        self.vrf_set.add('neighbor_bfd_multihop_interval_tx_interval')
        self.vrf_set.add('neighbor_bfd_multihop_set')
        self.vrf_set.add('neighbor_bfd_set')
        self.vrf_set.add('neighbor_bfd_singlehop')
        self.vrf_set.add('neighbor_bmp_activate_server')
        self.vrf_set.add('neighbor_capability_suppress_4_byte_as')
        self.vrf_set.add('neighbor_description')
        self.vrf_set.add('neighbor_disable_connected_check')
        self.vrf_set.add('neighbor_dont_capability_negotiate')
        self.vrf_set.add('neighbor_dscp')
        self.vrf_set.add('neighbor_dynamic_capability')
        self.vrf_set.add('neighbor_ebgp_multihop')
        self.vrf_set.add('neighbor_graceful_shutdown_activate_route_map')
        self.vrf_set.add('neighbor_graceful_shutdown_activate_set')
        self.vrf_set.add('neighbor_inherit_peer')
        self.vrf_set.add('neighbor_inherit_peer_session')
        self.vrf_set.add('neighbor_local_as')
        self.vrf_set.add('neighbor_log_neighbor_changes_disable')
        self.vrf_set.add('neighbor_log_neighbor_changes_set')
        self.vrf_set.add('neighbor_low_memory_exempt')
        self.vrf_set.add('neighbor_address')
        self.vrf_set.add('neighbor_affinity_group_group_id')
        self.vrf_set.add('neighbor_password_encryption')
        self.vrf_set.add('neighbor_password_key')
        # TODO make sure to add the following list()
        # to neighbor dict() prior to appending neighbor_dict()
        # to vrf_list
        # self.bgp_neighbor_path_attribute_list.
        self.vrf_set.add('neighbor_path_attribute_action')
        self.vrf_set.add('neighbor_path_attribute_range_end')
        self.vrf_set.add('neighbor_path_attribute_range_start')
        self.vrf_set.add('neighbor_path_attribute_type')
        self.vrf_set.add('neighbor_peer_type')
        self.vrf_set.add('neighbor_remote_as')
        self.vrf_set.add('neighbor_remove_private_as_all')
        self.vrf_set.add('neighbor_remove_private_as_replace_as')
        self.vrf_set.add('neighbor_remove_private_as_set')
        self.vrf_set.add('neighbor_shutdown')
        self.vrf_set.add('neighbor_timers_holdtime')
        self.vrf_set.add('neighbor_timers_keepalive')
        self.vrf_set.add('neighbor_transport_connection_mode_passive')
        self.vrf_set.add('neighbor_ttl_security_hops')
        self.vrf_set.add('neighbor_update_source')
        self.vrf_set.add('reconnect_interval')
        self.vrf_set.add('router_id')
        self.vrf_set.add('timers_bestpath_limit_always')
        self.vrf_set.add('timers_bestpath_limit_timeout')
        self.vrf_set.add('timers_bgp_holdtime')
        self.vrf_set.add('timers_bgp_keepalive')
        self.vrf_set.add('timers_prefix_peer_timeout')
        self.vrf_set.add('timers_prefix_peer_wait')
        self.vrf_set.add('vrf')

        # propery_map is used to convert the disambiguated property
        # names that users access, to the (potentially) ambiguous 
        # property names that nxos_bgp_global uses.
        self.property_map = dict()
        self.property_map['affinity_group_group_id'] = 'group_id'
        self.property_map['as_number'] = 'as_number'
        self.property_map['bestpath_always_compare_med'] = 'always_compare_med'
        self.property_map['bestpath_as_path_ignore'] = 'ignore'
        self.property_map['bestpath_as_path_multipath_relax'] = 'multipath_relax'
        self.property_map['bestpath_compare_neighborid'] = 'compare_neighborid'
        self.property_map['bestpath_compare_routerid'] = 'compare_routerid'
        self.property_map['bestpath_cost_community_ignore'] = 'cost_community_ignore'
        self.property_map['bestpath_igp_metric_ignore'] = 'igp_metric_ignore'
        self.property_map['bestpath_med_confed'] = 'confed'
        self.property_map['bestpath_med_missing_as_worst'] = 'missing_as_worst'
        self.property_map['bestpath_med_non_deterministic'] = 'non_deterministic'
        self.property_map['cluster_id'] = 'cluster_id'
        self.property_map['confederation_identifier'] = 'identifier'
        self.property_map['confederation_peers'] = 'peers'
        self.property_map['disable_policy_batching_ipv4_prefix_list'] = 'prefix_list'
        self.property_map['disable_policy_batching_ipv6_prefix_list'] = 'prefix_list'
        self.property_map['disable_policy_batching_nexthop'] = 'nexthop'
        self.property_map['disable_policy_batching_set'] = 'set'
        self.property_map['dynamic_med_interval'] = 'dynamic_med_interval'
        self.property_map['enforce_first_as'] = 'enforce_first_as'
        self.property_map['enhanced_error'] = 'enhanced_error'
        self.property_map['fabric_soo'] = 'fabric_soo'
        self.property_map['fast_external_fallover'] = 'fast_external_fallover'
        self.property_map['flush_routes'] = 'flush_routes'
        self.property_map['graceful_restart_helper'] = 'helper'
        self.property_map['graceful_restart_restart_time'] = 'restart_time'
        self.property_map['graceful_restart_set'] = 'set'
        self.property_map['graceful_restart_stalepath_time'] = 'stalepath_time'
        self.property_map['graceful_shutdown_activate_route_map'] = 'route_map'
        self.property_map['graceful_shutdown_activate_set'] = 'set'
        self.property_map['graceful_shutdown_aware'] = 'aware'
        self.property_map['isolate_include_local'] = 'include_local'
        self.property_map['isolate_set'] = 'set'
        self.property_map['log_neighbor_changes'] = 'log_neighbor_changes'
        self.property_map['maxas_limit'] = 'maxas_limit'
        self.property_map['neighbor_down_fib_accelerate'] = 'fib_accelerate'
        self.property_map['neighbor_bfd_multihop_interval_min_rx_interval'] = 'min_rx_interval'
        self.property_map['neighbor_bfd_multihop_interval_multiplier'] = 'multiplier'
        self.property_map['neighbor_bfd_multihop_interval_tx_interval'] = 'tx_interval'
        self.property_map['neighbor_bfd_multihop_set'] = 'set'
        self.property_map['neighbor_bfd_set'] = 'set'
        self.property_map['neighbor_bfd_singlehop'] = 'singlehop'
        self.property_map['neighbor_bmp_activate_server'] = 'bmp_activate_server'
        self.property_map['neighbor_capability_suppress_4_byte_as'] = 'suppress_4_byte_as'
        self.property_map['neighbor_description'] = 'description'
        self.property_map['neighbor_disable_connected_check'] = 'disable_connected_check'
        self.property_map['neighbor_dont_capability_negotiate'] = 'dont_capability_negotiate'
        self.property_map['neighbor_dscp'] = 'dscp'
        self.property_map['neighbor_dynamic_capability'] = 'dynamic_capability'
        self.property_map['neighbor_ebgp_multihop'] = 'ebgp_multihop'
        self.property_map['neighbor_graceful_shutdown_activate_route_map'] = 'route_map'
        self.property_map['neighbor_graceful_shutdown_activate_set'] = 'set'
        self.property_map['neighbor_inherit_peer'] = 'peer'
        self.property_map['neighbor_inherit_peer_session'] = 'peer_session'
        self.property_map['neighbor_local_as'] = 'local_as'
        self.property_map['neighbor_log_neighbor_changes_disable'] = 'disable'
        self.property_map['neighbor_log_neighbor_changes_set'] = 'set'
        self.property_map['neighbor_low_memory_exempt'] = 'exempt'
        self.property_map['neighbor_address'] = 'neighbor_address'
        self.property_map['neighbor_affinity_group_group_id'] = 'group_id'
        self.property_map['neighbor_password_encryption'] = 'encryption'
        self.property_map['neighbor_password_key'] = 'key'
        self.property_map['neighbor_path_attribute_action'] = 'action'
        self.property_map['neighbor_path_attribute_range_end'] = 'end'
        self.property_map['neighbor_path_attribute_range_start'] = 'start'
        self.property_map['neighbor_path_attribute_type'] = 'type'
        self.property_map['neighbor_peer_type'] = 'peer_type'
        self.property_map['neighbor_remote_as'] = 'remote_as'
        self.property_map['neighbor_remove_private_as_all'] = 'all'
        self.property_map['neighbor_remove_private_as_replace_as'] = 'replace_as'
        self.property_map['neighbor_remove_private_as_set'] = 'set'
        self.property_map['neighbor_shutdown'] = 'shutdown'
        self.property_map['neighbor_timers_holdtime'] = 'holdtime'
        self.property_map['neighbor_timers_keepalive'] = 'keepalive'
        self.property_map['neighbor_transport_connection_mode_passive'] = 'passive'
        self.property_map['neighbor_ttl_security_hops'] = 'hops'
        self.property_map['neighbor_update_source'] = 'update_source'
        self.property_map['nexthop_suppress_default_resolution'] = 'suppress_default_resolution'
        self.property_map['rd_dual'] = 'dual'
        self.property_map['rd_id'] = 'id'
        self.property_map['reconnect_interval'] = 'reconnect_interval'
        self.property_map['router_id'] = 'router_id'
        self.property_map['shutdown'] = 'shutdown'
        self.property_map['suppress_fib_pending'] = 'suppress_fib_pending'
        self.property_map['timers_bestpath_limit_always'] = 'always'
        self.property_map['timers_bestpath_limit_timeout'] = 'timeout'
        self.property_map['timers_bgp_holdtime'] = 'holdtime'
        self.property_map['timers_bgp_keepalive'] = 'keepalive'
        self.property_map['timers_prefix_peer_timeout'] = 'prefix_peer_timeout'
        self.property_map['timers_prefix_peer_wait'] = 'prefix_peer_wait'

        self.nxos_bgp_global_valid_log_neighbor_changes = set()
        self.nxos_bgp_global_valid_log_neighbor_changes.add('no')
        self.nxos_bgp_global_valid_log_neighbor_changes.add('yes')

        self.nxos_bgp_global_valid_state = set()
        self.nxos_bgp_global_valid_state.add('deleted')
        self.nxos_bgp_global_valid_state.add('gathered')
        self.nxos_bgp_global_valid_state.add('merged')
        self.nxos_bgp_global_valid_state.add('overridden')
        self.nxos_bgp_global_valid_state.add('parsed')
        self.nxos_bgp_global_valid_state.add('rendered')
        self.nxos_bgp_global_valid_state.add('replaced')

        self.nxos_bgp_global_timers_bgp_holdtime_min = 3
        self.nxos_bgp_global_timers_bgp_holdtime_max = 3600
        self.nxos_bgp_global_timers_bgp_keepalive_min = 1
        self.nxos_bgp_global_timers_bgp_keepalive_max = 3599

        self.nxos_bgp_global_timers_prefix_peer_timeout_min = 1
        self.nxos_bgp_global_timers_prefix_peer_timeout_max = 1200

        self.nxos_bgp_global_timers_prefix_peer_wait_min = 1
        self.nxos_bgp_global_timers_prefix_peer_wait_max = 1200

        self.nxos_bgp_global_neighbor_bfd_multihop_interval_min_rx_interval_min = 250
        self.nxos_bgp_global_neighbor_bfd_multihop_interval_min_rx_interval_max = 999
        self.nxos_bgp_global_neighbor_bfd_multihop_interval_multiplier_min = 1
        self.nxos_bgp_global_neighbor_bfd_multihop_interval_multiplier_max = 50
        self.nxos_bgp_global_neighbor_bfd_multihop_interval_tx_interval_min = 250
        self.nxos_bgp_global_neighbor_bfd_multihop_interval_tx_interval_max = 999

        # properties_set is the full set of disambiguated property
        # names found in nxos_bgp_global module.  This includes all
        # global, neighbor, vrf, and ansible properties.
        self.properties_set = set()
        self.properties_set.update(self.ansible_module_set)
        self.properties_set.update(self.bgp_global_set)
        self.properties_set.update(self.bgp_neighbor_set)
        self.properties_set.update(self.vrf_set)

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_bgp_global_affinity_group_group_id_min = 1
        self.nxos_bgp_global_affinity_group_group_id_max = 4294967295

        self.nxos_bgp_global_dynamic_med_interval_min = 1
        self.nxos_bgp_global_dynamic_med_interval_max = 4294967295

        self.nxos_bgp_global_neighbor_affinity_group_group_id_min = 1
        self.nxos_bgp_global_neighbor_affinity_group_group_id_max = 4294967295

        self.nxos_bgp_global_neighbor_bmp_activate_server_min = 1
        self.nxos_bgp_global_neighbor_bmp_activate_server_max = 2

        self.nxos_bgp_global_neighbor_ebgp_multihop_min = 1
        self.nxos_bgp_global_neighbor_ebgp_multihop_max = 255

        self.nxos_bgp_global_neighbor_path_attribute_range_end_min = 1
        self.nxos_bgp_global_neighbor_path_attribute_range_end_max = 255

        self.nxos_bgp_global_neighbor_path_attribute_range_start_min = 1
        self.nxos_bgp_global_neighbor_path_attribute_range_start_max = 255

        self.nxos_bgp_global_neighbor_path_attribute_type_min = 1
        self.nxos_bgp_global_neighbor_path_attribute_type_max = 255

        self.nxos_bgp_global_neighbor_timers_holdtime_min = 3
        self.nxos_bgp_global_neighbor_timers_holdtime_max = 3600

        self.nxos_bgp_global_neighbor_timers_keepalive_min = 1
        self.nxos_bgp_global_neighbor_timers_keepalive_max = 3599

        self.nxos_bgp_global_neighbor_ttl_security_hops_min = 1
        self.nxos_bgp_global_neighbor_ttl_security_hops_max = 254

        self.nxos_bgp_global_rd_id_min = 1
        self.nxos_bgp_global_rd_id_max = 65535

        self.nxos_bgp_global_timers_bestpath_limit_timeout_min = 1
        self.nxos_bgp_global_timers_bestpath_limit_timeout_max = 3600

        self.nxos_bgp_global_valid_neighbor_path_attribute_action = set()
        self.nxos_bgp_global_valid_neighbor_path_attribute_action.add('discard')
        self.nxos_bgp_global_valid_neighbor_path_attribute_action.add('treat-as-withdraw')

        self.nxos_bgp_global_valid_neighbor_dscp = set()
        for x in range(0,64):
            self.nxos_bgp_global_valid_neighbor_dscp.add(str(x))
        for x in range(1,5):
            for y in range(1,4):
                self.nxos_bgp_global_valid_neighbor_dscp.add('af{}{}'.format(x,y))
        for x in range(1,8):
            self.nxos_bgp_global_valid_neighbor_dscp.add('cs{}'.format(x))
        self.nxos_bgp_global_valid_neighbor_dscp.add('default')
        self.nxos_bgp_global_valid_neighbor_dscp.add('ef')

        self.nxos_bgp_global_valid_neighbor_password_encryption = set()
        self.nxos_bgp_global_valid_neighbor_password_encryption.add(0)
        self.nxos_bgp_global_valid_neighbor_password_encryption.add(3)
        self.nxos_bgp_global_valid_neighbor_password_encryption.add(7)

        self.nxos_bgp_global_valid_neighbor_peer_type = set()
        self.nxos_bgp_global_valid_neighbor_peer_type.add('fabric-border-leaf')
        self.nxos_bgp_global_valid_neighbor_peer_type.add('fabric-external')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def init_bgp_neighbor_path_attribute(self):
        for p in self.neighbor_path_attribute_set:
            self.properties[p] = None
    def init_bgp_neighbor(self):
        self.bgp_neighbor_path_attribute_list = list()
        for p in self.bgp_neighbor_set:
            self.properties[p] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.as_number == None:
            self.task_log.error('exiting. call instance.as_number before calling instance.update()')
            exit(1)

    def update_affinity_group(self):
        d = dict()
        if self.affinity_group_group_id != None:
            d['group_id'] = self.affinity_group_group_id
            self.config['affinity_group'] = deepcopy(d)
    def update_bestpath(self):
        d = dict()
        as_path = dict()
        med = dict()
        if self.bestpath_always_compare_med != None:
            d['always_compare_med'] = self.bestpath_always_compare_med
        if self.bestpath_compare_neighborid != None:
            d['compare_neighborid'] = self.bestpath_compare_neighborid
        if self.bestpath_compare_routerid != None:
            d['compare_routerid'] = self.bestpath_compare_routerid
        if self.bestpath_cost_community_ignore != None:
            d['cost_community_ignore'] = self.bestpath_cost_community_ignore
        if self.bestpath_igp_metric_ignore != None:
            d['igp_metric_ignore'] = self.bestpath_igp_metric_ignore

        if self.bestpath_as_path_ignore != None:
            as_path['ignore'] = self.bestpath_as_path_ignore
        if self.bestpath_as_path_multipath_relax != None:
            as_path['multipath_relax'] = self.bestpath_as_path_multipath_relax
        if len(as_path) != 0:
            d['as_path'] = deepcopy(as_path)

        if self.bestpath_med_confed != None:
            med['confed'] = self.bestpath_med_confed
        if self.bestpath_med_missing_as_worst != None:
            med['missing_as_worst'] = self.bestpath_med_missing_as_worst
        if self.bestpath_med_non_deterministic != None:
            med['non_deterministic'] = self.bestpath_med_non_deterministic
        if len(med) != 0:
            d['med'] = deepcopy(med)
        if len(d) != 0:
            self.config['bestpath'] = deepcopy(d)

    def update_confederation(self):
        d = dict()
        if self.confederation_identifier != None:
            d['identifier'] = self.confederation_identifier
        if self.confederation_peers != None:
            d['peers'] = self.confederation_peers
        if len(d) != 0:
            self.config['confederation'] = deepcopy(d)

    def update_disable_policy_batching(self):
        d = dict()
        ipv4 = dict()
        ipv6 = dict()
        if self.disable_policy_batching_ipv4_prefix_list != None:
            ipv4['prefix_list'] = self.disable_policy_batching_ipv4_prefix_list
        if self.disable_policy_batching_ipv6_prefix_list != None:
            ipv6['prefix_list'] = self.disable_policy_batching_ipv6_prefix_list
        if self.disable_policy_batching_nexthop != None:
            d['nexthop'] = self.disable_policy_batching_nexthop
        if self.disable_policy_batching_set != None:
            d['set'] = self.disable_policy_batching_set
        if len(ipv4) != 0:
            d['ipv4'] = deepcopy(ipv4)
        if len(ipv6) != 0:
            d['ipv6'] = deepcopy(ipv6)
        if len(d) != 0:
            self.config['disable_policy_batching'] = deepcopy(d)

    def update_graceful_restart(self):
        d = dict()
        if self.graceful_restart_helper != None:
            d['helper'] = self.graceful_restart_helper
        if self.graceful_restart_restart_time != None:
            d['restart_time'] = self.graceful_restart_restart_time
        if self.graceful_restart_set != None:
            d['set'] = self.graceful_restart_set
        if self.graceful_restart_stalepath_time != None:
            d['stalepath_time'] = self.graceful_restart_stalepath_time
        if len(d) != 0:
            self.config['graceful_restart'] = deepcopy(d)

    def update_graceful_shutdown(self):
        d = dict()
        activate = dict()
        if self.graceful_shutdown_activate_route_map != None:
            activate['route_map'] = self.graceful_shutdown_activate_route_map
        if self.graceful_shutdown_activate_set != None:
            activate['set'] = self.graceful_shutdown_activate_set
        if self.graceful_shutdown_aware != None:
            d['aware'] = self.graceful_shutdown_aware
        if len(activate) != 0:
            d['activate'] = deepcopy(activate)
        if len(d) != 0:
            self.config['graceful_shutdown'] = deepcopy(d)

    def update_isolate(self):
        d = dict()
        if self.isolate_include_local != None:
            d['include_local'] = self.isolate_include_local
        if self.isolate_set != None:
            d['set'] = self.isolate_set
        if len(d) != 0:
            self.config['isolate'] = deepcopy(d)

    def update_neighbor_down(self):
        d = dict()
        if self.neighbor_down_fib_accelerate != None:
            d['fib_accelerate'] = self.neighbor_down_fib_accelerate
        if len(d) != 0:
            self.config['neighbor_down'] = deepcopy(d)

    def update_nexthop(self):
        d = dict()
        if self.nexthop_suppress_default_resolution != None:
            d['suppress_default_resolution'] = self.nexthop_suppress_default_resolution
        if len(d) != 0:
            self.config['nexthop'] = deepcopy(d)

    def verify_rd(self):
        if self.rd_id != None and self.rd_dual == None:
            self.task_log.error('exiting. if rd_id is set, rd_dual must also be set')
            exit(1)
    def update_rd(self):
        self.verify_rd()
        d = dict()
        if self.rd_dual != None:
            d['dual'] = self.rd_dual
        if self.rd_id != None:
            d['id'] = self.rd_id
        if len(d) != 0:
            self.config['rd'] = deepcopy(d)

    def update_timers(self):
        d = dict()
        bestpath_limit = dict()
        bgp = dict()
        if self.timers_bestpath_limit_always != None:
            bestpath_limit['always'] = self.timers_bestpath_limit_always
        if self.timers_bestpath_limit_timeout != None:
            bestpath_limit['timeout'] = self.timers_bestpath_limit_timeout
        if self.timers_bgp_keepalive != None:
            bgp['keepalive'] = self.timers_bgp_keepalive
        if self.timers_bgp_holdtime != None:
            bgp['holdtime'] = self.timers_bgp_holdtime
        if self.timers_prefix_peer_timeout != None:
            d['prefix_peer_timeout'] = self.timers_prefix_peer_timeout
        if self.timers_prefix_peer_wait != None:
            d['prefix_peer_wait'] = self.timers_prefix_peer_wait
        if len(bestpath_limit) != 0:
            d['bestpath_limit'] = deepcopy(bestpath_limit) 
        if len(bgp) != 0:
            d['bgp'] = deepcopy(bgp) 
        if len(d) != 0:
            self.config['timers'] = deepcopy(d)

    def update_bgp_global_atomic(self):
        '''
        Update all atomic (not member of a dictionary) properties at
        the top-level of self.config
        '''
        for p in self.bgp_global_atomic_properties:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                self.config[mapped_p] = self.properties[p]

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        self.config = dict()
        self.update_affinity_group()
        self.update_bestpath()
        self.update_confederation()
        self.update_disable_policy_batching()
        self.update_graceful_restart()
        self.update_graceful_shutdown()
        self.update_isolate()
        self.update_neighbor_down()
        self.update_nexthop()
        self.update_rd()
        self.update_timers()
        self.update_bgp_global_atomic()
        if len(self.bgp_neighbors_list) != 0:
            self.config['neighbors'] = deepcopy(self.bgp_neighbors_list)
        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['config'] = deepcopy(self.config)
        self.ansible_task[self.ansible_module]['state'] = self.state

    def verify_bgp_neighbor_path_attribute(self):
        if self.properties['neighbor_path_attribute_action'] == None:
            self.task_log.error('exiting. neighbor_path_attribute_action must be set before calling add_bgp_neighbor_path_attribute()')
            exit(1)
        if self.properties['neighbor_path_attribute_type'] != None:
            if self.properties['neighbor_path_attribute_range_start'] != None:
                self.task_log.error('exiting. neighbor_path_attribute_type is mutually-exclusive with neighbor_path_attribute_range_start')
                exit(1)
            if self.properties['neighbor_path_attribute_range_end'] != None:
                self.task_log.error('exiting. neighbor_path_attribute_type is mutually-exclusive with neighbor_path_attribute_range_end')
                exit(1)
    def add_bgp_neighbor_path_attribute(self):
        '''
        Add path attribute configuration to a BGP neighbor.

        Example:

        instance.neighbor_path_attribute_action = 'discard'
        instance.neighbor_path_attribute_range_start = 10
        instance.neighbor_path_attribute_range_start = 20
        instance.add_bgp_neighbor_path_attribute()
        instance.neighbor_path_attribute_action = 'treat-as-withdraw'
        instance.neighbor_path_attribute_type = 2
        instance.add_bgp_neighbor_path_attribute()
        instance.add_bgp_neighbor()
        If the above is going into a vrf...
        instance.vrf = 'FOO'
        instance.add_vrf()
        '''
        self.verify_bgp_neighbor_path_attribute()
        d = dict()
        for p in self.neighbor_path_attribute_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) == 0:
            self.task_log.error('exiting. One or more path attribute properties must be set before calling add_bgp_neighbor_path_attribute()')
            exit(1)
        self.bgp_neighbor_path_attribute_list.append(deepcopy(d))
        self.init_bgp_neighbor_path_attribute()

    def verify_bgp_neighbor(self):
        if self.properties['neighbor_address'] == None:
            self.task_log.error('exiting. Set neighbor_address before calling instance.add_bgp_neighbor()')
            exit(1)

    def verify_bgp_neighbor_bfd(self):
        interval_set = set()
        interval_set.add(self.neighbor_bfd_multihop_interval_min_rx_interval)
        interval_set.add(self.neighbor_bfd_multihop_interval_multiplier)
        interval_set.add(self.neighbor_bfd_multihop_interval_tx_interval)
        if None in interval_set and len(interval_set) != 1:
            self.task_log.error('exiting. neighbor bfd multihop interval requires all multihop interval properties to be set.')
            self.task_log.error('min_rx_interval {}'.format(self.neighbor_bfd_multihop_interval_min_rx_interval))
            self.task_log.error('multiplier {}'.format(self.neighbor_bfd_multihop_interval_multiplier))
            self.task_log.error('tx_interval {}'.format(self.neighbor_bfd_multihop_interval_tx_interval))
            exit(1)

    def update_bgp_neighbor_affinity_group(self):
        d = dict()
        if self.neighbor_affinity_group_group_id != None:
            d['group_id'] = self.neighbor_affinity_group_group_id
        if len(d) != 0:
            self.bgp_neighbor_dict['neighbor_affinity_group'] = deepcopy(d)

    def update_bgp_neighbor_atomic_properties(self):
        for p in self.bgp_neighbor_atomic_properties:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                self.bgp_neighbor_dict[mapped_p] = self.properties[p]

    def update_bgp_neighbor_bfd(self):
        self.verify_bgp_neighbor_bfd()
        d = dict()
        multihop = dict()
        interval = dict()
        if self.neighbor_bfd_multihop_interval_min_rx_interval != None:
            interval['min_rx_interval'] = self.neighbor_bfd_multihop_interval_min_rx_interval
        if self.neighbor_bfd_multihop_interval_multiplier != None:
            interval['multiplier'] = self.neighbor_bfd_multihop_interval_multiplier
        if self.neighbor_bfd_multihop_interval_tx_interval != None:
            interval['tx_interval'] = self.neighbor_bfd_multihop_interval_tx_interval
        if self.neighbor_bfd_multihop_set != None:
            multihop['set'] = self.neighbor_bfd_multihop_set
        if self.neighbor_bfd_set != None:
            d['set'] = self.neighbor_bfd_set
        if self.neighbor_bfd_singlehop != None:
            d['singlehop'] = self.neighbor_bfd_singlehop
        if len(interval) != 0:
            multihop['interval'] = deepcopy(interval)
        if len(multihop) != 0:
            d['multihop'] = deepcopy(multihop)
        if len(d) != 0:
            self.bgp_neighbor_dict['bfd'] = deepcopy(d)

    def update_bgp_neighbor_capability(self):
        d = dict()
        if self.neighbor_capability_suppress_4_byte_as != None:
            d['suppress_4_byte_as'] = self.neighbor_capability_suppress_4_byte_as
        if len(d) != 0:
            self.bgp_neighbor_dict['capability'] = deepcopy(d)

    def update_bgp_neighbor_graceful_shutdown(self):
        d = dict()
        activate = dict()
        if self.neighbor_graceful_shutdown_activate_route_map != None:
            activate['route_map'] = self.neighbor_graceful_shutdown_activate_route_map
        if self.neighbor_graceful_shutdown_activate_set != None:
            activate['set'] = self.neighbor_graceful_shutdown_activate_set
        if len(activate) != 0:
            d['activate'] = deepcopy(activate)
        if len(d) != 0:
            self.bgp_neighbor_dict['graceful_shutdown'] = deepcopy(d)

    def update_bgp_neighbor_inherit(self):
        d = dict()
        if self.neighbor_inherit_peer != None:
            d['peer'] = self.neighbor_inherit_peer
        if self.neighbor_inherit_peer_session != None:
            d['peer_session'] = self.neighbor_inherit_peer_session
        if len(d) != 0:
            self.bgp_neighbor_dict['inherit'] = deepcopy(d)

    def update_bgp_neighbor_log_neighbor_changes(self):
        d = dict()
        if self.neighbor_log_neighbor_changes_disable != None:
            d['disable'] = self.neighbor_log_neighbor_changes_disable
        if self.neighbor_log_neighbor_changes_set != None:
            d['set'] = self.neighbor_log_neighbor_changes_set
        if len(d) != 0:
            self.bgp_neighbor_dict['log_neighbor_changes'] = deepcopy(d)

    def update_bgp_neighbor_low_memory(self):
        d = dict()
        if self.neighbor_low_memory_exempt != None:
            d['exempt'] = self.neighbor_low_memory_exempt
        if len(d) != 0:
            self.bgp_neighbor_dict['low_memory'] = deepcopy(d)

    def update_bgp_neighbor_password(self):
        d = dict()
        if self.neighbor_password_encryption != None:
            d['encryption'] = self.neighbor_password_encryption
        if self.neighbor_password_key != None:
            d['key'] = self.neighbor_password_key
        if len(d) != 0:
            self.bgp_neighbor_dict['password'] = deepcopy(d)

    def update_bgp_neighbor_remove_private_as(self):
        d = dict()
        if self.neighbor_remove_private_as_all != None:
            d['all'] = self.neighbor_remove_private_as_all
        if self.neighbor_remove_private_as_replace_as != None:
            d['replace_as'] = self.neighbor_remove_private_as_replace_as
        if self.neighbor_remove_private_as_set != None:
            d['set'] = self.neighbor_remove_private_as_set
        if len(d) != 0:
            self.bgp_neighbor_dict['remove_private_as'] = deepcopy(d)

    def update_bgp_neighbor_timers(self):
        d = dict()
        if self.neighbor_timers_holdtime != None:
            d['holdtime'] = self.neighbor_timers_holdtime
        if self.neighbor_timers_keepalive != None:
            d['keepalive'] = self.neighbor_timers_keepalive
        if len(d) != 0:
            self.bgp_neighbor_dict['timers'] = deepcopy(d)

    def update_bgp_neighbor_transport(self):
        d = dict()
        connection_mode = dict()
        if self.neighbor_transport_connection_mode_passive != None:
            connection_mode['passive'] = self.neighbor_transport_connection_mode_passive
        if len(connection_mode) != 0:
            d['connection_mode'] = deepcopy(connection_mode)
        if len(d) != 0:
            self.bgp_neighbor_dict['transport'] = deepcopy(d)

    def update_bgp_neighbor_ttl_security(self):
        d = dict()
        if self.neighbor_ttl_security_hops != None:
            d['hops'] = self.neighbor_ttl_security_hops
        if len(d) != 0:
            self.bgp_neighbor_dict['ttl_security'] = deepcopy(d)

    def add_bgp_neighbor(self):
        '''
        Add a BGP neighbor to self.bgp_neighbors_list

        Example:

        instance.neighbor_address = '1.1.1.1'
        instance.neighbor_description = 'ISP_A'
        instance.neighbor_remote_as = 65001
        instance.neighbor_bfd_set = True
        instance.add_bgp_neighbor()
        If the above is going into a vrf...
        instance.vrf = 'FOO'
        instance.add_vrf()
        '''
        self.verify_bgp_neighbor()
        self.bgp_neighbor_dict = dict()
        self.update_bgp_neighbor_affinity_group()
        self.update_bgp_neighbor_atomic_properties()
        self.update_bgp_neighbor_bfd()
        self.update_bgp_neighbor_capability()
        self.update_bgp_neighbor_graceful_shutdown()
        self.update_bgp_neighbor_inherit()
        # START HERE 
        self.update_bgp_neighbor_log_neighbor_changes()
        self.update_bgp_neighbor_low_memory()
        self.update_bgp_neighbor_remove_private_as()
        self.update_bgp_neighbor_timers()
        self.update_bgp_neighbor_transport()
        self.update_bgp_neighbor_ttl_security()
        self.update_bgp_neighbor_password()
        if len(self.bgp_neighbor_path_attribute_list) != 0:
            self.bgp_neighbor_dict['path_attribute'] = deepcopy(self.bgp_neighbor_path_attribute_list)
        if len(self.bgp_neighbor_dict) == 0:
            self.task_log.error('exiting. One or more bgp neighbor properties must be set before calling add_bgp_neighbor()')
            exit(1)
        self.bgp_neighbors_list.append(deepcopy(self.bgp_neighbor_dict))
        self.init_bgp_neighbor()

    def add_vrf(self):
        self.task_log.error('exiting. add_vrf() is not yet supported.')
        exit(1)

    def verify_nxos_bgp_global_affinity_group_group_id(self, x, parameter='affinity_group_group_id'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_affinity_group_group_id_min
        range_max = self.nxos_bgp_global_affinity_group_group_id_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_dscp(self, x, parameter='dscp'):
        verify_set = self.nxos_bgp_global_valid_neighbor_dscp
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_global_neighbor_dscp'
        expectation = ','.join(sorted([str(x) for x in verify_set]))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_global_neighbor_ebgp_multihop(self, x, parameter='neighbor_ebgp_multihop'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_ebgp_multihop_min
        range_max = self.nxos_bgp_global_neighbor_ebgp_multihop_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_path_attribute_action(self, x, parameter='neighbor_path_attribute_action'):
        verify_set = self.nxos_bgp_global_valid_neighbor_path_attribute_action
        if x in verify_set:
            return
        source_class = self.class_name
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_global_neighbor_path_attribute_range_end(self, x, parameter='neighbor_path_attribute_range_end'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_path_attribute_range_end_min
        range_max = self.nxos_bgp_global_neighbor_path_attribute_range_end_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_path_attribute_range_start(self, x, parameter='neighbor_path_attribute_range_start'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_path_attribute_range_start_min
        range_max = self.nxos_bgp_global_neighbor_path_attribute_range_start_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_path_attribute_type(self, x, parameter='neighbor_path_attribute_type'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_path_attribute_type_min
        range_max = self.nxos_bgp_global_neighbor_path_attribute_type_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_timers_holdtime(self, x, parameter):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_timers_holdtime_min
        range_max = self.nxos_bgp_global_neighbor_timers_holdtime_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_timers_keepalive(self, x, parameter):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_timers_keepalive_min
        range_max = self.nxos_bgp_global_neighbor_timers_keepalive_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_ttl_security_hops(self, x, parameter):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_ttl_security_hops_min
        range_max = self.nxos_bgp_global_neighbor_ttl_security_hops_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_cluster_id(self, x, parameter='unspecified'):
        if self.is_ipv4_address(x):
            return
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_global_cluster_id'
        expectation = '[digits or ipv4_address]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_global_confederation_peers(self, x, parameter='confederation_peers'):
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_global_confederation_peers'
        expectation = '[list of digits and/or digits.digits]. example: [65023, 45123, 33542.34000]'
        if not type(x) == type(list()):
            self.fail(source_class, source_method, x, parameter, expectation)
        for item in x:
            if self.is_digits(item):
                continue
            if re.search('^\d+\.\d+$', str(item)):
                continue
            self.fail(source_class, source_method, x, parameter, expectation)

    def verify_bgp_global_neighbor_affinity_group_group_id(self, x, parameter):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_affinity_group_group_id_min
        range_max = self.nxos_bgp_global_neighbor_affinity_group_group_id_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_bgp_global_neighbor_bmp_activate_server(self, x, parameter='neighbor_bmp_activate_server'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_bmp_activate_server_min
        range_max = self.nxos_bgp_global_neighbor_bmp_activate_server_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_dynamic_med_interval(self, x, parameter='dynamic_med_interval'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_dynamic_med_interval_min
        range_max = self.nxos_bgp_global_dynamic_med_interval_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_bgp_global_neighbor_address(self, x, parameter='neighbor_address'):
        if self.is_ipv4_address(x):
            return
        if self.is_ipv6_address(x):
            return
        if self.is_ipv4_address_with_prefix(x):
            return
        if self.is_ipv6_address_with_prefix(x):
            return
        source_class = self.class_name
        source_method = 'verify_bgp_global_neighbor_address'
        expectation = '[ipv4/ipv6 address with or without prefixlen]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_global_rd_id(self, x, parameter='rd_id'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_rd_id_min
        range_max = self.nxos_bgp_global_rd_id_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_router_id(self, x, parameter='router_id'):
        if self.is_ipv4_address(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_global_router_id'
        expectation = "IPv4 Address without prefixlen. Example: 134.45.1.1"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_global_state(self, x, parameter='state'):
        verify_set = self.nxos_bgp_global_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_global_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_global_timers_bestpath_limit_timeout(self, x, parameter='bestpath_limit_timeout'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_timers_bestpath_limit_timeout_min
        range_max = self.nxos_bgp_global_timers_bestpath_limit_timeout_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_timers_bgp_holdtime(self, x, parameter='timers_bgp_holdtime'):
        if self.is_default(x):
            return
        source_class = self.class_name
        range_min = self.nxos_bgp_global_timers_bgp_holdtime_min
        range_max = self.nxos_bgp_global_timers_bgp_holdtime_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_timers_bgp_keepalive(self, x, parameter='timers_bgp_keepalive'):
        if self.is_default(x):
            return
        source_class = self.class_name
        range_min = self.nxos_bgp_global_timers_bgp_keepalive_min
        range_max = self.nxos_bgp_global_timers_bgp_keepalive_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_timers_prefix_peer_timeout(self, x, parameter='timers_prefix_peer_timeout'):
        if self.is_default(x):
            return
        source_class = self.class_name
        range_min = self.nxos_bgp_global_timers_prefix_peer_timeout_min
        range_max = self.nxos_bgp_global_timers_prefix_peer_timeout_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_timers_prefix_peer_wait(self, x, parameter='timers_prefix_peer_wait'):
        if self.is_default(x):
            return
        source_class = self.class_name
        range_min = self.nxos_bgp_global_timers_prefix_peer_wait_min
        range_max = self.nxos_bgp_global_timers_prefix_peer_wait_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_bfd_multihop_interval_min_rx_interval(self, x, parameter='bfd_multihop_interval_min_rx_interval'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_bfd_multihop_interval_min_rx_interval_min
        range_max = self.nxos_bgp_global_neighbor_bfd_multihop_interval_min_rx_interval_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_bfd_multihop_interval_multiplier(self, x, parameter='bfd_multihop_interval_multiplier'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_bfd_multihop_interval_multiplier_min
        range_max = self.nxos_bgp_global_neighbor_bfd_multihop_interval_multiplier_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_bfd_multihop_interval_tx_interval(self, x, parameter='bfd_multihop_interval_tx_interval'):
        source_class = self.class_name
        range_min = self.nxos_bgp_global_neighbor_bfd_multihop_interval_tx_interval_min
        range_max = self.nxos_bgp_global_neighbor_bfd_multihop_interval_tx_interval_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_global_neighbor_password_encryption(self, x, parameter='neighbor_password_encryption'):
        verify_set = self.nxos_bgp_global_valid_neighbor_password_encryption
        if x in verify_set:
            return
        source_method = 'verify_nxos_bgp_global_neighbor_password_encryption'
        source_class = self.class_name
        expectation = ','.join(str(x) for x in sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_global_neighbor_peer_type(self, x, parameter='neighbor_peer_type'):
        verify_set = self.nxos_bgp_global_valid_neighbor_peer_type
        if x in verify_set:
            return
        source_method = 'verify_nxos_bgp_global_neighbor_peer_type'
        source_class = self.class_name
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_global_neighbor_update_source(self, x, parameter='neighbor_update_source'):
        if self.is_ethernet_interface(x):
            return
        if self.is_loopback_interface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_method = 'verify_nxos_bgp_global_neighbor_update_source'
        source_class = self.class_name
        expectation = 'An interface, limited to type: Ethernet, loopback, port-channel, Vlan'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def affinity_group_group_id(self):
        return self.properties['affinity_group_group_id']
    @affinity_group_group_id.setter
    def affinity_group_group_id(self, x):
        parameter = 'affinity_group_group_id'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_affinity_group_group_id(x, parameter)
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
    def bestpath_always_compare_med(self):
        return self.properties['bestpath_always_compare_med']
    @bestpath_always_compare_med.setter
    def bestpath_always_compare_med(self, x):
        parameter = 'bestpath_always_compare_med'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_as_path_ignore(self):
        return self.properties['bestpath_as_path_ignore']
    @bestpath_as_path_ignore.setter
    def bestpath_as_path_ignore(self, x):
        parameter = 'bestpath_as_path_ignore'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_as_path_multipath_relax(self):
        return self.properties['bestpath_as_path_multipath_relax']
    @bestpath_as_path_multipath_relax.setter
    def bestpath_as_path_multipath_relax(self, x):
        parameter = 'bestpath_as_path_multipath_relax'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_compare_neighborid(self):
        return self.properties['bestpath_compare_neighborid']
    @bestpath_compare_neighborid.setter
    def bestpath_compare_neighborid(self, x):
        parameter = 'bestpath_compare_neighborid'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_compare_routerid(self):
        return self.properties['bestpath_compare_routerid']
    @bestpath_compare_routerid.setter
    def bestpath_compare_routerid(self, x):
        parameter = 'bestpath_compare_routerid'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_cost_community_ignore(self):
        return self.properties['bestpath_cost_community_ignore']
    @bestpath_cost_community_ignore.setter
    def bestpath_cost_community_ignore(self, x):
        parameter = 'bestpath_cost_community_ignore'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_igp_metric_ignore(self):
        return self.properties['bestpath_igp_metric_ignore']
    @bestpath_igp_metric_ignore.setter
    def bestpath_igp_metric_ignore(self, x):
        parameter = 'bestpath_igp_metric_ignore'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_med_confed(self):
        return self.properties['bestpath_med_confed']
    @bestpath_med_confed.setter
    def bestpath_med_confed(self, x):
        parameter = 'bestpath_med_confed'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_med_missing_as_worst(self):
        return self.properties['bestpath_med_missing_as_worst']
    @bestpath_med_missing_as_worst.setter
    def bestpath_med_missing_as_worst(self, x):
        parameter = 'bestpath_med_missing_as_worst'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_med_non_deterministic(self):
        return self.properties['bestpath_med_non_deterministic']
    @bestpath_med_non_deterministic.setter
    def bestpath_med_non_deterministic(self, x):
        parameter = 'bestpath_med_non_deterministic'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def cluster_id(self):
        return self.properties['cluster_id']
    @cluster_id.setter
    def cluster_id(self, x):
        parameter = 'cluster_id'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_cluster_id(x, parameter)
        self.properties[parameter] = x

    @property
    def confederation_identifier(self):
        return self.properties['confederation_identifier']
    @confederation_identifier.setter
    def confederation_identifier(self, x):
        parameter = 'confederation_identifier'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def confederation_peers(self):
        return self.properties['confederation_peers']
    @confederation_peers.setter
    def confederation_peers(self, x):
        parameter = 'confederation_peers'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_confederation_peers(x, parameter)
        self.properties[parameter] = x

    @property
    def disable_policy_batching_set(self):
        return self.properties['disable_policy_batching_set']
    @disable_policy_batching_set.setter
    def disable_policy_batching_set(self, x):
        parameter = 'disable_policy_batching_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def disable_policy_batching_ipv4_prefix_list(self):
        return self.properties['disable_policy_batching_ipv4_prefix_list']
    @disable_policy_batching_ipv4_prefix_list.setter
    def disable_policy_batching_ipv4_prefix_list(self, x):
        parameter = 'disable_policy_batching_ipv4_prefix_list'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def disable_policy_batching_ipv6_prefix_list(self):
        return self.properties['disable_policy_batching_ipv6_prefix_list']
    @disable_policy_batching_ipv6_prefix_list.setter
    def disable_policy_batching_ipv6_prefix_list(self, x):
        parameter = 'disable_policy_batching_ipv6_prefix_list'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def disable_policy_batching_nexthop(self):
        return self.properties['disable_policy_batching_nexthop']
    @disable_policy_batching_nexthop.setter
    def disable_policy_batching_nexthop(self, x):
        parameter = 'disable_policy_batching_nexthop'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def dynamic_med_interval(self):
        return self.properties['dynamic_med_interval']
    @dynamic_med_interval.setter
    def dynamic_med_interval(self, x):
        parameter = 'dynamic_med_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_dynamic_med_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def enforce_first_as(self):
        return self.properties['enforce_first_as']
    @enforce_first_as.setter
    def enforce_first_as(self, x):
        parameter = 'enforce_first_as'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def enhanced_error(self):
        return self.properties['enhanced_error']
    @enhanced_error.setter
    def enhanced_error(self, x):
        parameter = 'enhanced_error'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def fabric_soo(self):
        return self.properties['fabric_soo']
    @fabric_soo.setter
    def fabric_soo(self, x):
        parameter = 'fabric_soo'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def fast_external_fallover(self):
        return self.properties['fast_external_fallover']
    @fast_external_fallover.setter
    def fast_external_fallover(self, x):
        parameter = 'fast_external_fallover'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

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
    def graceful_restart_helper(self):
        return self.properties['graceful_restart_helper']
    @graceful_restart_helper.setter
    def graceful_restart_helper(self, x):
        parameter = 'graceful_restart_helper'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def graceful_restart_restart_time(self):
        return self.properties['graceful_restart_restart_time']
    @graceful_restart_restart_time.setter
    def graceful_restart_restart_time(self, x):
        parameter = 'graceful_restart_restart_time'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 3600, self.class_name, parameter)
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
    def graceful_restart_stalepath_time(self):
        return self.properties['graceful_restart_stalepath_time']
    @graceful_restart_stalepath_time.setter
    def graceful_restart_stalepath_time(self, x):
        parameter = 'graceful_restart_stalepath_time'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 3600, self.class_name, parameter)
        self.properties[parameter] = x

    @property
    def graceful_shutdown_activate_route_map(self):
        return self.properties['graceful_shutdown_activate_route_map']
    @graceful_shutdown_activate_route_map.setter
    def graceful_shutdown_activate_route_map(self, x):
        parameter = 'graceful_shutdown_activate_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def graceful_shutdown_activate_set(self):
        return self.properties['graceful_shutdown_activate_set']
    @graceful_shutdown_activate_set.setter
    def graceful_shutdown_activate_set(self, x):
        parameter = 'graceful_shutdown_activate_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def graceful_shutdown_aware(self):
        return self.properties['graceful_shutdown_aware']
    @graceful_shutdown_aware.setter
    def graceful_shutdown_aware(self, x):
        parameter = 'graceful_shutdown_aware'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def isolate_include_local(self):
        return self.properties['isolate_include_local']
    @isolate_include_local.setter
    def isolate_include_local(self, x):
        parameter = 'isolate_include_local'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def isolate_set(self):
        return self.properties['isolate_set']
    @isolate_set.setter
    def isolate_set(self, x):
        parameter = 'isolate_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def local_as(self):
        return self.properties['local_as']
    @local_as.setter
    def local_as(self, x):
        parameter = 'local_as'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def log_neighbor_changes(self):
        return self.properties['log_neighbor_changes']
    @log_neighbor_changes.setter
    def log_neighbor_changes(self, x):
        parameter = 'log_neighbor_changes'
        if self.set_none(x, parameter):
            return
        if x not in self.nxos_bgp_global_valid_log_neighbor_changes:
            _expectation = ','.join(self.nxos_bgp_global_valid_log_neighbor_changes)
            self.fail(self.class_name, parameter, x, parameter, _expectation)
        self.properties[parameter] = x

    @property
    def maxas_limit(self):
        return self.properties['maxas_limit']
    @maxas_limit.setter
    def maxas_limit(self, x):
        parameter = 'maxas_limit'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 512, self.class_name, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_address(self):
        return self.properties['neighbor_address']
    @neighbor_address.setter
    def neighbor_address(self, x):
        parameter = 'neighbor_address'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_global_neighbor_address(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_affinity_group_group_id(self):
        return self.properties['neighbor_affinity_group_group_id']
    @neighbor_affinity_group_group_id.setter
    def neighbor_affinity_group_group_id(self, x):
        parameter = 'neighbor_affinity_group_group_id'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_global_neighbor_affinity_group_group_id(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_bfd_multihop_interval_min_rx_interval(self):
        return self.properties['neighbor_bfd_multihop_interval_min_rx_interval']
    @neighbor_bfd_multihop_interval_min_rx_interval.setter
    def neighbor_bfd_multihop_interval_min_rx_interval(self, x):
        parameter = 'neighbor_bfd_multihop_interval_min_rx_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_bfd_multihop_interval_min_rx_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_bfd_multihop_interval_multiplier(self):
        return self.properties['neighbor_bfd_multihop_interval_multiplier']
    @neighbor_bfd_multihop_interval_multiplier.setter
    def neighbor_bfd_multihop_interval_multiplier(self, x):
        parameter = 'neighbor_bfd_multihop_interval_multiplier'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_bfd_multihop_interval_multiplier(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_bfd_multihop_interval_tx_interval(self):
        return self.properties['neighbor_bfd_multihop_interval_tx_interval']
    @neighbor_bfd_multihop_interval_tx_interval.setter
    def neighbor_bfd_multihop_interval_tx_interval(self, x):
        parameter = 'neighbor_bfd_multihop_interval_tx_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_bfd_multihop_interval_tx_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_bfd_multihop_set(self):
        return self.properties['neighbor_bfd_multihop_set']
    @neighbor_bfd_multihop_set.setter
    def neighbor_bfd_multihop_set(self, x):
        parameter = 'neighbor_bfd_multihop_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_bfd_set(self):
        return self.properties['neighbor_bfd_set']
    @neighbor_bfd_set.setter
    def neighbor_bfd_set(self, x):
        parameter = 'neighbor_bfd_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_bfd_singlehop(self):
        return self.properties['neighbor_bfd_singlehop']
    @neighbor_bfd_singlehop.setter
    def neighbor_bfd_singlehop(self, x):
        parameter = 'neighbor_bfd_singlehop'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_bmp_activate_server(self):
        return self.properties['neighbor_bmp_activate_server']
    @neighbor_bmp_activate_server.setter
    def neighbor_bmp_activate_server(self, x):
        parameter = 'neighbor_bmp_activate_server'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_global_neighbor_bmp_activate_server(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_capability_suppress_4_byte_as(self):
        return self.properties['neighbor_capability_suppress_4_byte_as']
    @neighbor_capability_suppress_4_byte_as.setter
    def neighbor_capability_suppress_4_byte_as(self, x):
        parameter = 'neighbor_capability_suppress_4_byte_as'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_description(self):
        return self.properties['neighbor_description']
    @neighbor_description.setter
    def neighbor_description(self, x):
        parameter = 'neighbor_description'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def neighbor_disable_connected_check(self):
        return self.properties['neighbor_disable_connected_check']
    @neighbor_disable_connected_check.setter
    def neighbor_disable_connected_check(self, x):
        parameter = 'neighbor_disable_connected_check'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_dont_capability_negotiate(self):
        return self.properties['neighbor_dont_capability_negotiate']
    @neighbor_dont_capability_negotiate.setter
    def neighbor_dont_capability_negotiate(self, x):
        parameter = 'neighbor_dont_capability_negotiate'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_down_fib_accelerate(self):
        return self.properties['neighbor_down_fib_accelerate']
    @neighbor_down_fib_accelerate.setter
    def neighbor_down_fib_accelerate(self, x):
        parameter = 'neighbor_down_fib_accelerate'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_dscp(self):
        return self.properties['neighbor_dscp']
    @neighbor_dscp.setter
    def neighbor_dscp(self, x):
        parameter = 'neighbor_dscp'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_dscp(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_dynamic_capability(self):
        return self.properties['neighbor_dynamic_capability']
    @neighbor_dynamic_capability.setter
    def neighbor_dynamic_capability(self, x):
        parameter = 'neighbor_dynamic_capability'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_ebgp_multihop(self):
        return self.properties['neighbor_ebgp_multihop']
    @neighbor_ebgp_multihop.setter
    def neighbor_ebgp_multihop(self, x):
        parameter = 'neighbor_ebgp_multihop'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_ebgp_multihop(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_graceful_shutdown_activate_route_map(self):
        return self.properties['neighbor_graceful_shutdown_activate_route_map']
    @neighbor_graceful_shutdown_activate_route_map.setter
    def neighbor_graceful_shutdown_activate_route_map(self, x):
        parameter = 'neighbor_graceful_shutdown_activate_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def neighbor_graceful_shutdown_activate_set(self):
        return self.properties['neighbor_graceful_shutdown_activate_set']
    @neighbor_graceful_shutdown_activate_set.setter
    def neighbor_graceful_shutdown_activate_set(self, x):
        parameter = 'neighbor_graceful_shutdown_activate_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_inherit_peer(self):
        return self.properties['neighbor_inherit_peer']
    @neighbor_inherit_peer.setter
    def neighbor_inherit_peer(self, x):
        parameter = 'neighbor_inherit_peer'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def neighbor_inherit_peer_session(self):
        return self.properties['neighbor_inherit_peer_session']
    @neighbor_inherit_peer_session.setter
    def neighbor_inherit_peer_session(self, x):
        parameter = 'neighbor_inherit_peer_session'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def neighbor_local_as(self):
        return self.properties['neighbor_local_as']
    @neighbor_local_as.setter
    def neighbor_local_as(self, x):
        parameter = 'neighbor_local_as'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_log_neighbor_changes_disable(self):
        return self.properties['neighbor_log_neighbor_changes_disable']
    @neighbor_log_neighbor_changes_disable.setter
    def neighbor_log_neighbor_changes_disable(self, x):
        parameter = 'neighbor_log_neighbor_changes_disable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_log_neighbor_changes_set(self):
        return self.properties['neighbor_log_neighbor_changes_set']
    @neighbor_log_neighbor_changes_set.setter
    def neighbor_log_neighbor_changes_set(self, x):
        parameter = 'neighbor_log_neighbor_changes_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_low_memory_exempt(self):
        return self.properties['neighbor_low_memory_exempt']
    @neighbor_low_memory_exempt.setter
    def neighbor_low_memory_exempt(self, x):
        parameter = 'neighbor_low_memory_exempt'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_password_encryption(self):
        return self.properties['neighbor_password_encryption']
    @neighbor_password_encryption.setter
    def neighbor_password_encryption(self, x):
        parameter = 'neighbor_password_encryption'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_password_encryption(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_password_key(self):
        return self.properties['neighbor_password_key']
    @neighbor_password_key.setter
    def neighbor_password_key(self, x):
        parameter = 'neighbor_password_key'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def neighbor_path_attribute_action(self):
        return self.properties['neighbor_path_attribute_action']
    @neighbor_path_attribute_action.setter
    def neighbor_path_attribute_action(self, x):
        parameter = 'neighbor_path_attribute_action'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_path_attribute_action(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_path_attribute_range_start(self):
        return self.properties['neighbor_path_attribute_range_start']
    @neighbor_path_attribute_range_start.setter
    def neighbor_path_attribute_range_start(self, x):
        parameter = 'neighbor_path_attribute_range_start'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_path_attribute_range_start(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_path_attribute_range_end(self):
        return self.properties['neighbor_path_attribute_range_end']
    @neighbor_path_attribute_range_end.setter
    def neighbor_path_attribute_range_end(self, x):
        parameter = 'neighbor_path_attribute_range_end'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_path_attribute_range_end(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_path_attribute_type(self):
        return self.properties['neighbor_path_attribute_type']
    @neighbor_path_attribute_type.setter
    def neighbor_path_attribute_type(self, x):
        parameter = 'neighbor_path_attribute_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_path_attribute_type(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_peer_type(self):
        return self.properties['neighbor_peer_type']
    @neighbor_peer_type.setter
    def neighbor_peer_type(self, x):
        parameter = 'neighbor_peer_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_peer_type(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_remote_as(self):
        return self.properties['neighbor_remote_as']
    @neighbor_remote_as.setter
    def neighbor_remote_as(self, x):
        parameter = 'neighbor_remote_as'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_remove_private_as_all(self):
        return self.properties['neighbor_remove_private_as_all']
    @neighbor_remove_private_as_all.setter
    def neighbor_remove_private_as_all(self, x):
        parameter = 'neighbor_remove_private_as_all'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_remove_private_as_replace_as(self):
        return self.properties['neighbor_remove_private_as_replace_as']
    @neighbor_remove_private_as_replace_as.setter
    def neighbor_remove_private_as_replace_as(self, x):
        parameter = 'neighbor_remove_private_as_replace_as'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_remove_private_as_set(self):
        return self.properties['neighbor_remove_private_as_set']
    @neighbor_remove_private_as_set.setter
    def neighbor_remove_private_as_set(self, x):
        parameter = 'neighbor_remove_private_as_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_shutdown(self):
        return self.properties['neighbor_shutdown']
    @neighbor_shutdown.setter
    def neighbor_shutdown(self, x):
        parameter = 'neighbor_shutdown'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_timers_holdtime(self):
        return self.properties['neighbor_timers_holdtime']
    @neighbor_timers_holdtime.setter
    def neighbor_timers_holdtime(self, x):
        parameter = 'neighbor_timers_holdtime'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_timers_holdtime(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_timers_keepalive(self):
        return self.properties['neighbor_timers_keepalive']
    @neighbor_timers_keepalive.setter
    def neighbor_timers_keepalive(self, x):
        parameter = 'neighbor_timers_keepalive'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_timers_keepalive(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_transport_connection_mode_passive(self):
        return self.properties['neighbor_transport_connection_mode_passive']
    @neighbor_transport_connection_mode_passive.setter
    def neighbor_transport_connection_mode_passive(self, x):
        parameter = 'neighbor_transport_connection_mode_passive'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_ttl_security_hops(self):
        return self.properties['neighbor_ttl_security_hops']
    @neighbor_ttl_security_hops.setter
    def neighbor_ttl_security_hops(self, x):
        parameter = 'neighbor_ttl_security_hops'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_ttl_security_hops(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_update_source(self):
        return self.properties['neighbor_update_source']
    @neighbor_update_source.setter
    def neighbor_update_source(self, x):
        parameter = 'neighbor_update_source'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_neighbor_update_source(x, parameter)
        self.properties[parameter] = x

    @property
    def nexthop_suppress_default_resolution(self):
        return self.properties['nexthop_suppress_default_resolution']
    @nexthop_suppress_default_resolution.setter
    def nexthop_suppress_default_resolution(self, x):
        parameter = 'nexthop_suppress_default_resolution'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties['nexthop_suppress_default_resolution'] = x

    @property
    def rd_dual(self):
        return self.properties['rd_dual']
    @rd_dual.setter
    def rd_dual(self, x):
        parameter = 'rd_dual'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties['rd_dual'] = x

    @property
    def rd_id(self):
        return self.properties['rd_id']
    @rd_id.setter
    def rd_id(self, x):
        parameter = 'rd_id'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_rd_id(x, parameter)
        self.properties['rd_id'] = x

    @property
    def reconnect_interval(self):
        return self.properties['reconnect_interval']
    @reconnect_interval.setter
    def reconnect_interval(self, x):
        parameter = 'reconnect_interval'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 60, self.class_name, parameter)
        self.properties[parameter] = x

    @property
    def router_id(self):
        return self.properties['router_id']
    @router_id.setter
    def router_id(self, x):
        parameter = 'router_id'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_router_id(x, parameter)
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
        self.properties['shutdown'] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_fib_pending(self):
        return self.properties['suppress_fib_pending']
    @suppress_fib_pending.setter
    def suppress_fib_pending(self, x):
        parameter = 'suppress_fib_pending'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_bestpath_limit_always(self):
        return self.properties['timers_bestpath_limit_always']
    @timers_bestpath_limit_always.setter
    def timers_bestpath_limit_always(self, x):
        parameter = 'timers_bestpath_limit_always'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_bestpath_limit_timeout(self):
        return self.properties['timers_bestpath_limit_timeout']
    @timers_bestpath_limit_timeout.setter
    def timers_bestpath_limit_timeout(self, x):
        parameter = 'timers_bestpath_limit_timeout'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_timers_bestpath_limit_timeout(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_bgp_holdtime(self):
        return self.properties['timers_bgp_holdtime']
    @timers_bgp_holdtime.setter
    def timers_bgp_holdtime(self, x):
        parameter = 'timers_bgp_holdtime'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_timers_bgp_holdtime(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_bgp_keepalive(self):
        return self.properties['timers_bgp_keepalive']
    @timers_bgp_keepalive.setter
    def timers_bgp_keepalive(self, x):
        parameter = 'timers_bgp_keepalive'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_timers_bgp_keepalive(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_prefix_peer_timeout(self):
        return self.properties['timers_prefix_peer_timeout']
    @timers_prefix_peer_timeout.setter
    def timers_prefix_peer_timeout(self, x):
        parameter = 'timers_prefix_peer_timeout'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_timers_prefix_peer_timeout(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_prefix_peer_wait(self):
        return self.properties['timers_prefix_peer_wait']
    @timers_prefix_peer_wait.setter
    def timers_prefix_peer_wait(self, x):
        parameter = 'timers_prefix_peer_wait'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_global_timers_prefix_peer_wait(x, parameter)
        self.properties[parameter] = x
