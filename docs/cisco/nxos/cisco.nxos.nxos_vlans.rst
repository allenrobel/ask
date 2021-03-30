**************************************
NxosVlans()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
108

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
Method                      Description
========================    ============================================
add_vlan()                  Perform validation on the currently-set vlan
                            properties, and commit to the vlan list::

                                - Type: function()
                                - Example:
                                    # For full script, see ScriptKit Example above
                                    task = NxosVlans(log)
                                    task.append_to_task_name('Enable vlans')
                                    vlans = [10, 20]
                                    vnis = [10010, 10020]
                                    for vlan_id,mapped_vni in zip(vlans, vnis):
                                        task.enabled = True
                                        task.mapped_vni = mapped_vni
                                        task.vlan_state = 'active'
                                        task.vlan_id = vlan_id
                                        task.append_to_task_name(task.vlan_id)
                                        task.add_vlan()
                                    task.state = 'merged'
                                    task.commit()
                                    pb.add_task(task)

                                - Resulting playbook task:

                                    tasks:
                                    -   cisco.nxos.nxos_vlans:
                                            config:
                                            -   enabled: true
                                                mapped_vni: 10010
                                                state: active
                                                vlan_id: 10
                                            -   enabled: true
                                                mapped_vni: 10020
                                                state: active
                                                vlan_id: 20
                                            state: merged
                                        name: '[cisco.nxos.nxos_vlans : v.109], Enable vlans, 10, 20'

commit()                    Perform final verification and commit the 
                            current task::
                                - Type: function()
                                - Alias: update()
                                - Example - see add_vlan()

========================    ============================================

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

