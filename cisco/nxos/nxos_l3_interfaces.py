# NxosL3Interfaces() - cisco/nxos/nxos_l3_interfaces.py
our_version = 106
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_l3_interfaces.py

Description:

NxosL3Interfaces() generates Ansible Playbook tasks conformant with nxos_l3_interfaces
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_l3_interfaces.py

User properties:
    dot1q                   -   str() 802.1q vlan ID used in 'encapsulation dot1q <vlan ID'
    evpn_multisite_tracking -   str() VxLAN evpn multisite Interface tracking. Supported only on selected model
                                Valid values: fabric-tracking, dci-tracking
    ipv4_address            -   str() ipv4 interface address e.g. 10.1.1.0/31
    ipv4_secondary          -   bool() Is ipv4_address a secondary address
                                Valid values: no, yes
    ipv4_tag                -   int() URIB route tag value for local/direct ipv4 routes

    ipv6_address            -   str() ipv4 interface address e.g. 2001::0/127
    ipv6_tag                -   int() URIB route tag value for local/direct ipv6 routes

    redirects               -   bool() Enables/disables ipv4 redirects
                                Valid values: no, yes
    unreachables            -   bool() Enables/disables ip ICMP unreachables
    task_name               -   str() freeform name for the task

User methods:
    add_ipv4()              -   append ivp4 address and attributes to ipv4 attributes list
    add_ipv6()              -   append ivp6 address and attributes to ipv6 attributes list
Ansible module properties:
    dot1q                   -   str() 802.1q vlan ID used in 'encapsulation dot1q <vlan ID'
    evpn_multisite_tracking -   str() VxLAN evpn multisite Interface tracking. Supported only on selected model
                                Valid values: fabric-tracking, dci-tracking
    ipv4                    -   list_of_dict IPv4 address and attributes of the L3 interface
                                Keys: address, secondary, tag
    ipv6                    -   list_of_dict IPv6 address and attributes of the L3 interface
                                Keys: address, tag
    name                    -   str() Full name of L3 interface, i.e. Ethernet1/1
    redirects               -   bool() Enables/disables ipv4 redirects
                                Valid values: no, yes
    state                   -   str() see self.nxos_l3_interfaces_valid_state
    secondary               -   bool() yes, no. A boolean attribute to manage addition of secondary IP address
    tag                     -   int() URIB route tag value for local/direct routes
    unreachables            -   bool() Enables/disables ip ICMP unreachables
    running_config          
'''

class NxosL3Interfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_l3_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ipv4 = list() # list of dict
        self.ipv6 = list() # list of dict

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()

        self.nxos_l3_interfaces_valid_state = set()
        self.nxos_l3_interfaces_valid_state.add('merged')
        self.nxos_l3_interfaces_valid_state.add('replaced')
        self.nxos_l3_interfaces_valid_state.add('overridden')
        self.nxos_l3_interfaces_valid_state.add('deleted')

        self.nxos_l3_interfaces_valid_evpn_multisite_tracking = set()
        self.nxos_l3_interfaces_valid_evpn_multisite_tracking.add('fabric-tracking')
        self.nxos_l3_interfaces_valid_evpn_multisite_tracking.add('dci-tracking')

        # map disambiguated user property names back into the names expected by the ansible module
        self.property_map = dict()
        self.property_map['ipv4_address'] = 'address'
        self.property_map['ipv6_address'] = 'address'
        self.property_map['ipv4_tag'] = 'tag'
        self.property_map['ipv6_tag'] = 'tag'
        self.property_map['ipv4_secondary'] = 'secondary'

        self.properties_set = set()
        self.properties_set.add('dot1q')
        self.properties_set.add('evpn_multisite_tracking')
        self.properties_set.add('ipv4_address')
        self.properties_set.add('ipv4_secondary')
        self.properties_set.add('ipv4_tag')
        self.properties_set.add('ipv6_address')
        self.properties_set.add('ipv6_tag')
        self.properties_set.add('name')
        self.properties_set.add('redirects')
        self.properties_set.add('state')
        self.properties_set.add('unreachables')

        self.ipv4_set = set()
        self.ipv4_set.add('ipv4_address')
        self.ipv4_set.add('ipv4_secondary')
        self.ipv4_set.add('ipv4_tag')

        self.ipv6_set = set()
        self.ipv6_set.add('ipv6_address')
        self.ipv6_set.add('ipv6_tag')

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
        if len(self.ipv4) == 0 and len(self.ipv6) == 0 and self.state != 'deleted':
            self.task_log.error('exiting. at least one of [ipv4 attributes, ipv6 attributes] must be set.')
            self.task_log.error('ipv4_attribute properties: ipv4_address, ipv4_secondary, ipv4_tag')
            self.task_log.error('ipv6_attribute properties: ipv6_address, ipv6_tag')
            exit(1)
        secondary_count = 0
        for d in self.ipv4:
            try:
                if d['ipv4_secondary'] == 'yes':
                    secondary_count += 1
            except:
                pass
        if secondary_count > 1:
            self.task_log.error('exiting. ipv4_secondary allowed for a single ipv4_address.')
            self.task_log.error('We counted {} ipv4_secondary configured.'.format(secondary_count))
            exit(1)
    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        d = dict()
        d['name'] = self.name
        if self.dot1q != None:
            d['dot1q'] = self.dot1q
        if len(self.ipv4) != 0:
            d['ipv4'] = deepcopy(self.ipv4)
        if len(self.ipv6) != 0:
            d['ipv6'] = deepcopy(self.ipv6)
        if self.redirects != None:
            d['redirects'] = self.redirects
        if self.unreachables != None:
            d['unreachables'] = self.unreachables
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['config'].append(deepcopy(d))
        self.ansible_task[self.ansible_module]['state'] = self.state

    def verify_nxos_l3_interfaces_evpn_multisite_tracking(self, x, parameter='evpn_multisite_tracking'):
        verify_set = self.nxos_l3_interfaces_valid_evpn_multisite_tracking
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_l3_interfaces_evpn_multisite_tracking'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_l3_interfaces_state(self, x, parameter='state'):
        verify_set = self.nxos_l3_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_l3_interfaces_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_ipv4_attributes(self):
        if self.ipv4_address == None:
            self.task_log.error('exiting. Call intance.ipv4_address before calling instance.add_ipv4')
            exit(1)

    def verify_ipv6_attributes(self):
        if self.ipv6_address == None:
            self.task_log.error('exiting. Call intance.ipv6_address before calling instance.add_ipv6')
            exit(1)

    def init_ipv4_properties(self):
        for p in self.ipv4_set:
            self.properties[p] = None

    def init_ipv6_properties(self):
        for p in self.ipv6_set:
            self.properties[p] = None

    def add_ipv4(self):
        self.verify_ipv4_attributes()
        d = dict()
        for p in self.ipv4_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.ipv4.append(deepcopy(d))
        self.init_ipv4_properties()

    def add_ipv6(self):
        self.verify_ipv6_attributes()
        d = dict()
        for p in self.ipv6_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.ipv6.append(deepcopy(d))
        self.init_ipv6_properties()

    @property
    def dot1q(self):
        return self.properties['dot1q']
    @dot1q.setter
    def dot1q(self, x):
        parameter = 'dot1q'
        expectation = '{} >= int() <= {}'.format(self.min_vlan, self.max_vlan)
        if self.set_none(x, parameter):
            return
        self.verify_vlan(x, expectation, parameter)
        self.properties[parameter] = x

    @property
    def evpn_multisite_tracking(self):
        return self.properties['evpn_multisite_tracking']
    @evpn_multisite_tracking.setter
    def evpn_multisite_tracking(self, x):
        parameter = 'evpn_multisite_tracking'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l3_interfaces_evpn_multisite_tracking(x, parameter)
        self.properties[parameter] = x

    @property
    def ipv4_address(self):
        return self.properties['ipv4_address']
    @ipv4_address.setter
    def ipv4_address(self, x):
        parameter = 'ipv4_address'
        if self.set_none(x, parameter):
            return
        self.verify_ipv4_address_with_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def ipv4_secondary(self):
        return self.properties['ipv4_secondary']
    @ipv4_secondary.setter
    def ipv4_secondary(self, x):
        parameter = 'ipv4_secondary'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def ipv4_tag(self):
        return self.properties['ipv4_tag']
    @ipv4_tag.setter
    def ipv4_tag(self, x):
        parameter = 'ipv4_tag'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = x

    @property
    def ipv6_address(self):
        return self.properties['ipv6_address']
    @ipv6_address.setter
    def ipv6_address(self, x):
        parameter = 'ipv6_address'
        if self.set_none(x, parameter):
            return
        self.verify_ipv6_address_with_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def ipv6_tag(self):
        return self.properties['ipv6_tag']
    @ipv6_tag.setter
    def ipv6_tag(self, x):
        parameter = 'ipv6_tag'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_ip_interface(x, parameter) # in AnsCommon()
        self.properties[parameter] = x

    @property
    def redirects(self):
        return self.properties['redirects']
    @redirects.setter
    def redirects(self, x):
        parameter = 'redirects'
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
        self.verify_nxos_l3_interfaces_state(x, parameter)
        self.properties[parameter] = x

    @property
    def unreachables(self):
        return self.properties['unreachables']
    @unreachables.setter
    def unreachables(self, x):
        parameter = 'unreachables'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x
