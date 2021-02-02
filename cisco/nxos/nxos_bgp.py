# NxosBgp() - cisco/nxos/nxos_bgp.py
our_version = 114
# Deprecation: Ansible module nxos_bgp is DEPRECATED
# Deprecated on: 2021.01.27
# Removed after: 2023-01-27
# Alternative: nxos_bgp_global - cisco/nxos/nxos_bgp_global.py
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_bgp.py

Description:

NxosBgp() generates Ansible Playbook tasks using nxos_bgp
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_bgp.py

Properties:

    asn   # digits, digits.digits
    bestpath_always_compare_med         -   no, yes
    bestpath_aspath_multipath_relax     -   no, yes
    bestpath_compare_neighborid         -   no, yes
    bestpath_compare_routerid           -   no, yes
    bestpath_cost_community_ignore      -   no, yes
    bestpath_med_confed                 -   no, yes
    bestpath_med_missing_as_worst       -   no, yes
    bestpath_med_non_deterministic      -   no, yes
    cluster_id                          -   Route Reflector Cluster-ID
    confederation_id                    -   digits or digits.digits
    confederation_peers                 -   quoted space-separated list of "digits digits.digits"
    disable_policy_batching             -   no, yes
    disable_policy_batching_ipv4_prefix_list    -   str()
    disable_policy_batching_ipv6_prefix_list    -   str()
    enforce_first_as                    -   no, yes
    event_history_cli                   -   Valid values: size_small, size_medium, size_large, size_disable, default  
    event_history_detail                -   Valid values: size_small, size_medium, size_large, size_disable, default  
    event_history_events                -   Valid values: size_small, size_medium, size_large, size_disable, default  
    event_history_periodic              -   Valid values: size_small, size_medium, size_large, size_disable, default  
    fast_external_fallover              -   no, yes  
    flush_routes                        -   no, yes  
    graceful_restart                    -   no, yes  
    graceful_restart_helper             -   no, yes  
    graceful_restart_timers_restart     -   int() range: 1-3600, default is 120  
    graceful_restart_timers_stalepath_time  -   int() range: 1-3600
                                                Default: 300  
    isolate                             -   no, yes  
    local_as                            -   digits, digits.digits, digits:digits
    log_neighbor_changes                -   no, yes
    maxas_limit                         -   int() range: 1-512  
    neighbor_down_fib_accelerate        -   no, yes
    reconnect_interval                  -   int() range: 1-60
                                            Default: 60  
    router_id                           -   ipv4 address without prefix e.g. A.B.C.D  
    shutdown
    state                               -   str() absent, present
    suppress_fib_pending                -   no, yes
    task_name                           -   str() name of the task
    timer_bestpath_limit                -   int() range: 1-3600
                                            Default: 300
    timer_bgp_hold                      -   int() range: 1-3600
                                            Default: 180
    timer_bgp_keepalive                 -   int() range: 1-3600
                                            Default: 60
    vrf                                 -   str() vrf name
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
            if self.is_digits(x):
                continue
            if re.search('^\d+\.\d+$', str(x)):
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
        self.verify_integer_range(x, 1, 3600, self.class_name, parameter)
        self.properties[parameter] = x

    @property
    def timer_bgp_keepalive(self):
        return self.properties['timer_bgp_keepalive']
    @timer_bgp_keepalive.setter
    def timer_bgp_keepalive(self, x):
        parameter = 'timer_bgp_keepalive'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, 1, 3600, self.class_name, parameter)
        self.properties[parameter] = x
