# StcDrvSubscribe() - spirent/stc_drv_subscribe.py
our_version = 106
from copy import deepcopy
from ask.common.task import Task
'''
**************************************************
StcDrvSubscribe() - spirent/stc_drv_subscribe.py
**************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcDrvSubscribe() subscribes to a named Dynamic Result View (DRV).

It generates Ansible task instances conformant with Spirent's
Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run the playbook generated by StcDrvSubscribe(),
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_drv_subscribe.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_drv_subscribe.py>`_

Properties
----------

====================================    ==================================================
Property                                Description
====================================    ==================================================
drv_name                                Subscribe to this named Dynamic Result View (DRV)::

                                            - Type: str()
                                            - Spirent name: na
                                            - Default: 'Dropped Frames DRV'
                                            - Examples:
                                                - task.drv_name = 'my DRV'

reset_existing                          Reset any existing DRV results::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Default: False
                                            - Spirent name: reset_existing
                                            - Examples:
                                                - task.reset_existing = True

====================================    ==================================================

'''
class StcDrvSubscribe(Task):
    def __init__(self, task_log):
        ansible_module = 'stc'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.action = 'drv.subscribe'

        self.properties_set = set()
        self.properties_set.add('drv_name')
        self.properties_set.add('reset_existing')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

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
        return 'ref:/project/DynamicResultView[name="{}"]'.format(self.drv_name)

    def verify_stc_drv_subscribe_reset_existing(self, x, parameter):
        if self.is_boolean(x):
            return
        source_class = self.class_name
        source_method = 'verify_stc_drv_subscribe_reset_existing'
        expectation = 'bool(): True or False'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def reset_existing(self):
        return self.properties['reset_existing']
    @reset_existing.setter
    def reset_existing(self, x):
        parameter = 'reset_existing'
        if self.set_none(x, parameter):
            return
        self.verify_stc_drv_subscribe_reset_existing(x, parameter)
        self.properties[parameter] = x

    @property
    def drv_name(self):
        return self.properties['drv_name']
    @drv_name.setter
    def drv_name(self, x):
        parameter = 'drv_name'
        self.properties[parameter] = x

