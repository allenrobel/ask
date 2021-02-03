# NxosLagInterfaces() - cisco/nxos/nxos_lag_interfaces.py
our_version = 105

import re
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_lag_interfaces.py

Description:

NxosLagInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lag_interfaces
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_lag_interfaces.py

Properties:
    force       -   Valid values: no, yes
    member      -   e.g. Ethernet1/1
    mode        -   Valid values: active, on, passive
    name        -   Valid values: Po name e.g. port-channel20
    state       -   Valid values: deleted, gathered, merged, overridden, parsed, rendered, replaced
    task_name   -   Freeform name for the task
'''

class NxosLagInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_lag_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.config = list()
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()
        self.re_lag_interface = re.compile('^port-channel\d+$')

        self.lag_valid_state = set()
        self.lag_valid_state.add('deleted')
        self.lag_valid_state.add('gathered')
        self.lag_valid_state.add('merged')
        self.lag_valid_state.add('overridden')
        self.lag_valid_state.add('parsed')
        self.lag_valid_state.add('rendered')
        self.lag_valid_state.add('replaced')

        self.lag_valid_force = set()
        self.lag_valid_force.add('no')
        self.lag_valid_force.add('yes')

        self.lag_valid_mode = set()
        self.lag_valid_mode.add('active')
        self.lag_valid_mode.add('on')
        self.lag_valid_mode.add('passive')

        self.properties_set = set()
        self.properties_set.add('force')
        self.properties_set.add('member')
        self.properties_set.add('mode')
        self.properties_set.add('name')
        self.properties_set.add('state')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.properties['state'] == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if len(self.config) == 0:
            self.task_log.error('exiting. call at least one of instance.name + instance.add_member() + instance.add_lag() before calling instance.update()')
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()

        NOTE: update() is slightly different from other nxos_*_interfaces libraries.
        In add_member() we append to self.config
        In update() we set self.ansible_task[self.ansible_module]['config'] = self.config
        '''
        self.final_verification()
        self.ansible_task[self.ansible_module]['config'] = self.config
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.init_properties()

    def add_lag(self):
        try:
            foo = self.lag['name']
        except:
            self.task_log.error('exiting. call instance.name before calling add_lag()')
            exit(1)
        if len(self.lag['members']) == 0:
            self.task_log.warning('{} will be created with no members.'.format(self.lag['name']))
        self.config.append(deepcopy(self.lag))
        self.lag = None

    def add_member(self):
        if self.member == None:
            self.task_log.error('exiting. set instance.member to a valid ethernet interace name before calling add_member()')
            exit(1)
        try:
            foo = self.lag['name']
        except:
            self.task_log.error('exiting. call instance.name before calling instance.add_member()')
            exit(1)
        d = dict()
        d['member'] = self.member
        if self.mode != None:
            d['mode'] = self.mode
        if self.force != None:
            d['force'] = self.force
        self.lag['members'].append(deepcopy(d))
        self.mode = None
        self.force = None
        self.member = None

    def verify_force(self, x, parameter='force'):
        verify_set = self.lag_valid_force
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_force'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_mode(self, x, parameter='mode'):
        verify_set = self.lag_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_mode'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_state(self, x, parameter='state'):
        verify_set = self.lag_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lag_interface(self, x, parameter='name'):
        if self.re_lag_interface.search(x):
            return
        source_class = self.class_name
        source_method = 'verify_lag_interface'
        expectation = 'valid LAG interface name e.g.: port-channel1000'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lag_member(self, x, parameter='member'):
        if self.is_ethernet_interface(x): # inherited from AnsCommon()
            return
        source_class = self.class_name
        source_method = 'verify_lag_member'
        expectation = 'valid LAG member interface name e.g.: Ethernet1/1, Ethernet1/2/1'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def force(self):
        return self.properties['force']
    @force.setter
    def force(self, x):
        parameter = 'force'
        if self.set_none(x, parameter):
            return
        self.verify_force(x, parameter)
        self.properties[parameter] = x
    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_mode(x, parameter)
        self.properties[parameter] = x
    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_state(x, parameter)
        self.properties[parameter] = x

    @property
    def member(self):
        return self.properties['member']
    @member.setter
    def member(self, x):
        parameter = 'member'
        if self.set_none(x, parameter):
            return
        self.verify_lag_member(x, parameter)
        try:
            foo = self.lag['name']
        except:
            self.task_log.error('exiting. Call instance.name before calling instance.member')
            exit(1)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        '''
        creates empty dict() with the following keys:
        name: port-channel5
        members: list()
        '''
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_lag_interface(x, parameter)
        self.lag = dict()
        self.lag['name'] = x
        self.lag['members'] = list()

    @property
    def task_name(self):
        return self.properties['task_name']
    @task_name.setter
    def task_name(self, x):
        parameter = 'task_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
