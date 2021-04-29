# StcDrvDelete() - spirent/stc_drv_delete.py
our_version = 105
from copy import deepcopy
from ask.common.task import Task
'''
**************************************************
StcDrvDelete() - spirent/stc_drv_delete.py
**************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcDrvDelete() deletes a named Dynamic Result View (DRV).

It generates Ansible task instances conformant with Spirent's
Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run the playbook generated by StcDrvDelete(),
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_drv_delete.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_drv_delete.py>`_

Properties
----------

====================================    ==================================================
Property                                Description
====================================    ==================================================
drv_name                                Name of the Dynamic Result View to delete::

                                            - Type: str()
                                            - Spirent name: na
                                            - Default: 'Dropped Frames DRV'
                                            - Examples:
                                                - task.drv_name = 'my DRV'

reset_existing                          Reset any existing results::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Default: False
                                            - Spirent name: reset_existing
                                            - Examples:
                                                - task.reset_existing = True

====================================    ==================================================
'''
class StcDrvDelete(Task):
    def __init__(self, task_log):
        ansible_module = 'stc'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.action = 'delete'

        self.properties_set = set()
        self.properties_set.add('drv_name')
        self.properties_set.add('reset_existing')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        # used in self.update() to map between this class's property names
        # and Spirent's property names. This dict() is keyed on the items in
        # self.properties_set, and MUST contain all of these items.
        self.property_map = dict()
        self.property_map['drv_name'] = 'drv_name'
        self.property_map['reset_existing'] = 'reset_existing'

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None

    def final_verification(self):
        if self.drv_name == None:
            self.drv_name = "Dropped Frames DRV"
        if self.reset_existing == None:
            self.reset_existing = False

    def commit(self):
        self.update()
    def update(self):
        '''
        Call self.final_verification()
        Populate self.ansible_task dict()
        '''
        self.final_verification()
        d = dict()
        d['action'] = self.action
        d['objects'] = self.get_drv_ref()
        d['reset_existing'] = self.reset_existing
        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def get_drv_ref(self):
        if self.drv_name == None:
            self.drv_name = "Dropped Frames DRV"
        return 'ref:/project/DynamicResultView[name="{}"]'.format(self.drv_name)

    @property
    def drv_name(self):
        return self.properties['drv_name']
    @drv_name.setter
    def drv_name(self, x):
        parameter = 'drv_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def reset_existing(self):
        return self.properties['reset_existing']
    @reset_existing.setter
    def reset_existing(self, x):
        parameter = 'reset_existing'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
