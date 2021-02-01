# AskNxosInterfaceOspf() - python/lib3/ask_task_nxos_interface_ospf.py
our_version = 104
from ask_task import AskTask
'''
Name: ask_task_nxos_interface_ospf.py
Author: Allen Robel
Email: arobel@cisco.com
Description:

AskNxosInterfaceOspf() generates Ansible Playbook tasks conformant with Ansible module nxos_interface_ospf

These tasks can be passed to AnsPlaybook().add_task()

NOTES:
    1. Ansible module nxos_interface_ospf will be deprecated 2022-10-26
    2. Use nxos_ospf_interfaces after 2022-10-26

Revision history: Use git log

Example usage:

#!/usr/bin/env python3
from ans_playbook import AnsPlaybook
from ask_task_nxos_interface_ospf import AskNxosInterfaceOspf
from log import get_logger

module_name = 'cisco.nxos.nxos_interface_ospf'
log = get_logger('test_ask_task_{}'.format(module_name), 'INFO', 'DEBUG')

pb = AnsPlaybook(log)
pb.file = '/tmp/ans_playbook_{}.yaml'.format(module_name)
pb.name = '{} task'.format(module_name)
pb.add_host('tor-301')  # host in Ansible inventory

task = AskNxosInterfaceOspf(log)
task.task_name = module_name
task.ospf = '1'
task.area = '100'
task.interface = 'Ethernet1/1'
task.network = 'point-to-point'
task.state = 'present' # or 'absent'
pb.add_task(task)
if pb.tasks_pending():
    pb.write_playbook()
    print('wrote {}'.format(pb.file))

'''

class AskNxosInterfaceOspf(AnsTask):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_interface_ospf'
        super().__init__(ansible_module, task_log)
        self._version = our_version
        self._classname = __class__.__name__
        self.ansible_task = dict()

        self.init_properties()

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

    def init_properties(self):
        self.properties = dict()
        self.properties['area'] = None                              # Ospf area associated with this cisco_interface_ospf instance. 
                                                                    # Valid values: str(), formatted as an IP address (i.e. "0.0.0.0") or as an integer
        self.properties['bfd'] = None                               # Enables bfd at interface level. 
                                                                    # This overrides the bfd variable set at the ospf router level.
                                                                    # Valid values are 'enable', 'disable' or 'default'.
                                                                    # Dependency: ''feature bfd'
        self.properties['cost'] = None                              # The cost associated with this cisco_interface_ospf instance
        self.properties['dead_interval'] = None                     # Time interval an ospf neighbor waits for a hello packet before tearing down adjacencies.
                                                                    # Valid values are an integer or the keyword 'default'.
        self.properties['hello_interval'] = None                    # Time between sending successive hello packets. 
                                                                    # Valid values are an integer or the keyword 'default'.
        self.properties['interface'] = None                         # Name of this cisco_interface resource. Valid value is a string
        self.properties['message_digest'] = None                    # Enables or disables the usage of message digest authentication
                                                                    # Valid values: no, yes
        self.properties['message_digest_algorithm_type'] = None     # Algorithm used for authentication among neighboring routers within an area.
                                                                    # Valid values are 'md5' and 'default'
        self.properties['message_digest_encryption_type'] = None    # Specifies the scheme used for encrypting message_digest_password. 
                                                                    # Valid values: '3des', 'cisco_type_7', 'default'
        self.properties['message_digest_key_id'] = None             # Md5 authentication key-id associated with the ospf instance. 
                                                                    # If this is present, message_digest_encryption_type, message_digest_algorithm_type
                                                                    # and message_digest_password are mandatory. 
                                                                    # Valid value is an integer and 'default'.
        self.properties['message_digest_password'] = None           # Specifies the message_digest password.
                                                                    # Valid value is a string
        self.properties['network'] = None                           # Specifies interface ospf network type. 
                                                                    # Valid values: 'point-to-point', 'broadcast'
        self.properties['ospf'] = None                              # Name of the ospf instance
        self.properties['passive_interface'] = None                 # Enable or disable passive-interface state on this interface.
                                                                    # yes - (enable) Prevent OSPF from establishing an adjacency or sending routing updates on this interface.
                                                                    # no  - (disable) Override global 'passive-interface default' for this interface.
        self.properties['state'] = None                             # Determines whether the config should be present or not on the device
                                                                    # Valid values: present, absent

    def final_verification(self):
        '''
        final_verification is called by subclass.update() method
        It performs a final verification across the properties that the user has or hasn't set
        '''
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
        update verifies that mandatory module-specific parameters are set
        '''
        self.final_verification()

        d = dict()

        if self.area != None:
            d['area'] = self.area
        if self.cost != None:
            d['cost'] = self.cost
        if self.dead_interval != None:
            d['dead_interval'] = self.dead_interval
        if self.hello_interval != None:
            d['hello_interval'] = self.hello_interval
        if self.interface != None:
            d['interface'] = self.interface
        if self.message_digest != None:
            d['message_digest'] = self.message_digest
        if self.message_digest_algorithm_type != None:
            d['message_digest_algorithm_type'] = self.message_digest_algorithm_type
        if self.message_digest_encryption_type != None:
            d['message_digest_encryption_type'] = self.message_digest_encryption_type
        if self.message_digest_key_id != None:
            d['message_digest_key_id'] = self.message_digest_key_id
        if self.message_digest_password != None:
            d['message_digest_password'] = self.message_digest_password
        if self.network != None:
            d['network'] = self.network
        if self.ospf != None:
            d['ospf'] = self.ospf
        if self.passive_interface != None:
            d['passive_interface'] = self.passive_interface
        if self.state != None:
            d['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

        self.ansible_task[self.ansible_module] = d.copy()

        self.init_properties()



    def verify_area(self, x, parameter='area'):
        if self.is_ipv4_address(x):
            return
        if self.is_digits(x):
            return
        source_class = self._classname
        source_method = 'verify_area'
        expectation = '[digits or ipv4_address]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_bfd(self, x, parameter='bfd'):
        if x in ['enable', 'disable', 'default']:
            return
        source_class = self._classname
        source_method = 'verify_bfd'
        expectation = "['enable', 'disable', 'default']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_cost(self, x, parameter='cost'):
        if self.is_digits(x):
            return
        source_class = self._classname
        source_method = 'verify_cost'
        expectation = "['digits']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_dead_interval(self, x, parameter='dead_interval'):
        if self.is_digits(x):
            return
        if x in ['default']:
            return
        source_class = self._classname
        source_method = 'verify_dead_interval'
        expectation = "['digits', 'default']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_hello_interval(self, x, parameter='hello_interval'):
        if self.is_digits(x):
            return
        if x in ['default']:
            return
        source_class = self._classname
        source_method = 'verify_hello_interval'
        expectation = "['digits', 'default']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_interface(self, x, parameter='interface'):
        for interface_type in self.valid_ospf_interface:
            if interface_type in x:
                return
        source_class = self._classname
        source_method = 'verify_interface'
        expectation = "OSPF Interface type: {}".format(self.valid_ospf_interface)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_message_digest(self, x, parameter='message_digest'):
        self.verify_toggle(x)

    def verify_message_digest_algorithm_type(self, x, parameter='message_digest_algorithm_type'):
        if x in self.valid_message_digest_algorithm_type:
            return
        source_class = self._classname
        source_method = 'verify_message_digest_algorithm_type'
        expectation = "{}".format(self.valid_message_digest_algorithm_type)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_message_digest_encryption_type(self, x, parameter='message_digest_encryption_type'):
        if x in self.valid_message_digest_encryption_type:
            return
        source_class = self._classname
        source_method = 'verify_message_digest_encryption_type'
        expectation = "{}".format(self.valid_message_digest_encryption_type)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_message_digest_key_id(self, x, parameter='message_digest_key_id'):
        if self.is_digits(x):
            return
        if x in ['default']:
            return
        source_class = self._classname
        source_method = 'verify_message_digest_key_id'
        expectation = "['digits', 'default']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_network(self, x, parameter='network'):
        if x in self.valid_network:
            return
        source_class = self._classname
        source_method = 'verify_network'
        expectation = "{}".format(self.valid_network)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interface_ospf_passive_interface(self, x, parameter='force'):
        verify_set = self.nxos_interface_ospf_valid_passive_interface
        if x in verify_set:
            return
        source_class = self._classname
        source_method = 'verify_nxos_interface_ospf_passive_interface'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interface_ospf_state(self, x, parameter='state'):
        if x in self.nxos_interface_ospf_valid_state:
            return
        source_class = self._classname
        source_method = 'verify_nxos_interface_ospf_state'
        expectation = ','.join(self.nxos_interface_ospf_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def area(self):
        return self.properties['area']
    @area.setter
    def area(self, x):
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
        parameter = 'message_digest_password'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def network(self):
        return self.properties['network']
    @network.setter
    def network(self, x):
        '''
        '''
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
        '''
        '''
        parameter = 'ospf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def passive_interface(self):
        return self.properties['passive_interface']
    @passive_interface.setter
    def passive_interface(self, x):
        '''
        '''
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
        '''
        '''
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_ospf_state(x, parameter)
        self.properties[parameter] = x
