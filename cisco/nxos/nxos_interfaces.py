# NxosInterfaces() - cisco/nxos/nxos_interfaces.py
our_version = 116
from copy import deepcopy
from ask.common.task import Task
'''
Name: ask_task_nxos_interfaces.py

Description:

AskNxosInterfaces() generates Ansible Playbook tasks conformant with nxos_interfaces
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/nxos_interfaces.py

Properties:

    description                         -   interface description
    duplex                              -   Interface duplex. Applicable for Ethernet interfaces only.
    enabled                                 Administrative state of the interface. Set the value to
                                            yes to administratively enable the interface or no to disable it
                                            Valid values: no, yes
    fabric_forwarding_anycast_gateway   -   Associate SVI with anycast gateway under VLAN configuration mode. 
                                            Applicable for SVI interfaces only
                                            Valid values: no, yes
    ip_forward                          -   Disable (no) or enable (yes) IP forward feature on SVIs
                                            Valid values: no, yes
    mode                                -   Layer2 or Layer3 state of the interface.
                                            Applicable for Ethernet and port channel interfaces only
                                            Valid values: layer2, layer3.
    mtu                                 -   MTU for a specific interface. Applicable for Ethernet interfaces only.
                                            Valid values: int() Even number in range: 576-9216
    name                                -   Full name of interface, e.g. Ethernet1/1, port-channel10
    state                               -   see self.__init__().nxos_interfaces_valid_state
    speed                               -   Interface link speed. Applicable for Ethernet interfaces only
'''

class NxosInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('description')
        self.properties_set.add('duplex')
        self.properties_set.add('enabled')
        self.properties_set.add('fabric_forwarding_anycast_gateway')
        self.properties_set.add('ip_forward')
        self.properties_set.add('mode')
        self.properties_set.add('mtu')
        self.properties_set.add('speed')

        self.nxos_interfaces_valid_duplex = set()
        self.nxos_interfaces_valid_duplex.add('full')
        self.nxos_interfaces_valid_duplex.add('half')
        self.nxos_interfaces_valid_duplex.add('auto')

        self.nxos_interfaces_valid_mode = set()
        self.nxos_interfaces_valid_mode.add('layer2')
        self.nxos_interfaces_valid_mode.add('layer3')

        self.nxos_interfaces_valid_state = set()
        self.nxos_interfaces_valid_state.add('merged')
        self.nxos_interfaces_valid_state.add('replaced')
        self.nxos_interfaces_valid_state.add('overridden')
        self.nxos_interfaces_valid_state.add('deleted')

        self.min_mtu = 576
        self.max_mtu = 9216

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None

    def final_verification(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.update()')
            exit(1)
        if self.mode == 'layer2' and self.ip_forward == 'enable':
            self.task_log.error('exiting. mode is layer2 and ip_forward is enable.  Either set mode to layer3 or set ip_forward to either None or no')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if 'Loopback' in self.name and self.mtu != None:
            self.task_log.warning('mtu not valid for {}. Changing mtu to None.'.format(self.name))
            self.mtu = None

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
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = self.state
        self.ansible_task[self.ansible_module]['config'] = list()
        self.ansible_task[self.ansible_module]['config'].append(deepcopy(d))
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_interfaces_state(self, x, parameter='state'):
        if x in self.nxos_interfaces_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interfaces_state'
        expectation = ','.join(self.nxos_interfaces_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interfaces_duplex(self, x, parameter='duplex'):
        if x in self.nxos_interfaces_valid_duplex:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interfaces_duplex'
        expectation = ','.join(self.nxos_interfaces_valid_duplex)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interfaces_mode(self, x, parameter='mode'):
        if x in self.nxos_interfaces_valid_mode:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interfaces_mode'
        expectation = ','.join(self.nxos_interfaces_valid_mode)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interfaces_mtu(self, x, parameter='verify_nxos_interfaces_mtu'):
        self.verify_integer_range(x, self.min_mtu, self.max_mtu, self.class_name, parameter)

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
        self.verify_nxos_interfaces_duplex(x, parameter)
        self.properties[parameter] = x

    @property
    def enabled(self):
        return self.properties['enabled']
    @enabled.setter
    def enabled(self, x):
        parameter = 'enabled'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter) # inherited from AnsCommon()
        self.properties[parameter] = x

    @property
    def fabric_forwarding_anycast_gateway(self):
        return self.properties['fabric_forwarding_anycast_gateway']
    @fabric_forwarding_anycast_gateway.setter
    def fabric_forwarding_anycast_gateway(self, x):
        parameter = 'fabric_forwarding_anycast_gateway'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter) # inherited from AnsCommon()
        self.properties[parameter] = x

    @property
    def ip_forward(self):
        return self.properties['ip_forward']
    @ip_forward.setter
    def ip_forward(self, x):
        parameter = 'ip_forward'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter) # inherited from AnsCommon()
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interfaces_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def mtu(self):
        return self.properties['mtu']
    @mtu.setter
    def mtu(self, x):
        parameter = 'mtu'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interfaces_mtu(x, parameter)
        self.properties[parameter] = str(x)

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
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interfaces_state(x, parameter)
        self.properties[parameter] = x

    @property
    def speed(self):
        return self.properties['speed']
    @speed.setter
    def speed(self, x):
        parameter = 'speed'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter) # inherited from AnsCommon()
        self.properties[parameter] = x
