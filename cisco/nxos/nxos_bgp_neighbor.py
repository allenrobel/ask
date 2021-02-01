# AskNxosBgpNeighbor() - python/lib3/ask_task_nxos_bgp_neighbor.py
our_version = 110
# Ansible module nxos_bgp_neighbor is DEPRECATED as of 2021.01.27
# Use nxos_bgp_global instead
# AskNxosBfdGlobal() - python/lib3/ask_task_nxos_bfd_global.py
#
# standard library
import re
# DSSPERF library
from ask_task import AskTask
from ans_playbook_next_gen import AnsPlaybook
'''
Name: ask_task_nxos_bgp_neighbor.py
Author: Allen Robel
Email: arobel@cisco.com
Description:

AskNxosBgpNeighbor() generates Ansible Playbook tasks conformant with nxos_bgp_neighbor
which can be fed to AnsPlaybook().add_task()

Revision history: Use git log

Usage example:

from ans_playbook_next_gen import AnsPlaybook
from ask_task_nxos_bgp_neighbor import AskNxosBgpNeighbor
from log import get_logger
module_name = 'nxos_bgp_neighbor'
log = get_logger('test_ask_task_{}'.format(module_name), 'INFO', 'DEBUG')

def bgp_neighbor():
    task = AskBgpNeighbor(log)
    ipv4_neighbor = '10.8.0.1'
    task.task_name = 'configure bgp neighbor {}'.format(ipv4_neighbor)
    task.neighbor = ipv4_neighbor
    task.asn = '64518'            # i.e. router bgp <asn>
    task.local_as = '64518'       # as number that our peer uses for us
    task.remote_as = '64518'      # as number of our peer
    task.vrf = 'default'
    task.update_source = 'Ethernet1/49'
    task.state = 'present'
    task.task_name = '{}: asn {} local_as {} neighbor {} remote_as {} update_source {}'.format(
        ansible_module,
        task.asn,
        task.local_as,
        task.neighbor,
        task.remote_as,
        task.update_source)
    task.update()
    pb.add_task(task)

pb = AnsPlaybook(log)
pb.file = '/tmp/ans_playbook_{}.yaml'.format(module_name)
pb.name = '{} task'.format(module_name)
pb.add_host('dc-101')  # host in Ansible inventory

bgp_neighbor()

pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))

'''

class AskNxosBgpNeighbor(AnsTask):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp_neighbor'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self._classname = __class__.__name__
        self.ansible_task = dict()

        self.task_log.warning('*******************************************************************************************')
        self.task_log.warning('AskNxosBgpNeighbor is DEPRECATED as its Ansible module nxos_bgp_neighbor is DEPRECATED.')
        self.task_log.warning('Use AskNxosBgpGlobal() (nxos_bgp_global) instead.')
        self.task_log.warning('*******************************************************************************************')
        self.init_properties()

        self.nxos_bgp_neighbor_valid_log_neighbor_changes = ['enable', 'disable', 'inherit']
        self.nxos_bgp_neighbor_valid_pwd_type = ['3des', 'cisco_type_7', 'default']
        self.nxos_bgp_neighbor_valid_remove_private_as = ['enable', 'disable', 'all', 'replace-as']
        self.nxos_bgp_neighbor_valid_state = ['present', 'absent']

    def update(self):
        '''
        update verifies that mandatory module-specific parameters are set
        '''
        self.final_verification()

        d = dict()
        if self.asn != None:
            d['asn'] = self.asn
        if self.bfd != None:
            d['bfd'] = self.bfd
        if self.capability_negotiation != None:
            d['capability_negotiation'] = self.capability_negotiation
        if self.connected_check != None:
            d['connected_check'] = self.connected_check
        if self.description != None:
            d['description'] = self.description
        if self.dynamic_capability != None:
            d['dynamic_capability'] = self.dynamic_capability
        if self.ebgp_multihop != None:
            d['ebgp_multihop'] = self.ebgp_multihop
        if self.local_as != None:
            d['local_as'] = self.local_as
        if self.log_neighbor_changes != None:
            d['log_neighbor_changes'] = self.log_neighbor_changes
        if self.low_memory_exempt != None:
            d['low_memory_exempt'] = self.low_memory_exempt
        if self.maximum_peers != None:
            d['maximum_peers'] = self.maximum_peers
        if self.neighbor != None:
            d['neighbor'] = self.neighbor
        if self.pwd != None:
            d['pwd'] = self.pwd
        if self.pwd_type != None:
            d['pwd_type'] = self.pwd_type
        if self.remote_as != None:
            d['remote_as'] = self.remote_as
        if self.remove_private_as != None:
            d['remove_private_as'] = self.remove_private_as
        if self.shutdown != None:
            d['shutdown'] = self.shutdown
        if self.state != None:
            d['state'] = self.state
        if self.suppress_4_byte_as != None:
            d['suppress_4_byte_as'] = self.suppress_4_byte_as
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        if self.timers_holdtime != None:
            d['timers_holdtime'] = self.timers_holdtime
        if self.timers_keepalive != None:
            d['timers_keepalive'] = self.timers_keepalive
        if self.transport_passive_only != None:
            d['transport_passive_only'] = self.transport_passive_only
        if self.update_source != None:
            d['update_source'] = self.update_source

        self.ansible_task[self.ansible_module] = d.copy()
        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        self.properties['asn'] = None   # digits, digits.digits
        self.properties['bfd'] = None                              # enable, disable
        self.properties['capability_negotiation'] = None           # no, yes
        self.properties['connected_check'] = None                  # no, yes
        self.properties['description'] = None                      # quoted?  
        self.properties['dynamic_capability'] = None               # no, yes  
        self.properties['ebgp_multihop'] = None                    # int() 2-255, or "default"
        self.properties['local_as'] = None
        self.properties['log_neighbor_changes'] = None             # enable, disable, inherit
        self.properties['low_memory_exempt'] = None                # no, yes
        self.properties['maximum_peers'] = None                    # int() 1-1000, or "default". Accepted only on prefix peers
        self.properties['neighbor'] = None                         # str() IPv4 or IPv6 notation, with or without prefix length
        self.properties['pwd'] = None                              # str() password for neighbor
        self.properties['pwd_type'] = None                         # 3des, cisco_type_7, default
        self.properties['remote_as'] = None                        # str() asn in ASPLAIN or ASDOT notation
        self.properties['remove_private_as'] = None                # enable, disable, all, replace-as
        self.properties['shutdown'] = None
        self.properties['suppress_4_byte_as'] = None               # no, yes
        self.properties['task_name'] = None                        # int() the Ansible task name
        self.properties['timers_holdtime'] = None                  # int() 0-3600 seconds, or 'default', which is 180
        self.properties['timers_keepalive'] = None                 # int() 0-3600 seconds, or 'default', which is 60
        self.properties['transport_passive_only'] = None           # no, yes
        self.properties['update_source'] = None                    # str() source interface of BGP session and updates


    def final_verification(self):
        '''
        final_verification is called by subclass.update() method
        It performs a final verification across the properties that the user has or hasn't set
        '''
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.asn == None:
            self.task_log.error('exiting. call instance.asn before calling instance.update()')
            exit(1)
        if self.neighbor == None:
            self.task_log.error('exiting. call instance.neighbor before calling instance.update()')
            exit(1)

    def nxos_bgp_neighbor_verify_state(self, x, parameter='state'):
        if x in self.nxos_bgp_neighbor_valid_state:
            return
        source_class = self._classname
        source_method = 'nxos_bgp_neighbor_verify_state'
        expectation = ','.join(self.nxos_bgp_neighbor_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_verify_asn(self, x, parameter=''):
        if self.is_digits(x):
            return
        if re.search('^\d+\.\d+$', str(x)):
            return
        source_class = self._classname
        source_method = 'nxos_bgp_neighbor_verify_asn'
        expectation = '["digits", "digits.digits", "digits:digits"]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_verify_ebgp_multihop(self, x, parameter='ebgp_multihop'):
        '''
        verify ebgp_multihop is between 2-255 or == 'default'
        '''
        if self.is_default(x):
            return
        if x in list(range(2,256)):
            return
        source_class = self._classname
        source_method = 'nxos_bgp_neighbor_verify_ebgp_multihop'
        expectation = '[2-255, "default"]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_verify_neighbor_bgp(self, x, parameter='neighbor_bgp'):
        expectation = ''
        if self.maximum_peers == None:
            expectation = "[IPv4 Address, IPv6 Address]"
            if self.is_ipv4_address(x):
                return
            if self.is_ipv6_address(x):
                return
        else:
            expectation = "[IPv4 Network, IPv6 Network]"
            if self.is_ipv4_network(x):
                return
            if self.is_ipv6_network(x):
                return
        source_class = self._classname
        source_method = 'nxos_bgp_neighbor_verify_neighbor_bgp'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_verify_pwd_type(self, x, parameter='unspecified'):
        if x in self.nxos_bgp_neighbor_valid_pwd_type:
            return
        source_class = self._classname
        source_method = 'nxos_bgp_neighbor_verify_pwd_type'
        expectation = self.nxos_bgp_neighbor_valid_pwd_type 
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_verify_remove_private_as(self, x, parameter=''):
        if x in self.nxos_bgp_neighbor_valid_remove_private_as:
            return
        source_class = self._classname
        source_method = 'nxos_bgp_neighbor_verify_remove_private_as'
        expectation = self.nxos_bgp_neighbor_valid_remove_private_as
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_verify_timers(self, x, parameter='timers'):
        '''
        verify timers_holdtime and timers_keepalive are between 0-3600 or == 'default'
        '''
        if self.is_default(x):
            return
        if x in list(range(0,3601)):
            return
        source_class = self._classname
        source_method = 'nxos_bgp_neighbor_verify_timers'
        expectation = '[2-255, "default"]'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def asn(self):
        return self.properties['asn']
    @asn.setter
    def asn(self, x):
        '''
        nxos_bgp nxos_bgp_af
        '''
        parameter = 'asn'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def bfd(self):
        return self.properties['bfd']
    @bfd.setter
    def bfd(self, x):
        '''
        '''
        parameter = 'bfd'
        if self.set_none(x, parameter):
            return
        self.verify_enable_disable(x, parameter)
        self.properties[parameter] = x

    @property
    def capability_negotiation(self):
        return self.properties['capability_negotiation']
    @capability_negotiation.setter
    def capability_negotiation(self, x):
        '''
        '''
        parameter = 'capability_negotiation'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def connected_check(self):
        return self.properties['connected_check']
    @connected_check.setter
    def connected_check(self, x):
        '''
        '''
        parameter = 'connected_check'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def description(self):
        return self.properties['description']
    @description.setter
    def description(self, x):
        '''
        '''
        parameter = 'description'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def dynamic_capability(self):
        return self.properties['dynamic_capability']
    @dynamic_capability.setter
    def dynamic_capability(self, x):
        '''
        '''
        parameter = 'dynamic_capability'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def ebgp_multihop(self):
        return self.properties['ebgp_multihop']
    @ebgp_multihop.setter
    def ebgp_multihop(self, x):
        '''
        '''
        parameter = 'ebgp_multihop'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_ebgp_multihop(x, parameter)
        self.properties[parameter] = x

    @property
    def local_as(self):
        return self.properties['local_as']
    @local_as.setter
    def local_as(self, x):
        '''
        '''
        parameter = 'local_as'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def log_neighbor_changes(self):
        return self.properties['log_neighbor_changes']
    @log_neighbor_changes.setter
    def log_neighbor_changes(self, x):
        '''
        '''
        parameter = 'log_neighbor_changes'
        if self.set_none(x, parameter):
            return
        if x not in self.nxos_bgp_neighbor_valid_log_neighbor_changes:
            expectation = ','.join(self.nxos_bgp_neighbor_valid_log_neighbor_changes)
            self.fail(self._classname, parameter, x, parameter, expectation)
        self.properties[parameter] = x

    @property
    def low_memory_exempt(self):
        return self.properties['low_memory_exempt']
    @low_memory_exempt.setter
    def low_memory_exempt(self, x):
        '''
        '''
        parameter = 'low_memory_exempt'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def maximum_peers(self):
        return self.properties['maximum_peers']
    @maximum_peers.setter
    def maximum_peers(self, x):
        '''
        '''
        parameter = 'maximum_peers'
        if self.set_none(x, parameter):
            return
        result = 'fail'
        # maximum_peers is valid only with prefix-peering if neighbor
        # is defined, make sure it's a prefix
        # There is another test for maximum peers in self.nxos_bgp_neighbor_verify_neighbor_bgp()
        # which is called in @property neighbor
        if self.neighbor != None:
            if self.is_ipv4_address_with_prefix(self.neighbor):
                result = 'success'
            if self.is_ipv6_network(self.neighbor):
                result = 'success'
        if result == 'fail':
            expectation = "[IPv4 Network, IPv6 Network]"
            self.fail(self._classname, parameter, x, parameter, expectation)
        self.verify_maximum_peers(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor(self):
        return self.properties['neighbor']
    @neighbor.setter
    def neighbor(self, x):
        '''
        '''
        parameter = 'neighbor'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_neighbor_bgp(x)
        self.properties[parameter] = x

    @property
    def pwd(self):
        return self.properties['pwd']
    @pwd.setter
    def pwd(self, x):
        '''
        '''
        parameter = 'pwd'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def pwd_type(self):
        return self.properties['pwd_type']
    @pwd_type.setter
    def pwd_type(self, x):
        '''
        '''
        parameter = 'pwd_type'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_pwd_type(x)
        self.properties[parameter] = x

    @property
    def remote_as(self):
        return self.properties['remote_as']
    @remote_as.setter
    def remote_as(self, x):
        '''
        '''
        parameter = 'remote_as'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def remove_private_as(self):
        return self.properties['remove_private_as']
    @remove_private_as.setter
    def remove_private_as(self, x):
        '''
        '''
        parameter = 'remove_private_as'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_remove_private_as(x, parameter)
        self.properties[parameter] = x

    @property
    def shutdown(self):
        return self.properties['shutdown']
    @shutdown.setter
    def shutdown(self, x):
        '''
        '''
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
        '''
        '''
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_4_byte_as(self):
        return self.properties['suppress_4_byte_as']
    @suppress_4_byte_as.setter
    def suppress_4_byte_as(self, x):
        '''
        '''
        parameter = 'suppress_4_byte_as'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def task_name(self):
        return self.properties['task_name']
    @task_name.setter
    def task_name(self, x):
        parameter = 'task_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def timers_holdtime(self):
        return self.properties['timers_holdtime']
    @timers_holdtime.setter
    def timers_holdtime(self, x):
        '''
        '''
        parameter = 'timers_holdtime'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_timers(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_keepalive(self):
        return self.properties['timers_keepalive']
    @timers_keepalive.setter
    def timers_keepalive(self, x):
        '''
        '''
        parameter = 'timers_keepalive'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_verify_timers(x, parameter)
        self.properties[parameter] = x

    @property
    def transport_passive_only(self):
        return self.properties['transport_passive_only']
    @transport_passive_only.setter
    def transport_passive_only(self, x):
        '''
        '''
        parameter = 'transport_passive_only'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def update_source(self):
        return self.properties['update_source']
    @update_source.setter
    def update_source(self, x):
        '''
        '''
        parameter = 'update_source'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter)
        self.properties[parameter] = x
