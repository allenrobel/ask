# NxosGir() - cisco/nxos/nxos_gir.py
our_version = 100
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosGir()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
100

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
- NxosGir() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_gir
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_gir <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_gir_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_gir.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_gir.py>`_

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
                                    from ask.cisco.nxos.nxos_gir import NxosGir

                                    log_level_console = 'INFO'
                                    log_level_file = 'DEBUG'
                                    log = Log('my_log', log_level_console, log_level_file)

                                    pb = Playbook(log)
                                    pb.profile_nxos()
                                    pb.ansible_password = 'mypassword'
                                    pb.name = 'nxos_gir example'
                                    pb.add_host('dc-101')
                                    pb.file = '/tmp/nxos_gir.yaml'

                                    task = NxosGir(log)
                                    task.system_mode_maintenance = True
                                    task.state = 'present'
                                    task.task_name = 'gir isolate state {}'.format(task.state)
                                    task.commit()

                                    pb.add_task(task)
                                    pb.append_playbook()
                                    pb.write_playbook()
                                    log.info('wrote {}'.format(pb.file))

                                - Resulting tasks:

                                    hosts: dc-101
                                    name: nxos_gir example
                                    tasks:
                                    -   cisco.nxos.nxos_gir:
                                            system_mode_maintenance: true
                                            state: present
                                        name: gir isolate state present

========================    ============================================

|

================================================    ==============================================
Property                                            Description
================================================    ==============================================
state                                               Desired state::

                                                        - Type: str()
                                                        - Valid values:
                                                            - absent
                                                            - present
                                                        - Example:
                                                            task.state = 'present'
                                                        - Required

system_mode_maintenance                             If True, place all enabled protocols into 
                                                    maintenance mode (using the isolate command).
                                                    If False, place all enabled protocols into
                                                    normal mode (using the no isolate command).::

                                                        - Type: bool()
                                                        - Valid values:
                                                            - True
                                                            - False
                                                        - Example:
                                                            task.system_mode_maintenance = True
                                                        - NOTES
                                                            1. Mutually-exclusive with system_mode_maintenance_dont_generate_profile

system_mode_maintenance_dont_generate_profile       If True, prevents the dynamic searching
                                                    of enabled protocols and executes commands
                                                    configured in a maintenance-mode profile.
                                                    Use this option if you want the system to
                                                    use a maintenance-mode profile that you
                                                    have created.
                                                    If False, prevents the dynamic searching of
                                                    enabled protocols and executes commands
                                                    configured in a normal-mode profile. Use
                                                    this option if you want the system to use a
                                                    normal-mode profile that you have created.::

                                                        - Type: bool()
                                                        - Valid values:
                                                            - True
                                                            - False
                                                        - Example:
                                                            task.system_mode_maintenance_dont_generate_profile = True
                                                        - NOTES
                                                            1. Mutually-exclusive with system_mode_maintenance

system_mode_maintenance_on_reload_reset_reason      Boots the switch into maintenance mode
                                                    automatically in the event of a specified
                                                    system crash. Note that not all reset reasons
                                                    are applicable for all platforms. Also if reset reason is set to match_any, it is not idempotent as it turns on all reset reasons. If reset reason is match_any and state is absent, it turns off all the reset reasons.

                                                        - Type: str()
                                                        - Valid values:
                                                            - hw_error
                                                            - svc_failure
                                                            - kern_failure
                                                            - wdog_timeout
                                                            - fatal_error
                                                            - lc_failure
                                                            - match_any
                                                            - manual_reload
                                                            - any_other
                                                            - maintenance
                                                        - Example:
                                                            task.system_mode_maintenance_on_reload_reset_reason = 'hw_error'

system_mode_maintenance_shutdown                    If True, shuts down all protocols, vPC
                                                    domains, and interfaces except the management
                                                    interface (using the shutdown command). This
                                                    option is disruptive while
                                                    system_mode_maintenance (which uses the
                                                    isolate command) is not.::

                                                        - Type: bool()
                                                        - Valid values:
                                                            - True
                                                            - False
                                                        - Example:
                                                            task.system_mode_maintenance_shutdown = True
                                                        - NOTES
                                                            1. Mutually-exclusive with system_mode_maintenance
                                                            2. Mutually-exclusive with system_mode_maintenance_dont_generate_profile

system_mode_maintenance_timeout                     Keeps the switch in maintenance mode for a
                                                    specified time period::

                                                        - Type: int()
                                                        - Valid values:
                                                            - range: 5-65535
                                                        - Units: minutes
                                                        - Example:
                                                            # Stay in maintenance mode for one hour
                                                            task.system_mode_maintenance_timeout = 60

task_name                                           Name of the task. Ansible will display this
                                                    when the playbook is run::

                                                        - Type: str()
                                                        - Example:
                                                            - task.task_name = 'configure gir'
                                        
============================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''
class NxosGir(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_gir'
        super().__init__(ansible_module, task_log)
        self._version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('state')
        self.properties_set.add('system_mode_maintenance')
        self.properties_set.add('system_mode_maintenance_dont_generate_profile')
        self.properties_set.add('system_mode_maintenance_on_reload_reset_reason')
        self.properties_set.add('system_mode_maintenance_shutdown')
        self.properties_set.add('system_mode_maintenance_timeout')

        self.mutex = dict()
        self.mutex['system_mode_maintenance'] = set()
        self.mutex['system_mode_maintenance'].add('system_mode_maintenance_dont_generate_profile')
        self.mutex['system_mode_maintenance'].add('system_mode_maintenance_shutdown')

        self.mutex['system_mode_maintenance_dont_generate_profile'] = set()
        self.mutex['system_mode_maintenance_dont_generate_profile'].add('system_mode_maintenance')
        self.mutex['system_mode_maintenance_dont_generate_profile'].add('system_mode_maintenance_shutdown')

        self.mutex['system_mode_maintenance_shutdown'] = set()
        self.mutex['system_mode_maintenance_shutdown'].add('system_mode_maintenance')
        self.mutex['system_mode_maintenance_shutdown'].add('system_mode_maintenance_dont_generate_profile')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.valid_system_mode_maintenance_on_reload_reset_reason = set()
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('hw_error')
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('svc_failure')
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('kern_failure')
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('wdog_timeout')
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('fatal_error')
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('lc_failure')
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('match_any')
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('manual_reload')
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('any_other')
        self.valid_system_mode_maintenance_on_reload_reset_reason.add('maintenance')

        self.nxos_gir_valid_state = set()
        self.nxos_gir_valid_state.add('absent')
        self.nxos_gir_valid_state.add('present')

        self.system_mode_maintenance_timeout_min = 5
        self.system_mode_maintenance_timeout_max = 65535

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        for p in self.mutex:
            for mp in self.mutex[p]:
                if self.properties[p] != None and self.properties[mp] != None:
                    self.task_log.error('exiting. {} is mutually-exclusive with {}'.format(p, mp))
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

    def nxos_gir_verify_system_mode_maintenance_on_reload_reset_reason(self, x, parameter='system_mode_maintenance_on_reload_reset_reason '):
        verify_set = self.valid_system_mode_maintenance_on_reload_reset_reason
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_gir_verify_system_mode_maintenance_on_reload_reset_reason'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_gir_verify_system_mode_maintenance_timeout(self, x, parameter='system_mode_maintenance_timeout'):
        source_class = self.class_name
        range_min = self.system_mode_maintenance_timeout_min
        range_max = self.system_mode_maintenance_timeout_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def nxos_gir_verify_state(self, x, parameter='state'):
        verify_set = self.nxos_gir_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_gir_verify_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def system_mode_maintenance(self):
        return self.properties['system_mode_maintenance']
    @system_mode_maintenance.setter
    def system_mode_maintenance(self, x):
        parameter = 'system_mode_maintenance'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def system_mode_maintenance_dont_generate_profile(self):
        return self.properties['system_mode_maintenance_dont_generate_profile']
    @system_mode_maintenance_dont_generate_profile.setter
    def system_mode_maintenance_dont_generate_profile(self, x):
        parameter = 'system_mode_maintenance_dont_generate_profile'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def system_mode_maintenance_on_reload_reset_reason(self):
        return self.properties['system_mode_maintenance_on_reload_reset_reason']
    @system_mode_maintenance_on_reload_reset_reason.setter
    def system_mode_maintenance_on_reload_reset_reason(self, x):
        parameter = 'system_mode_maintenance_on_reload_reset_reason'
        if self.set_none(x, parameter):
            return
        self.nxos_gir_verify_system_mode_maintenance_on_reload_reset_reason(x, parameter)
        self.properties[parameter] = x

    @property
    def system_mode_maintenance_shutdown(self):
        return self.properties['system_mode_maintenance_shutdown']
    @system_mode_maintenance_shutdown.setter
    def system_mode_maintenance_shutdown(self, x):
        parameter = 'system_mode_maintenance_shutdown'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def system_mode_maintenance_timeout(self):
        return self.properties['system_mode_maintenance_timeout']
    @system_mode_maintenance_timeout.setter
    def system_mode_maintenance_timeout(self, x):
        parameter = 'system_mode_maintenance_timeout'
        if self.set_none(x, parameter):
            return
        self.nxos_gir_verify_system_mode_maintenance_timeout(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.nxos_gir_verify_state(x, parameter)
        self.properties[parameter] = x
