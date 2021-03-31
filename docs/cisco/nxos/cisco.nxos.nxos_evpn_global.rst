**************************************
NxosEvpnGlobal()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
107

ScriptKit Synopsis
------------------
- NxosEvpnGlobal() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_evpn_global
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_evpn_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_evpn_global_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_evpn_global.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_evpn_global.py>`_


|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task::
                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See also: ScriptKit Example above 

                                    #!/usr/bin/env python3
                                    # enable nv overlay evpn
                                    from ask.common.playbook import Playbook
                                    from ask.common.log import Log
                                    from ask.cisco.nxos.nxos_evpn_global import NxosEvpnGlobal

                                    log_level_console = 'INFO'
                                    log_level_file = 'DEBUG'
                                    log = Log('my_log', log_level_console, log_level_file)

                                    pb = Playbook(log)
                                    pb.profile_nxos()
                                    pb.ansible_password = 'mypassword'
                                    pb.name = 'nxos_evpn_global example'
                                    pb.add_host('dc-101')
                                    pb.file = '/tmp/nxos_evpn_global.yaml'

                                    task = NxosEvpnGlobal(log)
                                    task.nv_overlay_evpn = True
                                    task.task_name = 'configure nv overlay evpn'
                                    task.commit()

                                    pb.add_task(task)
                                    pb.append_playbook()
                                    pb.write_playbook()
                                    log.info('wrote {}'.format(pb.file))

                                - Resulting tasks:

                                    hosts: dc-101
                                    name: nxos_evpn_global example
                                    tasks:
                                    -   cisco.nxos.nxos_evpn_global:
                                            nv_overlay_evpn: true
                                        name: configure nv overlay evpn

                                - Resulting config:

                                    nv overlay evpn

========================    ============================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
nv_overlay_evpn                     Enable ``True`` / Disable ``False`` EVPN 
                                    control plane::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Examples:
                                            task.nv_overlay_evpn = True
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Examples:
                                            - task.task_name = 'my task'

================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

