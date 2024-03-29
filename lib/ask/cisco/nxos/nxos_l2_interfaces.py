# NxosL2Interfaces() - cisco/nxos/nxos_l2_interfaces.py
our_version = 111
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosL2Interfaces()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
111

ScriptKit Synopsis
------------------
- NxosL2Interfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_l2_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_l2_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_l2_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_l2_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_l2_interfaces.py>`_


|

====================================    ==============================================
Method                                  Description
====================================    ==============================================
add_interface()                         Add an interface to the configuration::

                                            - Type: function()
                                            - Example:
                                                #!/usr/bin/env python3
                                                # Configure one access and one trunk interface
                                                from ask.cisco.nxos.nxos_l2_interfaces import NxosL2Interfaces
                                                from ask.common.log import Log
                                                from ask.common.playbook import Playbook
                                                log_level_console = 'INFO'
                                                log_level_file = 'DEBUG'
                                                log = Log('my_log', log_level_console, log_level_file)
                                                pb = Playbook(log)
                                                pb.profile_nxos()
                                                pb.ansible_password = 'mypassword'
                                                pb.name = 'Example nxos_l2_interfaces'
                                                pb.add_host('dc-101')
                                                pb.file = '/tmp/nxos_l2_interfaces.yaml'
                                                task = NxosL2Interfaces(log)
                                                task.name = 'Ethernet1/1'
                                                task.mode = 'access'
                                                task.vlan = 11
                                                task.add_interface()
                                                task.name = 'Ethernet1/10'
                                                task.mode = 'trunk'
                                                task.native_vlan = 10
                                                task.allowed_vlans = '11,12,13'
                                                task.add_interface()
                                                task.state = 'merged'
                                                task.update()
                                                pb.add_task(task)
                                                pb.append_playbook()
                                                pb.write_playbook()

====================================    ==============================================

|

================    ======================================================
Property            Description
================    ======================================================
allowed_vlans       Comma-separated list of allowed VLANs on trunk port::

                        - Type: str()
                        - Example:
                            task.allowed_vlans = '2-5,10,20'

mode                Desired L2 mode of the interface::

                        - Type: str()
                        - Valid values:
                            - access
                            - trunk
                            - fex-fabric
                            - fabricpath
                        - Example:
                            task.mode = 'access'

name                Full name of interface::

                        - Type: str()
                        - Examples:
                            task.name = 'Ethernet1/1'
                            taks.name = 'port-channel20'
                        - Required except when ``running_config`` is set.

native_vlan         Native VLAN configured on trunk interface::

                        - Type: int()
                        - Valid values: range: 1-3967
                        - Examples:
                            task.native_vlan = 10

register            Ansible variable to save output to::

                        - Type: str()
                        - Examples:
                            task.register = 'result'

running_config      Full path to a file containing the output of
                    ``show running-config | section ^interface``::

                        - Type: str()
                        - Examples:
                            task.running_config = '/tmp/running.cfg'

state               Desired state after task has run::

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
                            task.state = 'merged'
                        - Required

vlan                Vlan configured on access port::

                        - Type: int()
                        - Valid values: range: 1-3967
                        - Examples:
                            task.vlan = 330

task_name           Name of the task. Ansible will display this
                    when the playbook is run::

                        - Type: str()
                        - Example:
                            - task.task_name = 'configure interfaces'
                                        
================    ======================================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)


'''

class NxosL2Interfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_l2_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.interface_list = list()

        self.interface_properties = set()
        self.interface_properties.add('allowed_vlans')
        self.interface_properties.add('mode')
        self.interface_properties.add('native_vlan')
        self.interface_properties.add('vlan')
        self.interface_properties.add('name')

        self.properties_set = set()
        self.properties_set.update(self.interface_properties)
        self.properties_set.add('register')
        self.properties_set.add('running_config')
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_l2_interfaces_valid_mode = set()
        self.nxos_l2_interfaces_valid_mode.add('access')
        self.nxos_l2_interfaces_valid_mode.add('trunk')
        self.nxos_l2_interfaces_valid_mode.add('fex-fabric')
        self.nxos_l2_interfaces_valid_mode.add('fabricpath')

        self.nxos_l2_interfaces_valid_state = set()
        self.nxos_l2_interfaces_valid_state.add('deleted')
        self.nxos_l2_interfaces_valid_state.add('gathered')
        self.nxos_l2_interfaces_valid_state.add('merged')
        self.nxos_l2_interfaces_valid_state.add('overridden')
        self.nxos_l2_interfaces_valid_state.add('parsed')
        self.nxos_l2_interfaces_valid_state.add('rendered')
        self.nxos_l2_interfaces_valid_state.add('replaced')

        self.nxos_l2_interfaces_native_vlan_min = 1
        self.nxos_l2_interfaces_native_vlan_max = 3967

        self.nxos_l2_interfaces_vlan_min = 1
        self.nxos_l2_interfaces_vlan_max = 3967

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if self.running_config != None and self.state != 'parsed':
            self.task_log.error('exiting. if running_config is set, state must be set to parsed')
            exit(1)
        if len(self.interface_list) == 0 and self.running_config == None:
            self.task_log.error('exiting. call instance.add_interface() at least once before calling instance.commit()')
            exit(1)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        populate and append dict() to self.ansible_task[self.ansible_module]['config']
        '''
        self.final_verification()

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        if self.running_config == None:
            self.ansible_task[self.ansible_module]['config'] = self.interface_list
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.running_config != None:
            self.ansible_task[self.ansible_module]['running_config'] = self.make_running_config()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        if self.register != None:
            self.ansible_task['register'] = self.register

    def make_running_config(self):
        return r'{{' +  " lookup(" + r'"file"' + ',' + r'"' + self.running_config + r'"' + ')' + r' }}'

    def verify_interface_properties(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.add_interface()')
            exit(1)
    def init_interface_properties(self):
        for p in self.interface_properties:
            self.properties[p] = None
    def add_interface(self):
        self.verify_interface_properties()
        d = dict()
        if self.mode != None:
            d['mode'] = self.mode
        d['name'] = self.name
        access = self.add_access()
        trunk = self.add_trunk()
        if access != False:
            d['access'] = access
        if trunk != False:
            d['trunk'] = trunk
        if len(d) == 0:
            self.task_log.error('exiting. Set at least instance.name before calling task.add_interface().')
            exit(1)
        self.interface_list.append(deepcopy(d))
        self.init_interface_properties()

    def verify_nxos_l2_interfaces_native_vlan(self, x, parameter='native_vlan'):
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interfaces_native_vlan'
        range_min = self.nxos_l2_interfaces_native_vlan_min
        range_max = self.nxos_l2_interfaces_native_vlan_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_l2_interfaces_vlan(self, x, parameter='vlan'):
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interfaces_vlan'
        range_min = self.nxos_l2_interfaces_vlan_min
        range_max = self.nxos_l2_interfaces_vlan_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_l2_interfaces_state(self, x, parameter='state'):
        verify_set = self.nxos_l2_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interfaces_state'
        expectation = ','.join(self.verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_l2_interfaces_mode(self, x, parameter='mode'):
        verify_set = self.nxos_l2_interfaces_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interfaces_mode'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def add_access(self):
        if self.vlan == None:
            return False
        d = dict()
        d['vlan'] = self.vlan
        return deepcopy(d)

    def add_trunk(self):
        if self.allowed_vlans == None and self.native_vlan == None:
            return False
        d = dict()
        if self.allowed_vlans != None:
            d['allowed_vlans'] = self.allowed_vlans
        if self.native_vlan != None:
            d['native_vlan'] = self.native_vlan
        return deepcopy(d)

    @property
    def allowed_vlans(self):
        return self.properties['allowed_vlans']
    @allowed_vlans.setter
    def allowed_vlans(self, x):
        parameter = 'allowed_vlans'
        if self.set_none(x, parameter):
            return
        self.verify_vlan_list(x)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interfaces_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def native_vlan(self):
        return self.properties['native_vlan']
    @native_vlan.setter
    def native_vlan(self, x):
        parameter = 'native_vlan'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interfaces_native_vlan(x, parameter)
        self.properties[parameter] = x

    @property
    def register(self):
        return self.properties['register']
    @register.setter
    def register(self, x):
        parameter = 'register'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def running_config(self):
        return self.properties['running_config']
    @running_config.setter
    def running_config(self, x):
        parameter = 'running_config'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def vlan(self):
        return self.properties['vlan']
    @vlan.setter
    def vlan(self, x):
        parameter = 'vlan'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interfaces_vlan(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interfaces_state(x, parameter)
        self.properties[parameter] = x
