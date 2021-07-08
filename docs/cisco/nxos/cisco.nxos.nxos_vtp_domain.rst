**************************************
NxosVtpDomain()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
100

ScriptKit Synopsis
------------------
- NxosVtpDomain() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_vtp_domain
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vtp_domain <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vtp_domain_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vtp_domain.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vtp_domain.py>`_


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
domain                              VTP domain name::

                                        - Type: str()
                                        - Examples:
                                            task.domain = 'domain1'
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

