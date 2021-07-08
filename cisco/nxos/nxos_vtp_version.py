# NxosVtpVersion() - cisco/nxos/nxos_vtp_version.py
our_version = 100
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosVtpVersion()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
100

ScriptKit Synopsis
------------------
- NxosVtpVersion() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_vtp_version
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vtp_version <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vtp_version_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vtp_version.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vtp_version.py>`_


|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task::

                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See ScriptKit Example above 

========================    ============================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
version                             VTP version number::

                                        - Type: int()
                                        - Valid values:
                                            - range 1-2
                                        - Examples:
                                            task.version = 1
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Examples:
                                            - task.task_name = 'my task'

================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosVtpVersion(Task):
    '''
    Example usage:

    '''
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vtp_version'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.properties_set = set()
        self.properties_set.add('version')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.mandatory_properties = set()
        self.mandatory_properties.add('version')

        self.valid_vtp_version = set()
        self.valid_vtp_version.add(1)
        self.valid_vtp_version.add(2)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def nxos_vtp_version_verify_version(self, x, parameter='version'):
        verify_set = self.valid_vtp_version
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_vtp_version_verify_version'
        expectation = ','.join([str(x) for x in sorted(verify_set)])
        self.fail(source_class, source_method, x, parameter, expectation)

    def final_verification(self):
        for p in self.mandatory_properties:
            if self.properties[p] == None:
                self.task_log.error('exiting. instance.{} must be set before calling instance.commit()'.format(p))
                exit(1)

    def commit(self):
        self.update()
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
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    @property
    def version(self):
        return self.properties['version']
    @version.setter
    def version(self, x):
        parameter = 'version'
        if self.set_none(x, parameter):
            return
        self.nxos_vtp_version_verify_version(x, parameter)
        self.properties[parameter] = x
