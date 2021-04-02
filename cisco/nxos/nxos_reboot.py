# NxosReboot() - cisco/nxos/nxos_reboot.py
our_version = 105
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosReboot()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosReboot() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_reboot
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_reboot <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_reboot_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_reboot.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_reboot.py>`_

|

================================    ==============================================
Property                            Description
================================    ==============================================
confirm                             Set to true if you're sure you want to reboot::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Default: False

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'my task'

================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosReboot(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_reboot'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('confirm')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.confirm == None:
            self.task_log.error('exiting. set instance.confirm prior to calling instance.commit()')
            exit(11)

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
        self.ansible_task[self.ansible_module] = d.copy()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    @property
    def confirm(self):
        return self.properties['confirm']
    @confirm.setter
    def confirm(self, x):
        parameter = 'confirm'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x
