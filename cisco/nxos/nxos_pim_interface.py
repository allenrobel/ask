# NxosPimInterface() - cisco/nxos/nxos_pim_interface.py
our_version = 101
from copy import deepcopy
import re
from ask.common.task import Task
'''
==========================================
NxosPimInterface() - nxos_pim_interface.py
==========================================

Description
-----------
NxosPimInterface() generates Ansible tasks conformant with Ansible module nxos_pim_interface
These can then be passed to Playbook().add_task()

Example usage
-------------
unit_test/cisco/nxos/unit_test_nxos_pim_interface.py

Dependencies
------------

The following must be enabled prior to applying nxos_pim_interface playbook
    - nv overlay evpn

Properties
----------

Valid values for all bool() types are: no, yes

bfd             str()   Enables BFD for PIM at the interface level. This overrides the bfd variable set at the pim global level.
                        Valid values: enable, disable, default
                        Dependency: feature bfd
border          bool()  Configures interface to be a boundary of a PIM domain
dr_prio         int()   Configures priority for PIM DR election on interface
                        Valid values: range 1-4294967295
hello_auth_key  str()   Authentication for hellos on this interface.
hello_interval  int()   Hello interval in milliseconds for this interface
                        Valid values: range 1-18724286
interface       str()   Full name of the interface e.g. Ethernet1/33
jp_policy_in    str()   Policy for join-prune messages (inbound)
jp_policy_out   str()   Policy for join-prune messages (outbound)
jp_type_in      str()   Type of policy mapped to jp_policy_in
                        Valid values: prefix, routemap
jp_type_out     str()   Type of policy mapped to jp_policy_out
                        Valid values: prefix, routemap
neighbor_policy str()   Configures a neighbor policy for filtering adjacencies
neighbor_type   str()   Type of policy mapped to neighbor_policy
                        Valid values: prefix, routemap
sparse          bool()  Enable/disable sparse-mode on the interface
state           str()   Manages desired state of the resource
                        Valid values: absent, default, present
                        Default: present
'''
class NxosPimInterface(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_pim_interface'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('bfd')
        self.properties_set.add('border')
        self.properties_set.add('dr_prio')
        self.properties_set.add('hello_auth_key')
        self.properties_set.add('hello_interval')
        self.properties_set.add('interface')
        self.properties_set.add('jp_policy_in')
        self.properties_set.add('jp_policy_out')
        self.properties_set.add('jp_type_in')
        self.properties_set.add('jp_type_out')
        self.properties_set.add('neighbor_policy')
        self.properties_set.add('neighbor_type')
        self.properties_set.add('sparse')
        self.properties_set.add('state')

        self.nxos_pim_interface_valid_bfd = set()
        self.nxos_pim_interface_valid_bfd.add('default')
        self.nxos_pim_interface_valid_bfd.add('disable')
        self.nxos_pim_interface_valid_bfd.add('enable')

        self.nxos_pim_interface_valid_jp_type_in = set()
        self.nxos_pim_interface_valid_jp_type_in.add('prefix')
        self.nxos_pim_interface_valid_jp_type_in.add('routemap')

        self.nxos_pim_interface_valid_jp_type_out = set()
        self.nxos_pim_interface_valid_jp_type_out.add('prefix')
        self.nxos_pim_interface_valid_jp_type_out.add('routemap')

        self.nxos_pim_interface_valid_neighbor_type = set()
        self.nxos_pim_interface_valid_neighbor_type.add('prefix')
        self.nxos_pim_interface_valid_neighbor_type.add('routemap')

        self.nxos_pim_interface_valid_state = set()
        self.nxos_pim_interface_valid_state.add('absent')
        self.nxos_pim_interface_valid_state.add('default')
        self.nxos_pim_interface_valid_state.add('present')

        self.pim_dr_priority_min = 1
        self.pim_dr_priority_max = 4294967295

        self.pim_hello_interval_min = 1
        self.pim_hello_interval_max = 18724286

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name']    = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.interface == None:
            self.task_log.error('exiting. instance.interface must be set prior to calling instance.update()')
            exit(1)
        if self.jp_policy_in != None and self.jp_type_in == None:
            self.task_log.error('exiting. instance.jp_type_in must be set if instance.jp_policy_in is set')
            exit(1)
        if self.jp_policy_out != None and self.jp_type_out == None:
            self.task_log.error('exiting. instance.jp_type_out must be set if instance.jp_policy_out is set')
            exit(1)
        if self.neighbor_policy != None and self.neighbor_type == None:
            self.task_log.error('exiting. instance.neighbor_type must be set if instance.neighbor_policy is set')
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

    def verify_nxos_pim_interface_bfd(self, x, parameter='bfd'):
        verify_set = self.nxos_pim_interface_valid_bfd
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_pim_interface_bfd'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_pim_interface_dr_prio(self, x):
        source_class = self.class_name
        source_method = 'verify_nxos_pim_interface_dr_prio'
        self.verify_integer_range(x, self.pim_dr_priority_min, self.pim_dr_priority_max, source_class, source_method)

    def verify_nxos_pim_interface_hello_interval(self, x):
        source_class = self.class_name
        source_method = 'verify_nxos_pim_interface_hello_interval'
        self.verify_integer_range(x, self.pim_hello_interval_min, self.pim_hello_interval_max, source_class, source_method)

    def verify_nxos_pim_interface_interface(self, x, parameter='interface'):
        if self.is_ethernet_interface(x):
            return
        if self.is_loopback_interface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_pim_interface_interface'
        expectation = ','.join(self.valid_ip_pim_interface)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_pim_interface_jp_type_in(self, x, parameter='jp_type_in'):
        verify_set = self.nxos_pim_interface_valid_jp_type_in
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_pim_interface_jp_type_in'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_pim_interface_jp_type_out(self, x, parameter='jp_type_out'):
        verify_set = self.nxos_pim_interface_valid_jp_type_out
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_pim_interface_jp_type_out'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_pim_interface_neighbor_type(self, x, parameter='neighbor_type'):
        verify_set = self.nxos_pim_interface_valid_neighbor_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_pim_interface_neighbor_type'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_pim_interface_state(self, x, parameter='state'):
        verify_set = self.nxos_pim_interface_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_pim_interface_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def bfd(self):
        return self.properties['bfd']
    @bfd.setter
    def bfd(self, x):
        parameter = 'bfd'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_interface_bfd(x, parameter)
        self.properties[parameter] = x

    @property
    def border(self):
        return self.properties['border']
    @border.setter
    def border(self, x):
        parameter = 'border'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def dr_prio(self):
        return self.properties['dr_prio']
    @dr_prio.setter
    def dr_prio(self, x):
        parameter = 'dr_prio'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_interface_dr_prio(x)
        self.properties[parameter] = str(x)

    @property
    def hello_auth_key(self):
        return self.properties['hello_auth_key']
    @hello_auth_key.setter
    def hello_auth_key(self, x):
        parameter = 'hello_auth_key'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def hello_interval(self):
        return self.properties['hello_interval']
    @hello_interval.setter
    def hello_interval(self, x):
        parameter = 'hello_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_interface_hello_interval(x)
        self.properties[parameter] = str(x)

    @property
    def interface(self):
        return self.properties['interface']
    @interface.setter
    def interface(self, x):
        parameter = 'interface'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_interface_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def jp_policy_in(self):
        return self.properties['jp_policy_in']
    @jp_policy_in.setter
    def jp_policy_in(self, x):
        parameter = 'jp_policy_in'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def jp_policy_out(self):
        return self.properties['jp_policy_out']
    @jp_policy_out.setter
    def jp_policy_out(self, x):
        parameter = 'jp_policy_out'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def jp_type_in(self):
        return self.properties['jp_type_in']
    @jp_type_in.setter
    def jp_type_in(self, x):
        parameter = 'jp_type_in'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_interface_jp_type_in(x, parameter)
        self.properties[parameter] = x

    @property
    def jp_type_out(self):
        return self.properties['jp_type_out']
    @jp_type_out.setter
    def jp_type_out(self, x):
        parameter = 'jp_type_out'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_interface_jp_type_out(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_policy(self):
        return self.properties['neighbor_policy']
    @neighbor_policy.setter
    def neighbor_policy(self, x):
        parameter = 'neighbor_policy'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def neighbor_type(self):
        return self.properties['neighbor_type']
    @neighbor_type.setter
    def neighbor_type(self, x):
        parameter = 'neighbor_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_interface_neighbor_type(x, parameter)
        self.properties[parameter] = x

    @property
    def sparse(self):
        return self.properties['sparse']
    @sparse.setter
    def sparse(self, x):
        parameter = 'sparse'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_interface_state(x, parameter)
        self.properties[parameter] = x
