# NxosOspfInterfaces() - cisco/nxos/nxos_ospf_interfaces.py
our_version = 103
from copy import deepcopy
from ask.common.task import Task
'''
nxos_ospf_interfaces.py
-----------------------

Description
-----------

NxosOspfInterfaces() generates Ansible Playbook tasks conformant with nxos_ospf_interfaces
which can be fed to Playbook().add_task()

Example usage
-------------
    unit_test/cisco/nxos/unit_test_nxos_ospf_interfaces.py

Properties
----------

    Address Family Properties
    -------------------------
    - call instance.add_address_family() after setting these

    afi                             -   Address Family Identifier (AFI) for OSPF settings on the interfaces
    authentication_enable           -   Enable/disable authentication on the interface
                                        Valid values: no, yes
    authentication_key_chain        -   Authentication password key-chain
                                        Valid values: str()
    authentication_message_digest   -   Use message-digest authentication
                                        Valid values: no, yes
    authentication_null_auth        -   Use null(disable) authentication
                                        Valid values: no, yes
    authentication_key_encryption   -   authentication key encryption type
                                        Valid values: 0, 3, 7
                                            0 UNENCRYPTED
                                            3 3DES ENCRYPTED
                                            7 Cisco type 7 ENCRYPTED
    authentication_key              -   Authentication key for the interface
                                        Valid values: str()
                                        Required
    cost                            -   Cost associated with interface
                                        Valid values: int() range: 1-65535
    dead_interval                   -   Dead interval value (in seconds)
                                        Valid values: int() range: 1-65535
    hello_interval                  -   Frequency (in seconds) of hello message transmission
                                        Valid values: int() range: 1-65535
                                        Default: 10
    instance                        -   Instance identifier
    message_digest_key_encryption   -   Message digest authentication encryption type
                                        Valid values: 0, 3, 7
                                            0 UNENCRYPTED
                                            3 3DES ENCRYPTED
                                            7 Cisco type 7 ENCRYPTED
    message_digest_key              -   Authentication key
                                        Valid values: str()
                                        Required
    message_digest_key_id           -   key ID
                                        Required
    mtu_ignore                      -   Enable/disable OSPF MTU mismatch detection
                                        Valid values: no, yes
    multi_areas                     -   Multi-Areas associated with interface (not tied to OSPF process)
                                        Valid values: python list() of Area Ids as int() or IP address
                                        Example: [10, 30, '10.1.1.1', '45.1.1.0']
    network                         -   Network type of interface
                                        Valid  values: broadcast, point-to-point
    passive_interface               -   Suppress routing updates on the interface
                                        Valid values: no, yes
    priority                        -   Router priority
                                        Valid values: int()
    retransmit_interval             -   Packet retransmission interval
                                        Valid values: int() range: 1-65535
                                        Default: 5
    shutdown                        -   Shutdown OSPF on this interface
                                        Valid values: no, yes
    transmit_delay                  -   Packet transmission delay
                                        Valid values: int() range: 1-450
                                        Default: 1

    OSPF Process Properties
    -----------------------
    - call instance.add_process() after setting these

    process_id                      -   OSPF process tag
                                        Valid values: str()
                                        Required
    process_area_id                 -   ip Area ID
                                        Valid values: int() or IP address
    process_area_secondaries        -   (Do not)? include secondary IPv4/IPv6 addresses
                                        Valid values: no, yes
    process_multi_areas             -   Multi-Areas associated with interface (not tied to OSPF process)
                                        Valid values: python list() of Area Ids as int() or IP address
                                        Example: [10, 30, '10.1.1.1', '45.1.1.0']

    Config Properties
    -----------------
    name                            -   Full name of interface, e.g. Ethernet1/1
                                        Required

    Module Properties
    -----------------
    state                           -   Valid values: deleted, gathered, merged, overridden, parsed, rendered, replaced
                                        Required
'''

class NxosOspfInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_ospf_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
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

        self.cost_min = 1
        self.cost_max = 65535

        self.dead_interval_min = 1
        self.dead_interval_max = 65535

        self.hello_interval_min = 1
        self.hello_interval_max = 65535
        self.hello_interval_default = 10

        self.retransmit_interval_min = 1
        self.retransmit_interval_max = 65535
        self.retransmit_interval_default = 5

        self.priority_min = 0
        self.priority_max = 255
        self.priority_default = 1

        self.transmit_delay_min = 1
        self.transmit_delay_max = 450
        self.transmit_delay_default = 1

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
        self.properties['name'] = None
        self.properties['state'] = None

    def verify_area(self):
        if self.process_area_id == None:
            self.task_log.error('exiting. instance.process_area_id must be set prior to adding area info to an ospf process')
            exit(1)
    def verify_address_family(self):
        if self.afi == None:
            self.task_log.error('exiting. instance.afi must be set prior to calling instance.add_address_family()')
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
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.update()')
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        d = dict()
        d['address_family'] = self.address_family
        d['name'] = self.name
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['config'].append(deepcopy(d))
        self.ansible_task[self.ansible_module]['state'] = self.state

        self.init_properties()

    def verify_nxos_ospf_interfaces_afi(self, x, parameter='receive'):
        if x in self.nxos_ospf_interfaces_valid_afi:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_afi'
        expectation = ','.join(self.nxos_ospf_interfaces_valid_afi)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_authentication_key_encryption(self, x, parameter='authentication_key_encryption'):
        if x in self.nxos_ospf_interfaces_valid_authentication_key_encryption:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_authentication_key_encryption'
        expectation = ','.join(self.nxos_ospf_interfaces_valid_authentication_key_encryption)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_cost(self, x, parameter='cost'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_cost'
        self.verify_integer_range(x, self.cost_min, self.cost_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_dead_interval(self, x, parameter='dead_interval'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_dead_interval'
        self.verify_integer_range(x, self.dead_interval_min, self.dead_interval_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_hello_interval(self, x, parameter='hello_interval'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_hello_interval'
        self.verify_integer_range(x, self.hello_interval_min, self.hello_interval_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_message_digest_key_encryption(self, x, parameter='message_digest_key_encryption'):
        if x in self.nxos_ospf_interfaces_valid_message_digest_key_encryption:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_message_digest_key_encryption'
        expectation = ','.join(self.nxos_ospf_interfaces_valid_message_digest_key_encryption)
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
        if x in self.nxos_ospf_interfaces_valid_network:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_network'
        expectation = ','.join(self.nxos_ospf_interfaces_valid_network)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_priority(self, x, parameter='priority'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_priority'
        self.verify_integer_range(x, self.priority_min, self.priority_max, source_class, source_method)

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
        self.verify_integer_range(x, self.retransmit_interval_min, self.retransmit_interval_max, source_class, source_method)

    def verify_nxos_ospf_interfaces_state(self, x, parameter='state'):
        if x in self.nxos_ospf_interfaces_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_state'
        expectation = ','.join(self.nxos_ospf_interfaces_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ospf_interfaces_transmit_delay(self, x, parameter='transmit_delay'):
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_interfaces_transmit_delay'
        self.verify_integer_range(x, self.transmit_delay_min, self.transmit_delay_max, source_class, source_method)


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
        self.verify_toggle(x, parameter)
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
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def authentication_null_auth(self):
        return self.properties['authentication_null_auth']
    @authentication_null_auth.setter
    def authentication_null_auth(self, x):
        parameter = 'authentication_null_auth'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
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
        self.verify_toggle(x, parameter)
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
        self.verify_toggle(x, parameter)
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
        self.verify_toggle(x, parameter)
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
        self.properties[parameter] = x

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
        self.verify_toggle(x, parameter)
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
