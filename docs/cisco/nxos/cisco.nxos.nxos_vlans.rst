***************************
NxosVlans() - nxos_vlans.py
***************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVlans() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vlans <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vlans_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vlans.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vlans.py>`_

Properties
----------

- Property names are identical to the cisco.nxos.nxos_vlans module, with the exception of:

========================    ===========
Ansible                     ScriptKit
========================    ===========
state                       vlan_state
========================    ===========

- NOTE: ``state`` above refers to the config dictionary.  Task ``state`` property is the same for both Ansible and ScriptKit.

========================    ===========
Property                    Description
========================    ===========
enabled                     Manage administrative state of the vlan.::

                                - Type: str()
                                - Valid values: no, yes
mapped_vni                  The Virtual Network Identifier (VNI) ID that is mapped to the VLAN::

                                - Type: int() or str()
                                - Valid values: int() range: 4096-16773119 or keyword 'default'
mode                        Set VLAN mode to classical ethernet or fabricpath.
                            This is a valid option for Nexus 5000, Nexus 6000, and Nexus 7000::

                                - Type: str()
                                - Valid values: ce, fabricpath 
name                        Name of VLAN::

                                - Type: str()
                                - Valid values: str()
state                       The state of the configuration after module completion. The state overridden would 
                            override the configuration of all the VLANs on the device (including VLAN 1) with
                            the provided configuration in the task. Use caution with this state.::

                                - Type: str()
                                - Valid values: deleted, gathered, merged, overridden, parsed, rendered, replaced

vlan_state                  Manage operational state of the vlan::

                                - Type: str()
                                - Valid values: active, suspend
vlan_id                     VLAN ID::

                                - Type: int()
                                - Valid values: int() range: 1-4094
                                - Required
========================    ===========

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
