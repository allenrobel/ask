**************************************
NxosHsrpInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosHsrpInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_hsrp_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_hsrp_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_hsrp_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_hsrp_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_hsrp_interfaces.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
name                                Full name of the interface::

                                        - Type: str()
                                        - Example:
                                            task.name = 'Ethernet1/1'
                                        - Required

bfd                                 Enable/Disable HSRP Bidirectional Forwarding
                                    Detection (BFD) on the interface::

                                        - Type: str()
                                        - Valid values:
                                            - disable
                                            - enable
                                        - Example:
                                            task.bfd = 'enable'

state                               Desired state of hsrp attributes on
                                    ``name`` interface::

                                        - Type: str()
                                        - Valid values:
                                            - deleted
                                            - gathered
                                            - merged
                                            - overridden
                                            - parsed
                                            - rendered
                                            - replaced
                                        - Example:
                                            task.state = 'enabled'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'Vlan10 HSRP BFD'
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
