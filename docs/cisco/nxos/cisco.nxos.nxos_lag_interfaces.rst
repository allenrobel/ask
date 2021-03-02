**************************************
NxosLagInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosLagInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lag_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_lag_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_lag_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_lag_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_lag_interfaces.py>`_


|

================    ==================================================
User Methods        Description
================    ==================================================
add_member()        Append a member interface to the task and reset
                    member properties to None to allow configuration
                    of another member interface. See
                    ``ScriptKit Example`` above for usage.

add_lag()           Append a lag interface, and its members (if any)
                    to the task and reset lag properties to None to
                    allow configuration of another lag interface. See
                    ``ScriptKit Example`` above for usage.
================    ==================================================


|
|

====================    ==============================================
Property                Description
====================    ==============================================
force                   When ``True`` adds the ``force`` keyword to the
                        NX-OS channel-group CLI::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.member = 'Ethernet1/1'
                                task.force = True
                                task.add_member()
                                task.name = 'port-channel20'
                                task.add_lag()
                            - Resulting Ansible task:
                                config:
                                - name: port-channel20
                                  members:
                                  - member: Ethernet1/1
                                    force: true
                            - Resulting NX-OS CLI:
                                interface Ethernet1/1
                                   channel-group 20 force

member                  The full name of the member ethernet interface::

                            - Type: str()
                            - Valid values: An ethernet interface name
                            - Example:
                                task.member = 'Ethernet1/1'

mode                    Member interface link aggregation mode::

                            - Type: str()
                            - Valid values:
                                - active
                                    Initiate negotiation with the remote end
                                    by sending LACP PDUs
                                - on
                                    Do not participate in LACP. This forces
                                    the interface's membership in the port-channel
                                    regardless of the state of the remote end
                                - passive
                                    Participate in LACP, by responding to received
                                    LACP PDUs, but do not initiate the negotiation
                            - Example:
                                task.member = 'Ethernet1/1'
                                task.mode = 'active'
                                task.add_member()

name                    Name of the port-channel interface::

                            - Type: str()
                            - Valid values: A port-channel interface name
                            - Example:
                                task.name = 'port-channel3'

register                Ansible variable to save output to::

                            - Type: str()
                            - Examples:
                                task.register = 'result'

running_config          Full path to a file containing the output of
                        ``show running-config | section ^interface``.
                        ``running_config`` is mutually-exclusive with
                        every other property except ``state`` and
                        ``register``.  ``state`` must be set to ``parsed``
                        if ``running_config`` is set.::

                            - Type: str()
                            - Examples:
                                task.state = 'parsed'
                                task.running_config = '/tmp/running.cfg'

state                   Desired state after task has run::

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

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'configure lag'

====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
