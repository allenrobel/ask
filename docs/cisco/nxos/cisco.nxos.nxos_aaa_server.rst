******************************************
NxosAaaServer() 
******************************************

ScriptKit Synopsis
------------------
NxosAaaServer() generates Ansible task instances conformant with cisco.nxos.nxos_aaa_server.
These task instances can then be passed to Playbook().add_task()

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_aaa_server.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_aaa_server.py>`_

Ansible Module Documentation
----------------------------
- `nxos_aaa_server <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_aaa_server_module.rst>`_

|

============================    ==============================================
Property                        Description
============================    ==============================================
deadtime                        Duration, in minutes, after which a non-reachable
                                AAA server is skipped::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-1440
                                    - Device default: 0
                                    - Example:
                                        task.deadtime = 20

directed_request                Enables direct authentication requests to AAA server::

                                    - Type: str()
                                    - Valid values:
                                        - enabled
                                        - disabled
                                        - default
                                    - Default: disabled
                                    - Example:
                                        task.directed_request = 'enabled'

encrypt_type                    The state of encryption applied to the entered global key.
                                Type-6 encryption is not supported::

                                    - Type: int()
                                    - Valid values: 0, 7
                                        0 - clear text
                                        7 - encrypted
                                    - Example:
                                        task.encrypt_type = 0

global_key                      Global AAA shared secret::

                                    - Type: str()
                                    - Valid values:
                                        - an AAA key
                                        - keyword: default
                                    - Examples:
                                        task.global_key = 'boopperfizly'
                                        task.global_key = 'default'

server_timeout                  Global AAA server timeout period, in seconds::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-60
                                        - keyword: default
                                    - Device default: 5
                                    - Examples:
                                        task.server_timeout = 10
                                        task.server_timeout = 'default'

server_type                     The protocol used to access the server::

                                    Type: str()
                                    Valid values:
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

============================    ==============================================

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
