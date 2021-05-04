# NxosOspfInterfaces() - cisco/nxos/nxos_ospf_interfaces.py
our_version = 109
from copy import deepcopy
from ask.common.task import Task
'''
***********************************
NxosOspfInterfaces()
***********************************

.. contents::
   :local:
   :depth: 1

Version
-------
109

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
                                            - cisco.nxos collection version: v2.0.2 ?
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

'''

class NxosOspfInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_ospf_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.interface_list = list()

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()

        self.properties_authentication = set()
        self.properties_authentication.add('authentication_enable')
        self.properties_authentication.add('authentication_key_chain')
        self.properties_authentication.add('authentication_message_digest')
        self.properties_authentication.add('authentication_null_auth')

        self.properties_authentication_key = set()
        self.properties_authentication_key.add('authentication_key')
        self.properties_authentication_key.add('authentication_key_encryption')

        self.properties_message_digest_key = set()
        self.properties_message_digest_key.add('message_digest_key')
        self.properties_message_digest_key.add('message_digest_key_id')
        self.properties_message_digest_key.add('message_digest_key_encryption')

        self.properties_address_family = set()
        self.properties_address_family.add('afi')
        self.properties_address_family.add('cost')
        self.properties_address_family.add('dead_interval')
        self.properties_address_family.add('default_passive_interface')
        self.properties_address_family.add('hello_interval')
        self.properties_address_family.add('instance')
        self.properties_address_family.add('mtu_ignore')
        self.properties_address_family.add('multi_areas')
        self.properties_address_family.add('network')
        self.properties_address_family.add('passive_interface')
        self.properties_address_family.add('priority')
        self.properties_address_family.add('retransmit_interval')
        self.properties_address_family.add('shutdown')
        self.properties_address_family.add('transmit_delay')

        self.properties_interface = set()
        self.properties_interface.add('name')

        self.properties_process = set()
        self.properties_process.add('process_id')
        self.properties_process.add('process_area_id')
        self.properties_process.add('process_area_secondaries')
        self.properties_process.add('process_multi_areas')

        # Maps disambiguated user properties into the property names
        # used by the Ansible module
        self.property_map = dict()
        self.property_map['authentication_enable']          = 'enable'
        self.property_map['authentication_key_chain']       = 'key_chain'
        self.property_map['authentication_message_digest']  = 'message_digest'
        self.property_map['authentication_null_auth']       = 'null_auth'
        self.property_map['authentication_key']             = 'key'
        self.property_map['authentication_key_encryption']  = 'encryption'
        self.property_map['message_digest_key_encryption']  = 'encryption'
        self.property_map['message_digest_key']             = 'key'
        self.property_map['message_digest_key_id']          = 'key_id'

        # properties_set is accessed by Task().append_to_task_name()
        # which uses it to set instance.task_name (the playbook task name)
        self.properties_set = set()
        self.properties_set.update(self.properties_process)
        self.properties_set.update(self.properties_address_family)
        self.properties_set.update(self.properties_message_digest_key)
        self.properties_set.update(self.properties_authentication)

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_ospf_interfaces_valid_afi = set()
        self.nxos_ospf_interfaces_valid_afi.add('ipv4')
        self.nxos_ospf_interfaces_valid_afi.add('ipv6')

        self.nxos_ospf_interfaces_valid_authentication_key_encryption = set()
        self.nxos_ospf_interfaces_valid_authentication_key_encryption.add(0)
        self.nxos_ospf_interfaces_valid_authentication_key_encryption.add(3)
        self.nxos_ospf_interfaces_valid_authentication_key_encryption.add(7)

        self.nxos_ospf_interfaces_valid_message_digest_key_encryption = set()
        self.nxos_ospf_interfaces_valid_message_digest_key_encryption.add(0)
        self.nxos_ospf_interfaces_valid_message_digest_key_encryption.add(3)
        self.nxos_ospf_interfaces_valid_message_digest_key_encryption.add(7)

        self.nxos_ospf_interfaces_valid_network = set()
        self.nxos_ospf_interfaces_valid_network.add('broadcast')
        self.nxos_ospf_interfaces_valid_network.add('point-to-point')

        self.nxos_ospf_interfaces_valid_state = set()
        self.nxos_ospf_interfaces_valid_state.add('deleted')
        self.nxos_ospf_interfaces_valid_state.add('gathered')
        self.nxos_ospf_interfaces_valid_state.add('merged')
        self.nxos_ospf_interfaces_valid_state.add('overridden')
        self.nxos_ospf_interfaces_valid_state.add('parsed')
        self.nxos_ospf_interfaces_valid_state.add('rendered')
        self.nxos_ospf_interfaces_valid_state.add('replaced')

        self.nxos_ospf_interfaces_cost_min = 1
        self.nxos_ospf_interfaces_cost_max = 65535

        self.nxos_ospf_interfaces_dead_interval_min = 1
        self.nxos_ospf_interfaces_dead_interval_max = 65535

        self.nxos_ospf_interfaces_hello_interval_min = 1
        self.nxos_ospf_interfaces_hello_interval_max = 65535
        self.nxos_ospf_interfaces_hello_interval_default = 10

        self.nxos_ospf_interfaces_retransmit_interval_min = 1
        self.nxos_ospf_interfaces_retransmit_interval_max = 65535
        self.nxos_ospf_interfaces_retransmit_interval_default = 5

        self.nxos_ospf_interfaces_priority_min = 0
        self.nxos_ospf_interfaces_priority_max = 255
        self.nxos_ospf_interfaces_priority_default = 1

        self.nxos_ospf_interfaces_transmit_delay_min = 1
        self.nxos_ospf_interfaces_transmit_delay_max = 450
        self.nxos_ospf_interfaces_transmit_delay_default = 1

        self.nxos_ospf_interfaces_process_id_min = 1
        self.nxos_ospf_interfaces_process_id_max = 65535

        self.init_properties()

    def init_properties_authentication(self):
        for p in self.properties_authentication:
            self.properties[p] = None

    def init_properties_authentication_key(self):
        for p in self.properties_authentication_key:
            self.properties[p] = None

    def init_properties_message_digest_key(self):
        for p in self.properties_message_digest_key:
            self.properties[p] = None

    def init_properties_address_family(self):
        self.processes = list()
        for p in self.properties_address_family:
            self.properties[p] = None
        self.init_properties_authentication()
        self.init_properties_authentication_key()
        self.init_properties_message_digest_key()

    def init_properties_process(self):
        for p in self.properties_process:
            self.properties[p] = None

    def init_properties(self):
        self.properties = dict()
        self.address_family = list()
        self.init_properties_address_family()
        self.init_properties_process()
        self.init_properties_interface()
        self.properties['state'] = None

    def verify_area(self):
        if self.process_area_id == None:
            self.task_log.error('exiting. instance.process_area_id must be set prior to adding area info to an ospf process')
            exit(1)

    def verify_address_family(self):
        if self.afi == None:
            self.task_log.error('exiting. instance.afi must be set prior to calling instance.add_address_family()')
            exit(1)
        if self.passive_interface != None and self.default_passive_interface != None:
            self.task_log.error('exiting. instance.passive_interface is mutually-exclusive with instance.default_passive_interface.  Unset one or the other.')
            exit(1)

    def verify_process(self):
        if self.process_id == None:
            self.task_log.error('exiting. instance.process_id must be set prior to calling instance.add_process()')
            exit(1)
    def add_process(self):
        self.verify_process()
        process = dict()
        area = dict()
        if self.process_area_id != None:
            area['area_id'] = self.process_area_id
        if self.process_area_secondaries != None:
            area['secondaries'] = self.process_area_secondaries
        if len(area) != 0:
            self.verify_area()
            process['area'] = deepcopy(area)

        if self.process_multi_areas != None:
            process['multi_areas'] = self.process_multi_areas
        if self.process_id != None:
            process['process_id'] = self.process_id
        self.processes.append(deepcopy(process))
        self.init_properties_process()

    def add_authentication(self):
        d = dict()
        for p in self.properties_authentication:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) == 0:
            return False
        return deepcopy(d)

    def add_authentication_key(self):
        d = dict()
        for p in self.properties_authentication_key:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) == 0:
            return False
        return deepcopy(d)

    def add_message_digest_key(self):
        d = dict()
        for p in self.properties_message_digest_key:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) == 0:
            return False
        return deepcopy(d)

    def add_address_family(self):
        self.verify_address_family()
        d = dict()
        authentication = self.add_authentication()
        authentication_key = self.add_authentication_key()
        message_digest_key = self.add_message_digest_key()
        if authentication != False:
            d['authentication'] = authentication
        if authentication_key != False:
            d['authentication_key'] = authentication_key
        if message_digest_key != False:
            d['message_digest_key'] = message_digest_key
        if len(self.processes) != 0:
            d['processes'] = self.processes
        for p in self.properties_address_family:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.address_family.append(deepcopy(d))
        self.init_properties_address_family()

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['config'] = deepcopy(self.interface_list)
        self.ansible_task[self.ansible_module]['state'] = self.state

    def init_properties_interface(self):
        for p in self.properties_interface:
            self.properties[p] = None
    def verify_interface_properties(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.add_interface()')
            exit(1)
    def add_interface(self):
        self.verify_interface_properties()
        d = dict()
        d['address_family'] = self.address_family
        for p in self.properties_interface:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        if len(d) == 0:
            self.task_log.error('exiting. Set at least one interface property before calling instance.interface()')
            exit(1)
        self.interface_list.append(deepcopy(d))
        self.address_family = list()
        self.init_properties_address_family()
        self.init_properties_process()
        self.init_properties_interface()

    def verify_nxos_ospf_interfaces_afi(self, x, parameter='receive'):
        verify_set = self.nxos_ospf_interfaces_valid_afi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_afi'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_authentication_key_encryption(self, x, parameter='authentication_key_encryption'):
        verify_set = self.nxos_ospf_interfaces_valid_authentication_key_encryption
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_authentication_key_encryption'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_cost(self, x, parameter='cost'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_cost'
        range_min = self.nxos_ospf_interfaces_cost_min
        range_max = self.nxos_ospf_interfaces_cost_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_dead_interval(self, x, parameter='dead_interval'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_dead_interval'
        range_min = self.nxos_ospf_interfaces_dead_interval_min
        range_max = self.nxos_ospf_interfaces_dead_interval_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_hello_interval(self, x, parameter='hello_interval'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_hello_interval'
        range_min = self.nxos_ospf_interfaces_hello_interval_min
        range_max = self.nxos_ospf_interfaces_hello_interval_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_message_digest_key_encryption(self, x, parameter='message_digest_key_encryption'):
        verify_set = self.nxos_ospf_interfaces_valid_message_digest_key_encryption
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_message_digest_key_encryption'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_message_digest_key_id(self, x, parameter='message_digest_key_id'):
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_message_digest_key_id'
        expectation = 'int()'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_multi_areas(self, x, parameter='multi_areas'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_multi_areas'
        expectation = 'python list() containing int() or ipv4 ip address e.g. [10, 1.1.1.1]'
        if type(x) != type(list()):
            self.fail(source_class, source_method, x, parameter, expectation)
        bad_item = False
        for item in x:
            if self.is_digits(item):
                continue
            if self.is_ipv4_unicast_address(item):
                continue
            bad_item = True
        if bad_item == True:
            self.fail(source_class, source_method, x, parameter, expectation)            

    def verify_nxos_ospf_interfaces_network(self, x, parameter='network'):
        verify_set = self.nxos_ospf_interfaces_valid_network
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_network'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_priority(self, x, parameter='priority'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_priority'
        range_min = self.nxos_ospf_interfaces_priority_min
        range_max = self.nxos_ospf_interfaces_priority_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_process_id(self, x, parameter='process_id'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_process_id'
        range_min = self.nxos_ospf_interfaces_process_id_min
        range_max = self.nxos_ospf_interfaces_process_id_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_process_area_id(self, x, parameter='area_id'):
        if self.is_ipv4_unicast_address(x):
            return
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_process_area_id'
        expectation = 'digits, or ipv4 unicast address without prefixlen/mask e.g. 10, 1.1.1.1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_process_multi_areas(self, x, parameter='process_multi_areas'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_process_multi_areas'
        expectation = 'python list() containing int() or ipv4 ip address e.g. [10, 1.1.1.1]'
        if type(x) != type(list()):
            self.fail(source_class, source_method, x, parameter, expectation)
        bad_item = False
        for item in x:
            if self.is_digits(item):
                continue
            if self.is_ipv4_unicast_address(item):
                continue
            bad_item = True
        if bad_item == True:
            self.fail(source_class, source_method, x, parameter, expectation)            

    def verify_nxos_ospf_interfaces_retransmit_interval(self, x, parameter='retransmit_interval'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_retransmit_interval'
        range_min = self.nxos_ospf_interfaces_retransmit_interval_min
        range_max = self.nxos_ospf_interfaces_retransmit_interval_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_state(self, x, parameter='state'):
        verify_set = self.nxos_ospf_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_transmit_delay(self, x, parameter='transmit_delay'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_transmit_delay'
        range_min = self.nxos_ospf_interfaces_transmit_delay_min
        range_max = self.nxos_ospf_interfaces_transmit_delay_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def authentication_enable(self):
        return self.properties['authentication_enable']
    @authentication_enable.setter
    def authentication_enable(self, x):
        parameter = 'authentication_enable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def authentication_key_chain(self):
        return self.properties['authentication_key_chain']
    @authentication_key_chain.setter
    def authentication_key_chain(self, x):
        parameter = 'authentication_key_chain'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def authentication_message_digest(self):
        return self.properties['authentication_message_digest']
    @authentication_message_digest.setter
    def authentication_message_digest(self, x):
        parameter = 'authentication_message_digest'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def authentication_null_auth(self):
        return self.properties['authentication_null_auth']
    @authentication_null_auth.setter
    def authentication_null_auth(self, x):
        parameter = 'authentication_null_auth'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def authentication_key_encryption(self):
        return self.properties['authentication_key_encryption']
    @authentication_key_encryption.setter
    def authentication_key_encryption(self, x):
        parameter = 'authentication_key_encryption'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_authentication_key_encryption(x, parameter)
        self.properties[parameter] = x

    @property
    def authentication_key(self):
        return self.properties['authentication_key']
    @authentication_key.setter
    def authentication_key(self, x):
        parameter = 'authentication_key'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def cost(self):
        return self.properties['cost']
    @cost.setter
    def cost(self, x):
        parameter = 'cost'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_cost(x, parameter)
        self.properties[parameter] = x

    @property
    def dead_interval(self):
        return self.properties['dead_interval']
    @dead_interval.setter
    def dead_interval(self, x):
        parameter = 'dead_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_dead_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def default_passive_interface(self):
        return self.properties['default_passive_interface']
    @default_passive_interface.setter
    def default_passive_interface(self, x):
        parameter = 'default_passive_interface'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def hello_interval(self):
        return self.properties['hello_interval']
    @hello_interval.setter
    def hello_interval(self, x):
        parameter = 'hello_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_hello_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def instance(self):
        return self.properties['instance']
    @instance.setter
    def instance(self, x):
        parameter = 'instance'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def message_digest_key_encryption(self):
        return self.properties['message_digest_key_encryption']
    @message_digest_key_encryption.setter
    def message_digest_key_encryption(self, x):
        parameter = 'message_digest_key_encryption'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_message_digest_key_encryption(x, parameter)
        self.properties[parameter] = x

    @property
    def message_digest_key(self):
        return self.properties['message_digest_key']
    @message_digest_key.setter
    def message_digest_key(self, x):
        parameter = 'message_digest_key'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def message_digest_key_id(self):
        return self.properties['message_digest_key_id']
    @message_digest_key_id.setter
    def message_digest_key_id(self, x):
        parameter = 'message_digest_key_id'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_message_digest_key_id(x, parameter)
        self.properties[parameter] = int(x)

    @property
    def mtu_ignore(self):
        return self.properties['mtu_ignore']
    @mtu_ignore.setter
    def mtu_ignore(self, x):
        parameter = 'mtu_ignore'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def multi_areas(self):
        return self.properties['multi_areas']
    @multi_areas.setter
    def multi_areas(self, x):
        parameter = 'multi_areas'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_multi_areas(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter) # inherited from AnsCommon()
        self.properties[parameter] = x

    @property
    def network(self):
        return self.properties['network']
    @network.setter
    def network(self, x):
        parameter = 'network'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_network(x, parameter)
        self.properties[parameter] = x

    @property
    def passive_interface(self):
        return self.properties['passive_interface']
    @passive_interface.setter
    def passive_interface(self, x):
        parameter = 'passive_interface'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def priority(self):
        return self.properties['priority']
    @priority.setter
    def priority(self, x):
        parameter = 'priority'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_priority(x, parameter)
        self.properties[parameter] = x

    @property
    def process_area_id(self):
        return self.properties['process_area_id']
    @process_area_id.setter
    def process_area_id(self, x):
        parameter = 'process_area_id'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_process_area_id(x, parameter)
        self.properties[parameter] = x

    @property
    def process_area_secondaries(self):
        return self.properties['process_area_secondaries']
    @process_area_secondaries.setter
    def process_area_secondaries(self, x):
        parameter = 'process_area_secondaries'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def process_multi_areas(self):
        return self.properties['process_multi_areas']
    @process_multi_areas.setter
    def process_multi_areas(self, x):
        parameter = 'process_multi_areas'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_process_multi_areas(x, parameter)
        self.properties[parameter] = x

    @property
    def process_id(self):
        return self.properties['process_id']
    @process_id.setter
    def process_id(self, x):
        parameter = 'process_id'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_process_id(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def retransmit_interval(self):
        return self.properties['retransmit_interval']
    @retransmit_interval.setter
    def retransmit_interval(self, x):
        parameter = 'retransmit_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_retransmit_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def shutdown(self):
        self.task_log.info('DEBUG: returning self.properties[shutdown] {}'.format(self.properties['shutdown']))
        return self.properties['shutdown']
    @shutdown.setter
    def shutdown(self, x):
        parameter = 'shutdown'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_state(x, parameter)
        self.properties[parameter] = x

    @property
    def transmit_delay(self):
        return self.properties['transmit_delay']
    @transmit_delay.setter
    def transmit_delay(self, x):
        parameter = 'transmit_delay'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ospf_interfaces_transmit_delay(x, parameter)
        self.properties[parameter] = x
