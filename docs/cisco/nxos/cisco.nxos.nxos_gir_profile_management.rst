**************************************
NxosGirProfileManagement()
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
                                            feature: bgp
                                            state: enabled
                                        name: configure feature bgp

                                - Resulting config:

                                    feature bgp

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

