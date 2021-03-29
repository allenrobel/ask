**************************************
NxosInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
122

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
Method                                  Description
====================================    ==============================================
add_interface()                         Add an interface to the configuration::

                                            - Type: function()
                                            - Example:
                                                #!/usr/bin/env python3
                                                # Configure one ethernet and one SVI interface
                                                from ask.cisco.nxos.nxos_interfaces import NxosInterfaces
                                                from ask.common.log import Log
                                                from ask.common.playbook import Playbook
                                                log_level_console = 'INFO'
                                                log_level_file = 'DEBUG'
                                                log = Log('my_log', log_level_console, log_level_file)
                                                pb = Playbook(log)
                                                pb.profile_nxos()
                                                pb.ansible_password = 'mypassword'
                                                pb.name = 'Example nxos_interfaces'
                                                pb.add_host('dc-101')
                                                pb.file = '/tmp/nxos_interfaces.yaml'
                                                task = NxosInterfaces(log)
                                                task.name = 'Ethernet1/1'
                                                task.enabled = True
                                                task.mode = 'layer3'
                                                task.mtu = 9216
                                                task.add_interface()
                                                task.name = 'Vlan2'
                                                task.enabled = True
                                                task.add_interface()
                                                task.state = 'merged'
                                                task.update()
                                                pb.add_task(task)
                                                pb.append_playbook()
                                                pb.write_playbook()

====================================    ==============================================

|

====================================    ==============================================
Property                                Description
====================================    ==============================================
description                             Interface description::

                                            - Type: str()
                                            - Example:
                                                task.description = 'Here be dragons'

duplex                                  Interface duplex. Applicable for Ethernet
                                        interfaces only.  If set, ``speed`` must
                                        also be set::

                                            - Type: str()
                                            - Valid values:
                                                - auto
                                                - full
                                                - half
                                            - Example:
                                                task.speed = 40000
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
                                            - Prerequisites:
                                                - feature fabric forwarding must be enabled
                                                    task = NxosFeature(log)
                                                    task.feature = 'fabric forwarding'
                                                    task.state = 'enabled'
                                                    task.update()
                                                    pb.add_task(task)
                                                - fabric forwarding anycast-gateway-mac
                                                  must be configured
                                                    task = NxosConfig(log)
                                                    cfg = list()
                                                    cfg.append('fabric forwarding anycast-gateway-mac 0000.0000.1111')
                                                    task.lines = cfg
                                                    task.update()
                                                    pb.add_task(task)
                                            - Example:
                                                task = NxosInterfaces(log)
                                                task.name = 'Vlan222'
                                                task.fabric_forwarding_anycast_gateway = True
                                                task.update()
                                                pb.add_task(task)

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

name                                    Full name of interface::

                                            - Type: str()
                                            - Examples:
                                                task.name = 'Ethernet1/1'
                                                task.name = 'Ethernet1/1.23'
                                                task.name = 'Loopback4'
                                                task.name = 'mgmt0'
                                                task.name = 'port-channel22'
                                                task.name = 'Vlan3'

speed                                   Interface link speed. Applicable for Ethernet
                                        interfaces only::

                                            - Type: int()
                                            - Valid values: digits
                                            - Example:
                                                task.speed = 100000

state                                   Desired state after task has run::

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
                                            - Required

task_name                               Name of the task. Ansible will display this
                                        when the playbook is run::

                                            - Type: str()
                                            - Example:
                                                - task.task_name = 'Create Vlan10'
                                        
====================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

