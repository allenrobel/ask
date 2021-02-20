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
                                    - Valid values: in, out
                                    - Required

acl_name                        Name of the ACL to be added/removed::

                                    - Type: str()
                                    - Required

acl_port                        Use ACL as port policy::

                                    If 'yes', interface must be a switchport
                                    If 'no', interface must be a routed port (i.e. no switchport)

                                    - Type: str()
                                    - Valid values: no, yes

afi                             Address Family Indicator of the ACLs to be configured::

                                    - Type: str()
                                    - Valid values: ipv4, ipv6
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
                                    - Required

task_name                       Name of the task. Ansible will display this when
                                executing the playbook::

                                    - Type: str()
                                    - Default: Task name is not displayed

============================    ==============================================

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
