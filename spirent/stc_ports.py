# StcPorts() - spirent/stc_ports.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
*******************************************
StcPorts() - spirent/stc_ports.py
*******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcPorts() generates Ansible task instances conformant with Spirent's
Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

StcPorts() creates and/or deletes Spirent ports.

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run the playbook generated by StcPorts(),
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_ports.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_ports.py>`_

====================================    ==================================================
Property /Method                        Description
====================================    ==================================================
action                                  Create or delete Spirent ports::

                                            - Type: str()
                                            - Spirent name: action
                                            - Valid values: create, delete
                                            - Examples:
                                                - task.action = 'create'
                                            - Required

chassis                                 Chassis number, starting with 1.  For
                                        single-chassis, use 1.::

                                            - Type: int()
                                            - Spirent name: location
                                            - Examples:
                                                - task.chassis = 1
                                            - Required

module                                  Module number::

                                            - Type: int()
                                            - Spirent name: location
                                            - Examples:
                                                - task.module = 2
                                            - Required

port                                    Port number::

                                            - Type: int()
                                            - Spirent name: location
                                            - Examples:
                                                - task.port = 1
                                            - Required

name                                    Name/Handle for the port.  This will be used
                                        to refer to the port in other Spirent tasks,
                                        e.g. in StcPortControl() to attach/detach ports.
                                        If not set, a default port handle is assigned
                                        with the following format:

                                            StcC/M/P where:
                                               C - Chassis (from task.chassis)
                                               M - Module  (from task.module)
                                               P - Port    (from task.port)

                                        For example:

                                            Stc1/2/3, chassis 1, module 2, port 3::

                                            - Type: str()
                                            - Spirent name: name
                                            - Default: Stc/C/M/P
                                                Where:
                                                    C = task.chassis
                                                    M = task.module
                                                    P = task.port
                                            - Examples:
                                                - task.name = 'MyPort1'

add_port()                              After setting task.chassis, task.module, and
                                        task.port, and optionally setting task.name, 
                                        call task.add_port().  This appends the port to a 
                                        list() in a format Spirent expects, and clears
                                        chassis, module, port so that you can set them
                                        again to add the next port.  Once all ports have
                                        been added, call task.action and task.update()
                                        to complete the task.

====================================    ==================================================

'''
class StcPorts(Task):
    def __init__(self, task_log):
        ansible_module = 'stc'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.port_list = list() # list() of dict(). Updated in self.add_port()

        self.properties = dict()
        self.properties['action'] = None

        # Don't include action in properties_set
        # since init_properties() gets called each 
        # time add_port() is called and we want action
        # to persist and apply for all ports in port_list.
        self.properties_set = set()
        self.properties_set.add('chassis')
        self.properties_set.add('module')
        self.properties_set.add('port')
        self.properties_set.add('name')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)
        self.scriptkit_properties.add('action')

        # used in self.update() to map between this class's property names
        # and Spirent's property names. This dict() is keyed on the items in
        # self.properties_set, and MUST contain all of these items.
        # property_map MAY contain other items in addition to those in properties_set
        self.property_map = dict()
        self.property_map['chassis']    = 'chassis'
        self.property_map['module']     = 'module'
        self.property_map['port']       = 'port'
        self.property_map['name']       = 'name'

        self.stc_ports_valid_action = set()
        self.stc_ports_valid_action.add('create')
        self.stc_ports_valid_action.add('delete')

        self.init_properties()

    def init_properties(self):
        for p in self.properties_set:
            self.properties[p] = None

    def final_verification(self):
        if len(self.port_list) == 0:
            self.task_log.error('exiting. call instance.add_port() at least once before calling instance.commit()')
            exit(1)
        if self.action == None:
            self.task_log.error('exiting. call instance.action before calling instance.commit()')
            exit(1)


    def commit(self):
        self.update()
    def update(self):
        '''
        Call self.final_verification()
        Populate self.ansible_task dict() which is required by Playbook()
        '''
        self.final_verification()

        d = dict()
        d['action'] = self.action
        self.ansible_task = dict()

        project = dict()
        project['project'] = deepcopy(self.port_list)
        d['objects'] = list()
        d['objects'].append(deepcopy(project))

        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def port_verification(self):
        if self.chassis == None:
            self.task_log.error('exiting. call instance.chassis before calling instance.add_port()')
            exit(1)
        if self.module == None:
            self.task_log.error('exiting. call instance.module before calling instance.add_port()')
            exit(1)
        if self.port == None:
            self.task_log.error('exiting. call instance.port before calling instance.add_port()')
            exit(1)
        if self.name == None:
            self.name = 'Stc{}/{}/{}'.format(self.chassis, self.module, self.port)
    def add_port(self):
        self.port_verification()
        d = dict()
        d['port'] = dict()
        d['port']['name'] = self.name
        d['port']['location'] = self.make_location()
        self.port_list.append(deepcopy(d))
        self.init_properties()

    def make_location(self):
        return "//${chassis[" + self.chassis + "]}" + "/{}/{}".format(self.module, self.port)

    def verify_stc_ports_action(self, x, parameter='action'):
        verify_set = self.stc_ports_valid_action
        if x not in verify_set:
            source_method = 'verify_stc_ports_action'
            expectation = '{}'.format(', '.join(verify_set))
            self.fail(self.class_name, source_method, x, parameter, expectation)

    @property
    def action(self):
        return self.properties['action']
    @action.setter
    def action(self, x):
        parameter = 'action'
        if self.set_none(x, parameter):
            return
        self.verify_stc_ports_action(x, parameter)
        self.properties[parameter] = x

    @property
    def chassis(self):
        return self.properties['chassis']
    @chassis.setter
    def chassis(self, x):
        parameter = 'chassis'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def module(self):
        return self.properties['module']
    @module.setter
    def module(self, x):
        parameter = 'module'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def port(self):
        return self.properties['port']
    @port.setter
    def port(self, x):
        parameter = 'port'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

