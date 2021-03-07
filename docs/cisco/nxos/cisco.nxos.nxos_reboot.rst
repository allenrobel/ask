**************************************
NxosReboot()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosReboot() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_reboot
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_reboot <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_reboot_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_reboot.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_reboot.py>`_

|

================================    ==============================================
Property                            Description
================================    ==============================================
confirm                             Set to true if you're sure you want to reboot::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Default: False

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'my task'

================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
