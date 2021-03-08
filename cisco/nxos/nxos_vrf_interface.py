# NxosVrfInterface() - cisco/nxos/nxos_vrf_interface.py
our_version = 105
from copy import deepcopy
from ask.common.task import Task
'''
*******************************************
NxosVrfInterface()
*******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVrfInterface() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vrf_interface <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vrf_interface_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vrf_interface.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vrf_interface.py>`_

Properties
----------

======================================  ==================================================
Property                                Description
======================================  ==================================================
interface                               Full name of interface to be managed::

                                            - Type: str()
                                            - Examples:
                                                task.interface = 'Ethernet1/1' 
                                                task.interface = 'Vlan10'
                                                task.interface = 'port-channel200'

state                                   Manages desired state of the resource::

                                            - Type: str()
                                            - Valid values:
                                                - absent
                                                - present
                                            - Example:
                                                task.state = 'present'

vrf                                     Name of VRF to be managed::

                                            - Type: str()
                                            - Example:
                                                task.vrf = 'my_vrf'

======================================  ==================================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosVrfInterface(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vrf_interface'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()

        self.nxos_vrf_interface_valid_state = set()
        self.nxos_vrf_interface_valid_state.add('present')
        self.nxos_vrf_interface_valid_state.add('absent')

        self.properties_set = set()
        self.properties_set.add('interface')
        self.properties_set.add('state')
        self.properties_set.add('vrf')

        # used in update() to resolve any disambiguated property
        # names back into the names used by the Ansible module.
        # In this case, there are currently no property names
        # that needed disambiguation, so this is essentially
        # a noop to maintain consistency with other ScriptKit
        # classes.
        self.property_map = dict()
        self.property_map['interface'] = 'interface'
        self.property_map['state'] = 'state'
        self.property_map['vrf'] = 'vrf'

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.interface == None:
            self.task_log.error('exiting. call instance.interface before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.vrf == None:
            self.task_log.error('exiting. call instance.vrf before calling instance.update()')
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
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def verify_nxos_vrf_interface_state(self, x, parameter='state'):
        verify_set = self.nxos_vrf_interface_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_interface_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def interface(self):
        return self.properties['interface']
    @interface.setter
    def interface(self, x):
        parameter = 'interface'
        if self.set_none(x, parameter):
            return
        self.verify_ip_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_interface_state(x, parameter)
        self.properties[parameter] = x

    @property
    def vrf(self):
        return self.properties['vrf']
    @vrf.setter
    def vrf(self, x):
        parameter = 'vrf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
