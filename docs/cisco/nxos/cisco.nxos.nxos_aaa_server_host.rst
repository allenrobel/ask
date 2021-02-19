
====================
NxosAaaServerHost() 
====================

ScriptKit Synopsis
------------------
NxosAaaServerHost() generates Ansible task instances conformant with cisco.nxos.nxos_aaa_server_host.
These task instances can then be passed to Playbook().add_task()

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_aaa_server_host.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_aaa_server_host.py>`_

Ansible Module Documentation
----------------------------
- `nxos_aaa_server_host <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_aaa_server_host.rst>`_

|

============================    ==============================================
Property                        Description
============================    ==============================================
acct_port                       Alternate UDP port for RADIUS accounting.::

                                    - Type: str()
                                    - Valid values: int() range: UDP port-range, or keyword 'default'
                                    - NOTES:
                                      - auto-converted to str()

address                         Address or name of the radius or tacacs host.::

                                    - Type: str()
                                    - Valid values: ip address or hostname
                                    - Required

auth_port                       Alternate UDP port for RADIUS authentication.::

                                    - Type: str()
                                    - Valid values: int() range: UDP port-range, or keyword 'default'
                                    - NOTES:
                                      - auto-converted to str()

encrypt_type                    The state of encryption applied to the entered global key.
                                Type-6 encryption is not supported.::

                                    - Type: str()
                                    - Valid values: 0, 7
                                        0 - clear text
                                        7 - encrypted
                                    - NOTES:
                                      - auto-converted to str()

host_timeout                    Timeout period for specified host.::

                                    - Type: str()
                                    - Units: seconds
                                    - Valid values: int() range: 1-60, or keyword 'default'
                                    - NOTES:
                                      - auto-converted to str()

key                             Shared secret for the specified host.::

                                    - Type: str()
                                    - Valid values: str(), or keyword 'default'

server_type                     The authentication protocol used by the server.::

                                    - Type: str()
                                    - Valid values: radius, tacacs

state                           State of the resource after playbook execution.::

                                    - Type: str()
                                    - Valid values: present, default
                                    - Default: present

tacacs_port                     Alternate TCP port TACACS Server.::

                                    - Type: str()
                                    - Valid values: int() range: TCP port-range, or keyword 'default'
                                    - NOTES:
                                      - auto-converted to str()

============================    ==============================================
