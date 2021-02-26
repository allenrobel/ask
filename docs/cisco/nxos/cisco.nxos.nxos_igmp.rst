**************************************
NxosIgmp()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosIgmp() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_igmp
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_igmp <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_igmp_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_igmp.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_igmp.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
enforce_rtr_alert                   Enables or disables the enforce router alert 
                                    option check for IGMPv2 and IGMPv3 packets::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.enforce_rtr_alert = False

flush_routes                        Removes routes when the IGMP process is 
                                    restarted. By default, routes are not 
                                    flushed::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.flush_routes = True

restart                             Restarts the igmp process (using an exec
                                    config command)::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.restart = True

snooping                            Enables/disables IGMP snooping on the switch::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.snooping = False

state                               Desired state after task has run::

                                        - Type: str()
                                        - Valid values:
                                            - absent
                                            - present
                                        - Example:
                                            task.state = 'present'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'enable lacp'
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
