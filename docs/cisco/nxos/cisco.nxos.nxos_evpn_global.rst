**************************************
NxosEvpnGlobal()
**************************************

.. contents::
   :local:
   :depth: 1

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
