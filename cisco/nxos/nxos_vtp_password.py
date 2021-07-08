# NxosVtpPassword() - cisco/nxos/nxos_vtp_password.py
our_version = 100
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosVtpPassword()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
100

ScriptKit Synopsis
------------------
- NxosVtpPassword() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_vtp_password
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vtp_password <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vtp_password_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vtp_password.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vtp_password.py>`_


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
state                               Manage the state of the resource::

                                        - Type: str()
                                        - Valid values:
                                            - absent
                                            - present
                                        - Example:
                                            task.state = 'present'
                                        - Required

vtp_password                        VTP password::

                                        - Type: str()
                                        - Examples:
                                            task.vtp_password = 'my_vtp_password'
                                        - Required if state == present

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

class NxosVtpPassword(Task):
    '''
    Example usage:

    '''
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vtp_password'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.properties_set = set()
        self.properties_set.add('vtp_password')
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.mandatory_properties = set()
        self.mandatory_properties.add('state')

        self.nxos_vtp_password_valid_state = set()
        self.nxos_vtp_password_valid_state.add('absent')
        self.nxos_vtp_password_valid_state.add('present')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def nxos_vtp_password_verify_state(self, x, parameter='state'):
        verify_set = self.nxos_vtp_password_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_vtp_password_verify_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def final_verification(self):
        for p in self.mandatory_properties:
            if self.properties[p] == None:
                self.task_log.error('exiting. instance.{} must be set before calling instance.commit()'.format(p))
                exit(1)
        if self.state == 'present' and self.vtp_password == None:
            self.task_log.error('exiting. instance.vtp_password must be set if instance.state == present')
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
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.nxos_vtp_password_verify_state(x, parameter)
        self.properties[parameter] = x

    @property
    def vtp_password(self):
        return self.properties['vtp_password']
    @vtp_password.setter
    def vtp_password(self, x):
        parameter = 'vtp_password'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
