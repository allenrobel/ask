******************************************
NxosAaaServerHost() 
******************************************

Version
-------
107

ScriptKit Synopsis
------------------
NxosAaaServerHost() generates Ansible task instances conformant with cisco.nxos.nxos_aaa_server_host.
These task instances can then be passed to Playbook().add_task()

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_aaa_server_host.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_aaa_server_host.py>`_

Ansible Module Documentation
----------------------------
- `nxos_aaa_server_host <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_aaa_server_host_module.rst>`_

|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task::
                                - Type: function()
                                - Alias: update()
                                - Example:
                                    # see ScriptKit Example above for
                                    # full script
                                    pb = Playbook(log)
                                    task = NxosAaaServerHost(log)
                                    task.address = '172.29.167.250'
                                    task.encrypt_type = 0
                                    task.host_timeout = 10
                                    task.key = 'foobar'
                                    task.server_type = 'tacacs'
                                    task.state = 'present'
                                    task.commit()
                                    pb.add_task(task)

========================    ============================================

|

============================    ==============================================
Property                        Description
============================    ==============================================
acct_port                       Alternate UDP port for RADIUS accounting::

                                    - Type: int() or str()
                                    - Valid values:
                                        - range: UDP port-range
                                        - keyword: default
                                    - Examples:
                                        task.acct_port = 8030
                                        task.acct_port = 'default'

address                         Address or name of the radius or tacacs host::

                                    - Type: str()
                                    - Valid values:
                                        - ip address
                                        - hostname
                                    - Examples:
                                        task.address = '10.1.1.2'
                                        task.address = 'aaa.foo.com'
                                    - Required

auth_port                       Alternate UDP port for RADIUS authentication::

                                    - Type: int() or str()
                                    - Valid values:
                                        - range: UDP port-range
                                        - keyword: default
                                    - Examples:
                                        task.auth_port = 8031
                                        task.auth_port = 'default'

encrypt_type                    The state of encryption applied to the entered global key.
                                Type-6 encryption is not supported::

                                    - Type: str()
                                    - Valid values:
                                        0 - clear text
                                        7 - encrypted
                                    - Example:
                                        task.encrypt_type = 7

host_timeout                    Timeout period for the specified host::

                                    - Type: int() or str()
                                    - Units: seconds
                                    - Valid values:
                                        - range: 1-60
                                        - keyword: default
                                    - Examples:
                                        task.host_timeout = 30
                                        task.host_timeout = 'default'

key                             Shared secret for the specified host::

                                    - Type: str()
                                    - Valid values:
                                        - a shared secret key
                                        - keyword: default
                                    - Examples:
                                        task.key = 'a1fe45004f'
                                        task.key = 'default'

server_type                     The authentication protocol used by the server::

                                    - Type: str()
                                    - Valid values:
                                        - radius
                                        - tacacs
                                    - Example:
                                        task.server_type = 'tacacs'

state                           State of the resource after playbook execution::

                                    - Type: str()
                                    - Valid values:
                                        - present
                                        - default
                                    - Default: present
                                    - Example:
                                        task.state = 'default'

tacacs_port                     Alternate TCP port TACACS Server::

                                    - Type: str()
                                    - Valid values:
                                        - range: TCP port-range
                                        - keyword: default
                                    - Examples:
                                        task.tacacs_port = 8045
                                        task.tacacs_port = 'default'

============================    ==============================================

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

