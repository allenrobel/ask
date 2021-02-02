# NxosInterfaceOspf() - cisco/nxos/nxos_interface_ospf.py
our_version = 105
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_interface_ospf.py

Description:

NxosInterfaceOspf() generates Ansible Playbook tasks conformant with Ansible module nxos_interface_ospf

These tasks can be passed to Playbook().add_task()

NOTES:
    1. Ansible module nxos_interface_ospf will be deprecated 2022-10-26
    2. Use nxos_ospf_interfaces after 2022-10-26

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_interface_ospf.py

Properties:
    area                            -   Ospf area associated with this cisco_interface_ospf instance. 
                                        Valid values: str(), formatted as an IP address (i.e. "0.0.0.0") or as an integer
    bfd                             -   Enables bfd at interface level. 
                                        This overrides the bfd variable set at the ospf router level.
                                        Valid values: enable, disable. default
                                        Dependency: feature bfd
    cost                            -   The cost associated with this cisco_interface_ospf instance
    dead_interval                   -   Time interval an ospf neighbor waits for a hello packet before tearing down adjacencies.
                                        Valid values: int(), or keyword 'default'
    hello_interval                  -   Time between sending successive hello packets. 
                                        Valid values: int(), or keyword 'default'
    interface                       -   Name of this cisco_interface resource. Valid value is a string
    message_digest                  -   Enables or disables the usage of message digest authentication
                                        Valid values: no, yes
    message_digest_algorithm_type   -   Algorithm used for authentication among neighboring routers within an area.
                                        Valid values: md5, default
    message_digest_encryption_type  -   Specifies the scheme used for encrypting message_digest_password. 
                                        Valid values: 3des, cisco_type_7, default
    message_digest_key_id           -   Md5 authentication key-id associated with the ospf instance. 
                                        If this is present, message_digest_encryption_type, message_digest_algorithm_type
                                        and message_digest_password are mandatory. 
                                        Valid values: int(), or keyword 'default'
    message_digest_password         -   Specifies the message_digest password.
                                        Valid values: str()
    network                         -   Specifies interface ospf network type. 
                                        Valid values: point-to-point, broadcast
    ospf                            -   Name of the ospf instance
    passive_interface               -   Enable or disable passive-interface state on this interface
                                        Valid values: yes, no
                                            yes - (enable) Prevent OSPF from establishing an adjacency or sending routing updates on this interface.
                                            no  - (disable) Override global 'passive-interface default' for this interface.
    state                           -   Determines whether the config should be present or not on the device
                                        Valid values: absent, present
'''

class NxosInterfaceOspf(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_interface_ospf'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.valid_message_digest_algorithm_type = set()
        self.valid_message_digest_algorithm_type.add('md5')
        self.valid_message_digest_algorithm_type.add('default')

        self.valid_message_digest_encryption_type = set()
        self.valid_message_digest_encryption_type.add('3des')
        self.valid_message_digest_encryption_type.add('cisco_type_7')
        self.valid_message_digest_encryption_type.add('default')

        self.valid_network = set()
        self.valid_network.add('point-to-point')
        self.valid_network.add('broadcast')

        self.nxos_interface_ospf_valid_passive_interface = set()
        self.nxos_interface_ospf_valid_passive_interface.add('no')
        self.nxos_interface_ospf_valid_passive_interface.add('yes')

        self.nxos_interface_ospf_valid_state = set()
        self.nxos_interface_ospf_valid_state.add('present')
        self.nxos_interface_ospf_valid_state.add('absent')

        self.properties_set = set()
        self.properties_set.add('area')
        self.properties_set.add('bfd')
        self.properties_set.add('cost')
        self.properties_set.add('dead_interval')
        self.properties_set.add('hello_interval')
        self.properties_set.add('interface')
        self.properties_set.add('message_digest')
        self.properties_set.add('message_digest_algorithm_type')
        self.properties_set.add('message_digest_encryption_type')
        self.properties_set.add('message_digest_key_id')
        self.properties_set.add('message_digest_password')
        self.properties_set.add('network')
        self.properties_set.add('ospf')
        self.properties_set.add('passive_interface')
        self.properties_set.add('state')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None

    def final_verification(self):
        if self.ospf == None:
            self.task_log.error('exiting. self.ospf is is mandatory, but is not set.')
            exit(1)
        if self.interface == None:
            self.task_log.error('exiting. self.interface is is mandatory, but is not set.')
            exit(1)
        if self.message_digest_key_id != None:
            if self.message_digest_algorithm_type == None:
                self.task_log.error('exiting. message_digest_algorithm_type is mandatory, but is not set.')
                exit(1)
            if self.message_digest_encryption_type == None:
                self.task_log.error('exiting. message_digest_encryption_type is mandatory, but is not set.')
                exit(1)
            if self.message_digest_password == None:
                self.task_log.error('exiting. message_digest_password is mandatory, but is not set.')
                exit(1)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def verify_area(self, x, parameter='area'):
        if self.is_ipv4_address(x):
            return
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_area'
        expectation = '[digits or ipv4_address]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_bfd(self, x, parameter='bfd'):
        if x in ['enable', 'disable', 'default']:
            return
        source_class = self.class_name
        source_method = 'verify_bfd'
        expectation = "['enable', 'disable', 'default']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_cost(self, x, parameter='cost'):
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_cost'
        expectation = "['digits']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_dead_interval(self, x, parameter='dead_interval'):
        if self.is_digits(x):
            return
        if x in ['default']:
            return
        source_class = self.class_name
        source_method = 'verify_dead_interval'
        expectation = "['digits', 'default']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_hello_interval(self, x, parameter='hello_interval'):
        if self.is_digits(x):
            return
        if x in ['default']:
            return
        source_class = self.class_name
        source_method = 'verify_hello_interval'
        expectation = "['digits', 'default']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_interface(self, x, parameter='interface'):
        for interface_type in self.valid_ospf_interface:
            if interface_type in x:
                return
        source_class = self.class_name
        source_method = 'verify_interface'
        expectation = "OSPF Interface type: {}".format(self.valid_ospf_interface)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_message_digest(self, x, parameter='message_digest'):
        self.verify_toggle(x)

    def verify_message_digest_algorithm_type(self, x, parameter='message_digest_algorithm_type'):
        if x in self.valid_message_digest_algorithm_type:
            return
        source_class = self.class_name
        source_method = 'verify_message_digest_algorithm_type'
        expectation = "{}".format(self.valid_message_digest_algorithm_type)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_message_digest_encryption_type(self, x, parameter='message_digest_encryption_type'):
        if x in self.valid_message_digest_encryption_type:
            return
        source_class = self.class_name
        source_method = 'verify_message_digest_encryption_type'
        expectation = "{}".format(self.valid_message_digest_encryption_type)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_message_digest_key_id(self, x, parameter='message_digest_key_id'):
        if self.is_digits(x):
            return
        if x in ['default']:
            return
        source_class = self.class_name
        source_method = 'verify_message_digest_key_id'
        expectation = "['digits', 'default']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_network(self, x, parameter='network'):
        if x in self.valid_network:
            return
        source_class = self.class_name
        source_method = 'verify_network'
        expectation = "{}".format(self.valid_network)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interface_ospf_passive_interface(self, x, parameter='force'):
        verify_set = self.nxos_interface_ospf_valid_passive_interface
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_ospf_passive_interface'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interface_ospf_state(self, x, parameter='state'):
        if x in self.nxos_interface_ospf_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_ospf_state'
        expectation = ','.join(self.nxos_interface_ospf_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def area(self):
        return self.properties['area']
    @area.setter
    def area(self, x):
        parameter = 'area'
        if self.set_none(x, parameter):
            return
        self.verify_area(x, parameter)
        self.properties[parameter] = x

    @property
    def bfd(self):
        return self.properties['bfd']
    @bfd.setter
    def bfd(self, x):
        parameter = 'bfd'
        if self.set_none(x, parameter):
            return
        self.verify_bfd(x, parameter)
        self.properties[parameter] = x

    @property
    def cost(self):
        return self.properties['cost']
    @cost.setter
    def cost(self, x):
        parameter = 'cost'
        if self.set_none(x, parameter):
            return
        self.verify_cost(x, parameter)
        self.properties[parameter] = x

    @property
    def dead_interval(self):
        return self.properties['dead_interval']
    @dead_interval.setter
    def dead_interval(self, x):
        parameter = 'dead_interval'
        if self.set_none(x, parameter):
            return
        self.verify_dead_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def hello_interval(self):
        return self.properties['hello_interval']
    @hello_interval.setter
    def hello_interval(self, x):
        parameter = 'hello_interval'
        if self.set_none(x, parameter):
            return
        self.verify_hello_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def interface(self):
        return self.properties['interface']
    @interface.setter
    def interface(self, x):
        parameter = 'interface'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def message_digest(self):
        return self.properties['message_digest']
    @message_digest.setter
    def message_digest(self, x):
        parameter = 'message_digest'
        if self.set_none(x, parameter):
            return
        self.verify_message_digest(x, parameter)
        self.properties[parameter] = x

    @property
    def message_digest_algorithm_type(self):
        return self.properties['message_digest_algorithm_type']
    @message_digest_algorithm_type.setter
    def message_digest_algorithm_type(self, x):
        parameter = 'message_digest_algorithm_type'
        if self.set_none(x, parameter):
            return
        self.verify_message_digest_algorithm_type(x, parameter)
        self.properties[parameter] = x

    @property
    def message_digest_encryption_type(self):
        return self.properties['message_digest_encryption_type']
    @message_digest_encryption_type.setter
    def message_digest_encryption_type(self, x):
        parameter = 'message_digest_encryption_type'
        if self.set_none(x, parameter):
            return
        self.verify_message_digest_encryption_type(x, parameter)
        self.properties[parameter] = x

    @property
    def message_digest_key_id(self):
        return self.properties['message_digest_key_id']
    @message_digest_key_id.setter
    def message_digest_key_id(self, x):
        parameter = 'message_digest_key_id'
        if self.set_none(x, parameter):
            return
        self.verify_message_digest_key_id(x, parameter)
        self.properties[parameter] = x

    @property
    def message_digest_password(self):
        return self.properties['message_digest_password']
    @message_digest_key_id.setter
    def message_digest_password(self, x):
        parameter = 'message_digest_password'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def network(self):
        return self.properties['network']
    @network.setter
    def network(self, x):
        parameter = 'network'
        if self.set_none(x, parameter):
            return
        self.verify_network(x, parameter)
        self.properties[parameter] = x

    @property
    def ospf(self):
        return self.properties['ospf']
    @ospf.setter
    def ospf(self, x):
        parameter = 'ospf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def passive_interface(self):
        return self.properties['passive_interface']
    @passive_interface.setter
    def passive_interface(self, x):
        parameter = 'passive_interface'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_ospf_passive_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_ospf_state(x, parameter)
        self.properties[parameter] = x
