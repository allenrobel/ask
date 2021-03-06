**************************************
NxosNtp()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosNtp() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_ntp
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_ntp <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_ntp_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_ntp.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_ntp.py>`_


|

====================    ==============================================
Property                Description
====================    ==============================================
key_id                  Authentication key identifier to use with
                        given NTP server or peer, or keyword
                        ``default``::

                            - Type: int() or str()
                            - Valid values:
                                - int()
                                - keyword: default
                            - Examples:
                                task.key_id = 32
                                task.key_id = 'default'
                            - Required

peer                    Network address of NTP peer::

                            - Type: str()
                            - Valid values:
                                - ipv4 address
                                - ipv6 address
                            - Examples:
                                task.peer = '10.1.1.1'
                                task.peer = '2000:aaaa::2'

prefer                  Makes given NTP server or peer the
                        preferred NTP server or peer for the
                        device::

                            - Type: str()
                            - Valid values:
                                - disabled
                                - enabled
                            - Examples:
                                task.prefer = 'enabled'

server                  Network address of NTP server::

                            - Type: str()
                            - Valid values:
                                - ipv4 address
                                - ipv6 address
                            - Examples:
                                task.server = '10.1.1.1'
                                task.server = '2000:aaaa::2'

source_addr             Local source address from which NTP
                        messages are sent::

                            - Type: str()
                            - Valid values:
                                - ipv4 address
                                - ipv6 address
                            - Examples:
                                task.source_addr = '10.1.1.2'
                                task.source_addr = '2000:aaaa::3'

source_int              Local source interface from which NTP
                        messages are sent::

                            - Type: str()
                            - Valid values:
                                - interface name
                                - keyword: default
                            - Examples:
                                task.source_int = 'mgmt0'
                                task.source_int = 'Ethernet1/1'
                                task.source_int = 'default'

state                   The state of the configuration after
                        module completion::

                            - Type: str()
                            - Valid values:
                                - absent
                                - present
                            - Example:
                                task.state = 'present'
                            - Required

stratum                 If ``master`` is True, an optional stratum
                        can be supplied::

                            - Type: int()
                            - Valid values: range 1-15
                            - Default: 8
                            - Example:
                                task.stratum = 10

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'ntp config'

vrf_name                Makes the device communicate with the given
                        NTP server or peer over a specific VRF::

                            - Type: str()
                            - Valid values:
                                - VRF name
                                - keyword: default
                            - Examples:
                                task.vrf_name = 'management'
                                task.vrf_name = 'default'

====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
