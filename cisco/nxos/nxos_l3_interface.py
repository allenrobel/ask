# NxosL3Interface() - cisco/nxos/nxos_l3_interface.py
our_version = 109
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_l3_interface.py

Description:
    NxosL3Interface() generates Ansible Playbook tasks conformant with nxos_l3_interface
    which can be fed to AnsPlaybook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_l3_interface.py

Properties:
    ipv4        -   str() ipv4 address with prefixlen
                    Examples: 10.1.1.0/31
    ipv6        -   str() ipv6 address with prefixlen
                    Examples: 2001:a::1/120
    name        -   str() Full name of the L3 interface
                    Examples: Ethernet1/1, port-channel10
    state       -   str() Desired state
                    Valid values: absent, present
    task_name   -   str() name of the task
'''

class NxosL3Interface(Task):
    def __init__(self, task_log):
        ansible_module = 'nxos_l3_interface'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.nxos_l3_interface_valid_state = set()
        self.nxos_l3_interface_valid_state.add('absent')
        self.nxos_l3_interface_valid_state.add('present')

        self.properties_set = set()
        self.properties_set.add('ipv4')
        self.properties_set.add('ipv6')
        self.properties_set.add('name')
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.ipv4 == None and self.ipv6 == None:
            self.task_log.error('exiting. at least one of [ipv4, ipv6] must be set.')
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

    def verify_nxos_l3_interface_state(self, x, parameter='state'):
        verify_set = self.nxos_l3_interface_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_l3_interface_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def ipv4(self):
        return self.properties['ipv4']
    @ipv4.setter
    def ipv4(self, x):
        parameter = 'ipv4'
        if self.set_none(x, parameter):
            return
        self.verify_ipv4_address_with_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def ipv6(self):
        return self.properties['ipv6']
    @ipv6.setter
    def ipv6(self, x):
        parameter = 'ipv6'
        if self.set_none(x, parameter):
            return
        self.verify_ipv6_address_with_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_ip_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l3_interface_state(x, parameter)
        self.properties[parameter] = x
