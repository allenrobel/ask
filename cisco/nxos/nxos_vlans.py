# NxosVlans() - cisco/nxos/nxos_vlans.py
our_version = 106
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosVlans()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosVlans() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_vlans
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vlans <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vlans_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vlans.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vlans.py>`_


|

========================    ============================================
Property                    Description
========================    ============================================
enabled                     Manage administrative state of the vlan.::

                                - Type: bool()
                                - Valid values:
                                    - False
                                    - True
                                - Example:
                                    task.enabled = True

mapped_vni                  The Virtual Network Identifier (VNI) ID that
                            is mapped to the VLAN::

                                - Type: int() or str()
                                - Valid values:
                                    - range: 4096-16773119
                                    - keyword: default
                                - Examples:
                                    task.mapped_vni = 20200
                                    task.mapped_vni = 'default'

mode                        Set VLAN mode to classical ethernet or fabricpath.
                            This is a valid option for Nexus 5000, Nexus 6000,
                            and Nexus 7000::

                                - Type: str()
                                - Valid values:
                                    - ce   (classic ethernet)
                                    - fabricpath
                                - Example:
                                    task.mode = 'ce'

name                        Name of VLAN::

                                - Type: str()
                                - Example:
                                    task.name = 'ENG'

state                       The state of the configuration after module completion.
                            The state ``overridden`` would override the configuration
                            of all the VLANs on the device (including VLAN 1) with
                            the provided configuration in the task. Use caution
                            with this state.::

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

vlan_state                  Manage operational state of the vlan::

                                - Type: str()
                                - Valid values:
                                    - active
                                    - suspend
                                - Example:
                                    task.vlan_state = 'active'

vlan_id                     VLAN ID::

                                - Type: int()
                                - Valid values:
                                    - range: 1-4094
                                - Example:
                                    task.vlan_id = 400
                                - Required

========================    ============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''
class NxosVlans(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vlans'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.vlan_list = list() # appended to in add_vlan()

        self.valid_mode = set()
        self.valid_mode.add('ce')
        self.valid_mode.add('fabricpath')

        self.valid_state = set()
        self.valid_state.add('deleted')
        self.valid_state.add('gathered')
        self.valid_state.add('merged')
        self.valid_state.add('overridden')
        self.valid_state.add('parsed')
        self.valid_state.add('rendered')
        self.valid_state.add('replaced')

        self.valid_vlan_state = set()
        self.valid_vlan_state.add('active')
        self.valid_vlan_state.add('suspend')

        self.vni_min = 1
        self.vni_max = 16777214

        self.properties_set = set()
        self.properties_set.add('enabled')
        self.properties_set.add('mapped_vni')
        self.properties_set.add('mode')
        self.properties_set.add('name')
        self.properties_set.add('vlan_state')
        self.properties_set.add('vlan_id')

        self.property_map = dict()
        self.property_map['vlan_state'] = 'state'

        self.init_properties()


    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['state'] = None
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
        self.ansible_task[self.ansible_module]['state'] = self.state
        self.ansible_task[self.ansible_module]['config'] = deepcopy(self.vlan_list)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_vlans_state(self, x, parameter='verify_nxos_vlans_state'):
        if x in self.valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vlans_state'
        expectation = ','.join(self.valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vlans_mode(self, x, parameter='mode'):
        if x in self.valid_mode:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vlans_mode'
        expectation = ','.join(self.valid_mode)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vlans_vlan_state(self, x, parameter='vlan_state'):
        if x in self.valid_vlan_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vlans_vlan_state'
        expectation = ','.join(self._valid_vlan_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vlans_mapped_vni(self, x, parameter='mapped_vni'):
        self.verify_integer_range(x, self._min_vni, self._max_vni, self.class_name, 'verify_nxos_vlans_mapped_vni')

    def add_vlan_verification(self):
        if self.vlan_id == None:
            self.task_log.error('exiting. call instance.vlan_id before calling instance.add_vlan()')
            exit(1)
    def add_vlan(self):
        self.add_vlan_verification()
        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                if p in self.property_map:
                    mapped_p = self.property_map[p]
                else:
                    mapped_p = p
                d[mapped_p] = self.properties[p]
        self.vlan_list.append(deepcopy(d))

    @property
    def enabled(self):
        return self.properties['enabled']
    @enabled.setter
    def enabled(self, x):
        parameter = 'enabled'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x)
        self.properties[parameter] = x

    @property
    def mapped_vni(self):
        return self.properties['mapped_vni']
    @mapped_vni.setter
    def mapped_vni(self, x):
        parameter = 'mapped_vni'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, self.vni_min, self.vni_max, parameter, parameter)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vlans_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x


    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vlans_state(x, parameter)
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
    def vlan_id(self):
        return self.properties['vlan_id']
    @vlan_id.setter
    def vlan_id(self, x):
        parameter = 'vlan_id'
        if self.set_none(x, parameter):
            return
        expectation = 'int() within 2-4094 inclusive'
        self.verify_vlan(x, expectation, parameter)
        self.properties[parameter] = x

    @property
    def vlan_state(self):
        return self.properties['vlan_state']
    @vlan_state.setter
    def vlan_state(self, x):
        parameter = 'vlan_state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vlans_vlan_state(x, parameter)
        self.properties[parameter] = x

