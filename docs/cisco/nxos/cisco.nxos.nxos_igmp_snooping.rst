**************************************
NxosIgmpSnooping()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosIgmpSnooping() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_igmp_snooping
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_igmp_snooping <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_igmp_snooping_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_igmp_snooping.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_igmp_snooping.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
group_timeout                       Group membership timeout value for all VLANs 
                                    on the remote device::

                                        - Type: int() or str()
                                        - Units: minutes
                                        - Valid values:
                                            - int() range 1-10080 (minutes)
                                            - never : Never expire ports from group membership
                                            - default : Remove explicit group-timeout config
                                        Examples:
                                            task.group_timeout = 20
                                            task.group_timeout = 'never'
                                            task.group_timeout = 'default'

link_local_grp_supp                 Global link-local groups suppression::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.link_local_grp_supp = True

report_supp                         Global IGMPv1/IGMPv2 Report Suppression::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.report_supp = False

snooping                            Enables/disables IGMP snooping on the switch::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.snooping = False

state                               Desired state after task has run::

                                        - Type: str()
                                        - Valid values:
                                            - default
                                            - present
                                        - Example:
                                            task.state = 'default'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'enable lacp'

v3_report_supp                      Global IGMPv3 Report Suppression and Proxy Reporting::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.v3_report_supp = False
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

