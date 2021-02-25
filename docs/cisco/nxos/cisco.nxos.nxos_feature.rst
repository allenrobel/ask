**************************************
NxosFeature()
**************************************

.. contents::
   :local:
   :depth: 1

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
