**************************************
NxosVpcInterface()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosVpcInterface() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_vpc_interface
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vpc_interface <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vpc_interface_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vpc_interface.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vpc_interface.py>`_


|

========================    ==============================================
Property                    Description
========================    ==============================================
peer_link                   Set to True (enable) or False (disable) to
                            configure VPC Peer Link on the associated
                            portchannel interface::

                                - Type: bool()
                                - Valid values:
                                    - False
                                    - True
                                - Example:
                                    task.peer_link = False

portchannel                 Group number of the portchannel that will be
                            configured::

                                - Type: int()
                                - Valid values:
                                    - range: 1-4096
                                - Example:
                                    task.portchannel = 10
                                - Required


vpc                         VPC group/id that will be configured on associated portchannel::

                                - Type: int()
                                - Valid values:
                                    - range: 1-4096
                                - Example:
                                    task.vpc = 10

state                       Desired state after task completion::

                                - Type: str()
                                - Valid values:
                                    - absent
                                    - present
                                - Example:
                                    task.state = 'present'
                                - Required

task_name                   Name of the task. Ansible will display this
                            when the playbook is run::

                                - Type: str()
                                - Example:
                                    - task.task_name = 'my task'
                                        
========================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
