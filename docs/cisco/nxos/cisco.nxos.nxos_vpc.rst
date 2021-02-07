******************************************
NxosVpc() - nxos_vpc.py
******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVpc() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vpc <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vpc_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vpc.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vpc.py>`_

Properties
----------

- Property names are identical to the cisco.nxos.nxos_vpc module.

============================    ===========
Property                        Description
============================    ===========
auto_recovery                   Enables/Disables auto recovery on platforms that support disable
                                timers are not modifiable with this attribute
                                mutually exclusive with auto_recovery_reload_delay::

                                    - Type: bool()
                                    - Valid values: no, yes
                                    - Example: task.auto_recovery = 'no'
auto_recovery_reload_delay      Group number of the portchannel that will be configured::

                                    - Type: str()
                                    - Valid values: int() range: 1-4096
                                    - Example: task.portchannel = 10
                                    - Required
delay_restore                   Delay in bringing up the vPC links (in seconds).
                                NxosVpc() converts this to str() prior to adding to the playbook::

                                    - Type: int() converted to str()
                                    - Valid values: int() range: 1-3600
                                    - Example: task.delay_restore = 300
delay_restore_interface_vlan    Delay in bringing-up interface-vlan, in seconds.
                                NxosVpc() converts this to str() prior to adding to the playbook::

                                    - Type: int() converted to str()
                                    - Valid values: int() range: 1-3600
                                    - Example: task.delay_restore_interface_vlan = 150
delay_restore_orphan_port       vPC orphan-port delay bring-up timer, in seconds.
                                NxosVpc() converts this to str() prior to adding to the playbook::

                                    - Type: int() converted to str()
                                    - Valid values: int() range: 0-300
                                    - Example: task.delay_restore_orphan_port = 150
domain                          vPC domain.
                                NxosVpc() converts this to str() prior to adding to the playbook::

                                    - Type: int() converted to str()
                                    - Valid values: int() range: 1-1000
                                    - Example: task.domain = 1
peer_gw                         Enables/Disables peer gateway::

                                    - Type: bool()
                                    - Valid values: no, yes
                                    - Example: task.peer_gw = 'yes'
pkl_dest                        Destination (remote) IP address used for peer keepalive link.
                                pkl_dest is required whenever pkl options are used::

                                    - Type: str()
                                    - Valid values: ipv4 address without prefix
                                    - Example: task.pkl_dest = '1.1.1.2'
pkl_src                         Source IP address used for peer keepalive link::

                                    - Type: str()
                                    - Valid values: ipv4 address without prefix
                                    - Example: task.pkl_src = '1.1.1.1'
pkl_vrf                         VRF used for peer keepalive link.
                                The VRF must exist on the device before using pkl_vrf.
                                (Note) 'default' is an overloaded term: Default vrf 
                                context for pkl_vrf is 'management'; 'pkl_vrf: default'
                                refers to the literal 'default' rib.::

                                    - Type: str()
                                    - Valid values: vrf name
                                    - Example: task.pkl_vrf = 'myVrf'
role_priority                   Priority to be used during vPC role (primary/secondary) election.
                                Lower value will become vpc primary::

                                    - Type: int()
                                    - Valid values: int() range: 1-65535
                                    - Example: task.role_priority = 100

state                           The state of the configuration after module completion.::

                                - Type: str()
                                - Valid values: absent, present
                                - Example: task.state = 'present'

system_priority                 System device priority. Value must match on both vpc peers.::

                                - Type: int()
                                - Valid values: int() range: 1-65535
                                - Example: task.system_priority = 2000
============================    ===========

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
