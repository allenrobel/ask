# AskNxosBgp() - python/lib3/ask_task_nxos_bgp.py
our_version = 113
# Ansible module nxos_bgp was DEPRECATED on 2021.01.27.
# It will be removed from Ansible in the future.
from ans_playbook_next_gen import AnsPlaybook
from ask_task import AskTask
'''
Name: ask_task_nxos_bgp.py
Author: Allen Robel
Email: arobel@cisco.com
Description:

AskNxosBgp() generates Ansible Playbook tasks using nxos_bgp
which can be fed to AnsPlaybook().add_task()

Revision history: Use git log

Example usage:

#!/usr/bin/env python3
from ans_playbook import AnsPlaybook
from ask_task_nxos_bgp import AskNxosBgp
from log import get_logger

module_name = 'nxos_bgp'
log = get_logger('test_ask_task_{}'.format(module_name), 'INFO', 'DEBUG')

pb = AnsPlaybook(log)
pb.file = '/tmp/ans_playbook_{}.yaml'.format(module_name)
pb.name = '{} task'.format(module_name)
pb.add_host('t301')  # host in Ansible inventory

task = AskNxosBgp(log)
task.task_name = module_name
task.asn = 65045
task.vrf = 'my_vrf'
task.router_id = '10.10.1.1'
task.state = 'present' # or 'absent'
pb.add_task(task)
pb.write_playbook()
print('wrote {}'.format(pb.file))

'''

#class AskNxosBgp(AnsTask, AnsCommonNxosBgp):
class AskNxosBgp(AnsTask):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self._classname = __class__.__name__
        self.ansible_task = dict()

        self.task_log.warning('*******************************************************************************************')
        self.task_log.warning('AskNxosBgp() is DEPRECATED as its Ansible module nxos_bgp is DEPRECATED.')
        self.task_log.warning('Use AskNxosBgpGlobal() (nxos_bgp_global) instead.')
        self.task_log.warning('*******************************************************************************************')

        self.init_properties()

        self.nxos_bgp_valid_event_history = ['size_small', 'size_medium', 'size_large', 'size_disable', 'default']
        self.nxos_bgp_valid_log_neighbor_changes = ['no', 'yes']
        self.nxos_bgp_valid_state = ['present', 'absent'] # override AnsCommon() to remove 'default'

    def init_properties(self):
        self.properties = dict()
        self.properties['asn'] = None   # digits, digits.digits
        self.properties['bestpath_always_compare_med'] = None       # no, yes
        self.properties['bestpath_aspath_multipath_relax'] = None   # no, yes
        self.properties['bestpath_compare_neighborid'] = None       # no, yes
        self.properties['bestpath_compare_routerid'] = None         # no, yes
        self.properties['bestpath_cost_community_ignore'] = None    # no, yes
        self.properties['bestpath_med_confed'] = None               # no, yes
        self.properties['bestpath_med_missing_as_worst'] = None     # no, yes
        self.properties['bestpath_med_non_deterministic'] = None    # no, yes
        self.properties['cluster_id'] = None                        # Route Reflector Cluster-ID
        self.properties['confederation_id'] = None                  # digits or digits.digits
        self.properties['confederation_peers'] = None               # quoted space-separated list of "digits digits.digits"
        self.properties['disable_policy_batching'] = None           # no, yes
        self.properties['disable_policy_batching_ipv4_prefix_list'] = None # str()
        self.properties['disable_policy_batching_ipv6_prefix_list'] = None # str()
        self.properties['enforce_first_as'] = None                  # no, yes
        self.properties['event_history_cli'] = None                 # str() one of: size_small, size_medium, size_large, size_disable, default  
        self.properties['event_history_detail'] = None              # str() one of: size_small, size_medium, size_large, size_disable, default  
        self.properties['event_history_events'] = None              # str() one of: size_small, size_medium, size_large, size_disable, default  
        self.properties['event_history_periodic'] = None            # str() one of: size_small, size_medium, size_large, size_disable, default  
        self.properties['fast_external_fallover'] = None            # no, yes  
        self.properties['flush_routes'] = None                      # no, yes  
        self.properties['graceful_restart'] = None                  # no, yes  
        self.properties['graceful_restart_helper'] = None           # no, yes  
        self.properties['graceful_restart_timers_restart'] = None         # int() 1-3600, default is 120  
        self.properties['graceful_restart_timers_stalepath_time'] = None  # int() 1-3600, default is 300  
        self.properties['isolate'] = None                           # no, yes  
        self.properties['local_as'] = None                          # digits, digits.digits, digits:digits
        self.properties['log_neighbor_changes'] = None              # no, yes
        self.properties['maxas_limit'] = None                       # int() 1-512  
        self.properties['neighbor_down_fib_accelerate'] = None      # no, yes
        self.properties['reconnect_interval'] = None                # int() 1-60, default is 60  
        self.properties['router_id'] = None                         # A.B.C.D ipv4-address format  
        self.properties['shutdown'] = None
        self.properties['suppress_fib_pending'] = None              # no, yes
        self.properties['timer_bestpath_limit'] = None              # int() 1-3600, default is 300
        self.properties['timer_bgp_hold'] = None                    # int() 1-3600, default is 180
        self.properties['timer_bgp_keepalive'] = None               # int() 1-3600, default is 60
        self.properties['vrf'] = None                               # stf() vrf name

        self.properties['state']                        = None  # str() present, absent. Mandatory
        self.properties['task_name']                    = None  # str() Name of the task

    def final_verification(self):
        '''
        final_verification is called by update() method
        It performs a final verification across the properties that the user has or hasn't set
        '''
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.asn == None:
            self.task_log.error('exiting. call instance.asn before calling instance.update()')
            exit(1)

    def update(self):
        '''
        update verifies that mandatory module-specific parameters are set
        '''
        self.final_verification()

        d = dict()
        if self.asn != None:
            d['asn'] = self.asn
        if self.bestpath_always_compare_med != None:
            d['bestpath_always_compare_med'] = self.bestpath_always_compare_med
        if self.bestpath_aspath_multipath_relax != None:
            d['bestpath_aspath_multipath_relax'] = self.bestpath_aspath_multipath_relax
        if self.bestpath_compare_neighborid != None:
            d['bestpath_compare_neighborid'] = self.bestpath_compare_neighborid
        if self.bestpath_compare_routerid != None:
            d['bestpath_compare_routerid'] = self.bestpath_compare_routerid
        if self.bestpath_cost_community_ignore != None:
            d['bestpath_cost_community_ignore'] = self.bestpath_cost_community_ignore
        if self.bestpath_med_confed != None:
            d['bestpath_med_confed'] = self.bestpath_med_confed
        if self.bestpath_med_missing_as_worst != None:
            d['bestpath_med_missing_as_worst'] = self.bestpath_med_missing_as_worst
        if self.bestpath_med_non_deterministic != None:
            d['bestpath_med_non_deterministic'] = self.bestpath_med_non_deterministic
        if self.cluster_id != None:
            d['cluster_id'] = self.cluster_id
        if self.confederation_id != None:
            d['confederation_id'] = self.confederation_id
        if self.confederation_peers != None:
            d['confederation_peers'] = self.confederation_peers
        if self.disable_policy_batching != None:
            d['disable_policy_batching'] = self.disable_policy_batching
        if self.disable_policy_batching_ipv4_prefix_list != None:
            d['disable_policy_batching_ipv4_prefix_list'] = self.disable_policy_batching_ipv4_prefix_list
        if self.disable_policy_batching_ipv6_prefix_list != None:
            d['disable_policy_batching_ipv6_prefix_list'] = self.disable_policy_batching_ipv6_prefix_list
        if self.enforce_first_as != None:
            d['enforce_first_as'] = self.enforce_first_as
        if self.event_history_cli != None:
            d['event_history_cli'] = self.event_history_cli
        if self.event_history_detail != None:
            d['event_history_detail'] = self.event_history_detail
        if self.event_history_events != None:
            d['event_history_events'] = self.event_history_events
        if self.event_history_periodic != None:
            d['event_history_periodic'] = self.event_history_periodic
        if self.fast_external_fallover != None:
            d['fast_external_fallover'] = self.fast_external_fallover
        if self.flush_routes != None:
            d['flush_routes'] = self.flush_routes
        if self.graceful_restart != None:
            d['graceful_restart'] = self.graceful_restart
        if self.graceful_restart_helper != None:
            d['graceful_restart_helper'] = self.graceful_restart_helper
        if self.graceful_restart_timers_restart != None:
            d['graceful_restart_timers_restart'] = self.graceful_restart_timers_restart
        if self.graceful_restart_timers_stalepath_time != None:
            d['graceful_restart_timers_stalepath_time'] = self.graceful_restart_timers_stalepath_time
        if self.isolate != None:
            d['isolate'] = self.isolate
        if self.local_as != None:
            d['local_as'] = self.local_as
        if self.log_neighbor_changes != None:
            d['log_neighbor_changes'] = self.log_neighbor_changes
        if self.maxas_limit != None:
            d['maxas_limit'] = self.maxas_limit
        if self.neighbor_down_fib_accelerate != None:
            d['neighbor_down_fib_accelerate'] = self.neighbor_down_fib_accelerate
        if self.reconnect_interval != None:
            d['reconnect_interval'] = self.reconnect_interval
        if self.router_id != None:
            d['router_id'] = self.router_id
        if self.shutdown != None:
            d['shutdown'] = self.shutdown
        if self.suppress_fib_pending != None:
            d['suppress_fib_pending'] = self.suppress_fib_pending
        if self.timer_bestpath_limit != None:
            d['timer_bestpath_limit'] = self.timer_bestpath_limit
        if self.timer_bgp_hold != None:
            d['timer_bgp_hold'] = self.timer_bgp_hold
        if self.timer_bgp_keepalive != None:
            d['timer_bgp_keepalive'] = self.timer_bgp_keepalive
        if self.vrf != None:
            d['vrf'] = self.vrf

        if self.state != None:
            d['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

        self.ansible_task[self.ansible_module] = d.copy()

        self.init_properties()

    def nxos_bgp_verify_cluster_id(self, x, parameter='unspecified'):
        if self.is_ipv4_address(x):
            return
        if self.is_digits(x):
            return
        source_class = self._classname
        source_method = 'nxos_bgp_verify_cluster_id'
        expectation = '[digits or ipv4_address]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_verify_confederation_peers(self, x, parameter='confederation_peers'):
        source_class = self._classname
        source_method = 'nxos_bgp_verify_confederation_peers'
        expectation = '[list of digits and/or digits.digits]. example: [65023, 45123, 33542.34000]'
        if not type(x) == type(list()):
            self.fail(source_class, source_method, x, parameter, expectation)
        for item in x:
            if self.is_digits(x):
                continue
            if re.search('^\d+\.\d+$', str(x)):
                continue
            self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_verify_event_history(self, x, parameter='event_history'):
        if x in self.nxos_bgp_valid_event_history:
            return
        source_class = self._classname
        source_method = 'nxos_bgp_verify_event_history'
        expectation = self.nxos_bgp_valid_event_history
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_verify_router_id(self, x, parameter='router_id'):
        if self.is_ipv4_address(x):
            return
        source_class = self._classname
        source_method = 'nxos_bgp_verify_router_id'
        expectation = "IPv4 Address without prefixlen. Example: 134.45.1.1"
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_verify_state(self, x, parameter='state'):
        if x in self.nxos_bgp_valid_state:
            return
        source_class = self._classname
        source_method = 'nxos_bgp_verify_state'
        expectation = ','.join(self.nxos_bgp_neighbor_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def asn(self):
        return self.properties['asn']
    @asn.setter
    def asn(self, x):
        '''
        '''
        _parameter = 'asn'
        if self.set_none(x, _parameter):
            return
        self.verify_bgp_asn(x, _parameter) # inherited from AnsCommon
        self.properties[_parameter] = x

    @property
    def bestpath_always_compare_med(self):
        return self.properties['bestpath_always_compare_med']
    @bestpath_always_compare_med.setter
    def bestpath_always_compare_med(self, x):
        '''
        '''
        _parameter = 'bestpath_always_compare_med'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def bestpath_aspath_multipath_relax(self):
        return self.properties['bestpath_aspath_multipath_relax']
    @bestpath_aspath_multipath_relax.setter
    def bestpath_aspath_multipath_relax(self, x):
        '''
        '''
        _parameter = 'bestpath_aspath_multipath_relax'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def bestpath_compare_neighborid(self):
        return self.properties['bestpath_compare_neighborid']
    @bestpath_compare_neighborid.setter
    def bestpath_compare_neighborid(self, x):
        '''
        '''
        _parameter = 'bestpath_compare_neighborid'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def bestpath_compare_routerid(self):
        return self.properties['bestpath_compare_routerid']
    @bestpath_compare_routerid.setter
    def bestpath_compare_routerid(self, x):
        '''
        '''
        _parameter = 'bestpath_compare_routerid'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def bestpath_cost_community_ignore(self):
        return self.properties['bestpath_cost_community_ignore']
    @bestpath_cost_community_ignore.setter
    def bestpath_cost_community_ignore(self, x):
        '''
        '''
        _parameter = 'bestpath_cost_community_ignore'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def bestpath_med_confed(self):
        return self.properties['bestpath_med_confed']
    @bestpath_med_confed.setter
    def bestpath_med_confed(self, x):
        '''
        '''
        _parameter = 'bestpath_med_confed'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def bestpath_med_missing_as_worst(self):
        return self.properties['bestpath_med_missing_as_worst']
    @bestpath_med_missing_as_worst.setter
    def bestpath_med_missing_as_worst(self, x):
        '''
        '''
        _parameter = 'bestpath_med_missing_as_worst'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def bestpath_med_non_deterministic(self):
        return self.properties['bestpath_med_non_deterministic']
    @bestpath_med_non_deterministic.setter
    def bestpath_med_non_deterministic(self, x):
        '''
        '''
        _parameter = 'bestpath_med_non_deterministic'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def cluster_id(self):
        return self.properties['cluster_id']
    @cluster_id.setter
    def cluster_id(self, x):
        '''
        '''
        _parameter = 'cluster_id'
        if self.set_none(x, _parameter):
            return
        self.nxos_bgp_verify_cluster_id(x, _parameter)
        self.properties[_parameter] = x

    @property
    def confederation_id(self):
        return self.properties['confederation_id']
    @confederation_id.setter
    def confederation_id(self, x):
        '''
        '''
        _parameter = 'confederation_id'
        if self.set_none(x, _parameter):
            return
        self.verify_bgp_asn(x, _parameter) # inherited from AnsCommon
        self.properties[_parameter] = x

    @property
    def confederation_peers(self):
        return self.properties['confederation_peers']
    @confederation_peers.setter
    def confederation_peers(self, x):
        '''
        '''
        _parameter = 'confederation_peers'
        if self.set_none(x, _parameter):
            return
        self.nxos_bgp_verify_confederation_peers(x, _parameter)
        self.properties[_parameter] = ' '.join(x)

    @property
    def disable_policy_batching(self):
        return self.properties['disable_policy_batching']
    @disable_policy_batching.setter
    def disable_policy_batching(self, x):
        '''
        '''
        _parameter = 'disable_policy_batching'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def disable_policy_batching_ipv4_prefix_list(self):
        return self.properties['disable_policy_batching_ipv4_prefix_list']
    @disable_policy_batching_ipv4_prefix_list.setter
    def disable_policy_batching_ipv4_prefix_list(self, x):
        '''
        '''
        _parameter = 'disable_policy_batching_ipv4_prefix_list'
        if self.set_none(x, _parameter):
            return
        self.properties[_parameter] = x

    @property
    def disable_policy_batching_ipv6_prefix_list(self):
        return self.properties['disable_policy_batching_ipv6_prefix_list']
    @disable_policy_batching_ipv6_prefix_list.setter
    def disable_policy_batching_ipv6_prefix_list(self, x):
        '''
        '''
        _parameter = 'disable_policy_batching_ipv6_prefix_list'
        if self.set_none(x, _parameter):
            return
        self.properties[_parameter] = x

    @property
    def enforce_first_as(self):
        return self.properties['enforce_first_as']
    @enforce_first_as.setter
    def enforce_first_as(self, x):
        '''
        '''
        _parameter = 'enforce_first_as'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def event_history_cli(self):
        return self.properties['event_history_cli']
    @event_history_cli.setter
    def event_history_cli(self, x):
        '''
        '''
        _parameter = 'event_history_cli'
        if self.set_none(x, _parameter):
            return
        self.nxos_bgp_verify_event_history(x, _parameter)
        self.properties[_parameter] = x

    @property
    def event_history_detail(self):
        return self.properties['event_history_detail']
    @event_history_detail.setter
    def event_history_detail(self, x):
        '''
        '''
        _parameter = 'event_history_detail'
        if self.set_none(x, _parameter):
            return
        self.nxos_bgp_verify_event_history(x, _parameter)
        self.properties[_parameter] = x

    @property
    def event_history_events(self):
        return self.properties['event_history_events']
    @event_history_events.setter
    def event_history_events(self, x):
        '''
        '''
        _parameter = 'event_history_events'
        if self.set_none(x, _parameter):
            return
        self.nxos_bgp_verify_event_history(x, _parameter)
        self.properties[_parameter] = x

    @property
    def event_history_periodic(self):
        return self.properties['event_history_periodic']
    @event_history_periodic.setter
    def event_history_periodic(self, x):
        '''
        '''
        _parameter = 'event_history_periodic'
        if self.set_none(x, _parameter):
            return
        self.nxos_bgp_verify_event_history(x, _parameter)
        self.properties[_parameter] = x

    @property
    def fast_external_fallover(self):
        return self.properties['fast_external_fallover']
    @fast_external_fallover.setter
    def fast_external_fallover(self, x):
        '''
        '''
        _parameter = 'fast_external_fallover'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def flush_routes(self):
        return self.properties['flush_routes']
    @flush_routes.setter
    def flush_routes(self, x):
        '''
        '''
        _parameter = 'flush_routes'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def graceful_restart(self):
        return self.properties['graceful_restart']
    @graceful_restart.setter
    def graceful_restart(self, x):
        '''
        '''
        _parameter = 'graceful_restart'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def graceful_restart_helper(self):
        return self.properties['graceful_restart_helper']
    @graceful_restart_helper.setter
    def graceful_restart_helper(self, x):
        '''
        '''
        _parameter = 'graceful_restart_helper'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def graceful_restart_timers_restart(self):
        return self.properties['graceful_restart_timers_restart']
    @graceful_restart_timers_restart.setter
    def graceful_restart_timers_restart(self, x):
        '''
        '''
        _parameter = 'graceful_restart_timers_restart'
        if self.set_none(x, _parameter):
            return
        self.verify_integer_range(x, 1, 3600, self._classname, _parameter)
        self.properties[_parameter] = x

    @property
    def graceful_restart_timers_stalepath_time(self):
        return self.properties['graceful_restart_timers_stalepath_time']
    @graceful_restart_timers_stalepath_time.setter
    def graceful_restart_timers_stalepath_time(self, x):
        '''
        '''
        _parameter = 'graceful_restart_timers_stalepath_time'
        if self.set_none(x, _parameter):
            return
        self.verify_integer_range(x, 1, 3600, self._classname, _parameter)
        self.properties[_parameter] = x

    @property
    def isolate(self):
        return self.properties['isolate']
    @isolate.setter
    def isolate(self, x):
        '''
        '''
        _parameter = 'isolate'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def local_as(self):
        return self.properties['local_as']
    @local_as.setter
    def local_as(self, x):
        '''
        '''
        _parameter = 'local_as'
        if self.set_none(x, _parameter):
            return
        self.verify_bgp_asn(x, _parameter) # inherited from AnsCommon
        self.properties[_parameter] = x

    @property
    def log_neighbor_changes(self):
        return self.properties['log_neighbor_changes']
    @log_neighbor_changes.setter
    def log_neighbor_changes(self, x):
        '''
        '''
        _parameter = 'log_neighbor_changes'
        if self.set_none(x, _parameter):
            return
        if x not in self.nxos_bgp_valid_log_neighbor_changes:
            _expectation = ','.join(self.nxos_bgp_valid_log_neighbor_changes)
            self.fail(self._classname, _parameter, x, _parameter, _expectation)
        self.properties[_parameter] = x

    @property
    def maxas_limit(self):
        return self.properties['maxas_limit']
    @maxas_limit.setter
    def maxas_limit(self, x):
        '''
        '''
        _parameter = 'maxas_limit'
        if self.set_none(x, _parameter):
            return
        self.verify_integer_range(x, 1, 512, self._classname, _parameter)
        self.properties[_parameter] = x

    @property
    def neighbor_down_fib_accelerate(self):
        return self.properties['neighbor_down_fib_accelerate']
    @neighbor_down_fib_accelerate.setter
    def neighbor_down_fib_accelerate(self, x):
        '''
        '''
        _parameter = 'neighbor_down_fib_accelerate'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def reconnect_interval(self):
        return self.properties['reconnect_interval']
    @reconnect_interval.setter
    def reconnect_interval(self, x):
        '''
        '''
        _parameter = 'reconnect_interval'
        if self.set_none(x, _parameter):
            return
        self.verify_integer_range(x, 1, 60, self._classname, _parameter)
        self.properties[_parameter] = x

    @property
    def router_id(self):
        return self.properties['router_id']
    @router_id.setter
    def router_id(self, x):
        '''
        '''
        _parameter = 'router_id'
        if self.set_none(x, _parameter):
            return
        self.nxos_bgp_verify_router_id(x, _parameter)
        self.properties[_parameter] = x

    @property
    def shutdown(self):
        return self.properties['shutdown']
    @shutdown.setter
    def shutdown(self, x):
        '''
        '''
        _parameter = 'shutdown'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties['shutdown'] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        '''
        '''
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_verify_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_fib_pending(self):
        return self.properties['suppress_fib_pending']
    @suppress_fib_pending.setter
    def suppress_fib_pending(self, x):
        '''
        '''
        _parameter = 'suppress_fib_pending'
        if self.set_none(x, _parameter):
            return
        self.verify_toggle(x, _parameter)
        self.properties[_parameter] = x

    @property
    def timer_bestpath_limit(self):
        return self.properties['timer_bestpath_limit']
    @timer_bestpath_limit.setter
    def timer_bestpath_limit(self, x):
        '''
        '''
        _parameter = 'timer_bestpath_limit'
        if self.set_none(x, _parameter):
            return
        self.verify_integer_range(x, 1, 3600, self._classname, _parameter)
        self.properties[_parameter] = x

    @property
    def timer_bgp_hold(self):
        return self.properties['timer_bgp_hold']
    @timer_bgp_hold.setter
    def timer_bgp_hold(self, x):
        '''
        '''
        _parameter = 'timer_bgp_hold'
        if self.set_none(x, _parameter):
            return
        self.verify_integer_range(x, 1, 3600, self._classname, _parameter)
        self.properties[_parameter] = x

    @property
    def timer_bgp_keepalive(self):
        return self.properties['timer_bgp_keepalive']
    @timer_bgp_keepalive.setter
    def timer_bgp_keepalive(self, x):
        '''
        '''
        _parameter = 'timer_bgp_keepalive'
        if self.set_none(x, _parameter):
            return
        self.verify_integer_range(x, 1, 3600, self._classname, _parameter)
        self.properties[_parameter] = x

