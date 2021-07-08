**************************************
NxosVtpPassword()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
100

ScriptKit Synopsis
------------------
- NxosVtpPassword() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_vtp_password
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vtp_password <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vtp_password_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vtp_password.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vtp_password.py>`_


|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task::

                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See ScriptKit Example above 

========================    ============================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
state                               Manage the state of the resource::

                                        - Type: str()
                                        - Valid values:
                                            - absent
                                            - present
                                        - Example:
                                            task.state = 'present'
                                        - Required

vtp_password                        VTP password::

                                        - Type: str()
                                        - Examples:
                                            task.vtp_password = 'my_vtp_password'
                                        - Required if state == present

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

