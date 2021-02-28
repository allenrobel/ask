**************************************
NxosInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_interfaces.py>`_


|

====================================    ==============================================
Property                                Description
====================================    ==============================================
description                             Interface description::

                                            - Type: str()
                                            - Example:
                                                task.description = 'Here be dragons'

duplex                                  Interface duplex. Applicable for Ethernet
                                        interfaces only::

                                            - Type: str()
                                            - Valid values:
                                                - auto
                                                - full
                                                - half
                                            - Example:
                                                task.duplex = 'auto'

enabled                                 Administrative state of the interface. Set
                                        the value to ``True`` to administratively
                                        enable the interface or  ``False`` to disable
                                        it::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Example:
                                                task.enabled = True

fabric_forwarding_anycast_gateway       Associate SVI with anycast gateway under VLAN
                                        configuration mode. Applicable for SVI interfaces
                                        only::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Example:
                                                task.fabric_forwarding_anycast_gateway = True

ip_forward                              Disable ``False`` or enable ``True`` IP forward
                                        feature on SVIs::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Example:
                                                task.ip_forward = False

mode                                    Layer2 or Layer3 state of the interface.
                                        Applicable for Ethernet and port channel
                                        interfaces only::

                                            - Type: str()
                                            - Valid values:
                                                - layer2
                                                - layer3
                                            - Example:
                                                task.mode = 'layer2'

mtu                                     Maximum transfer unit (MTU) for a specific
                                        interface::

                                            - Type: int()
                                            - Valid values:
                                                - range:  68-9216  SVI
                                                - range: 576-9216  port-channel
                                                - range: 576-9216  Ethernet
                                            - Example:
                                                task.mtu = 9216

name                                -   Full name of interface, e.g. Ethernet1/1, port-channel10
state                               -   see self.__init__().nxos_interfaces_valid_state
speed                               -   Interface link speed. Applicable for Ethernet interfaces only

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
