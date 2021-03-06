**************************************
NxosNtpAuth()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosNtpAuth() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_ntp_auth
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_ntp_auth <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_ntp_auth_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_ntp_auth.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_ntp_auth.py>`_


|

====================    ==============================================
Property                Description
====================    ==============================================
auth_type               Whether the given md5string is in cleartext
                        or has been encrypted.  If in cleartext, the
                        device will encrypt it before storing it::

                            - Type: str()
                            - Valid values:
                                - encrypt
                                - text
                            - Example:
                                task.auth_type = 'encrypt'

authentication          Turns NTP authentication on or off::

                            - Type: str()
                            - Valid values:
                                - off
                                - on
                            - Example:
                                task.authentication = 'on'

key_id                  Authentication key identifier (numeric)::

                            - Type: int()
                            - Example:
                                task.key_id = 2

md5string               MD5 String::

                            - Type: str()
                            - Example:
                                task.md5string = 'e1rgdr6w'

trusted_key             Whether the given key is required to be
                        supplied by a time source for the device
                        to synchronize to the time source::

                            - Type: bool()
                            - Valid values:
                                - False
                                - True
                            - Example:
                                task.trusted_key = False

state                   The state of the configuration after
                        module completion::

                            - Type: str()
                            - Valid values:
                                - absent
                                - present
                            - Example:
                                task.state = 'present'
                            - Required

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'ntp auth config'
                                        
====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
