# NxosBgp() - cisco/nxos/nxos_bgp.py
our_version = 118
from copy import deepcopy
from ask.common.task import Task
'''
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

'''

class NxosBgp(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.task_log.warning('*******************************************************************************************')
        self.task_log.warning('NxosBgp() is DEPRECATED as its Ansible module nxos_bgp is DEPRECATED.')
        self.task_log.warning('Use NxosBgpGlobal() (nxos_bgp_global) instead.')
        self.task_log.warning('*******************************************************************************************')

        self.nxos_bgp_valid_event_history = set()
        self.nxos_bgp_valid_event_history.add('size_small')
        self.nxos_bgp_valid_event_history.add('size_medium')
        self.nxos_bgp_valid_event_history.add('size_large')
        self.nxos_bgp_valid_event_history.add('size_disable')
        self.nxos_bgp_valid_event_history.add('default')

        self.nxos_bgp_valid_log_neighbor_changes = set()
        self.nxos_bgp_valid_log_neighbor_changes.add('no')
        self.nxos_bgp_valid_log_neighbor_changes.add('yes')

        self.nxos_bgp_valid_state = set()
        self.nxos_bgp_valid_state.add('absent')
        self.nxos_bgp_valid_state.add('present')

        self.nxos_bgp_timer_bgp_hold_min = 3
        self.nxos_bgp_timer_bgp_hold_max = 3600
        self.nxos_bgp_timer_bgp_keepalive_min = 1
        self.nxos_bgp_timer_bgp_keepalive_max = 3599

        self.properties_set = set()
        self.properties_set.add('asn')
        self.properties_set.add('bestpath_always_compare_med')
        self.properties_set.add('bestpath_aspath_multipath_relax')
        self.properties_set.add('bestpath_compare_neighborid')
        self.properties_set.add('bestpath_compare_routerid')
        self.properties_set.add('bestpath_cost_community_ignore')
        self.properties_set.add('bestpath_med_confed')
        self.properties_set.add('bestpath_med_missing_as_worst')
        self.properties_set.add('bestpath_med_non_deterministic')
        self.properties_set.add('cluster_id')
        self.properties_set.add('confederation_id')
        self.properties_set.add('confederation_peers')
        self.properties_set.add('disable_policy_batching')
        self.properties_set.add('disable_policy_batching_ipv4_prefix_list')
        self.properties_set.add('disable_policy_batching_ipv6_prefix_list')
        self.properties_set.add('enforce_first_as')
        self.properties_set.add('event_history_cli')
        self.properties_set.add('event_history_detail')
        self.properties_set.add('event_history_events')
        self.properties_set.add('event_history_periodic')
        self.properties_set.add('fast_external_fallover')
        self.properties_set.add('flush_routes')
        self.properties_set.add('graceful_restart')
        self.properties_set.add('graceful_restart_helper')
        self.properties_set.add('graceful_restart_timers_restart')
        self.properties_set.add('graceful_restart_timers_stalepath_time')
        self.properties_set.add('isolate')
        self.properties_set.add('local_as')
        self.properties_set.add('log_neighbor_changes')
        self.properties_set.add('maxas_limit')
        self.properties_set.add('neighbor_down_fib_accelerate')
        self.properties_set.add('reconnect_interval')
        self.properties_set.add('router_id')
        self.properties_set.add('shutdown')
        self.properties_set.add('state')
        self.properties_set.add('suppress_fib_pending')
        self.properties_set.add('timer_bestpath_limit')
        self.properties_set.add('timer_bgp_hold')
        self.properties_set.add('timer_bgp_keepalive')
        self.properties_set.add('vrf')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.asn == None:
            self.task_log.error('exiting. call instance.asn before calling instance.update()')
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def verify_nxos_bgp_cluster_id(self, x, parameter='unspecified'):
        if self.is_ipv4_address(x):
            return
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_cluster_id'
        expectation = '[digits or ipv4_address]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_confederation_peers(self, x, parameter='confederation_peers'):
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_confederation_peers'
        expectation = '[list of digits and/or digits.digits]. example: [65023, 45123, 33542.34000]'
        if not type(x) == type(list()):
            self.fail(source_class, source_method, x, parameter, expectation)
        for item in x:
            if self.is_digits(item):
                continue
            if re.search('^\d+\.\d+$', str(item)):
                continue
            self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_event_history(self, x, parameter='event_history'):
        if x in self.nxos_bgp_valid_event_history:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_event_history'
        expectation = self.nxos_bgp_valid_event_history
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_router_id(self, x, parameter='router_id'):
        if self.is_ipv4_address(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_router_id'
        expectation = "IPv4 Address without prefixlen. Example: 134.45.1.1"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_state(self, x, parameter='state'):
        if x in self.nxos_bgp_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_state'
        expectation = ','.join(self.nxos_bgp_neighbor_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_timer_bgp_hold(self, x, parameter='timer_bgp_hold'):
        if self.is_default(x):
            return
        source_class = self.class_name
        range_min = self.nxos_bgp_timer_bgp_hold_min
        range_max = self.nxos_bgp_timer_bgp_hold_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_bgp_timer_bgp_keepalive(self, x, parameter='timer_bgp_keepalive'):
        if self.is_default(x):
            return
        source_class = self.class_name
        range_min = self.nxos_bgp_timer_bgp_keepalive_min
        range_max = self.nxos_bgp_timer_bgp_keepalive_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    @property
    def asn(self):
        return self.properties['asn']
    @asn.setter
    def asn(self, x):
        parameter = 'asn'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter) # inherited from AnsCommon
        self.properties[parameter] = x

    @property
    def bestpath_always_compare_med(self):
        return self.properties['bestpath_always_compare_med']
    @bestpath_always_compare_med.setter
    def bestpath_always_compare_med(self, x):
        parameter = 'bestpath_always_compare_med'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_aspath_multipath_relax(self):
        return self.properties['bestpath_aspath_multipath_relax']
    @bestpath_aspath_multipath_relax.setter
    def bestpath_aspath_multipath_relax(self, x):
        parameter = 'bestpath_aspath_multipath_relax'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_compare_neighborid(self):
        return self.properties['bestpath_compare_neighborid']
    @bestpath_compare_neighborid.setter
    def bestpath_compare_neighborid(self, x):
        parameter = 'bestpath_compare_neighborid'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_compare_routerid(self):
        return self.properties['bestpath_compare_routerid']
    @bestpath_compare_routerid.setter
    def bestpath_compare_routerid(self, x):
        parameter = 'bestpath_compare_routerid'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_cost_community_ignore(self):
        return self.properties['bestpath_cost_community_ignore']
    @bestpath_cost_community_ignore.setter
    def bestpath_cost_community_ignore(self, x):
        parameter = 'bestpath_cost_community_ignore'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_med_confed(self):
        return self.properties['bestpath_med_confed']
    @bestpath_med_confed.setter
    def bestpath_med_confed(self, x):
        parameter = 'bestpath_med_confed'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_med_missing_as_worst(self):
        return self.properties['bestpath_med_missing_as_worst']
    @bestpath_med_missing_as_worst.setter
    def bestpath_med_missing_as_worst(self, x):
        parameter = 'bestpath_med_missing_as_worst'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def bestpath_med_non_deterministic(self):
        return self.properties['bestpath_med_non_deterministic']
    @bestpath_med_non_deterministic.setter
    def bestpath_med_non_deterministic(self, x):
        parameter = 'bestpath_med_non_deterministic'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def cluster_id(self):
        return self.properties['cluster_id']
    @cluster_id.setter
    def cluster_id(self, x):
        parameter = 'cluster_id'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_cluster_id(x, parameter)
        self.properties[parameter] = x

    @property
    def confederation_id(self):
        return self.properties['confederation_id']
    @confederation_id.setter
    def confederation_id(self, x):
        parameter = 'confederation_id'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter) # inherited from AnsCommon
        self.properties[parameter] = x

    @property
    def confederation_peers(self):
        return self.properties['confederation_peers']
    @confederation_peers.setter
    def confederation_peers(self, x):
        parameter = 'confederation_peers'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_confederation_peers(x, parameter)
        self.properties[parameter] = ' '.join(x)

    @property
    def disable_policy_batching(self):
        return self.properties['disable_policy_batching']
    @disable_policy_batching.setter
    def disable_policy_batching(self, x):
        parameter = 'disable_policy_batching'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
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
    def enforce_first_as(self):
        return self.properties['enforce_first_as']
    @enforce_first_as.setter
    def enforce_first_as(self, x):
        parameter = 'enforce_first_as'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def event_history_cli(self):
        return self.properties['event_history_cli']
    @event_history_cli.setter
    def event_history_cli(self, x):
        parameter = 'event_history_cli'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_event_history(x, parameter)
        self.properties[parameter] = x

    @property
    def event_history_detail(self):
        return self.properties['event_history_detail']
    @event_history_detail.setter
    def event_history_detail(self, x):
        parameter = 'event_history_detail'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_event_history(x, parameter)
        self.properties[parameter] = x

    @property
    def event_history_events(self):
        return self.properties['event_history_events']
    @event_history_events.setter
    def event_history_events(self, x):
        parameter = 'event_history_events'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_event_history(x, parameter)
        self.properties[parameter] = x

    @property
    def event_history_periodic(self):
        return self.properties['event_history_periodic']
    @event_history_periodic.setter
    def event_history_periodic(self, x):
        parameter = 'event_history_periodic'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_event_history(x, parameter)
        self.properties[parameter] = x

    @property
    def fast_external_fallover(self):
        return self.properties['fast_external_fallover']
    @fast_external_fallover.setter
    def fast_external_fallover(self, x):
        parameter = 'fast_external_fallover'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def flush_routes(self):
        return self.properties['flush_routes']
    @flush_routes.setter
    def flush_routes(self, x):
        parameter = 'flush_routes'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def graceful_restart(self):
        return self.properties['graceful_restart']
    @graceful_restart.setter
    def graceful_restart(self, x):
        parameter = 'graceful_restart'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def graceful_restart_helper(self):
        return self.properties['graceful_restart_helper']
    @graceful_restart_helper.setter
    def graceful_restart_helper(self, x):
        parameter = 'graceful_restart_helper'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def graceful_restart_timers_restart(self):
        return self.properties['graceful_restart_timers_restart']
    @graceful_restart_timers_restart.setter
    def graceful_restart_timers_restart(self, x):
        parameter = 'graceful_restart_timers_restart'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 3600, self.class_name, parameter)
        self.properties[parameter] = x

    @property
    def graceful_restart_timers_stalepath_time(self):
        return self.properties['graceful_restart_timers_stalepath_time']
    @graceful_restart_timers_stalepath_time.setter
    def graceful_restart_timers_stalepath_time(self, x):
        parameter = 'graceful_restart_timers_stalepath_time'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 3600, self.class_name, parameter)
        self.properties[parameter] = x

    @property
    def isolate(self):
        return self.properties['isolate']
    @isolate.setter
    def isolate(self, x):
        parameter = 'isolate'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def local_as(self):
        return self.properties['local_as']
    @local_as.setter
    def local_as(self, x):
        parameter = 'local_as'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter) # inherited from AnsCommon
        self.properties[parameter] = x

    @property
    def log_neighbor_changes(self):
        return self.properties['log_neighbor_changes']
    @log_neighbor_changes.setter
    def log_neighbor_changes(self, x):
        parameter = 'log_neighbor_changes'
        if self.set_none(x, parameter):
            return
        if x not in self.nxos_bgp_valid_log_neighbor_changes:
            _expectation = ','.join(self.nxos_bgp_valid_log_neighbor_changes)
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
    def neighbor_down_fib_accelerate(self):
        return self.properties['neighbor_down_fib_accelerate']
    @neighbor_down_fib_accelerate.setter
    def neighbor_down_fib_accelerate(self, x):
        parameter = 'neighbor_down_fib_accelerate'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

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
        self.verify_nxos_bgp_router_id(x, parameter)
        self.properties[parameter] = x

    @property
    def shutdown(self):
        return self.properties['shutdown']
    @shutdown.setter
    def shutdown(self, x):
        parameter = 'shutdown'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties['shutdown'] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_fib_pending(self):
        return self.properties['suppress_fib_pending']
    @suppress_fib_pending.setter
    def suppress_fib_pending(self, x):
        parameter = 'suppress_fib_pending'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def timer_bestpath_limit(self):
        return self.properties['timer_bestpath_limit']
    @timer_bestpath_limit.setter
    def timer_bestpath_limit(self, x):
        parameter = 'timer_bestpath_limit'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 3600, self.class_name, parameter)
        self.properties[parameter] = x

    @property
    def timer_bgp_hold(self):
        return self.properties['timer_bgp_hold']
    @timer_bgp_hold.setter
    def timer_bgp_hold(self, x):
        parameter = 'timer_bgp_hold'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_timer_bgp_hold(x, parameter)
        self.properties[parameter] = x

    @property
    def timer_bgp_keepalive(self):
        return self.properties['timer_bgp_keepalive']
    @timer_bgp_keepalive.setter
    def timer_bgp_keepalive(self, x):
        parameter = 'timer_bgp_keepalive'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_timer_bgp_keepalive(x, parameter)
        self.properties[parameter] = x
