# NxosHsrpInterfaces() - cisco/nxos/nxos_hsrp_interfaces.py
our_version = 106
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosHsrpInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
106

ScriptKit Synopsis
------------------
- NxosHsrpInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_hsrp_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_hsrp_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_hsrp_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_hsrp_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_hsrp_interfaces.py>`_

================================    ==============================================
Method                              Description
================================    ==============================================
add_interface()                         Add an interface to the configuration::

                                            - Type: function()
                                            - Example:
                                                #!/usr/bin/env python3
                                                # Enable HSRP BFD on 5 interfaces
                                                from ask.cisco.nxos.nxos_hsrp_interfaces import NxosHsrpInterfaces
                                                from ask.common.log import Log
                                                from ask.common.playbook import Playbook
                                                log_level_console = 'INFO'
                                                log_level_file = 'DEBUG'
                                                log = Log('my_log', log_level_console, log_level_file)
                                                pb = Playbook(log)
                                                pb.profile_nxos()
                                                pb.ansible_password = 'mypassword'
                                                pb.name = 'Example nxos_hsrp_interfaces'
                                                pb.add_host('dc-101')
                                                pb.file = '/tmp/nxos_hsrp_interfaces.yaml'
                                                task = NxosHsrpInterfaces(log)
                                                task.append_to_task_name('HSRP BFD enable:')
                                                for port in range(1,6):
                                                    task.name = 'Ethernet1/{}'.format(port)
                                                    task.bfd = 'enable'
                                                    task.append_to_task_name(task.name)
                                                    task.add_interface()
                                                task.state = 'merged'
                                                task.update()
                                                pb.add_task(task)
                                                pb.append_playbook()
                                                pb.write_playbook()

================================    ==============================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
name                                Full name of the interface::

                                        - Type: str()
                                        - Example:
                                            task.name = 'Ethernet1/1'
                                        - Required

bfd                                 Enable/Disable HSRP Bidirectional Forwarding
                                    Detection (BFD) on the interface::

                                        - Type: str()
                                        - Valid values:
                                            - disable
                                            - enable
                                        - Example:
                                            task.bfd = 'enable'

state                               Desired state of hsrp attributes on
                                    ``name`` interface::

                                        - Type: str()
                                        - Valid values:
                                            - deleted
                                            - gathered
                                            - merged
                                            - overridden
                                            - parsed
                                            - rendered
                                            - replaced
                                        - Example:
                                            task.state = 'enabled'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'Vlan10 HSRP BFD'
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosHsrpInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_hsrp_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.interface_list = list()

        self.interface_properties = set()
        self.interface_properties.add('name')
        self.interface_properties.add('bfd')

        self.properties_set = set()
        self.properties_set.update(self.interface_properties)
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_hsrp_interfaces_valid_bfd = set()
        self.nxos_hsrp_interfaces_valid_bfd.add('disable')
        self.nxos_hsrp_interfaces_valid_bfd.add('enable')

        self.nxos_hsrp_interfaces_valid_state = set()
        self.nxos_hsrp_interfaces_valid_state.add('deleted')
        self.nxos_hsrp_interfaces_valid_state.add('gathered')
        self.nxos_hsrp_interfaces_valid_state.add('merged')
        self.nxos_hsrp_interfaces_valid_state.add('overridden')
        self.nxos_hsrp_interfaces_valid_state.add('parsed')
        self.nxos_hsrp_interfaces_valid_state.add('rendered')
        self.nxos_hsrp_interfaces_valid_state.add('replaced')

        self.nxos_hsrp_interfaces_valid_interface_examples = set()
        self.nxos_hsrp_interfaces_valid_interface_examples.add('EthernetX/Y')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('EthernetX/Y/Z')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('EthernetX/Y.S')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('EthernetX/Y/Z.S')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('port-channelX')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('VlanX')

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
    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['config'] = deepcopy(self.interface_list)
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def init_interface_properties(self):
        for p in self.interface_properties:
            self.properties[p] = None
    def verify_interface_properties(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.add_interface()')
            exit(1)
    def add_interface(self):
        self.verify_interface_properties()
        d = dict()
        for p in self.interface_properties:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        if len(d) == 0:
            self.task_log.error('exiting. Set at least one interface property before calling instance.interface()')
            exit(1)
        self.interface_list.append(deepcopy(d))
        self.init_interface_properties()

    def verify_nxos_hsrp_interfaces_bfd(self, x, parameter='bfd'):
        verify_set = self.nxos_hsrp_interfaces_valid_bfd
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_hsrp_interfaces_bfd'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_hsrp_interfaces_interface(self, x, parameter='interface'):
        if self.is_ethernet_interface(x):
            return
        if self.is_ethernet_subinterface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_hsrp_interfaces_interface'
        expectation = ','.join(sorted(self.nxos_hsrp_interfaces_valid_interface_examples))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_hsrp_interfaces_state(self, x, parameter='state'):
        verify_set = self.nxos_hsrp_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_hsrp_interfaces_state'
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
        self.verify_nxos_hsrp_interfaces_bfd(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_interfaces_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_interfaces_state(x, parameter)
        self.properties[parameter] = x

