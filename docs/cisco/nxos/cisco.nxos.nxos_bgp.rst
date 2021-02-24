**************************************
NxosBgp()
**************************************

.. contents::
   :local:
   :depth: 1

Deprecation
-----------

- Status: ``DEPRECATED``
- Alternative: `nxos_bgp_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_global_module.rst>`_
- 2021-01-27, deprecation date
- 2023-01-27, removal date (module may be removed after this date)

ScriptKit Synopsis
------------------
- NxosBgp() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
asn                                 BGP autonomous system number, in ``ASPLAIN`` 
                                    or ``ASDOT`` notation::

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

bestpath_always_compare_med         Enable/Disable MED comparison on paths from 
                                    different autonomous systems::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.bestpath_always_compare_med = False

bestpath_aspath_multipath_relax     Enable/Disable load sharing across peers 
                                    with different (but equal-length) AS paths::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.bestpath_aspath_multipath_relax = True

bestpath_compare_neighborid         Enable/Disable neighborid comparison. Use this
                                    when more are paths available than max path config::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.bestpath_compare_neighborid = True

bestpath_compare_routerid           Enable/Disable comparison of router IDs for identical
                                    eBGP paths::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.bestpath_compare_routerid = True

bestpath_cost_community_ignore      Enable/Disable Ignores the cost community for
                                    BGP best-path calculations::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.bestpath_cost_community_ignore = True

bestpath_med_confed                 Enable/Disable enforcement of bestpath to do a
                                    MED comparison only between paths originated
                                    within a confederation::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.bestpath_med_confed = True

bestpath_med_missing_as_worst       Enable/Disable assigns the value of infinity to
                                    received routes that do not carry the MED
                                    attribute, making these routes the least
                                    desirable::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.bestpath_med_missing_as_worst = True

bestpath_med_non_deterministic      Enable/Disable deterministic selection of the 
                                    best MED path from among the paths from the 
                                    same autonomous system::

                                        - Type: bool()
                                        - Valid values: False, True
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

confederation_id                    Routing domain confederation AS::

                                        - Type: int() or str()
                                        - Valid values:
                                            - int() range 1-4294967295
                                            - <1-65535>.<0-65535>
                                        - Examples:
                                            task.confederation_id = 64512
                                            task.confederation_id = 4200000000
                                            task.confederation_id = '2301.0'

confederation_peers                 Peer ASs in BGP confederation::

                                        - Type: str()
                                        - Valid values:
                                            - quoted, space-separated list of ASs
                                        Example:
                                            peers = list()
                                            peers.append('64512')
                                            peers.append('64513.0')
                                            peers.append('64523')
                                            task.confederation_peers = ' '.join(peers)
                                        NOTES:
                                            - confederation_id must be configured first

disable_policy_batching             Enable/Disable the batching evaluation of
                                    prefix advertisement to all peers::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.disable_policy_batching = True
================================    ==============================================

|

========================================    =========================================
Property                                    Description
========================================    =========================================
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
========================================    =========================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
enforce_first_as                    Enable ``True`` or disable ``False`` enforcement
                                    that the neighbor autonomous system must be the
                                    first AS number listed in the AS path attribute
                                    for eBGP::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.enforce_first_as = True

event_history_cli                   Modify size of the cli event history buffer::

                                        - Type: str()
                                        - Valid values:
                                            - size_small
                                            - size_medium
                                            - size_large
                                            - size_disable
                                            - default
                                        - Example:
                                            task.event_history_cli = 'size_large'

event_history_detail                Modify size of the detail event history buffer::

                                        - Type: str()
                                        - Valid values:
                                            - size_small
                                            - size_medium
                                            - size_large
                                            - size_disable
                                            - default
                                        - Example:
                                            task.event_history_detail = 'size_disable'

event_history_events                Modify size of the events history buffer::

                                        - Type: str()
                                        - Valid values:
                                            - size_small
                                            - size_medium
                                            - size_large
                                            - size_disable
                                            - default
                                        - Example:
                                            task.event_history_events = 'default'

event_history_periodic              Modify size of the periodic event history buffer::

                                        - Type: str()
                                        - Valid values:
                                            - size_small
                                            - size_medium
                                            - size_large
                                            - size_disable
                                            - default
                                        - Example:
                                            task.event_history_periodic = 'size_small'

fast_external_fallover              Enable ``True`` or disable ``False``
                                    immediate session reset  if the link to a 
                                    directly connected BGP peer goes down::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.fast_external_fallover = True

flush_routes                        Enable ``True`` or disable ``False``  
                                    flush routes in RIB upon controlled restart::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.flush_routes = True

graceful_restart                    Enable ``True`` or disable ``False`` 
                                    graceful restart::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.graceful_restart = True

graceful_restart_helper             Enable ``True`` or disable ``False``
                                    graceful restart helper mode::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.graceful_restart_helper = True

graceful_restart_timers_restart     Set maximum time for a restart sent to the BGP peer::

                                        - Type: int()
                                        - Valid values: range: 1-3600
                                        - Default: 120
                                        - Example:
                                            task.graceful_restart_timers_restart = 300

================================    ==============================================

|

========================================    =========================================
Property                                    Description
========================================    =========================================
graceful_restart_timers_stalepath_time      Set maximum time that BGP keeps the stale
                                            routes from the restarting BGP peer::

                                                - Type: int()
                                                - Valid values: range: 1-3600
                                                - Default: 300
                                                - Example:
                                                    task.graceful_restart_timers_restart = 120

========================================    =========================================

============================    ==============================================
Property                        Description
============================    ==============================================
isolate                         Enable ``True`` or disable ``False``  
                                isolate this router from BGP perspective::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.isolate = False

local_as                        Specify the local-as number to be used
                                within a BGP router VRF instance
                                in ``ASPLAIN`` or ``ASDOT`` notation::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-4294967295
                                        - <1-65535>.<0-65535>
                                        - str() Keyword: default (remove local_as config)
                                    - Examples:
                                        task.vrf = 'FOO'
                                        task.local_as = 64512
                                    - NOTES:
                                        - bgp router vrf will be created
                                          if it does not exist.

log_neighbor_changes            Enable ``True`` or disable ``False``
                                message logging for neighbor up/down event::

                                    - Type: bool()
                                    - Valid values: False, True
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
                                    - Valid values: False, True
                                    - Example:
                                        task.neighbor_down_fib_accelerate = True
                                    - NOTES:
                                        - Must be used only in a pure BGP environment
                                          where all non-direct routes are installed
                                          by BGP.

reconnect_interval              The BGP reconnection interval for dropped sessions::

                                    - Type: int()
                                    - Valid values:
                                        - int() range 1-60
                                    - Units: seconds
                                    - Default: 60
                                    - Example:
                                        task.reconnect_interval = 15

router_id                       Router Identifier (ID) of the BGP router
                                VRF instance::

                                    - Type: str()
                                    - Valid values:
                                        - An ipv4 address without prefixlen
                                    - Example:
                                        task.vrf = 'FOO'
                                        task.router_id = '10.1.1.3'
                                    - NOTES:
                                        - bgp router vrf must be specified
                                          and will be created if it does not
                                          exist.

shutdown                        Administratively shutdown the BGP router::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.shutdown = False

state                           Determines whether the config should be present
                                or not on the device::

                                    - Type: str()
                                    - Valid values:
                                        - absent
                                        - present
                                    - Example:
                                        task.vrf = 'FOO'

suppress_fib_pending                Enable ``True`` or disable ``False``
                                    advertise only routes programmed in 
                                    hardware to peers::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.suppress_fib_pending = True

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Examples:
                                        - task.task_name = 'my task'

timer_bestpath_limit            Specify timeout for the first best path
                                after a restart::

                                    - Type: int()
                                    - Valid values:
                                        - int() range 1-3600
                                    - Units: seconds
                                    - Default: 300
                                    - Example:
                                        task.timer_bestpath_limit = 120

timer_bgp_hold                  Set BGP holddown timer.  How long before
                                resetting bgp sessions after keepalives
                                are not received from neighbors::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 3-3600
                                        - str() keyword: default
                                    - Units: seconds
                                    - Default: 180
                                    - Example:
                                        task.timer_bgp_hold = 60
                                    - NOTES:
                                        - While the NXOS CLI claims the valid range
                                          is 0-3600, the lowest accepted value is 3.

timer_bgp_keepalive             Set BGP keepalive timer. How often to send
                                keepalive messages to neighbors::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-3599
                                        - str() keyword: default
                                    - Units: seconds
                                    - Default: 60
                                    - Example:
                                        task.timer_bgp_keepalive = 60
                                    - NOTES:
                                        - While the NXOS CLI claims the valid range
                                          is 0-3600, the lowest accepted value is 1
                                          and the highest accepted value is 3599.

vrf                             Name of VRF to create under the bgp router::

                                    - Type: str()
                                    - Examples:
                                        - task.vrf = 'MY_VRF'

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
