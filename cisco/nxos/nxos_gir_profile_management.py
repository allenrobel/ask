# NxosGirProfileManagement() - cisco/nxos/nxos_gir_profile_management.py
our_version = 101
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosGirProfileManagement()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
101

Status
------

- BETA

- This library is in development and not yet fully-tested.
- See TODO below for missing functionality.

TODO
----

1. Basic testing complete, but needs more testing before moving to Supported state

ScriptKit Synopsis
------------------
- NxosGirProfileManagement() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_gir_profile_management
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_gir_profile_management <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_gir_profile_management_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_gir_profile_management.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_gir_profile_management.py>`_

|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task.::

                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See also: ScriptKit Example above
                                    #!/usr/bin/env python3
                                    from ask.common.playbook import Playbook
                                    from ask.common.log import Log
                                    from ask.cisco.nxos.nxos_gir_profile_management import NxosGirProfileManagement

                                    log_level_console = 'INFO'
                                    log_level_file = 'DEBUG'
                                    log = Log('my_log', log_level_console, log_level_file)

                                    pb = Playbook(log)
                                    pb.profile_nxos()
                                    pb.ansible_password = 'mypassword'
                                    pb.name = 'nxos_gir_profile_management example'
                                    pb.add_host('dc-101')
                                    pb.file = '/tmp/nxos_gir_profile_management.yaml'

                                    commands = list()
                                    commands.append('router ospf 1')
                                    commands.append('isolate')
                                    task = NxosGirProfileManagement(log)
                                    task.commands = commands
                                    task.mode = 'maintenance'
                                    task.state = 'present'
                                    task.task_name = 'gir mode {} state {}'.format(task.mode, task.state)
                                    task.commit()

                                    pb.add_task(task)
                                    pb.append_playbook()
                                    pb.write_playbook()
                                    log.info('wrote {}'.format(pb.file))

                                - Resulting tasks:

                                    hosts: dc-101
                                    name: nxos_gir_profile_management example
                                    tasks:
                                    -   cisco.nxos.nxos_gir_profile_management:
                                            commands:
                                            - router ospf 1
                                            - isolate
                                            mode: maintenance
                                            state: present
                                        name: gir mode maintenance state present

========================    ============================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
commands                            List of commands to be included into the profile::

                                        - Type: list()
                                        - Example:
                                            commands = list()
                                            commands.append('router ospf 1')
                                            commands.append('isolate')
                                            task.commands = commands
                                        - Required

mode                                Configure the profile as Maintenance or Normal mode::

                                        - Type: str()
                                        - Valid values:
                                            - maintenance
                                            - normal
                                        - Example:
                                            task.mode = 'maintenance'
                                        - Required

state                               Desired state of ``feature``::

                                        - Type: str()
                                        - Valid values:
                                            - absent
                                            - present
                                        - Example:
                                            task.state = 'present'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'configure gir'
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''
class NxosGirProfileManagement(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_gir_profile_management'
        super().__init__(ansible_module, task_log)
        self._version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('commands')
        self.properties_set.add('mode')
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_gir_profile_management_valid_mode = set()
        self.nxos_gir_profile_management_valid_mode.add('maintenance')
        self.nxos_gir_profile_management_valid_mode.add('normal')

        self.nxos_gir_profile_management_valid_state = set()
        self.nxos_gir_profile_management_valid_state.add('absent')
        self.nxos_gir_profile_management_valid_state.add('present')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.mode == None:
            self.task_log.error('exiting. call instance.mode before calling instance.commit()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
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
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def nxos_gir_profile_management_verify_mode(self, x, parameter='mode'):
        verify_set = self.nxos_gir_profile_management_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_gir_profile_management_verify_mode'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_gir_profile_management_verify_state(self, x, parameter='state'):
        verify_set = self.nxos_gir_profile_management_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_gir_profile_management_verify_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def commands(self):
        return self.properties['commands']
    @commands.setter
    def commands(self, x):
        parameter = 'commands'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.nxos_gir_profile_management_verify_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.nxos_gir_profile_management_verify_state(x, parameter)
        self.properties[parameter] = x
