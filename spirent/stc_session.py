# StcSession() - spirent/stc_session.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
******************************
StcSession() - stc_session.py
******************************

ScriptKit Synopsis
------------------

StcSession() generates Ansible Playbook tasks using stc_session
which can be fed to AnsPlaybook().add_task()

Example usage:

**************************************************
StcSession() - spirent/stc_session.py
**************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcSession() creates a session with a Spirent LabServer. 

It generates Ansible task instances conformant with Spirent's
Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

Caveats
-------

1.  Sessions currently cannot be deleted using Ansible.  This is
    a current limitation of Spirent's Ansible implementation.
    To delete a session, use the Session Manager GUI. 

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run the playbook generated by StcSession(),
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_session.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_session.py>`_

Properties
----------

====================================    ==================================================
Property                                Description
====================================    ==================================================
chassis                                 IP address of one or more Spirent chassis.  If more
                                        than one, they should be space separated.  This can
                                        also be an Ansible variable.::

                                            - Type: str()
                                            - Valid values: One or more space-separated ipv4 addresses
                                                            Ansible variable
                                            - Default: '{{ hostvars[inventory_hostname].chassis }}'
                                            - Spirent name: chassis
                                            - Examples:
                                                - task.chassis = '10.1.1.2'
                                                - task.chassis = '10.1.1.2 10.1.1.3'
                                                - task.chassis = '{{ hostvars[inventory_hostname].chassis }}'
                                            In the last case above, your inventory yaml file might look like:

                                                ---
                                                labserver:
                                                  hosts:
                                                    labserver-2001:
                                                        ansible_host: 10.1.1.1
                                                        chassis: "10.1.1.2 10.1.1.3"

command                                 Create or delete the session::

                                            - Type: str()
                                            - Valid values: create, delete
                                            - Spirent name: none
                                            - Examples:
                                                - task.command = 'create'
                                            - NOTE: delete is not currently supported.

kill_existing                           If the session exists, destroy it before creating it.::

                                            - Type: bool()
                                            - Valid values: True, False
                                            - Default: False
                                            - Spirent name: kill_existing
                                            - Examples:
                                                - task.kill_existing = True

name                                    Name of the session.::

                                            - Type: str()
                                            - Spirent name: name
                                            - Examples:
                                                - task.name = 'my_session'

reset_existing                          If the session exists, reset it.::

                                            - Type: bool()
                                            - Valid values: True, False
                                            - Default: False
                                            - Spirent name: reset_existing
                                            - Examples:
                                                - task.reset_existing = True
                                            - TODO: Add a definition of 'reset'

user                                    Username for the session.::

                                            - Type: str()
                                            - Spirent name: user
                                            - Examples:
                                                - task.user = 'Administrator'

====================================    ==================================================

'''
class StcSession(Task):
    def __init__(self, task_log):
        ansible_module = 'stc'
        super().__init__(ansible_module, task_log)
        self._version = our_version
        self.class_name = __class__.__name__

        self.action = 'session'

        self.stc_properties_set = set()
        self.stc_properties_set.add('command')
        self.stc_properties_set.add('chassis')
        self.stc_properties_set.add('kill_existing')
        self.stc_properties_set.add('name')
        self.stc_properties_set.add('reset_existing')
        self.stc_properties_set.add('user')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.stc_properties_set)
        self.scriptkit_properties.add('action')

        # used in self.update() to map between this class's property names
        # and Spirent's property names. This dict() is keyed on the items in
        # self.stc_properties_set, and MUST contain all of these items.
        self.property_map = dict()
        self.property_map['command'] = 'command'
        self.property_map['chassis'] = 'chassis'
        self.property_map['kill_existing'] = 'kill_existing'
        self.property_map['name'] = 'name'
        self.property_map['reset_existing'] = 'reset_existing'
        self.property_map['user'] = 'user'

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.stc_properties_set:
            self.properties[p] = None

    def final_verification(self):
        if self.command == 'delete':
            self.task_log.error('exiting. delete is not currently supported for instance.command')
            exit(1)
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.commit()')
            exit(1)
        if self.user == None:
            self.task_log.error('exiting. call instance.user before calling instance.commit()')
            exit(1)
        if self.command == None:
            self.command = 'create'
        if self.chassis == None:
            self.chassis = "{{ hostvars[inventory_hostname].chassis }}"

    def commit(self):
        self.update()
    def update(self):
        '''
        Call self.final_verification()
        Populate self.ansible_task dict() which is required by Playbook()
        '''
        self.final_verification()
        d = dict()
        if self.command == 'create':
            d['action'] = self.action
        d['chassis'] = self.chassis
        d['name'] = self.name
        d['user'] = self.user
        if self.kill_existing != None:
            d['kill_existing'] = self.kill_existing
        if self.reset_existing != None:
            d['reset_existing'] = self.reset_existing
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    @property
    def command(self):
        return self.properties['command']
    @command.setter
    def command(self, x):
        parameter = 'command'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def chassis(self):
        return self.properties['chassis']
    @chassis.setter
    def chassis(self, x):
        parameter = 'chassis'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def kill_existing(self):
        return self.properties['kill_existing']
    @kill_existing.setter
    def kill_existing(self, x):
        parameter = 'kill_existing'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
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
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def user(self):
        return self.properties['user']
    @user.setter
    def user(self, x):
        parameter = 'user'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
