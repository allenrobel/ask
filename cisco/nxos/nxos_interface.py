# NxosInterface() - cisco/nxos/nxos_interface.py
our_version = 114
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_interface.py

Description:

deprecated, removed after 2022-06-01
Use NxosInterfaces() (nxos_interfaces.py) instead.

NxosInterface() generates Ansible Playbook tasks conformant with nxos_interface
which can be fed to AnsPlaybook().add_task()

Example usage:
    unit_test/cisco/nxos/nxos_interface.py

Properties:

    admin_state         Valid values: up, down
    aggregate
    delay               Valid values: int()
    description         str()
    duplex              Valid values: full, half, auto
    fabric_forwarding_anycast_gateway   Valid values: no, yes
    interface_type      interface to be unconfigured
                            Valid values: loopback, portchannel, svi, nve
    ip_forward          Valid values: enable, disable
    mode                Valid values: layer2, layer3
    mtu                 Valid values: int() range: 512-9216
    name                Full name of interface e.g. Ethernet1/1, port-channel10
    neighbors           list_of_dict see add_neighbor_host() and add_neighbor_port() methods
    rx_rate             state_check only. Ansible will ensure ingress rate is rx_rate bps before claiming interface up
                        Valid values: int()
    speed               speed config on the interface e.g 10000000, 40000000, 25000000, etc.
                        Valid for ethernet only
                        Valid values: int()
    state               Valid values: present, absent, default
    task_name           Name of the task
    tx_rate             state_check only (Ansible will ensure egress rate is tx_rate bps before claiming interface up)
                        Valid values: int()
'''

class NxosInterface(Task):
    def __init__(self, log):
        ansible_module = 'nxos_interface'
        super().__init__(ansible_module, log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.task_log.warning('*******************************************************************************************')
        self.task_log.warning('NxosInterface() is DEPRECATED as its Ansible module nxos_interface is DEPRECATED.')
        self.task_log.warning('NxosInterface() will be removed after 2022-06-01')
        self.task_log.warning('Use NxosInterfaces() (cisco/nxos/nxos_interfaces.py) instead.')
        self.task_log.warning('*******************************************************************************************')

        self.nxos_interface_valid_admin_state = set()
        self.nxos_interface_valid_admin_state.add('up')
        self.nxos_interface_valid_admin_state.add('down')

        self.nxos_interface_valid_duplex = set()
        self.nxos_interface_valid_duplex.add('full')
        self.nxos_interface_valid_duplex.add('half')
        self.nxos_interface_valid_duplex.add('auto')

        self.nxos_interface_valid_interface_type = set() # interfaces which support CLI 'no interface X'
        self.nxos_interface_valid_interface_type.add('loopback')
        self.nxos_interface_valid_interface_type.add('portchannel')
        self.nxos_interface_valid_interface_type.add('svi')
        self.nxos_interface_valid_interface_type.add('nve')

        self.nxos_interface_valid_ip_forward = set()
        self.nxos_interface_valid_ip_forward.add('enable')
        self.nxos_interface_valid_ip_forward.add('disable')

        self.nxos_interface_valid_mode = set()
        self.nxos_interface_valid_mode.add('layer2')
        self.nxos_interface_valid_mode.add('layer3')

        self.nxos_interface_valid_state = set()
        self.nxos_interface_valid_state.add('present')
        self.nxos_interface_valid_state.add('absent')
        self.nxos_interface_valid_state.add('default')

        self.nxos_interface_min_delay = 1
        self.nxos_interface_max_delay = 16777215
        self.nxos_interface_min_mtu = 576
        self.nxos_interface_max_mtu = 9216

        self.properties_set = set()
        self.properties_set.add('admin_state')
        self.properties_set.add('aggregate')
        self.properties_set.add('delay')
        self.properties_set.add('description')
        self.properties_set.add('duplex')
        self.properties_set.add('fabric_forwarding_anycast_gateway')
        self.properties_set.add('interface_type')
        self.properties_set.add('ip_forward')
        self.properties_set.add('mode')
        self.properties_set.add('mtu')
        self.properties_set.add('name')
        self.properties_set.add('rx_rate')
        self.properties_set.add('tx_rate')
        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['neighbors']    = list()
        self.properties['task_name']    = None
        self.properties['neighbor_port'] = None
        self.properties['neighbor_host'] = None

    def final_verification(self):
        '''
        final_verification is called by subclass.update() method
        It performs a final verification across the properties that the user has or hasn't set
        '''
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.update()')
            exit(1)
        if self.mode == 'layer2' and self.ip_forward == 'enable':
            self.task_log.error('exiting. mode is layer2 and ip_forward is enable.  Either set mode to layer3 or set ip_forward to either None or disable')
            exit(1)
        if 'loopback' in self.name.lower() and self.mtu != None:
            self.task_log.info('mtu not valid for {}. Changing mtu to None.'.format(self.name))
            self.properties['mtu'] = None

    def update(self):
        '''
        '''
        self.final_verification()
        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.add_neighbors()
        if len(self.properties['neighbors']) > 0:
            d['neighbors'] = self.properties['neighbors']
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)
        self.init_properties()

    def add_neighbors(self):
        '''
        If user has set either self.neighbor_port or self.neighbor_host
        Append dict() d to self.properties['neighbors']
        '''
        if not self.is_lldp_interface(self.name):
            self.task_log.info('skipping lldp state check for interface {}: not LLDP capable'.format(self.name))
            return
        d = dict()
        if self.neighbor_port != None:
            d['port'] = self.neighbor_port
        if self.neighbor_host != None:
            d['host'] = self.neighbor_host
        if len(d) != 0:
            self.properties['neighbors'].append(deepcopy(d))
        self.neighbor_host = None
        self.neighbor_port = None

    def nxos_interface_verify_admin_state(self, x, parameter='admin_state'):
        verify_set = self.nxos_interface_valid_admin_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_interface_verify_admin_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_interface_verify_duplex(self, x, parameter='duplex'):
        verify_set = self.nxos_interface_valid_duplex
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_interface_verify_duplex'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_interface_verify_interface_type(self, x, parameter='interface_type'):
        for interface_type in self.nxos_interface_valid_interface_type:
            if interface_type in x.lower():
                return
        source_class = self.class_name
        source_method = 'nxos_interface_verify_interface_type'
        expectation = ','.join(self.nxos_interface_valid_interface_type)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_interface_verify_ip_forward(self, x, parameter='ip_forward'):
        verify_set = self.nxos_interface_valid_ip_forward
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_interface_verify_ip_forward'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_interface_verify_mode(self, x, parameter='mode'):
        verify_set = self.nxos_interface_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_interface_verify_mode'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_interface_verify_mtu(self, x, parameter='mtu'):
        self.verify_integer_range(x, self.nxos_interface_min_mtu, self.nxos_interface_max_mtu, self.class_name, parameter)

    def verify_nxos_interface_state(self, x, parameter='state'):
        verify_set = self.nxos_interface_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def admin_state(self):
        return self.properties['admin_state']
    @admin_state.setter
    def admin_state(self, x):
        parameter = 'admin_state'
        if self.set_none(x, parameter):
            return
        self.nxos_interface_verify_admin_state(x, parameter)
        self.properties[parameter] = x

    @property
    def delay(self):
        return self.properties['delay']
    @delay.setter
    def delay(self, x):
        parameter = 'delay'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, self.nxos_interface_min_delay, self.nxos_interface_max_delay, self.class_name, parameter)
        self.properties[parameter] = x

    @property
    def description(self):
        return self.properties['description']
    @description.setter
    def description(self, x):
        parameter = 'description'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def duplex(self):
        return self.properties['duplex']
    @duplex.setter
    def duplex(self, x):
        parameter = 'duplex'
        if self.set_none(x, parameter):
            return
        self.nxos_interface_verify_duplex(x, parameter)
        self.properties[parameter] = x

    @property
    def fabric_forwarding_anycast_gateway(self):
        return self.properties['fabric_forwarding_anycast_gateway']
    @fabric_forwarding_anycast_gateway.setter
    def fabric_forwarding_anycast_gateway(self, x):
        parameter = 'fabric_forwarding_anycast_gateway'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def interface_type(self):
        return self.properties['interface_type']
    @interface_type.setter
    def interface_type(self, x):
        parameter = 'interface_type'
        if self.set_none(x, parameter):
            return
        self.nxos_interface_verify_interface_type(x, parameter)
        self.properties[parameter] = x

    @property
    def ip_forward(self):
        return self.properties['ip_forward']
    @ip_forward.setter
    def ip_forward(self, x):
        parameter = 'ip_forward'
        if self.set_none(x, parameter):
            return
        self.nxos_interface_verify_ip_forward(x, parameter)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.nxos_interface_verify_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def mtu(self):
        return self.properties['mtu']
    @mtu.setter
    def mtu(self, x):
        parameter = 'mtu'
        if self.set_none(x, parameter):
            return
        self.nxos_interface_verify_mtu(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_host(self):
        return self.properties['neighbor_host']
    @neighbor_host.setter
    def neighbor_host(self, x):
        parameter = 'neighbor_host'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def neighbor_port(self):
        return self.properties['neighbor_port']
    @neighbor_port.setter
    def neighbor_port(self, x):
        parameter = 'neighbor_port'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def rx_rate(self):
        return self.properties['rx_rate']
    @rx_rate.setter
    def rx_rate(self, x):
        parameter = 'rx_rate'
        if self.set_none(x, parameter):
            return
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits. Got {}'.format(x))
            exit(1)
        self.properties[parameter] = x

    @property
    def speed(self):
        return self.properties['speed']
    @speed.setter
    def speed(self, x):
        parameter = 'speed'
        if self.set_none(x, parameter):
            return
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits. Got {}'.format(x))
            exit(1)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_state(x, parameter)
        self.properties[parameter] = x

    @property
    def tx_rate(self):
        return self.properties['tx_rate']
    @tx_rate.setter
    def tx_rate(self, x):
        parameter = 'tx_rate'
        if self.set_none(x, parameter):
            return
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits. Got {}'.format(x))
            exit(1)
        self.properties[parameter] = x
