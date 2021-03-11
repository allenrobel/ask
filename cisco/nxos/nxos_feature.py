# NxosFeature() - cisco/nxos/nxos_feature.py
our_version = 108
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosFeature()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosFeature() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_feature
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_feature <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_feature_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_feature.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_feature.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
feature                             Name of the feature to enable/disable::

                                        - Type: str()
                                        - Example:
                                            task.feature = 'lacp'
                                        - Required

state                               Desired state of ``feature``::

                                        - Type: str()
                                        - Valid values:
                                            - disabled
                                            - enabled
                                        - Example:
                                            task.state = 'enabled'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'enable lacp'
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''
class NxosFeature(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_feature'
        super().__init__(ansible_module, task_log)
        self._version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('feature')
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_feature_valid_state = set()
        self.nxos_feature_valid_state.add('enabled')
        self.nxos_feature_valid_state.add('disabled')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.feature == None:
            self.task_log.error('exiting. call instance.feature before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)

    def update(self):
        '''
        call final_verification()
        update ansible_task dict()
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

    def nxos_feature_verify_state(self, x, parameter='state'):
        verify_set = self.nxos_feature_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_feature_verify_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def feature(self):
        return self.properties['feature']
    @feature.setter
    def feature(self, x):
        parameter = 'feature'
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
        self.nxos_feature_verify_state(x, parameter)
        self.properties[parameter] = x
