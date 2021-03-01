**************************************
NxosL3Interfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosL3Interfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_l3_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_l3_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_l3_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_l3_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_l3_interfaces.py>`_


|

================================    ==============================================
User Methods                        Description
================================    ==============================================
add_ipv4()                          Append ivp4 properties to the ipv4
                                    attributes list and reset the properties
                                    to None::

                                        - Example:

                                            pb = Playbook(log_instance)
                                            task = NxosL3Interfaces(log_instance)
                                            task.name = 'Ethernet1/49'
                                            task.ipv4_address = '10.1.1.1/24'
                                            task.ipv4_tag = 10
                                            task.add_ipv4()
                                            task.ipv4_address = '10.2.1.1/24'
                                            task.ipv4_tag = 20
                                            task.ipv4_secondary = 'yes'
                                            task.add_ipv4()
                                            task.state = 'merged'
                                            task.update()
                                            pb.add_task(task)

                                        - Resulting playbook task:

                                            tasks:
                                            -   cisco.nxos.nxos_l3_interfaces:
                                                    config:
                                                    -   ipv4:
                                                        -   address: 10.1.1.1/24
                                                            tag: 10
                                                        -   address: 10.2.1.1/24
                                                            secondary: 'yes'
                                                            tag: 20
                                                        name: Ethernet1/49
                                                    state: merged

add_ipv6()                          Append ivp6 properties to ipv6
                                    attributes list and reset the properties
                                    to None::

                                        - Example:

                                            pb = Playbook(log_instance)
                                            task = NxosL3Interfaces(log_instance)
                                            task.name = 'Ethernet1/49'
                                            task.ipv6_address = '2001:aaaa::1/64'
                                            task.ipv6_tag = 10
                                            task.add_ipv6()
                                            task.ipv6_address = '2001:bbbb::1/64'
                                            task.ipv6_tag = 20
                                            task.add_ipv6()
                                            task.state = 'merged'
                                            task.update()
                                            pb.add_task(task)

                                        - Resulting playbook task:
                                            config:
                                            -   ipv6:
                                                -   address: 2001:aaaa::1/64
                                                    tag: 10
                                                -   address: 2001:bbbb::1/64
                                                    tag: 20
                                                name: Ethernet1/49
                                            state: merged

================================    ==============================================


================================    ==============================================
Property                            Description
================================    ==============================================
dot1q                               802.1q vlan ID used in the following CLI
                                    ``encapsulation dot1q <vlan ID>``::

                                        - Type: int()
                                        - Example:
                                            task.dot1q = 10

evpn_multisite_tracking             VxLAN evpn multisite Interface tracking.
                                    Supported only on selected models::

                                        - Type: str()
                                        - Valid values:
                                            - fabric-tracking
                                            - dci-tracking
                                        - Example:
                                            task.evpn_multisite_tracking = 'fabric-tracking'

ipv4_address                        ipv4 interface address::

                                        - Type: str()
                                        - Example:
                                            task.ipv4_address = '10.1.1.0/31'

ipv4_secondary                      ipv4_address is a secondary address::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.ipv4_secondary = True

ipv4_tag                            URIB route tag value for local/direct ipv4 routes::

                                        - Type: int()
                                        - Example:
                                            task.ipv4_tag = 200

ipv6_address                        ipv6 interface address::

                                        - Type: str()
                                        - Example:
                                            task.ipv4_address = '2001::0/127'

ipv6_tag                            URIB route tag value for local/direct ipv6 routes::

                                        - Type: int()
                                        - Example:
                                            task.ipv6_tag = 200

redirects                           Enables/disables ipv4 redirects::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.redirects = False

register                            Ansible variable to save output to::

                                        - Type: str()
                                        - Examples:
                                            task.register = 'result'

running_config                      Full path to a file containing the output of
                                    ``show running-config | section ^interface``::

                                        - Type: str()
                                        - Examples:
                                            task.running_config = '/tmp/running.cfg'

state                               Desired state after task has run::

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

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'enable lacp'

unreachables                        Enables/disables ip ICMP unreachables::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Example:
                                            task.unreachables = True
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
