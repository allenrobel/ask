# NxosL3Interfaces() - cisco/nxos/nxos_l3_interfaces.py
our_version = 110
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosL3Interfaces()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
110

ScriptKit Synopsis
------------------
- NxosL3Interfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_l3_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_l3_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_l3_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_l3_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_l3_interfaces.py>`_


|

================================    ==============================================
User Methods                        Description
================================    ==============================================
add_interface()                         Add an interface to the configuration::

                                            - Type: function()
                                            - Example:
                                                #!/usr/bin/env python3
                                                # Ethernet1/1 - ipv4 interface with secondary
                                                # Vlan3 - dual-stack interface
                                                from ask.cisco.nxos.nxos_l3_interfaces import NxosL3Interfaces
                                                from ask.common.log import Log
                                                from ask.common.playbook import Playbook
                                                log_level_console = 'INFO'
                                                log_level_file = 'DEBUG'
                                                log = Log('my_log', log_level_console, log_level_file)
                                                pb = Playbook(log)
                                                pb.profile_nxos()
                                                pb.ansible_password = 'mypassword'
                                                pb.name = 'Example nxos_l3_interfaces'
                                                pb.add_host('dc-101')
                                                pb.file = '/tmp/nxos_l3_interfaces.yaml'
                                                task = NxosL3Interfaces(log)
                                                task.name = 'Ethernet1/1'
                                                task.ipv4_address = '10.1.1.1/24'
                                                task.ipv4_tag = 10
                                                task.add_ipv4()
                                                task.ipv4_address = '10.2.1.1/24'
                                                task.ipv4_tag = 20
                                                task.ipv4_secondary = True
                                                task.add_ipv4()
                                                task.add_interface()
                                                task.name = 'Vlan3'
                                                task.ipv4_address = '10.3.1.1/24'
                                                task.ipv4_tag = 10
                                                task.add_ipv4()
                                                task.ipv6_address = '2001:cccc::1/64'
                                                task.ipv6_tag = 10
                                                task.add_ipv6()
                                                task.add_interface()
                                                task.state = 'merged'
                                                task.update()
                                                pb.add_task(task)
                                                pb.append_playbook()
                                                pb.write_playbook()

                                        - Resulting playbook task:

                                            tasks:
                                            -   cisco.nxos.nxos_l3_interfaces:
                                                    config:
                                                    -   ipv4:
                                                        -   address: 10.1.1.1/24
                                                            tag: 10
                                                        -   address: 10.2.1.1/24
                                                            secondary: true
                                                            tag: 20
                                                        name: Ethernet1/1
                                                    -   ipv4:
                                                        -   address: 10.3.1.1/24
                                                            tag: 10
                                                        ipv6:
                                                        -   address: 2001:cccc::1/64
                                                            tag: 10
                                                        name: Vlan3
                                                    state: merged

add_ipv4()                          Append ivp4 properties to the ipv4
                                    attributes list and reset the properties
                                    to None::

                                        - Type: function()
                                        - Example (see add_interface() for full example):

                                            task = NxosL3Interfaces(log)
                                            task.name = 'Ethernet1/49'
                                            task.ipv4_address = '10.1.1.1/24'
                                            task.ipv4_tag = 10
                                            task.add_ipv4()
                                            task.ipv4_address = '10.2.1.1/24'
                                            task.ipv4_tag = 20
                                            task.ipv4_secondary = True
                                            task.add_ipv4()
                                            task.add_interface()
                                            task.state = 'merged'
                                            task.update()

                                        - Resulting playbook task:

                                            tasks:
                                            -   cisco.nxos.nxos_l3_interfaces:
                                                    config:
                                                    -   ipv4:
                                                        -   address: 10.1.1.1/24
                                                            tag: 10
                                                        -   address: 10.2.1.1/24
                                                            secondary: true
                                                            tag: 20
                                                        name: Ethernet1/49
                                                    state: merged

add_ipv6()                          Append ivp6 properties to ipv6
                                    attributes list and reset the properties
                                    to None::

                                        - Type: function()
                                        - Example (see add_interface() for full example):

                                            task.name = 'Ethernet1/49'
                                            task.ipv6_address = '2001:aaaa::1/64'
                                            task.ipv6_tag = 10
                                            task.add_ipv6()
                                            task.ipv6_address = '2001:bbbb::1/64'
                                            task.ipv6_tag = 20
                                            task.add_ipv6()
                                            task.add_interface()
                                            task.state = 'merged'
                                            task.update()

                                        - Resulting playbook task:

                                            tasks:
                                            -   cisco.nxos.nxos_l3_interfaces:
                                                    config:
                                                    -   ipv6:
                                                        -   address: 2001:aaaa::1/64
                                                            tag: 10
                                                        -   address: 2001:bbbb::1/64
                                                            tag: 20
                                                        name: Ethernet1/49
                                                    state: merged

================================    ==============================================


================================    ==============================================
Property                            Description
================================    ==============================================
dot1q                               802.1q vlan ID used in the following CLI
                                    ``encapsulation dot1q <vlan ID>``::

                                        - Type: int()
                                        - Example:
                                            task.dot1q = 10

evpn_multisite_tracking             VxLAN evpn multisite Interface tracking.
                                    Supported only on selected models::

                                        - Type: str()
                                        - Valid values:
                                            - fabric-tracking
                                            - dci-tracking
                                        - Example:
                                            task.evpn_multisite_tracking = 'fabric-tracking'

ipv4_address                        ipv4 interface address::

                                        - Type: str()
                                        - Example:
                                            task.ipv4_address = '10.1.1.0/31'

ipv4_secondary                      ipv4_address is a secondary address::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.ipv4_secondary = True

ipv4_tag                            URIB route tag value for local/direct ipv4 routes::

                                        - Type: int()
                                        - Example:
                                            task.ipv4_tag = 200

ipv6_address                        ipv6 interface address::

                                        - Type: str()
                                        - Example:
                                            task.ipv4_address = '2001::0/127'

ipv6_tag                            URIB route tag value for local/direct ipv6 routes::

                                        - Type: int()
                                        - Example:
                                            task.ipv6_tag = 200

redirects                           Enables/disables ipv4 redirects::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.redirects = False

register                            Ansible variable to save output to::

                                        - Type: str()
                                        - Examples:
                                            task.register = 'result'

running_config                      Full path to a file containing the output of
                                    ``show running-config | section ^interface``::

                                        - Type: str()
                                        - Examples:
                                            task.running_config = '/tmp/running.cfg'

state                               Desired state after task has run::

                                        - Type: str()
                                        - Valid values:
                                            - deleted
                                            - gathered
                                            - merged
                                            - overridden
                                            - parsed
                                            - rendered
                                            - replaced
                                        - Example:
                                            task.state = 'merged'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'enable lacp'

unreachables                        Enables/disables ip ICMP unreachables::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.unreachables = True
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosL3Interfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_l3_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.interface_list = list() # list() of dict()
        self.ipv4 = list() # list() of dict()
        self.ipv6 = list() # list() of dict()

        self.nxos_l3_interfaces_valid_state = set()
        self.nxos_l3_interfaces_valid_state.add('deleted')
        self.nxos_l3_interfaces_valid_state.add('gathered')
        self.nxos_l3_interfaces_valid_state.add('merged')
        self.nxos_l3_interfaces_valid_state.add('overridden')
        self.nxos_l3_interfaces_valid_state.add('parsed')
        self.nxos_l3_interfaces_valid_state.add('rendered')
        self.nxos_l3_interfaces_valid_state.add('replaced')

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

        self.interface_properties = set()
        self.interface_properties.add('dot1q')
        self.interface_properties.add('evpn_multisite_tracking')
        self.interface_properties.add('ipv4_address')
        self.interface_properties.add('ipv4_secondary')
        self.interface_properties.add('ipv4_tag')
        self.interface_properties.add('ipv6_address')
        self.interface_properties.add('ipv6_tag')
        self.interface_properties.add('name')
        self.interface_properties.add('redirects')
        self.interface_properties.add('unreachables')

        self.properties_set = set()
        self.properties_set.update(self.interface_properties)
        self.properties_set.add('register')
        self.properties_set.add('running_config')
        self.properties_set.add('state')

        self.ipv4_set = set()
        self.ipv4_set.add('ipv4_address')
        self.ipv4_set.add('ipv4_secondary')
        self.ipv4_set.add('ipv4_tag')

        self.ipv6_set = set()
        self.ipv6_set.add('ipv6_address')
        self.ipv6_set.add('ipv6_tag')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)
        self.scriptkit_properties.update(self.ipv4_set)
        self.scriptkit_properties.update(self.ipv6_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification_running_config(self):
        if self.state != 'parsed':
            self.task_log.error('exiting. if running_config is set, state must be set to parsed')
            exit(1)
    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.running_config != None:
            self.final_verification_running_config()
        else:
            if self.state == 'deleted':
                return
            for d in self.interface_list:
                if 'ipv4' not in d and 'ipv6' not in d:
                    self.task_log.error('exiting. {} at least one of [ipv4 attributes, ipv6 attributes] must be set.'.format(d['name']))
                    self.task_log.error('ipv4_attribute properties: ipv4_address, ipv4_secondary, ipv4_tag')
                    self.task_log.error('ipv6_attribute properties: ipv6_address, ipv6_tag')
                    exit(1)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()

        if self.running_config == None:
            self.ansible_task[self.ansible_module]['config'] = deepcopy(self.interface_list)
        else:
            self.ansible_task[self.ansible_module]['running_config'] = self.make_running_config()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.register != None:
            self.ansible_task['register'] = self.register

    def make_running_config(self):
        return r'{{' +  " lookup(" + r'"file"' + ',' + r'"' + self.running_config + r'"' + ')' + r' }}'

    def verify_interface_properties(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.add_interface()')
            exit(1)
        ipv4_without_secondary = 0
        for d in self.ipv4:
            if 'secondary' in d:
                if d['secondary'] == False:
                    ipv4_without_secondary += 1
            else:
                ipv4_without_secondary += 1
        if ipv4_without_secondary > 1:
            self.task_log.error('exiting. {} multiple ipv4_address without ipv4_secondary detected.'.format(self.name))
            self.task_log.error('We counted {} ipv4_address without secondary.'.format(ipv4_without_secondary))
            exit(1)

    def init_interface_properties(self):
        for p in self.interface_properties:
            self.properties[p] = None
        self.ipv4 = list()
        self.ipv6 = list()
    def add_interface(self):
        self.verify_interface_properties()
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
        if len(d) == 0:
            self.task_log.error('exiting. Set at least instance.name before calling task.add_interface().')
            exit(1)
        self.interface_list.append(deepcopy(d))
        self.init_interface_properties()

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
        self.verify_boolean(x, parameter)
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
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def register(self):
        return self.properties['register']
    @register.setter
    def register(self, x):
        parameter = 'register'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def running_config(self):
        return self.properties['running_config']
    @running_config.setter
    def running_config(self, x):
        parameter = 'running_config'
        if self.set_none(x, parameter):
            return
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
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x
