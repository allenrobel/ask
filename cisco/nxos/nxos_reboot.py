# NxosReboot() - cisco/nxos/nxos_reboot.py
our_version = 103
from copy import deepcopy
from ask.common.task import Task
'''
=============================
NxosReboot() - nxos_reboot.py
=============================

Description
-----------
NxosReboot() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Example usage
-------------

unit_test/cisco/nxos/unit_test_nxos_reboot.py

Properties
----------

=========== ===========
Property    Description
=========== ===========
confirm     Safeguard boolean. Set to true if you're sure you want to reboot::

                - Type: bool()
                - Valid values: no, yes
                - Default: no
=========== ===========

'''

class NxosReboot(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_reboot'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('confirm')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.confirm == None:
            self.task_log.error('exiting. set instance.confirm prior to calling instance.update()')
            exit(11)

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
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x
