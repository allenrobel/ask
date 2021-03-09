******************************************
NxosAclInterfaces()
******************************************

ScriptKit Synopsis
------------------
NxosAclInterfaces() generates Ansible task instances conformant with cisco.nxos.nxos_acl_interfaces.
These task instances can then be passed to Playbook().add_task()

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_acl_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_acl_interfaces.py>`_

Ansible Module Documentation
----------------------------
- `nxos_acl_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_acl_interfaces_module.rst>`_

|

============================    ==============================================
Property                        Description
============================    ==============================================
acl_direction                   Direction to be applied for the ACL::

                                    - Type: str()
                                    - Valid values:
                                        - in
                                        - out
                                    - Example:
                                        task.acl_direction = 'out'
                                    - Required

acl_name                        Name of the ACL to be added/removed::

                                    - Type: str()
                                    - Example:
                                        task.acl_name = 'TOR_OUT'
                                    - Required

acl_port                        Use ACL as port policy. If True, ``name``
                                must be a (L2) switchport.  If False, ``name``
                                must be a (L3) routed port::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.acl_port = True

afi                             Address Family Indicator of the ACLs to be configured::

                                    - Type: str()
                                    - Valid values:
                                        - ipv4
                                        - ipv6
                                    - Example:
                                        task.afi = 'ipv4'
                                    - Required

name                            Name of the interface on which the ACL is applied::

                                    - Type: str()
                                    - Examples:
                                        - task.name = 'Ethernet1/1'
                                        - task.name = 'Vlan10'
                                    - Required

state                           The state after playbook has executed::

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

task_name                       Name of the task. Ansible will display this when
                                executing the playbook::

                                    - Type: str()
                                    - Default: Task name is not displayed
                                    - Example:
                                        task.task_name = 'my task'

============================    ==============================================

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
