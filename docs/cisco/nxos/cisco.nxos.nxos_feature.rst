**************************************
NxosFeature()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
109

ScriptKit Synopsis
------------------
- NxosFeature() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_feature
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_feature <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_feature_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_feature.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_feature.py>`_

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
                                    # enable feature bgp
                                    from ask.common.playbook import Playbook
                                    from ask.common.log import Log
                                    from ask.cisco.nxos.nxos_feature import NxosFeature

                                    log_level_console = 'INFO'
                                    log_level_file = 'DEBUG'
                                    log = Log('my_log', log_level_console, log_level_file)

                                    pb = Playbook(log)
                                    pb.profile_nxos()
                                    pb.ansible_password = 'mypassword'
                                    pb.name = 'nxos_feature example'
                                    pb.add_host('dc-101')
                                    pb.file = '/tmp/nxos_feature.yaml'

                                    task = NxosFeature(log)
                                    task.feature = 'bgp'
                                    task.state = 'enabled'
                                    task.task_name = 'configure feature {}'.format(task.feature)
                                    task.commit()

                                    pb.add_task(task)
                                    pb.append_playbook()
                                    pb.write_playbook()
                                    log.info('wrote {}'.format(pb.file))

                                - Resulting tasks:

                                    hosts: dc-101
                                    name: nxos_feature example
                                    tasks:
                                    -   cisco.nxos.nxos_feature:
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
feature                             Name of the feature to enable/disable::

                                        - Type: str()
                                        - Example:
                                            task.feature = 'lacp'
                                        - Required

state                               Desired state of ``feature``::

                                        - Type: str()
                                        - Valid values:
                                            - disabled
                                            - enabled
                                        - Example:
                                            task.state = 'enabled'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'enable lacp'
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

