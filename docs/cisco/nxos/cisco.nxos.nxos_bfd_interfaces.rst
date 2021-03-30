**************************************
NxosBfdInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
105

ScriptKit Synopsis
------------------
- NxosBfdInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bfd_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bfd_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bfd_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bfd_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bfd_interfaces.py>`_


|

========================    ============================================
Method                      Description
========================    ============================================
add_interface()             Apply all currently-set interface properties
                            and append the interface ``name`` to the
                            configuration::

                                - Type: function()
                                - Example:
                                    See commit()

commit()                    Perform final verification and commit the 
                            current task::
                                - Type: function()
                                - Alias: update()
                                - Example:
                                    # see ScriptKit Example above for
                                    # full script
                                    pb = Playbook(log)
                                    task = NxosBfdInterfaces(log)
                                    for port in [5,6,7,8]:
                                        task.name = 'Ethernet1/{}'.format(port)
                                        task.bfd = 'enable'
                                        task.add_interface()
                                    task.state = 'merged'
                                    task.task_name = 'enable bfd on Eth1/5-8'
                                    task.commit()
                                    pb.add_task(task)

========================    ============================================

|

============================    ==============================================
Property                        Description
============================    ==============================================
bfd                             Enable/Disable Bidirectional Forwarding Detection 
                                (BFD) on the interface::

                                    - Type: str()
                                    - Valid values: enable, disable
                                    - Examples:
                                        - task.bfd = 'enable'

echo                            Enable/Disable BFD Echo functionality on the interface::

                                    - Type: str()
                                    - Valid values: enable, disable
                                    - Examples:
                                        - task.echo = 'disable'

name                            Full name of interface::

                                    - Type: str()
                                    - Examples:
                                        - task.name = 'Ethernet1/10'
                                        - task.name = 'port-channel4'

state                           The state of the resource after playbook
                                execution::

                                    - Type: str()
                                    - Valid values:
                                        - deleted
                                        - gathered
                                        - merged
                                        - overridden
                                        - parsed
                                        - rendered
                                        - replaced
                                    - Examples:
                                        - task.state = 'deleted'

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Examples:
                                        - task.task_name = 'my task'

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

