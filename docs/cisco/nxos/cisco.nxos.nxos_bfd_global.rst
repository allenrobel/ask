***********************************
NxosBfdGlobal()
***********************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosBfdGlobal() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bfd_global
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bfd_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bfd_global_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bfd_global.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bfd_global.py>`_

Notes
-----
This class deviates from the Ansible module for certain property
names to disambiguate them. See the table below for details.

|

============================    ==============================================
Property                        Description
============================    ==============================================
bfd_fabricpath_interval         BFD fabricpath session interval::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999
                                    - Example:
                                        task.bfd_fabricpath_interval = 999

bfd_fabricpath_min_rx           Minimum RX interval for fabricpath sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999
                                    - Example:
                                        task.bfd_fabricpath_min_rx = 50


bfd_fabricpath_multiplier       Detect multiplier for fabricpath bfd sessions::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.bfd_fabricpath_multiplier = 3

bfd_interval                    TX interval::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_interval = 999

bfd_min_rx                      Minimum RX interval::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values: range: 50-999  
                                    - Example:
                                        task.bfd_min_rx = 50

bfd_multiplier                  Detect multiplier for bfd sessions::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.bfd_multiplier = 3

bfd_ipv4_interval               TX interval for ipv4 sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_ipv4_interval = 999

bfd_ipv4_min_rx                 Minimum RX interval for ipv4 sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_ipv4_min_rx = 50

bfd_ipv4_multiplier             Detect multiplier for ipv4 bfd sessions::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.bfd_ipv4_multiplier = 3

bfd_ipv6_interval               TX interval for ipv6 sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_ipv6_interval = 999

bfd_ipv6_min_rx                 Minimum RX interval for ipv6 sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_ipv6_min_rx = 50

bfd_ipv6_multiplier             Detect multiplier for ipv6 bfd sessions::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.bfd_ipv6_multiplier = 3

echo_interface                  Interface used for bfd echo frames::

                                    - Type: str()
                                    - Valid values:
                                        - A loopback interface
                                        - The keyword 'deleted'
                                    - Examples:
                                        - task.echo_interface = 'Loopback2'
                                        - task.echo_interface = 'deleted'

echo_rx_interval                BFD session echo rx interval::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.echo_rx_interval = 3

fabricpath_slow_timer           BFD fabricpath slow rate timer::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.fabricpath_slow_timer = 10

fabricpath_vlan                 BFD fabricpath control vlan::

                                    - Type: int()
                                    - Unit: vlan ID
                                    - Example:
                                        task.fabricpath_vlan = 2002

ipv4_echo_rx_interval           Echo rx-interval for ipv4 BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999
                                    - Example:
                                        task.ipv4_echo_rx_interval = 50

ipv4_slow_timer                 Slow mode timer for ipv4 BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1000-30000
                                    - Example:
                                        task.ipv4_slow_timer = 2000

ipv6_echo_rx_interval           Echo rx-interval for ipv6 BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999
                                    - Example:
                                        task.ipv6_echo_rx_interval = 50

ipv6_slow_timer                 Slow mode timer for ipv6 BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1000-30000
                                    - Example:
                                        task.ipv6_slow_timer = 2000

slow_timer                      Slow mode timer for BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1000-30000
                                    - Example:
                                        task.slow_timer = 2000

startup_timer                   Delayed Start Up timer for BFD sessions::

                                    - Type: int()
                                    - Unit: seconds
                                    - Valid values:
                                        - range: 0-30
                                    - Example:
                                        task.startup_timer = 20

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
