*************************
NxosVlan() - nxos_vlan.py
*************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVlan() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Deprecation
-----------
NxosVlan() is deprecated and will be removed after 2022-06-01.  Use NxosVlans() instead.

Ansible Module Documentation
----------------------------
- `nxos_vlan <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vlan.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vlan.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vlan.py>`_

Properties
----------

- Property names are identical to the nxos_vlan module.
- aggregate is not accessed directly by the user when using ScriptKit.
    - Rather, use the NxosVlan().add_vlan() method to add vlans to the aggregate list.  Then call NxosVlan().update()
    - See the ScriptKit Example at the link above for an example of this.

========================    ===========
Property                    Description
========================    ===========
admin_state                 Manage the VLAN administrative state of the VLAN.
                            Equivalent to shut/no shut in VLAN config mode::

                                - Type: str()
                                - Valid values: up, down
aggregate                   List of VLAN definitions.
                            This property is not accessed directly.
                            Use ScriptKit's add_vlan() method to populate the aggregate list().
                            If add_vlan() is not called prior to update(), then the task will contain
                            a single vlan and aggregate is not used.
associated_interfaces       This is a intent option and checks the operational state of the
                            or given vlan name for associated interfaces. If the value in the
                            associated_interfaces does not match with the operational state of
                            vlan interfaces on device it will result in failure::

                                - Type: list() of interface names
delay                       Time in seconds to wait before checking for the opertational state
                            on remove device::

                                - Type: int()
                                - Default: 10
interfaces                  Interfaces associated with vlan_id::

                                - Type: list() or str()
                                - Valid values: list() of interface names, or keyword 'default'
mapped_vni                  The Virtual Network Identifier (VNI) ID that is mapped to the VLAN::

                                - Type: int() or str()
                                - Valid values: int() range: 4096-16773119 or keyword 'default'
mode                        Set VLAN mode to classical ethernet or fabricpath.
                            This is a valid option for Nexus 5000::

                                - Type: str()
                                - Valid values: ce, fabricpath 
name                        Name of VLAN::

                                - Type: str()
                                - Valid values: str() or keyword 'default'
state                       Manage the state of the resource::

                                - Type: str()
                                - Valid values: absent, present
vlan_id                     Single VLAN ID::

                                - Type: int()
                                - Valid values: int() range: 1-4094
                                - Required
vlan_range                  Range of VLANs::

                                - Type: str()
                                - Valid values: NX-OS vlan range string e.g. 2-10 or 2,5,10-15
vlan_state                  Manage the vlan operational state of the VLAN::

                                - Type: str()
                                - Valid values: active, suspend
========================    ===========


Authors
~~~~~~~

- Allen Robel (@PacketCalc)
