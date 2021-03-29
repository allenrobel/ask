**************************************
NxosHsrpInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
106

ScriptKit Synopsis
------------------
- NxosHsrpInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_hsrp_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_hsrp_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_hsrp_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_hsrp_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_hsrp_interfaces.py>`_

================================    ==============================================
Property                            Description
================================    ==============================================
add_interface()                         Add an interface to the configuration::

                                            - Type: function()
                                            - Example:
                                                #!/usr/bin/env python3
                                                # Enable HSRP BFD on 5 interfaces
                                                from ask.cisco.nxos.nxos_hsrp_interfaces import NxosHsrpInterfaces
                                                from ask.common.log import Log
                                                from ask.common.playbook import Playbook
                                                log_level_console = 'INFO'
                                                log_level_file = 'DEBUG'
                                                log = Log('my_log', log_level_console, log_level_file)
                                                pb = Playbook(log)
                                                pb.profile_nxos()
                                                pb.ansible_password = 'mypassword'
                                                pb.name = 'Example nxos_hsrp_interfaces'
                                                pb.add_host('dc-101')
                                                pb.file = '/tmp/nxos_hsrp_interfaces.yaml'
                                                task = NxosHsrpInterfaces(log)
                                                task.append_to_task_name('HSRP BFD enable:')
                                                for port in range(1,6):
                                                    task.name = 'Ethernet1/{}'.format(port)
                                                    task.bfd = 'enable'
                                                    task.append_to_task_name(task.name)
                                                    task.add_interface()
                                                task.state = 'merged'
                                                task.update()
                                                pb.add_task(task)
                                                pb.append_playbook()
                                                pb.write_playbook()

================================    ==============================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
name                                Full name of the interface::

                                        - Type: str()
                                        - Example:
                                            task.name = 'Ethernet1/1'
                                        - Required

bfd                                 Enable/Disable HSRP Bidirectional Forwarding
                                    Detection (BFD) on the interface::

                                        - Type: str()
                                        - Valid values:
                                            - disable
                                            - enable
                                        - Example:
                                            task.bfd = 'enable'

state                               Desired state of hsrp attributes on
                                    ``name`` interface::

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
                                            task.state = 'enabled'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'Vlan10 HSRP BFD'
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

