***********************************
NxosOspfInterfaces()
***********************************

.. contents::
   :local:
   :depth: 1

Version
-------
110

ScriptKit Synopsis
------------------
- NxosOspfInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_ospf_interfaces
- These can then be passed to Playbook().add_task()


Ansible Module Documentation
----------------------------
- `cisco.nxos.nxos_ospf_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_ospf_interfaces_module.rst>`_


ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_ospf_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_ospf_interfaces.py>`_

Caveats
-------
-  `#264 nxos_ospf_interfaces: no ip ospf passive-interface is never issued. <https://github.com/ansible-collections/cisco.nxos/issues/264>`_

|

============================    ==============================================
Method                          Description
============================    ==============================================
add_interface()                 Add an interface to the configuration::

                                    - Type: function()
                                    - Example:
                                        #!/usr/bin/env python3
                                        # Configure OSPF ipv4 and ipv6 afi on 5 interfaces
                                        from ask.cisco.nxos.nxos_ospf_interfaces import NxosOspfInterfaces
                                        from ask.common.log import Log
                                        from ask.common.playbook import Playbook
                                        log_level_console = 'INFO'
                                        log_level_file = 'DEBUG'
                                        log = Log('my_log', log_level_console, log_level_file)
                                        pb = Playbook(log)
                                        pb.profile_nxos()
                                        pb.ansible_password = 'mypassword'
                                        pb.name = 'Example nxos_ospf_interfaces'
                                        pb.add_host('dc-101')
                                        pb.file = '/tmp/nxos_ospf_interfaces.yaml'
                                        task = NxosOspfInterfaces(log)
                                        task.append_to_task_name('OSPF enable:')
                                        for port in range(1,6):
                                            task.name = 'Ethernet1/{}'.format(port)
                                            # ospf general interface properties
                                            task.mtu_ignore = False
                                            task.network = 'point-to-point'
                                            task.passive_interface = False

                                            # ospf ipv4 afi
                                            task.afi = 'ipv4'
                                            task.cost = 100
                                            task.process_area_id = 0
                                            task.process_id = 1
                                            task.add_process()
                                            task.add_address_family()

                                            # ospf ipv6 afi 
                                            # Requires 'feature ospfv3' to be enabled
                                            task.afi = 'ipv6'
                                            task.cost = 100
                                            task.process_area_id = 0
                                            task.process_id = 1
                                            task.add_process()
                                            task.add_address_family()

                                            task.append_to_task_name(task.name)
                                            task.add_interface()
                                        task.state = 'merged'
                                        task.update()
                                        pb.add_task(task)
                                        pb.append_playbook()
                                        pb.write_playbook()

                                    - Resulting task (all but two interfaces removed)

                                        tasks:
                                        -   cisco.nxos.nxos_ospf_interfaces:
                                                config:
                                                -   address_family:
                                                    -   afi: ipv4
                                                        cost: 100
                                                        mtu_ignore: false
                                                        network: point-to-point
                                                        passive_interface: false
                                                        processes:
                                                        -   area:
                                                                area_id: 0
                                                            process_id: '1'
                                                    -   afi: ipv6
                                                        cost: 100
                                                        processes:
                                                        -   area:
                                                                area_id: 0
                                                            process_id: '1'
                                                    name: Ethernet1/1
                                                -   address_family:
                                                    -   afi: ipv4
                                                        cost: 100
                                                        mtu_ignore: false
                                                        network: point-to-point
                                                        passive_interface: false
                                                        processes:
                                                        -   area:
                                                                area_id: 0
                                                            process_id: '1'
                                                    -   afi: ipv6
                                                        cost: 100
                                                        processes:
                                                        -   area:
                                                                area_id: 0
                                                            process_id: '1'
                                                    name: Ethernet1/2
                                                state: merged
                                            name: '[cisco.nxos.nxos_ospf_interfaces : v.106], OSPF enable:, Ethernet1/1,
                                                Ethernet1/2, Ethernet1/3, Ethernet1/4, Ethernet1/5'

add_process()                   Add an ospf process to an interface::

                                    - Type: function()
                                    - Example: See add_interface()

add_address_family()            Add an ospf afi (ipv4 or ipv6) to an interface::

                                    - Type: function()
                                    - Example: See add_interface()

============================    ==============================================

|

======================================  ==================================================
Module Properties                       Description
======================================  ==================================================
state                                   Desired state after task completion::

                                            - Type: str()
                                            - Valid values:
                                                - deleted
                                                - gathered
                                                - merged
                                                - overridden
                                                - parsed (not currently supported by ScriptKit)
                                                - rendered
                                                - replaced
                                            - Example:
                                                task.state = 'merged'
                                            - Required

task_name                               Name of the task (Ansible will print this when the task
                                        is run)::

                                            - Type: str()
                                            - Example:
                                                task.name = 'my task'

======================================  ==================================================

|
|

======================================  ==================================================
Config Properties                       Description
======================================  ==================================================
name                                    Full name of the interface to be configured::

                                            - Type: str()
                                            - Example:
                                                task.name = 'Ethernet1/1'
                                                task.name = 'port-channel3'
                                            - Required

======================================  ==================================================

|
|

======================================  ==================================================
Address Family Properties / Methods     Description
======================================  ==================================================
add_address_family()                    Applies address-family properties, and resets them
                                        to None.  Call instance.add_address_family() after
                                        setting the properties in this table::

                                            - Type: method
                                            - Example:
                                                task.afi = 'ipv4'
                                                task.cost = 20
                                                task.instance = 100
                                                task.add_address_family()
                                                task.afi = 'ipv6'
                                                task.cost = 20
                                                task.instance = 100
                                                task.add_address_family()

afi                                     Address Family Identifier (AFI) for OSPF interface
                                        configuration::

                                            - Type: str()
                                            - Valid values:
                                                - ipv4
                                                - ipv6
                                            - Example:
                                                task.afi = 'ipv4'

authentication_enable                   Enable/disable authentication on the interface::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.authentication_enable = True

authentication_key_chain                Authentication password key-chain::

                                            - Type: str()
                                            - Example:
                                                task.authentication_key_chain = 'fizbang'

authentication_message_digest           Use message-digest authentication::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.authentication_message_digest = True

authentication_null_auth                Use null(disable) authentication::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.authentication_null_auth = False

authentication_key_encryption           Authentication key encryption type::

                                            - Type: int()
                                            - Valid values:
                                                - 0  : UNENCRYPTED
                                                - 3  : 3DES ENCRYPTED
                                                - 7  : Cisco type 7 ENCRYPTED
                                            - Example:
                                                task.authentication_key_encryption = 7

authentication_key                      Authentication key for the interface::

                                            - Type: str()
                                            - Example:
                                                task.authentication_key = 'fizbang'
                                            - Required

cost                                    OSPF cost associated with interface::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-65535
                                            - Example:
                                                task.cost = 200

dead_interval                           OSPF dead interval::

                                            - Type: int()
                                            - Units: seconds
                                            - Valid values:
                                                - range: 1-65535
                                            - Example:
                                                task.dead_interval = 3

default_passive_interface               Remove any passive-interface configuration from the interface.
                                        This issues the following on the interface
                                        'default ip ospf passive-interface'
                                        'default ipv6 ospf passive-interface'::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - cisco.nxos collection version:  v2.3.0
                                            - Example:
                                                task.default_passive_interface = True
                                            - NOTES:
                                                1. mutually-exclusive with passive_interface

hello_interval                          Frequency of hello message transmission::

                                            - Type: int()
                                            - Units: seconds
                                            - Default: 10
                                            - Valid values:
                                                - range: 1-65535
                                            - Example:
                                                task.hello_interval = 1

instance                                OSPF instance identifier associated
                                        with the interface::

                                            - Type: int()
                                            - Example:
                                                task.instance = 100

message_digest_key_encryption           Message digest authentication encryption
                                        type::

                                            - Type: int()
                                            - Valid values:
                                                - 0  : UNENCRYPTED
                                                - 3  : 3DES ENCRYPTED
                                                - 7  : Cisco type 7 ENCRYPTED
                                            - Example:
                                                task.message_digest_key_encryption = 7

message_digest_key                      Authentication key::

                                            - Type: str()
                                            - Example:
                                                task.message_digest_key = 'fizbang'
                                            - Required

message_digest_key_id                   Key ID::

                                            - Type: int()
                                            - Example:
                                                task.message_digest_key_id = 2
                                            - Required

mtu_ignore                              Enable/disable OSPF MTU mismatch detection::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.mtu_ignore = False

multi_areas                             Multi-Areas associated with interface (not tied
                                        to OSPF process)::

                                            - Type: list() of OSPF area IDs
                                            - Example:
                                                areas = list()
                                                areas.append(10)
                                                areas.append('0.0.0.17')
                                                task.multi_areas = areas

network                                 OSPF Network type of the interface::

                                            - Type: str()
                                            - Valid values:
                                                - broadcast
                                                - point-to-point
                                            - Example:
                                                task.network = 'point-to-point'

passive_interface                       Suppress routing updates on the interface::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.passive_interface = False
                                            - NOTES:
                                                1. mutually-exclusive with default_passive_interface

priority                                Router priority::

                                            - Type: int()
                                            - Example:
                                                task.priority = 100

retransmit_interval                     Packet retransmission interval::

                                            - Type: int()
                                            - Units: seconds
                                            - Default: 5
                                            - Valid values:
                                                - range: 1-65535
                                            - Example:
                                                task.retransmit_interval = 2

shutdown                                Shutdown OSPF on this interface::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.shutdown = False

transmit_delay                          Packet transmission delay::

                                            - Type: int()
                                            - Units: seconds
                                            - Default: 1
                                            - Valid values:
                                                - range: 1-450
                                            - Example:
                                                task.transmit_delay = 3

======================================  ==================================================

|
|

======================================  ==================================================
OSPF Process Properties /Methods        Description
======================================  ==================================================
add_process()                           Applies OSPF process properties, and resets them
                                        to None.  Call instance.add_process() after
                                        setting the properties in this table::

                                            - Type: method
                                            - Example:
                                                task.process_area_id = 0
                                                task.process_secondaries = 'no'
                                                task.process_multi_areas = [11, 21]
                                                task.process_id = 1
                                                task.add_process()

process_id                              OSPF process ID associated with the interface::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-65535
                                            - Example:
                                                task.process_id = 100
                                            - Required

process_area_id                         OSPF Area ID as a decimal or dotted decimal
                                        address format::

                                            - Type: int() or str()
                                            - Valid values:
                                                - int()
                                                - ipv4 address format
                                                    - though not necessarily an
                                                      actual address
                                            - Example:
                                                task.process_area_id = 0
                                                task.process_area_id = '0.0.0.20'
                                                task.process_area_id = '10.1.1.1'

process_area_secondaries                Include secondary IPv4/IPv6 addresses::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.process_area_secondaries = False

process_multi_areas                     Multi-Areas associated with interface (not
                                        tied to OSPF process)::

                                            - Type: list() of OSPF area IDs
                                            - Example:
                                                areas = list()
                                                areas.append(10)
                                                areas.append('0.0.0.17')
                                                task.process_multi_areas = areas

======================================  ==================================================

|

NOTES
=====

1. Properties names which differ from the Ansible Module

================    ==============================
Ansible Module      ScriptKit
================    ==============================
enable              authentication_enable
key_chain           authentication_key_chain
message_digest      authentication_message_digest
null_auth           authentication_null_auth
key_encryption      authentication_key_encryption
key                 authentication_key
key_encryption      message_digest_key_encryption
key                 message_digest_key
key_id              message_digest_key_id
area_id             process_area_id
area_secondaries    process_area_secondaries
multi_areas         process_multi_areas
multi_areas         multi_areas
================    ==============================


2. multi_areas property

- Appears under both address_family and processes
- Use task.process_multi_areas when adding to a process
- Use task.multi_areas when adding to an address_family 


Authors
~~~~~~~

- Allen Robel (@PacketCalc)

