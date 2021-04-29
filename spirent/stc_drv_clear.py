# StcDrvClear() - spirent/stc_drv_clear.py
our_version = 106
from copy import deepcopy
from ask.common.task import Task
'''
**************************************************
StcDrvClear() - spirent/stc_drv_clear.py
**************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcDrvClear() clears Dynamic Result View (DRV) results on a 
set of Spirent ports.

It generates Ansible task instances conformant with Spirent's
Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run the playbook generated by StcDrvClear(),
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_drv_clear.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_drv_clear.py>`_

Properties
----------

====================================    ==================================================
Property                                Description
====================================    ==================================================
port_list                               List of Spirent port references on which to clear
                                        Dynamic Result View results::

                                            - Type: str()
                                            - Spirent name: PortList
                                            - Default: ref:/port
                                            - Examples:
                                                - task.port_list = 'ref:/port'

====================================    ==================================================

'''
class StcDrvClear(Task):
    def __init__(self, task_log):
        ansible_module = 'stc'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.stc_properties_set = set()
        self.stc_properties_set.add('port_list')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.stc_properties_set)

        # used in self.update() to map between this class's property names
        # and Spirent's property names. This dict() is keyed on the items in
        # self.stc_properties_set, and MUST contain all of these items.
        self.property_map = dict()
        self.property_map['port_list'] = 'PortList'

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.stc_properties_set:
            self.properties[p] = None

    def final_verification(self):
        if self.properties['port_list'] == None:
            self.properties['port_list'] = 'ref:/port'

    def commit(self):
        self.update()
    def update(self):
        '''
        Call self.final_verification()
        Populate self.ansible_task dict() which is required by Playbook()
        '''
        self.final_verification()
        d = dict()
        d['action'] = 'perform'
        d['command'] = 'ResultsClearAll'
        d['properties'] = dict()
        for p in self.stc_properties_set:
            stc_property_name = self.property_map[p]
            d['properties'][stc_property_name] = self.properties[p]

        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    @property
    def port_list(self):
        return self.properties['port_list']
    @port_list.setter
    def port_list(self, x):
        parameter = 'port_list'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
