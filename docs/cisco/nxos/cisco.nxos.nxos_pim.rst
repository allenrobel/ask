**************************************
NxosPim()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosPim() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_pim
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_pim <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_pim_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_pim.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_pim.py>`_

Dependencies
------------
The following must be enabled prior to applying nxos_pim playbook::

  feature pim

|

================    ==============================================
Property            Description
================    ==============================================
bfd                 Enables BFD on all PIM interfaces::

                        - Type: str()  
                        - Valid values:
                            - disable
                            - enable
                        - Dependency: 'feature bfd
                        - Example:
                            task.bfd = 'enable'

ssm_range           Configure group ranges for Source Specific Multicast (SSM)::

                        - Type: list() or str()
                        - Valid values:
                            - default
                                - set ssm_range to 232.0.0.0/8
                            - none
                                - remove all ssm group ranges
                            - list()
                                - list of multicast group ranges
                        - Examples:
                            task.ssm_range = 'default'
                            task.ssm_range = 'none'

                            ssm = list()
                            ssm.append('225.1.0.0/16')
                            ssm.append('225.4.1.0/24')
                            task.ssm_range = ssm

================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
