# NxosBfdInterfaces() - cisco/nxos/nxos_bfd_interfaces.py
our_version = 104

from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosBfdInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosBfdInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bfd_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bfd_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bfd_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bfd_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bfd_interfaces.py>`_


|

============================    ==============================================
Property                        Description
============================    ==============================================
bfd                             Enable/Disable Bidirectional Forwarding Detection 
                                (BFD) on the interface::

                                    - Type: str()
                                    - Valid values: enable, disable
                                    - Examples:
                                        - task.bfd = 'enable'

echo                            Enable/Disable BFD Echo functionality on the interface::

                                    - Type: str()
                                    - Valid values: enable, disable
                                    - Examples:
                                        - task.echo = 'disable'

name                            Full name of interface::

                                    - Type: str()
                                    - Examples:
                                        - task.name = 'Ethernet1/10'
                                        - task.name = 'port-channel4'

state                           The state of the resource after playbook
                                execution::

                                    - Type: str()
                                    - Valid values:
                                        - deleted
                                        - gathered
                                        - merged
                                        - overridden
                                        - parsed
                                        - rendered
                                        - replaced
                                    - Examples:
                                        - task.state = 'deleted'

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Examples:
                                        - task.task_name = 'my task'

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosBfdInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bfd_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        # list() of dict()
        # updated in add_interface()
        self.interface_list = list()

        self.properties_set = set()
        self.properties_set.add('bfd')
        self.properties_set.add('echo')
        self.properties_set.add('name')
        self.properties_set.add('state')

        self.interface_properties_set = set()
        self.interface_properties_set.add('bfd')
        self.interface_properties_set.add('echo')
        self.interface_properties_set.add('name')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        # map disambiguated property names back into
        # their ambiguous names.  For example:
        #  foo:
        #     units: 10
        #  bar:
        #     units: msec
        #
        # Above, units is ambiguous and we would need to 
        # disambiguate it into, say, foo_units and bar_units.
        # We would then need to map these back into their
        # original ambiguous names when writing the playbook
        # task, so we'd add these to property_map, like:
        #
        # self.property_map['foo_units'] = 'units'
        # self.property_map['bar_units'] = 'units'
        #
        # Since nxos_bfd_interfaces does not have any 
        # ambiguous names, property_map is currently a noop.
        self.property_map = dict()
        self.property_map['bfd'] = 'bfd'
        self.property_map['echo'] = 'echo'
        self.property_map['name'] = 'name'
        self.property_map['state'] = 'state'

        self.nxos_bfd_interfaces_valid_bfd = set()
        self.nxos_bfd_interfaces_valid_bfd.add('enable')
        self.nxos_bfd_interfaces_valid_bfd.add('disable')

        self.nxos_bfd_interfaces_valid_echo = set()
        self.nxos_bfd_interfaces_valid_echo.add('enable')
        self.nxos_bfd_interfaces_valid_echo.add('disable')

        self.nxos_bfd_interfaces_valid_state = set()
        self.nxos_bfd_interfaces_valid_state.add('deleted')
        self.nxos_bfd_interfaces_valid_state.add('gathered')
        self.nxos_bfd_interfaces_valid_state.add('merged')
        self.nxos_bfd_interfaces_valid_state.add('overridden')
        self.nxos_bfd_interfaces_valid_state.add('parsed')
        self.nxos_bfd_interfaces_valid_state.add('rendered')
        self.nxos_bfd_interfaces_valid_state.add('replaced')

        self.init_properties()

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if len(self.interface_list) == 0 and self.state != 'deleted':
            self.task_log.error('exiting. call instance.add_interface() at least once before calling instance.update()')
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate dict() self.ansible_task
        '''
        self.final_verification()

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        if len(self.interface_list) != 0:
            self.ansible_task[self.ansible_module]['config'] = deepcopy(self.interface_list)
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def init_interface_properties(self):
        for p in self.interface_properties_set:
            self.properties[p] = None
    def interface_verification(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.add_interface()')
            exit(1)
    def add_interface(self):
        self.interface_verification()
        d = dict()
        for p in self.interface_properties_set:
            if self.properties[p] == None:
                continue
            mapped_p = self.property_map[p]
            d[mapped_p] = self.properties[p]
        self.interface_list.append(deepcopy(d))
        self.init_interface_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None


    def verify_nxos_bfd_interfaces_bfd(self, x, parameter='bfd'):
        if x in self.nxos_bfd_interfaces_valid_bfd:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_interfaces_bfd'
        expectation = ','.join(self.nxos_bfd_interfaces_valid_bfd)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bfd_interfaces_echo(self, x, parameter='echo'):
        if x in self.nxos_bfd_interfaces_valid_echo:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_interfaces_echo'
        expectation = ','.join(self.nxos_bfd_interfaces_valid_echo)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bfd_interfaces_name(self, x, parameter='name'):
        if self.is_ethernet_interface(x):
            return
        if self.is_ethernet_subinterface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_interfaces_name'
        expectation = 'Full name of a BFD-capable interface. e.g. Ethernet1/1, port-channel4'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bfd_interfaces_state(self, x, parameter='state'):
        if x in self.nxos_bfd_interfaces_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_interfaces_state'
        expectation = ','.join(self.nxos_bfd_interfaces_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def bfd(self):
        return self.properties['bfd']
    @bfd.setter
    def bfd(self, x):
        parameter = 'bfd'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_interfaces_bfd(x, parameter)
        self.properties[parameter] = x

    @property
    def echo(self):
        return self.properties['echo']
    @echo.setter
    def echo(self, x):
        parameter = 'echo'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_interfaces_echo(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_interfaces_name(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_interfaces_state(x, parameter)
        self.properties[parameter] = x
