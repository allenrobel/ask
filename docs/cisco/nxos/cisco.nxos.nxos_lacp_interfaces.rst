**************************************
NxosLacpInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosLacpInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lacp_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_lacp_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_lacp_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_lacp_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_lacp_interfaces.py>`_


|

================    ==============================================
User Methods        Description
================    ==============================================
add_interface()     Append lacp interface properties to the task
                    config list and reset the properties to None to
                    allow configuration of another interface.
                    See ``ScriptKit Example`` above for usage.
================    ==============================================


|
|

====================    ==============================================
Property                Description
====================    ==============================================
graceful                port-channel lacp graceful convergence.
                        Disable this only with lacp ports connected to
                        Non-Nexus peer. Disabling this with Nexus peer
                        can lead to port suspension::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.graceful = True

min                     Minimum number of member interfaces in the
                        port-channel that must be up before the
                        port-channel interface is brought up::

                            - Type: int()
                            - Valid values: range: 1-32
                            - Example:
                                task.min = 8

max                     Maximum number of interfaces in the
                        port-channel.  Member interfaces above this
                        limit will be placed in hot-standby mode::

                            - Type: int()
                            - Valid values: range: 1-32
                            - Example:
                                task.max = 16

mode                    Configure delayed lacp on the port-channel.
                        LACP port-channels exchange LACP PDUs for quick
                        bundling of links when connecting a server and
                        a switch. However, the links go into suspended
                        state when the PDUs are not received.  The delayed
                        LACP feature enables one port-channel member, the
                        delayed-LACP port, to come up first as a member of
                        a regular port-channel before LACP PDUs are received.
                        After it is connected in LACP mode, other members,
                        the auxiliary LACP ports, are brought up. This avoids
                        the links becoming suspended when PDUs are not
                        received.  If ``mode`` is set, ``name`` must refer to
                        a port-channel interface::

                            - Type: str()
                            - Valid values: delay
                            - Example:
                                task.mode = 'delay'

name                    Name of the interface::

                            - Type: str()
                            - Valid values:
                                - port-channelX
                                - EthernetX/Y
                            - Examples:
                                task.name = 'port-channel3'
                                task.name = 'Ethernet1/1'
                            - Required
                            - NOTES:
                                - Depending on which properties
                                  are set, only one of port-channel
                                  or ethernet will be valid.  Refer
                                  to individual properties for
                                  details.

port_priority           LACP port priority assigned to the
                        member ethernet interface. A higher port
                        priority value increases the likelihood
                        that a member port will be chosen to be
                        active in a bundle in the event that the
                        ``max`` (max-bundle) value is exceeded. 
                        Applicable only for Ethernet.
                        If ``port_priority`` is set, ``name``
                        must refer to a member ethernet interface::

                            - Type: int()
                            - Valid values: range: 1-65535
                            - Example:
                                task.name = 'Ethernet1/1'
                                task.port_priority = 8216

rate                    Rate at which PDUs are sent by LACP.
                        Applicable only for Ethernet.  At fast
                        rate LACP is transmitted once every 1
                        second. At normal rate LACP is transmitted
                        every 30 seconds after the link is bundled.
                        If ``rate`` is set, ``name`` must refer to
                        a member ethernet interface.

                            - Type: str()
                            - Valid values:
                                - fast
                                - normal
                            - Example:
                                task.name 'Ethernet1/1'
                                task.rate = 'fast'

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

suspend_individual      Disabling this will cause lacp to place a
                        member port into individual state (rather than
                        suspend it) in the event the individual port 
                        does not receive LACP BPDUs from its peer port.
                        If ``suspend_individual`` is set, ``name`` must
                        refer to a port-channel interface::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.name = 'port-channel3'
                                task.suspend_individual = True

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'enable lacp'

vpc                     Enable lacp convergence for vPC port
                        channels. If ``vpc`` is set, ``name``
                        must refer to a port-channel interface::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.name = 'port-channel3'
                                task.vpc = True

====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)