# NxosOspf() - cisco/nxos/nxos_ospf.py
our_version = 110
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_ospf.py

Description:

NxosOspf() generates Ansible Playbook tasks using nxos_ospf
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_ospf.py

Properties:
    ospf        -   Name of the ospf instance 
                    Valid values: IP address (e.g. "1.1.1.1") or int() e.g. 10
    state       -   Determines whether the config should be present or not on the device
                    Valid values: present, absent
    task_name   -   Name of the task
'''

class NxosOspf(Task):
    def __init__(self, task_log):
        ansible_module = 'nxos_ospf'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.properties_set = set()
        self.properties_set.add('ospf')
        self.properties_set.add('state')

        self.nxos_ospf_valid_state = set()
        self.nxos_ospf_valid_state.add('absent')
        self.nxos_ospf_valid_state.add('present')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.ospf == None:
            self.log.error('exiting. call instance.ospf before calling instance.update()')
            exit(1)
        if self.state == None:
            self.log.error('exiting. call instance.state before calling instance.update()')
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
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_ospf_state(self, x, parameter='state'):
        verify_set = self.nxos_ospf_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ospf_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def ospf(self):
        return self.properties['ospf']
    @ospf.setter
    def ospf(self, x):
        parameter = 'ospf'
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
        self.verify_nxos_ospf_state(x, parameter)
        self.properties[parameter] = x
