***********************************
NxosOspfInterfaces()
***********************************

.. contents::
   :local:
   :depth: 1

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
