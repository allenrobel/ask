**************************************
NxosNtpOptions()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosNtpOptions() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_ntp_options
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_ntp_options <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_ntp_options_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_ntp_options.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_ntp_options.py>`_


|

====================    ==============================================
Property                Description
====================    ==============================================
logging                 Sets whether NTP logging is enabled on the
                        device::

                            - Type: bool()
                            - Valid values:
                                - False
                                - True
                            - Example:
                                task.logging = False

master                  Sets whether the device is an authoritative
                        NTP server::

                            - Type: bool()
                            - Valid values:
                                - False
                                - True
                            - Example:
                                task.master = False

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
                                - task.task_name = 'ntp auth config'
                                        
====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
