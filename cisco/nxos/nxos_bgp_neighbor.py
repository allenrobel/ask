# NxosBgpNeighbor() - cisco/nxos/nxos_bgp_neighbor.py
our_version = 111
# Deprecation: Ansible module nxos_bgp_neighbor is DEPRECATED
# Deprecated on: 2021.01.27
# Removed after: 2023-01-27
# Alternative: nxos_bgp_global - cisco/nxos/nxos_bgp_global.py
#
import re
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_bgp_neighbor.py

Description:

NxosBgpNeighbor() generates Ansible Playbook tasks conformant with nxos_bgp_neighbor
which can be fed to Playbook().add_task()

Usage example:
    unit_test/cisco/nxos/unit_test_bgp_neighbor.py

Properties:

    asn                     - digits, digits.digits
    bfd                     - enable, disable
    capability_negotiation  - no, yes
    connected_check         - no, yes
    description             - quoted?  
    dynamic_capability      - no, yes  
    ebgp_multihop           - int() 2-255, or "default"
    local_as
    log_neighbor_changes    - enable, disable, inherit
    low_memory_exempt       - no, yes
    maximum_peers           - int() 1-1000, or "default". Accepted only on prefix peers
    neighbor                - str() IPv4 or IPv6 notation, with or without prefix length
    pwd                     - str() password for neighbor
    pwd_type                - 3des, cisco_type_7, default
    remote_as               - str() asn in ASPLAIN or ASDOT notation
    remove_private_as       - enable, disable, all, replace-as
    shutdown
    suppress_4_byte_as      - no, yes
    task_name               - int() the Ansible task name
    timers_holdtime         - int() 0-3600 seconds, or 'default', which is 180
    timers_keepalive        - int() 0-3600 seconds, or 'default', which is 60
    transport_passive_only  - no, yes
    update_source           - str() source interface of BGP session and updates

'''

class NxosBgpNeighbor(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp_neighbor'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.task_log.warning('*******************************************************************************************')
        self.task_log.warning('NxosBgpNeighbor is DEPRECATED as its Ansible module nxos_bgp_neighbor is DEPRECATED.')
        self.task_log.warning('Use NxosBgpGlobal() (nxos_bgp_global) instead.')
        self.task_log.warning('*******************************************************************************************')
        self.init_properties()

        self.nxos_bgp_neighbor_valid_log_neighbor_changes = set()
        self.nxos_bgp_neighbor_valid_log_neighbor_changes.add('enable')
        self.nxos_bgp_neighbor_valid_log_neighbor_changes.add('disable')
        self.nxos_bgp_neighbor_valid_log_neighbor_changes.add('inherit')

        self.nxos_bgp_neighbor_valid_pwd_type = set()
        self.nxos_bgp_neighbor_valid_pwd_type.add('3des')
        self.nxos_bgp_neighbor_valid_pwd_type.add('cisco_type_7')
        self.nxos_bgp_neighbor_valid_pwd_type.add('default')

        self.nxos_bgp_neighbor_valid_remove_private_as = set()
        self.nxos_bgp_neighbor_valid_remove_private_as.add('enable')
        self.nxos_bgp_neighbor_valid_remove_private_as.add('disable')
        self.nxos_bgp_neighbor_valid_remove_private_as.add('all')
        self.nxos_bgp_neighbor_valid_remove_private_as.add('replace-as')

        self.nxos_bgp_neighbor_valid_state = set()
        self.nxos_bgp_neighbor_valid_state.add('absent')
        self.nxos_bgp_neighbor_valid_state.add('present')

        self.properties_set = set()
        self.properties_set.add('asn')
        self.properties_set.add('bfd')
        self.properties_set.add('capability_negotiation')
        self.properties_set.add('connected_check')
        self.properties_set.add('description')
        self.properties_set.add('dynamic_capability')
        self.properties_set.add('ebgp_multihop')
        self.properties_set.add('local_as')
        self.properties_set.add('log_neighbor_changes')
        self.properties_set.add('low_memory_exempt')
        self.properties_set.add('maximum_peers')
        self.properties_set.add('neighbor')
        self.properties_set.add('pwd')
        self.properties_set.add('pwd_type')
        self.properties_set.add('remote_as')
        self.properties_set.add('remove_private_as')
        self.properties_set.add('shutdown')
        self.properties_set.add('state')
        self.properties_set.add('suppress_4_byte_as')
        self.properties_set.add('timers_holdtime')
        self.properties_set.add('timers_keepalive')
        self.properties_set.add('transport_passive_only')
        self.properties_set.add('update_source')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

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
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_bgp_neighbor_state(self, x, parameter='state'):
        if x in self.nxos_bgp_neighbor_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_state'
        expectation = ','.join(self.nxos_bgp_neighbor_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_asn(self, x, parameter=''):
        if self.is_digits(x):
            return
        if re.search('^\d+\.\d+$', str(x)):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_asn'
        expectation = '["digits", "digits.digits", "digits:digits"]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_ebgp_multihop(self, x, parameter='ebgp_multihop'):
        '''
        verify ebgp_multihop is between 2-255 or == 'default'
        '''
        if self.is_default(x):
            return
        if x in list(range(2,256)):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_ebgp_multihop'
        expectation = '[2-255, "default"]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_neighbor_bgp(self, x, parameter='neighbor_bgp'):
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
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_neighbor_bgp'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_pwd_type(self, x, parameter='unspecified'):
        if x in self.nxos_bgp_neighbor_valid_pwd_type:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_pwd_type'
        expectation = self.nxos_bgp_neighbor_valid_pwd_type 
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_remove_private_as(self, x, parameter=''):
        if x in self.nxos_bgp_neighbor_valid_remove_private_as:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_remove_private_as'
        expectation = self.nxos_bgp_neighbor_valid_remove_private_as
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_timers(self, x, parameter='timers'):
        '''
        verify timers_holdtime and timers_keepalive are between 0-3600 or == 'default'
        '''
        if self.is_default(x):
            return
        if x in list(range(0,3601)):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_timers'
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
        self.verify_nxos_bgp_neighbor_asn(x, parameter)
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
        self.verify_nxos_bgp_neighbor_ebgp_multihop(x, parameter)
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
        self.verify_nxos_bgp_neighbor_asn(x, parameter)
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
            self.fail(self.class_name, parameter, x, parameter, expectation)
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
        # There is another test for maximum peers in self.verify_nxos_bgp_neighbor_neighbor_bgp()
        # which is called in @property neighbor
        if self.neighbor != None:
            if self.is_ipv4_address_with_prefix(self.neighbor):
                result = 'success'
            if self.is_ipv6_network(self.neighbor):
                result = 'success'
        if result == 'fail':
            expectation = "[IPv4 Network, IPv6 Network]"
            self.fail(self.class_name, parameter, x, parameter, expectation)
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
        self.verify_nxos_bgp_neighbor_neighbor_bgp(x)
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
        self.verify_nxos_bgp_neighbor_pwd_type(x)
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
        self.verify_nxos_bgp_neighbor_asn(x, parameter)
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
        self.verify_nxos_bgp_neighbor_remove_private_as(x, parameter)
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
        self.verify_nxos_bgp_neighbor_state(x, parameter)
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
    def timers_holdtime(self):
        return self.properties['timers_holdtime']
    @timers_holdtime.setter
    def timers_holdtime(self, x):
        '''
        '''
        parameter = 'timers_holdtime'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_timers(x, parameter)
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
        self.verify_nxos_bgp_neighbor_timers(x, parameter)
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
