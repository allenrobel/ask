# StcDeviceControl() - spirent/stc_device_control.py
our_version = 103
from copy import deepcopy
from ask.common.task import Task
'''
**************************************************
StcDeviceControl() - spirent/stc_device_control.py
**************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcDeviceControl() starts or stops sets of Spirent emulated devices.
It generates Ansible task instances conformant with Spirent's
Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run the playbook generated by StcDeviceControl(),
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_device_control.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_device_control.py>`_

Properties
----------

====================================    ==================================================
Property                                Description
====================================    ==================================================
command                                 Start or stop the set of emulated devices
                                        referenced by device_list::

                                            - Type: str()
                                            - Spirent name: command
                                            - Valid values: start, stop
                                            - Examples:
                                                - task.command = 'start'

device_list                             A Spirent ref pointing to one or more devices::

                                            - Type: str()
                                            - Spirent name: DeviceList
                                            - Default: ref:/project
                                                - Starts or stops all devices
                                            - Examples:
                                                - task.device_list = 'ref:/project'

====================================    ==================================================


'''
class StcDeviceControl(Task):
    def __init__(self, log):
        ansible_module = 'stc'
        super().__init__(ansible_module, log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.action = 'perform'

        self.stc_device_control_valid_command = set()
        self.stc_device_control_valid_command.add('start')
        self.stc_device_control_valid_command.add('stop')
        # see update()
        self.command_map = dict()
        self.command_map['start'] = 'DeviceStart'
        self.command_map['stop'] = 'DeviceStop'

        self.stc_properties_set = set()
        self.stc_properties_set.add('device_list')

        # used in self.update() to map between this class's property names
        # and Spirent's property names. This dict() is keyed on the items in
        # self.stc_properties_set, and MUST contain all of these items.
        self.property_map = dict()
        self.property_map['device_list'] = 'DeviceList'

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        self.properties['command'] = None
        self.properties['device_list'] = None

    def final_verification(self):
        if self.device_list == None:
            self.device_list = 'ref:/project'
        if self.command == None:
            self.task_log.error('exiting. Call instance.command before calling instance.update()')
            self.task_log.error('Valid values for command: {}'.format(','.join(self.stc_device_control_valid_command)))
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        d = dict()
        d['action'] = self.action
        d['command'] = self.command_map[self.command]
        d['properties'] = dict()
        for p in self.stc_properties_set:
            mapped_p = self.property_map[p]
            d['properties'][mapped_p] = self.properties[p]
        self.ansible_task = dict()
        self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def verify_stc_device_control_command(self, x, parameter):
        if x not in self.stc_device_control_valid_command:
            expectation = '{}'.format(', '.join(self.stc_device_control_valid_command))
            self.fail(self.class_name, parameter, x, parameter, expectation)

    @property
    def command(self):
        return self.properties['command']
    @command.setter
    def command(self, x):
        parameter = 'command'
        if self.set_none(x, parameter):
            return
        self.verify_stc_device_control_command(x, parameter)
        self.properties[parameter] = x

    @property
    def device_list(self):
        return self.properties['device_list']
    @device_list.setter
    def device_list(self, x):
        parameter = 'device_list'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x