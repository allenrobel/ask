**************************************
NxosBanner()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosBanner() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_banner
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_banner <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_banner_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_banner.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_banner.py>`_


|

============================    ==============================================
Property                        Description
============================    ==============================================
banner                          Specifies which banner to configure on the 
                                remote device::

                                    - Type: str()
                                    - Valid values:
                                        - exec
                                        - motd
                                    - Example:
                                        task.banner = 'motd'
                                    - Required

text                            The banner text that should be present in the
                                remote device running configuration. This 
                                argument accepts a multiline string, with no
                                empty lines::

                                    - Type: str()
                                    - Example:
                                        task.text = 'message of the day'
                                    - Requires: task.state = 'present'
                                    - Notes:
                                        1. Ampersand '@' cannot be used within
                                           text, since this is the delimiter
                                           character.

state                           Controls whether banner should be configured
                                on the remote device::

                                    - Type: str()
                                    - Valid values:
                                        - absent
                                        - present
                                    - Example:
                                        task.state = 'present'

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Example:
                                        task.task_name = 'my task'

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
