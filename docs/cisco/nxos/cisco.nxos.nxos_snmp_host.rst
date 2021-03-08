**************************************
NxosSnmpHost()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosSnmpHost() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_snmp_host
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_snmp_host <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_snmp_host_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_snmp_host.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_snmp_host.py>`_

|

============    ==============================================
Property        Description
============    ==============================================
community       Community string or v3 username::

                    - Type: str()
                    - Example:
                        task.community = 'public'

snmp_host       Address of SNMP receiver host::

                    - Type: str()
                    - Value values:
                        - IPv4 address without prefix
                        - IPv6 address without prefix
                        - domain name
                    - Examples:
                        task.snmp_host = '10.1.1.1'
                        task.snmp_host = '2000:aaaa::3a'
                        task.snmp_host = 'snmp.foo.com'
                    - Required

snmp_type       Type of message to send to snmp_host::

                    - Type: str()
                    - Valid values:
                        - inform
                        - trap
                    - Default: trap
                    - Example:
                        task.snmp_type = 'inform'

src_intf        Source interface. Must be fully qualified
                interface name::

                    - Type: str()
                    - Examples:
                        task.src_intf = 'mgmt0'
                        task.src_intf = 'Ethernet1/1'

state           Manage the state of the resource::

                    - Type: str()
                    - Value values:
                        - absent
                        - present
                    - Example:
                        task.state = 'present'
                    - NOTES:
                        - If state == present, the host is added to the
                          configuration
                        - If only vrf and/or vrf_filter and/or src_intf
                          are given, they will be added to the existing
                          host configuration
                        - If state == absent, the host is removed if
                          community parameter is given
                        - It is possible to remove only vrf and/or src_int
                          and/or vrf_filter by providing only those parameters
                          and no community parameter

udp             UDP port number::

                    - Type: int()
                    - Valid values:
                        - range: 0-65535
                    - Default: 162
                    - Example:
                        task.udp = 8162

v3              SNMPv3 Security level.  Valid when ``version`` is v3::

                    - Type: str()
                    - Valid values:
                        - auth
                        - noauth
                        - priv
                    - Example:
                        task.v3 = 'priv'

version         SNMP version. If this is not specified, v1 is used::

                    - Type: str()
                    - Valid values:
                        - v1
                        - v2c
                        - v3
                    - Example:
                        task.version = 'v3'

vrf             VRF in which SNMP traffic is originated::

                    - Type: str()
                    - Example:
                        task.vrf = 'management'

vrf_filter      Filters notifications to the notification host
                receiver based on the configured VRF::

                    - Type: str()
                    - Valid values:
                        - A VRF name
                    - Example:
                        task.vrf_filter = 'management'
                    - NOTES:
                        - If state == absent, the vrf is removed from the filter

task_name       Name of the task. Ansible will display this
                when the playbook is run::

                    - Type: str()
                    - Example:
                        - task.task_name = 'my task'

============    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
