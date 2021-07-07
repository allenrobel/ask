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

