**************************************
NxosInterface()
**************************************

.. contents::
   :local:
   :depth: 1

Deprecation
-----------

- Status: ``DEPRECATED``
- Alternative: `nxos_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_interfaces_module.rst>`_
- 2020-06-01, deprecation date
- 2022-06-01, removal date (module may be removed after this date)

ScriptKit Synopsis
------------------
- NxosInterface() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_interface
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_interface <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_interface_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_interface.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_interface.py>`_


|

====================================    ==============================================
Property                                Description
====================================    ==============================================
admin_state                             Administrative state of the interface::

                                            - Type: str()
                                            - Valid values:
                                                - down
                                                - up
                                            - Example:
                                                task.admin_state = 'down'

delay                                   Time in seconds to wait before checking for the
                                        operational state on remote device. This wait
                                        is applicable for operational state arguments::

                                            - Type: int()
                                            - Units: seconds
                                            - Default: 10
                                            - Example:
                                                task.delay = 20

description                             Interface description::

                                            - Type: str()
                                            - Example:
                                                task.description = 'Eth1/1 : peer 101.Eth2.1'

duplex                                  Interface duplex. Applicable for ethernet
                                        interface only::

                                            - Type: str()
                                            - Valid values:
                                                - auto
                                                - full
                                                - half
                                            - Example:
                                                task.duplex = 'full'

fabric_forwarding_anycast_gateway       Associate SVI with anycast gateway under
                                        VLAN configuration mode. Applicable for 
                                        SVI interface only::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Example:
                                                task.fabric_forwarding_anycast_gateway = True

interface_type                          Interface type to be unconfigured from the device::

                                            - Type: str()
                                            - Valid values:
                                                - loopback
                                                - nve
                                                - portchannel
                                                - svi
                                            - Example:
                                                task.interface_type = 'loopback'

ip_forward                              Enable/Disable ip forward feature on SVIs::

                                            - Type: str()
                                            - Valid values:
                                                - disable
                                                - enable
                                            - Example:
                                                task.ip_forward = 'disable'

mode                                    Manage Layer 2 or Layer 3 state of the interface. 
                                        Applicable for ethernet and portchannel interface
                                        only::

                                            - Type: str()
                                            - Valid values:
                                                - layer2
                                                - layer3
                                            - Example:
                                                task.mode = 'layer3'

mtu                                     Maximum transfer unit (MTU) for the interface.
                                        Applicable for ethernet interface only::

                                            - Type: int()
                                            - Valid values:
                                                - even int() range: 576-9216
                                            - Example:
                                                task.mtu = 9118

name                                    Full name of interface::

                                            - Type: str()
                                            - Examples:
                                                task.name = 'Ethernet1/1'
                                                task.name = 'port-channel22'

neighbor_host                           An LLDP neighbor that should be present if the
                                        interface is fully operational.  If this neighbor
                                        is not present, Ansible will declare the port down.
                                        Can be combined with neighbor_port::

                                            - Type: str()
                                            - Example:
                                                task.neighbor_host = 'foo_neighbor'
                                                task.add_neighbors()
                                            - See also: neighbor_port

neighbor_port                           An LLDP neighbor port name that should be present
                                        if the interface is fully operational.  If this
                                        port name is not present, Ansible will declare the
                                        port down.  Can be combined with neighbor_host::

                                            - Type: str()
                                            - Example:
                                                task.neighbor_port = 'Ethernet1/1'
                                                task.add_neighbors()
                                            - See also: neighbor_host

rx_rate                                 state_check only. Ansible will ensure ingress rate is
                                        at least ``rx_rate`` bps before declaring the interface
                                        up::

                                            - Type: int()
                                            - Units: bits per second (bps)
                                            - Example:
                                                task.rx_rate = 500000

speed                                   Interface link speed. Applicable for ethernet
                                        interface only.  Specifying speed will enable
                                        ``no negotiate auto`` (unless ``auto`` is used)::

                                            - Type: int() or str()
                                            - Valid values:
                                                  - 100     100Mb/s
                                                  - 1000    1Gb/s
                                                  - 10000   10Gb/s
                                                  - 100000  100Gb/s
                                                  - 200000  200Gb/s
                                                  - 25000   25Gb/s
                                                  - 40000   40Gb/s
                                                  - 400000  400Gb/s
                                                  - auto    Auto negotiate speed
                                            - Examples:
                                                task.speed = 40000
                                                task.speed = 'auto'
                                            - NOTES:
                                                - Different platforms will support different
                                                  values.  And certainly transceivers will
                                                  not support all values.  ScriptKit allows
                                                  any int() value, or 'auto' keyword.

state                                   Desired state after task has run::

                                            - Type: str()
                                            - Valid values:
                                                - absent
                                                - default
                                                - present
                                            - Example:
                                                task.state = 'present'
                                            - Required

task_name                               Name of the task. Ansible will display this
                                        when the playbook is run::

                                            - Type: str()
                                            - Example:
                                                - task.task_name = 'enable lacp'

tx_rate                                 state_check only. Ansible will ensure egress rate is
                                        at least ``tx_rate`` bps before declaring the interface
                                        up::

                                            - Type: int()
                                            - Units: bits per second (bps)
                                            - Example:
                                                task.tx_rate = 500000

====================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
