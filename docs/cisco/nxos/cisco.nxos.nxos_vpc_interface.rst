******************************************
NxosVpcInterface() - nxos_vpc_interface.py
******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVpcInterface() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vpc_interface <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vpc_interface_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vpc_interface.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vpc_interface.py>`_

Properties
----------

- Property names are identical to the cisco.nxos.nxos_vpc_interface module.

========================    ===========
Property                    Description
========================    ===========
peer_link                   Set to true/false for peer link config on associated portchannel.::

                                - Type: str()
                                - Valid values: no, yes
                                - Example: task.peer_link = 'no'
portchannel                 Group number of the portchannel that will be configured::

                                - Type: str()
                                - Valid values: int() range: 1-4096
                                - Example: task.portchannel = 10
                                - Required
state                       The state of the configuration after module completion. The state overridden would 
                            override the configuration of all the VLANs on the device (including VLAN 1) with
                            the provided configuration in the task. Use caution with this state.::

                                - Type: str()
                                - Valid values: deleted, gathered, merged, overridden, parsed, rendered, replaced
                                - Example: task.state = 'merged'

vpc                         VPC group/id that will be configured on associated portchannel::

                                - Type: int()
                                - Valid values: int() range: 1-4096
                                - Example: task.vpc = 10
========================    ===========

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
