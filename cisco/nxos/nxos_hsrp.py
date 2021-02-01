# NxosHsrp() - cisco/nxos/nxos_hsrp.py
our_version = 105
# standard library
from copy import deepcopy
# scriptkit library
from ask.common.task import Task
'''
Name: nxos_hsrp.py

Description:

NxosHsrp() generates Ansible Playbook tasks using nxos_hsrp
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/nxos_hsrp.py
'''

class NxosHsrp(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_hsrp'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('auth_string')
        self.properties_set.add('auth_type')
        self.properties_set.add('group')
        self.properties_set.add('interface')
        self.properties_set.add('preempt')
        self.properties_set.add('priority')
        self.properties_set.add('version')
        self.properties_set.add('vip')
        self.properties_set.add('state')

        self.nxos_hsrp_valid_auth_type = set()
        self.nxos_hsrp_valid_auth_type.add('text')
        self.nxos_hsrp_valid_auth_type.add('md5')

        self.nxos_hsrp_valid_preempt = set()
        self.nxos_hsrp_valid_preempt.add('enabled')
        self.nxos_hsrp_valid_preempt.add('disabled')

        self.nxos_hsrp_valid_state = set()
        self.nxos_hsrp_valid_state.add('present')
        self.nxos_hsrp_valid_state.add('absent')

        self.nxos_hsrp_valid_version = set()
        self.nxos_hsrp_valid_version.add(1)
        self.nxos_hsrp_valid_version.add(2)

        self.nxos_hsrp_valid_interface_examples = set()
        self.nxos_hsrp_valid_interface_examples.add('EthernetX/Y')
        self.nxos_hsrp_valid_interface_examples.add('EthernetX/Y/Z')
        self.nxos_hsrp_valid_interface_examples.add('EthernetX/Y.S')
        self.nxos_hsrp_valid_interface_examples.add('EthernetX/Y/Z.S')
        self.nxos_hsrp_valid_interface_examples.add('port-channelX')
        self.nxos_hsrp_valid_interface_examples.add('VlanX')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        '''
        final verification across the properties that the user has or hasn't set
        '''
        if self.group == None:
            self.task_log.error('exiting. call instance.group before calling instance.update()')
            exit(1)
        if self.interface == None:
            self.task_log.error('exiting. call instance.interface before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
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

    def nxos_hsrp_verify_auth_type(self, x, parameter=''):
        if x in self.nxos_hsrp_valid_auth_type:
            return
        source_class = self.class_name
        source_method = 'nxos_hsrp_verify_auth_type'
        expectation = ','.join(sorted(self.nxos_hsrp_valid_auth_type))
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_hsrp_verify_interface(self, x, parameter='interface'):
        if self.is_ethernet_interface(x):
            return
        if self.is_ethernet_subinterface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_class = self.class_name
        source_method = 'nxos_hsrp_verify_interface'
        expectation = ','.join(sorted(self.nxos_hsrp_valid_interface_examples))
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_hsrp_verify_preempt(self, x, parameter='preempt'):
        if x in self.nxos_hsrp_valid_preempt:
            return
        source_class = self.class_name
        source_method = 'nxos_hsrp_verify_preempt'
        expectation = ','.join(sorted(self.nxos_hsrp_valid_preempt))
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_hsrp_verify_state(self, x, parameter='state'):
        if x in self.nxos_hsrp_valid_state:
            return
        source_class = self.class_name
        source_method = 'nxos_hsrp_verify_state'
        expectation = ','.join(sorted(self.nxos_hsrp_valid_state))
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_hsrp_verify_version(self, x, parameter=''):
        if self.is_digits(x):
            if int(x) in self.nxos_hsrp_valid_version:
                return
        source_class = self.class_name
        source_method = 'nxos_hsrp_verify_version'
        expectation = ','.join(sorted(self.nxos_hsrp_valid_version))
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_hsrp_verify_vip(self, x, parameter=''):
        if self.is_ipv4_interface(x):
            return
        source_class = self.class_name
        source_method = 'nxos_hsrp_verify_vip'
        expectation = 'ipv4 address with prefixlen e.g. 10.0.0.1/24'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def auth_string(self):
        return self.properties['auth_string']
    @auth_string.setter
    def auth_string(self, x):
        parameter = 'auth_string'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def auth_type(self):
        return self.properties['auth_type']
    @auth_type.setter
    def auth_type(self, x):
        parameter = 'auth_type'
        if self.set_none(x, parameter):
            return
        self.nxos_hsrp_verify_auth_type(x, parameter)
        self.properties[parameter] = x

    @property
    def group(self):
        return self.properties['group']
    @group.setter
    def group(self, x):
        parameter = 'group'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def interface(self):
        return self.properties['interface']
    @interface.setter
    def interface(self, x):
        parameter = 'interface'
        if self.set_none(x, parameter):
            return
        self.nxos_hsrp_verify_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def preempt(self):
        return self.properties['preempt']
    @preempt.setter
    def preempt(self, x):
        parameter = 'preempt'
        if self.set_none(x, parameter):
            return
        self.nxos_hsrp_verify_preempt(x, parameter)
        self.properties[parameter] = x


    @property
    def priority(self):
        return self.properties['priority']
    @priority.setter
    def priority(self, x):
        parameter = 'priority'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter) # inherited from AnsCommon()
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
        self.nxos_hsrp_verify_state(x, parameter)
        self.properties[parameter] = x

    @property
    def version(self):
        return self.properties['version']
    @version.setter
    def version(self, x):
        '''
        '''
        parameter = 'version'
        if self.set_none(x, parameter):
            return
        self.nxos_hsrp_verify_version(x, parameter)
        self.properties[parameter] = x

    @property
    def vip(self):
        return self.properties['vip']
    @vip.setter
    def vip(self, x):
        '''
        '''
        parameter = 'vip'
        if self.set_none(x, parameter):
            return
        self.nxos_hsrp_verify_vip(x, parameter)
        self.properties[parameter] = x
