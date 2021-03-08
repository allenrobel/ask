**************************************
NxosVlans()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosVlans() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_vlans
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vlans <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vlans_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vlans.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vlans.py>`_


|

========================    ============================================
Property                    Description
========================    ============================================
enabled                     Manage administrative state of the vlan.::

                                - Type: bool()
                                - Valid values:
                                    - False
                                    - True
                                - Example:
                                    task.enabled = True

mapped_vni                  The Virtual Network Identifier (VNI) ID that
                            is mapped to the VLAN::

                                - Type: int() or str()
                                - Valid values:
                                    - range: 4096-16773119
                                    - keyword: default
                                - Examples:
                                    task.mapped_vni = 20200
                                    task.mapped_vni = 'default'

mode                        Set VLAN mode to classical ethernet or fabricpath.
                            This is a valid option for Nexus 5000, Nexus 6000,
                            and Nexus 7000::

                                - Type: str()
                                - Valid values:
                                    - ce   (classic ethernet)
                                    - fabricpath
                                - Example:
                                    task.mode = 'ce'

name                        Name of VLAN::

                                - Type: str()
                                - Example:
                                    task.name = 'ENG'

state                       The state of the configuration after module completion.
                            The state ``overridden`` would override the configuration
                            of all the VLANs on the device (including VLAN 1) with
                            the provided configuration in the task. Use caution
                            with this state.::

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
                                    task.state = 'merged'

vlan_state                  Manage operational state of the vlan::

                                - Type: str()
                                - Valid values:
                                    - active
                                    - suspend
                                - Example:
                                    task.vlan_state = 'active'

vlan_id                     VLAN ID::

                                - Type: int()
                                - Valid values:
                                    - range: 1-4094
                                - Example:
                                    task.vlan_id = 400
                                - Required

========================    ============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
