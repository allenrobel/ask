# NxosLldpInterfaces() - cisco/nxos/nxos_lldp_interfaces.py
our_version = 103

from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_lldp_interfaces.py

Description:

NxosLldpInterfaces() generates Ansible Playbook tasks conformant with Ansible module nxos_lldp_interfaces
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_lldp_interfaces.py

Properties:

    name                        -   Full name of interface
                                    Required
                                    Examples: Ethernet1/1
    receive                     -   Enable/Disable reception of LLDP packets on the interface
                                    By default, this is enabled after LLDP is enabled globally
                                    Valid values: no, yes
    state                       -   Desired state after module is processed
                                    Valid values: deleted, gathered, merged, overridden, parsed, rendered, replaced
    tlv_set_management_address  -   Advertise the IPv4 or IPv6 management address for the interface
                                    Valid values: ipv4 or ipv6 unicast address without prefixlen/mask
                                    Examples: 1.1.1.1, 2001::1
    tlv_set_vlan                -   Advertise the VLAN for the interface
                                    Valid values: int() range: 1-4094
    transmit                    -   Enable/Disable transmission of LLDP packets on the interface
                                    By default, this is enabled after LLDP is enabled globally
                                    Valid values: no, yes
'''

class NxosLldpInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_lldp_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()

        self.nxos_lldp_interfaces_valid_state = set()
        self.nxos_lldp_interfaces_valid_state.add('deleted')
        self.nxos_lldp_interfaces_valid_state.add('gathered')
        self.nxos_lldp_interfaces_valid_state.add('merged')
        self.nxos_lldp_interfaces_valid_state.add('overridden')
        self.nxos_lldp_interfaces_valid_state.add('parsed')
        self.nxos_lldp_interfaces_valid_state.add('rendered')
        self.nxos_lldp_interfaces_valid_state.add('replaced')

        self.min_vlan = 1
        self.max_vlan = 4094

        self.properties_set = set()
        self.properties_set.add('tlv_set_management_address')
        self.properties_set.add('name')
        self.properties_set.add('receive')
        self.properties_set.add('transmit')
        self.properties_set.add('state')
        self.properties_set.add('tlv_set_vlan')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

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
        tlv_set = dict()
        d['name'] = self.name
        if self.transmit != None:
            d['transmit'] = self.transmit
        if self.receive != None:
            d['receive'] = self.receive
        if self.tlv_set_management_address != None:
            tlv_set['management_address'] = self.tlv_set_management_address
        if self.tlv_set_vlan != None:
            tlv_set['vlan'] = self.tlv_set_vlan
        if len(tlv_set) != 0:
            d['tlv_set'] = deepcopy(tlv_set)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['config'].append(deepcopy(d))
        self.ansible_task[self.ansible_module]['state'] = self.state

        self.init_properties()

    def verify_nxos_lldp_interfaces_tlv_set_management_address(self, x, parameter='tlv_set_management_address'):
        if self.is_ipv6_address(x):
            return
        if self.is_ipv4_unicast_address(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lldp_interfaces_tlv_set_management_address'
        expectation = 'ipv4 or ipv6 unicast address without prefixlen/mask e.g. 1.1.1.1, 2001::1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lldp_interfaces_state(self, x, parameter='state'):
        if x in self.nxos_lldp_interfaces_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lldp_interfaces_state'
        expectation = ','.join(self.nxos_lldp_interfaces_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lldp_interfaces_tlv_set_vlan(self, x, parameter='tlv_set_vlan'):
        source_class = self.class_name
        source_method = 'verify_nxos_lldp_interfaces_tlv_set_vlan'
        self.verify_integer_range(x, self.min_vlan, self.max_vlan, source_class, source_method)

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
    def receive(self):
        return self.properties['receive']
    @receive.setter
    def receive(self, x):
        parameter = 'receive'
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
        self.verify_nxos_lldp_interfaces_state(x, parameter)
        self.properties[parameter] = x

    @property
    def task_name(self):
        return self.properties['task_name']
    @task_name.setter
    def task_name(self, x):
        parameter = 'task_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def tlv_set_management_address(self):
        return self.properties['tlv_set_management_address']
    @tlv_set_management_address.setter
    def tlv_set_management_address(self, x):
        parameter = 'tlv_set_management_address'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lldp_interfaces_tlv_set_management_address(x, parameter)
        self.properties[parameter] = x

    @property
    def tlv_set_vlan(self):
        return self.properties['tlv_set_vlan']
    @tlv_set_vlan.setter
    def tlv_set_vlan(self, x):
        parameter = 'tlv_set_vlan'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lldp_interfaces_tlv_set_vlan(x, parameter)
        self.properties[parameter] = x

    @property
    def transmit(self):
        return self.properties['transmit']
    @transmit.setter
    def transmit(self, x):
        parameter = 'transmit'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x
