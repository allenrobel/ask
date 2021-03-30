******************************************
NxosAclInterfaces()
******************************************

Version
-------
107

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

====================    ============================================
Method                  Description
====================    ============================================
add_access_group()      Add access_group configuration to the list
                        of access-groups to apply to ``name`` when
                        ``add_interface()`` is called.  access-group
                        configuration consists of ``afi`` and the
                        list of ACLs built by calling ``add_acl()``::

                            - Type: function()
                            - Example:
                                See commit() in this table for a short example
                                See ScriptKit Example above for a full script

add_acl()               Add ACL configuration to the list of ACLs
                        to apply to access-group when ``add_access_group()``
                        is called.  ACL configuration consists of ``acl_name``,
                        ``acl_direction`` and, optionally, ``acl_port``::

                            - Type: function()
                            - Example:
                                See commit() in this table for a short example
                                See ScriptKit Example above for a full script

add_interface()         Add interface configuration to the list of interfaces
                        to apply when ``commit()`` is called.  Interface 
                        configuration consists of ``name``::

                            - Type: function()
                            - Example:
                                See commit() in this table for a short example
                                See ScriptKit Example above for a full script

commit()                Perform final verification and commit the current task::
                            - Type: function()
                            - Alias: update()
                            - Example (See also: ScriptKit Example above):
                                #!/usr/bin/env python3
                                # Configure an ipv4 access-group with two ACLs on interface Eth1/3
                                from ask.cisco.nxos.nxos_acl_interfaces import NxosAclInterfaces
                                from ask.common.log import Log
                                from ask.common.playbook import Playbook

                                log_level_console = 'INFO'
                                log_level_file = 'DEBUG'
                                log = Log('my_log', log_level_console, log_level_file)

                                pb = Playbook(log)
                                pb.profile_nxos()
                                pb.ansible_password = 'mypassword'
                                pb.name = 'Example nxos_acl_interfaces'
                                pb.add_host('dc-101')
                                pb.file = '/tmp/nxos_acl_interfaces.yaml'

                                task = NxosAclInterfaces(log)
                                task.acl_name = 'IPv4_ACL_IN'
                                task.acl_port = False
                                task.acl_direction = 'in'
                                task.add_acl()
                                task.acl_name = 'IPv4_ACL_OUT'
                                task.acl_port = False
                                task.acl_direction = 'out'
                                task.add_acl()
                                task.afi = 'ipv4'
                                task.add_access_group()
                                task.name = 'Ethernet1/3'
                                task.add_interface()
                                task.state = 'merged'
                                task.commit()

                                pb.add_task(task)
                                pb.append_playbook()
                                pb.write_playbook()

                            - Resulting task (full playbook not shown):

                                tasks:
                                -   cisco.nxos.nxos_acl_interfaces:
                                        config:
                                        -   access_groups:
                                            -   acls:
                                                -   direction: in
                                                    name: IPv4_ACL_IN
                                                    port: false
                                                -   direction: out
                                                    name: IPv4_ACL_OUT
                                                    port: false
                                                afi: ipv4
                                            name: Ethernet1/3
                                        state: merged

                            - Resulting config on remote device:

                                interface Ethernet1/3
                                  ip access-group IPv4_ACL_IN in
                                  ip access-group IPv4_ACL_OUT out

====================    ============================================

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

