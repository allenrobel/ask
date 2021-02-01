# NxosAclInterfaces() - cisco/nxos/nxos_acl_interfaces.py
our_version = 102
# standard library
from copy import deepcopy
# scriptkit library
from ask.common.task import Task
'''
Name: nxos_acl_interfaces.py

Description:

NxosAclInterfaces() generates Ansible Playbook tasks conformant with nxos_acl_interfaces
which can be fed to Playbook().add_task()

Properties:

    acl_direction   - Direction to be applied for the ACL
                        Valid values: in, out
                        Required
    acl_name        - Name of the ACL to be added/removed
                        Required
    acl_port        - Use ACL as port policy
                        If 'yes', interface must be a switchport
                        If 'no', interface must be a routed port (i.e. no switchport)
                        Valid values: no, yes
    afi             - Address Family Indicator of the ACLs to be configured
                        Valid values: ipv4, ipv6
                        Required
    name            - Name of the interface e.g. Ethernet1/1
    state           - The state the configuration should be left in
                        Valid values: See self.nxos_acl_interfaces_valid_state
    task_name       - Name of the task. Ansible will display this when executing the playbook

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_acl_interfaces.py
'''

class NxosAclInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_acl_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()

        self.nxos_acl_interfaces_valid_afi = set()
        self.nxos_acl_interfaces_valid_afi.add('ipv4')
        self.nxos_acl_interfaces_valid_afi.add('ipv6')

        self.nxos_acl_interfaces_valid_direction = set()
        self.nxos_acl_interfaces_valid_direction.add('in')
        self.nxos_acl_interfaces_valid_direction.add('out')

        self.nxos_acl_interfaces_valid_port = set()
        self.nxos_acl_interfaces_valid_port.add('no')
        self.nxos_acl_interfaces_valid_port.add('yes')

        self.nxos_acl_interfaces_valid_state = set()
        self.nxos_acl_interfaces_valid_state.add('deleted')
        self.nxos_acl_interfaces_valid_state.add('gathered')
        self.nxos_acl_interfaces_valid_state.add('merged')
        self.nxos_acl_interfaces_valid_state.add('overridden')
        self.nxos_acl_interfaces_valid_state.add('rendered')
        self.nxos_acl_interfaces_valid_state.add('replaced')
        self.nxos_acl_interfaces_valid_state.add('parsed')

        self.properties_set = set()
        self.properties_set.add('acl_direction')
        self.properties_set.add('acl_name')
        self.properties_set.add('acl_port')
        self.properties_set.add('afi')
        self.properties_set.add('name')
        self.properties_set.add('state')
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
        if self.acl_name == None:
            self.task_log.error('exiting. call instance.acl_name before calling instance.update()')
            exit(1)
        if self.acl_direction == None:
            self.task_log.error('exiting. call instance.direction before calling instance.update()')
            exit(1)
        if self.afi == None:
            self.task_log.error('exiting. call instance.afi before calling instance.update().')
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate and append dict() to self.ansible_task[self.ansible_module]['config']
        '''
        self.final_verification()

        acl = dict()
        acl['direction'] = self.acl_direction
        acl['name'] = self.acl_name
        acl['port'] = self.acl_port
        access_group = dict()
        access_group['afi'] = self.afi
        access_group['acls'] = list()
        access_group['acls'].append(deepcopy(acl))

        d = dict()
        d['name'] = self.name
        d['access_groups'] = list()
        d['access_groups'].append(deepcopy(access_group))

        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['config'].append(deepcopy(d))
        self.ansible_task[self.ansible_module]['state'] = self.state

    def nxos_acl_interfaces_verify_afi(self, x, parameter='afi'):
        verify_set = self.nxos_acl_interfaces_valid_afi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_acl_interfaces_verify_afi'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_acl_interfaces_verify_direction(self, x, parameter='direction'):
        verify_set = self.nxos_acl_interfaces_valid_direction
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_acl_interfaces_verify_direction'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_acl_interfaces_verify_port(self, x, parameter='port'):
        verify_set = self.nxos_acl_interfaces_valid_port
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_acl_interfaces_verify_port'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_acl_interfaces_verify_state(self, x, parameter='state'):
        verify_set = self.nxos_acl_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_acl_interfaces_verify_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.nxos_acl_interfaces_verify_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def acl_direction(self):
        return self.properties['acl_direction']
    @acl_direction.setter
    def acl_direction(self, x):
        parameter = 'acl_direction'
        if self.set_none(x, parameter):
            return
        self.nxos_acl_interfaces_verify_direction(x, parameter)
        self.properties[parameter] = x

    @property
    def acl_name(self):
        return self.properties['acl_name']
    @acl_name.setter
    def acl_name(self, x):
        parameter = 'acl_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def acl_port(self):
        return self.properties['acl_port']
    @acl_port.setter
    def acl_port(self, x):
        parameter = 'acl_port'
        if self.set_none(x, parameter):
            return
        self.nxos_acl_interfaces_verify_port(x, parameter)
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
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.nxos_acl_interfaces_verify_state(x, parameter)
        self.properties[parameter] = x
