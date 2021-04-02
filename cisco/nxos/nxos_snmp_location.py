# NxosSnmpLocation() - cisco/nxos/nxos_snmp_location.py
our_version = 106
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosSnmpLocation()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosSnmpLocation() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_snmp_location
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_snmp_location <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_snmp_location_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_snmp_location.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_snmp_location.py>`_

|

============    ==============================================
Property        Description
============    ==============================================
location        Location information::

                    - Type: str()
                    - Example:
                        task.location = 'Row: 7, Rack: 10'
                    - Required

state           Manage the state of the resource::

                    - Type: str()
                    - Value values:
                        - absent
                        - present
                    - Example:
                        - task.state = 'present'

task_name       Name of the task. Ansible will display this
                when the playbook is run::

                    - Type: str()
                    - Example:
                        - task.task_name = 'my task'

============    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosSnmpLocation(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_snmp_location'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('location')
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_snmp_location_valid_state = set()
        self.nxos_snmp_location_valid_state.add('present')
        self.nxos_snmp_location_valid_state.add('absent')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.location == None:
            self.task_log.error('exiting. Set instance.location before calling instance.commit()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. Set instance.state before calling instance.commit()')
            exit(1)

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
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_snmp_location_state(self, x, parameter='state'):
        verify_set = self.nxos_snmp_location_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_location_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def location(self):
        return self.properties['location']
    @location.setter
    def location(self, x):
        parameter = 'location'
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
        self.verify_nxos_snmp_location_state(x, parameter)
        self.properties[parameter] = x
