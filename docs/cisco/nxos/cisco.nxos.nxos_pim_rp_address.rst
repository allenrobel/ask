**************************************
NxosPimRpAddress()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosPimRpAddress() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_pim_rp_address
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_pim_rp_address <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_pim_rp_address_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_pim_rp_address.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_pim_rp_address.py>`_

Dependencies
------------
The following must be enabled prior to applying nxos_pim_rp_address playbook::

  feature pim

NOTES
-----

   1. state=absent is currently not supported on all platforms


|

================    ==============================================
Property            Description
================    ==============================================
bidir               If True, ``group_list`` refers to a set of PIM
                    bidirectional mode multicast groups.
                    If False, ``group_list`` refers to a set of
                    PIM Sparse mode groups::

                        - Type: bool()  
                        - Valid values:
                            - False
                            - True
                        - Example:
                            task.bidir = False

group_list          Multicast groups for which ``rp_address`` will
                    act as the rendezvous point::

                        - Type: str()
                        - Valid values:
                            - ipv4 multicast address with prefixlen
                              - A.B.C.D/LEN
                        - Example:
                            task.group_list = '225.1.0.0/16'

prefix_list         Prefix list policy for static RP::

                        - Type: str()
                        - Valid values:
                            - ip prefix-list name
                        - Example:
                            task.prefix_list = 'ALLOW_SOURCES'

route_map           Route map policy for static RP::

                        - Type: str()
                        - Valid values:
                            route-map name
                        - Example:
                            task.route_map = 'ALLOW_SOURCES'

rp_address          Configures a Protocol Independent Multicast
                    (PIM) static rendezvous point (RP) address::

                        - Type: str()
                        - Valid values:
                            - ipv4 unicast address
                              - A.B.C.D
                        - Example:
                            task.rp_address = '10.1.1.3'

state               Desired state after task completion::

                        - Type: str()
                        - Valid values:
                            - absent
                            - present
                        - Example:
                            task.state = 'present'
                        - Required

task_name           Name of the task. Ansible will display this
                    when the playbook is run::

                        - Type: str()
                        - Example:
                            - task.task_name = 'my task'

================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
