**************************************
NxosLldpGlobal()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosLldpGlobal() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lldp_global
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_lldp_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_lldp_global_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_lldp_global.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_lldp_global.py>`_

Dependencies
------------

1. ``feature lldp`` must enabled on the target before using this module

|

========================    ==============================================
Property                    Description
========================    ==============================================
dcbxp                       Enable ``True`` or disable ``False``
                            Data Center Bridging Exchange Protocol TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.dcbxp = False

holdtime                    Amount of time the receiving device should
                            hold the information::

                                - Type: int()
                                - Valid values: range: 0-65535
                                - Units: seconds
                                - Example:
                                    task.holdtime = 300

management_address_v4       Enable ``True`` or disable ``False``
                            Management address with TLV ipv4::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.management_address_v4 = True

management_address_v6       Enable ``True`` or disable ``False``
                            Management address with TLV ipv6::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.management_address_v6 = False

port_description            Enable ``True`` or disable ``False``
                            port description TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.port_description = False

port_id                     Advertise interface names in the long(0)
                            or short(1) form::

                                - Type: int()
                                - Valid values: 0, 1
                                - Example:
                                    task.port_id = 0

port_vlan                   Enable ``True`` or disable ``False``
                            port VLAN ID TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.port_vlan = False

power_management            Enable ``True`` or disable ``False``
                            IEEE 802.3 DTE Power via MDI TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.power_management = False

register                    Ansible variable to save output to::

                                - Type: str()
                                - Examples:
                                    task.register = 'result'

reinit                      Amount of time to delay the initialization
                            of LLDP on any interface::

                                - Type: int()
                                - Valid values: range: 0-65535
                                - Units: seconds
                                - Example:
                                    task.reinit = 30

running_config              Full path to a file containing the output of
                            ``show running-config | include lldp``.
                            ``running_config`` is mutually-exclusive with
                            every other property except ``state`` and
                            ``register``.  ``state`` must be set to ``parsed``
                            if ``running_config`` is set.::

                                - Type: str()
                                - Examples:
                                    task.state = 'parsed'
                                    task.running_config = '/tmp/running.cfg'

state                       Desired state after task has run::

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

system_capabilities         Enable ``True`` or disable ``False``
                            system capabilities TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.system_capabilities = False

system_description          Enable ``True`` or disable ``False``
                            system description TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.system_description = False

system_name                 Enable ``True`` or disable ``False``
                            system name TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.system_name = False

task_name                   Name of the task. Ansible will display this
                            when the playbook is run::

                                - Type: str()
                                - Example:
                                    - task.task_name = 'configure lldp global'

timer                       LLDP update transmission frequency::

                                - Type: int()
                                - Valid values: range: 0-65535
                                - Units: seconds
                                - Example:
                                    task.timer = 30

========================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
