**************************************
NxosLldpInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosLldpInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lldp_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_lldp_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_lldp_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_lldp_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_lldp_interfaces.py>`_


|

================    ==================================================
User Methods        Description
================    ==================================================
add_interface()     Append an LLDP interface to the task and reset
                    lldp interface properties to None to allow 
                    configuration of another interface. See
                    ``ScriptKit Example`` above for example usage.
================    ==================================================


|
|

============================    ==============================================
Property                        Description
============================    ==============================================
name                            Full name of the interface on which to
                                configure LLDP::

                                    - Type: str()
                                    - Valid values: An LLDP-capable interface name
                                    - Required (if running_config is not set)
                                    - Example:
                                        task.name = 'Ethernet1/1'

receive                         Enable ``True`` or disable ``False``
                                reception of LLDP packets on ``name``.
                                By default, this is enabled after LLDP is
                                enabled globally:

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.receive = True

tlv_set_management_address      Advertise the IPv4 or IPv6 management address 
                                associated with ``name``.

                                    - Type: str()
                                    - Valid values: an IPv4 or IPv6 address
                                    - Example:
                                        task.tlv_set_management_address = '10.1.2.3'

tlv_set_vlan                    Advertise the VLAN ID associated with ``name``.

                                    - Type: str()
                                    - Valid values: range 1-4094
                                    - Example:
                                        task.tlv_set_vlan = 30

transmit                        Enable ``True`` or Disable ``False``
                                transmission of LLDP packets on ``name``.
                                By default, this is enabled after LLDP is
                                enabled globally.

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.transmit = True

register                        Ansible variable to save output to::

                                    - Type: str()
                                    - Examples:
                                        task.register = 'result'

running_config                  Full path to a file containing the output of
                                ``show running-config | section ^interface``.
                                ``running_config`` is mutually-exclusive with
                                every other property except ``state`` and
                                ``register``.  ``state`` must be set to ``parsed``
                                if ``running_config`` is set.::

                                    - Type: str()
                                    - Examples:
                                        task.state = 'parsed'
                                        task.running_config = '/tmp/running.cfg'

state                           Desired state after the task has run::

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

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Example:
                                        - task.task_name = 'configure lldp interfaces'

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
