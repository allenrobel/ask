# NxosHsrp() - cisco/nxos/nxos_hsrp.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosHsrp()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosHsrp() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_hsrp
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_hsrp <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_hsrp_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_hsrp.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_hsrp.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
auth_string                         Authentication string. If this needs to be 
                                    hidden(for md5 type), the string should be 7
                                    followed by the key string. Otherwise, it can
                                    be 0 followed by key string or just key string
                                    (for backward compatibility). For text type,
                                    this should be just be a key string. if this
                                    is 'default', authentication is removed.::

                                        - Type: str()
                                        - Valid values:
                                            - An authentication string
                                            - keyword: default
                                        - Examples:
                                            task.auth_string = '7 asdeir123'
                                            task.auth_string = '0 foobar'
                                            task.auth_string = 'foobar'
                                            task.auth_string = 'default'

auth_type                           Authentication type::

                                        - Type: str()
                                        - Valid values:
                                            - md5
                                            - text
                                        - Examples:
                                            task.auth_type = 'md5'
                                            task.auth_type = 'text'

group                               HSRP group number::

                                        - Type: int()
                                        - Valid values:
                                            - range 0-255 (version 1)
                                            - range 0-4095 (version 2)
                                        - Example:
                                            task.group = 10
                                        - Required

interface                           Full name of interface that is being managed for HSRP::

                                        - Type: str()
                                        - Examples:
                                            task.interface = 'Vlan10'
                                            task.interface = 'Ethernet1/1'
                                        - Required

preempt                             Enable/Disable HSRP preempt::

                                        - Type: str()
                                        - Valid values:
                                            - disabled
                                            - enabled
                                        - Example:
                                            task.preempt = 'disabled'

priority                            HSRP priority or keyword ``default``::

                                        - Type: int() or str()
                                        - Valid values:
                                            - range 0-255
                                            - keyword: default
                                        - Example:
                                            task.priority = 150
                                            task.priority = 'default'

state                               Desired state of ``hsrp`` attributes::

                                        - Type: str()
                                        - Valid values:
                                            - absent
                                            - present
                                        - Example:
                                            task.state = 'present'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'configure HSRP'

version                             HSRP version::

                                        - Type: int()
                                        - Valid values:
                                            - 1
                                            - 2
                                        - Default: 1
                                        - Example:
                                            task.version = 2

vip                                 HSRP virtual IP address or keyword ``default``::

                                        - Type: str()
                                        - Valid values:
                                            - An ip address with prefixlen
                                            - keyword: default
                                        - Examples:
                                            task.vip = '10.1.1.3/24'
                                            task.vip = 'default'

================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosHsrp(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_hsrp'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('auth_string')
        self.properties_set.add('auth_type')
        self.properties_set.add('group')
        self.properties_set.add('interface')
        self.properties_set.add('preempt')
        self.properties_set.add('priority')
        self.properties_set.add('state')
        self.properties_set.add('version')
        self.properties_set.add('vip')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_hsrp_valid_auth_type = set()
        self.nxos_hsrp_valid_auth_type.add('text')
        self.nxos_hsrp_valid_auth_type.add('md5')

        self.nxos_hsrp_valid_preempt = set()
        self.nxos_hsrp_valid_preempt.add('enabled')
        self.nxos_hsrp_valid_preempt.add('disabled')

        self.nxos_hsrp_valid_state = set()
        self.nxos_hsrp_valid_state.add('present')
        self.nxos_hsrp_valid_state.add('absent')

        self.nxos_hsrp_valid_version = set()
        self.nxos_hsrp_valid_version.add(1)
        self.nxos_hsrp_valid_version.add(2)

        self.nxos_hsrp_valid_interface_examples = set()
        self.nxos_hsrp_valid_interface_examples.add('EthernetX/Y')
        self.nxos_hsrp_valid_interface_examples.add('EthernetX/Y/Z')
        self.nxos_hsrp_valid_interface_examples.add('EthernetX/Y.S')
        self.nxos_hsrp_valid_interface_examples.add('EthernetX/Y/Z.S')
        self.nxos_hsrp_valid_interface_examples.add('port-channelX')
        self.nxos_hsrp_valid_interface_examples.add('VlanX')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        '''
        final verification across the properties that the user has or hasn't set
        '''
        if self.group == None:
            self.task_log.error('exiting. call instance.group before calling instance.update()')
            exit(1)
        if self.interface == None:
            self.task_log.error('exiting. call instance.interface before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        self.verify_nxos_hsrp_group(self.group, 'group')


    def commit(self):
        self.update()
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

    def verify_nxos_hsrp_auth_type(self, x, parameter=''):
        verify_set = self.nxos_hsrp_valid_auth_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_hsrp_auth_type'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_hsrp_group(self, x, parameter='group'):
        if self.version == None:
            self.verify_integer_range(x, 0, 4095, self.class_name, parameter)
        elif int(self.version) == 1:
            self.verify_integer_range(x, 0, 255, self.class_name, parameter)
        elif int(self.version) == 2:
            self.verify_integer_range(x, 0, 4095, self.class_name, parameter)
        else:
            self.task_log.error('exiting. unknown hsrp version {}'.format(self.version))
            exit(1)

    def nxos_hsrp_verify_interface(self, x, parameter='interface'):
        if self.is_ethernet_interface(x):
            return
        if self.is_ethernet_subinterface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_class = self.class_name
        source_method = 'nxos_hsrp_verify_interface'
        expectation = ','.join(sorted(self.nxos_hsrp_valid_interface_examples))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_hsrp_preempt(self, x, parameter='preempt'):
        verify_set = self.nxos_hsrp_valid_preempt
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_hsrp_preempt'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_hsrp_priority(self, x, parameter='priority'):
        if self.is_default(x):
            return
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits, or keyword: default. Got {}'.format(x))
            exit(1)
        self.verify_integer_range(x, 0, 255, self.class_name, parameter)

    def verify_nxos_hsrp_state(self, x, parameter='state'):
        verify_set = self.nxos_hsrp_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_hsrp_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_hsrp_version(self, x, parameter=''):
        if self.is_digits(x):
            if int(x) in self.nxos_hsrp_valid_version:
                return
        source_class = self.class_name
        source_method = 'verify_nxos_hsrp_version'
        expectation = ','.join(sorted(self.nxos_hsrp_valid_version))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_hsrp_vip(self, x, parameter=''):
        if self.is_default(x):
            return
        if self.is_ipv4_address_with_prefix(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_hsrp_vip'
        expectation = 'ipv4 address with prefixlen e.g. 10.0.0.1/24, or keyword: default'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def auth_string(self):
        return self.properties['auth_string']
    @auth_string.setter
    def auth_string(self, x):
        parameter = 'auth_string'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def auth_type(self):
        return self.properties['auth_type']
    @auth_type.setter
    def auth_type(self, x):
        parameter = 'auth_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_auth_type(x, parameter)
        self.properties[parameter] = x

    @property
    def group(self):
        return self.properties['group']
    @group.setter
    def group(self, x):
        parameter = 'group'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def interface(self):
        return self.properties['interface']
    @interface.setter
    def interface(self, x):
        parameter = 'interface'
        if self.set_none(x, parameter):
            return
        self.nxos_hsrp_verify_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def preempt(self):
        return self.properties['preempt']
    @preempt.setter
    def preempt(self, x):
        parameter = 'preempt'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_preempt(x, parameter)
        self.properties[parameter] = x


    @property
    def priority(self):
        return self.properties['priority']
    @priority.setter
    def priority(self, x):
        parameter = 'priority'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_priority(x, parameter)
        self.properties[parameter] = x

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
        self.verify_nxos_hsrp_state(x, parameter)
        self.properties[parameter] = x

    @property
    def version(self):
        return self.properties['version']
    @version.setter
    def version(self, x):
        '''
        '''
        parameter = 'version'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_version(x, parameter)
        self.properties[parameter] = x

    @property
    def vip(self):
        return self.properties['vip']
    @vip.setter
    def vip(self, x):
        '''
        '''
        parameter = 'vip'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_vip(x, parameter)
        self.properties[parameter] = x
