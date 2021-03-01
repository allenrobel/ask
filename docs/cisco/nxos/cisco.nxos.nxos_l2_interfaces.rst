**************************************
NxosL2Interfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosL2Interfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_l2_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_l2_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_l2_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_l2_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_l2_interfaces.py>`_


|

================    ======================================================
Property            Description
================    ======================================================
allowed_vlans       Comma-separated list of allowed VLANs on trunk port::

                        - Type: str()
                        - Example:
                            task.allowed_vlans = '2-5,10,20'

mode                Desired L2 mode of the interface::

                        - Type: str()
                        - Valid values:
                            - access
                            - trunk
                            - fex-fabric
                            - fabricpath
                        - Example:
                            task.mode = 'access'

name                Full name of interface::

                        - Type: str()
                        - Examples:
                            task.name = 'Ethernet1/1'
                            taks.name = 'port-channel20'
                        - Required except when ``running_config`` is set.

native_vlan         Native VLAN configured on trunk interface::

                        - Type: int()
                        - Valid values: range: 1-3967
                        - Examples:
                            task.native_vlan = 10

register            Ansible variable to save output to::

                        - Type: str()
                        - Examples:
                            task.register = 'result'

running_config      Full path to a file containing the output of
                    ``show running-config | section ^interface``::

                        - Type: str()
                        - Examples:
                            task.running_config = '/tmp/running.cfg'

state               Desired state after task has run::

                        - Type: str()
                        - Valid values:
                            - deleted
                            - gathered
                            - merged
                            - overridden
                            - parsed
                            - rendered
                            - replaced
                        - Example:
                            task.state = 'merged'
                        - Required

vlan                Vlan configured on access port::

                        - Type: int()
                        - Valid values: range: 1-3967
                        - Examples:
                            task.vlan = 330

task_name           Name of the task. Ansible will display this
                    when the playbook is run::

                        - Type: str()
                        - Example:
                            - task.task_name = 'configure interfaces'
                                        
================    ======================================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
