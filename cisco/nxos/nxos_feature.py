# NxosFeature() - cisco/nxos/nxos_feature.py
our_version = 106
# standard library
from copy import deepcopy
# scriptkit library
from ask.common.task import Task
'''
Name: nxos_feature.py

Description:

NxosFeature() generates Ansible Playbook tasks conformant with nxos_feature
which can be fed to Playbook().add_task()

Usage example:
    unit_test/cisco/nxos/unit_test_nxos_feature.py

Properties:
    feature     An NX-OS feature e.g. bfd, interface-vlan, etc
    state       Desired state of feature
                Valid values: enabled, disabled
'''
class NxosFeature(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_feature'
        super().__init__(ansible_module, task_log)
        self._version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('feature')
        self.properties_set.add('state')

        self.nxos_feature_valid_state = set()
        self.nxos_feature_valid_state.add('enabled')
        self.nxos_feature_valid_state.add('disabled')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.feature == None:
            self.task_log.error('exiting. call instance.feature before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)

    def update(self):
        '''
        call final_verification()
        update ansible_task dict()
        '''
        self.final_verification()
        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def nxos_feature_verify_state(self, x, parameter='state'):
        if x in self.nxos_feature_valid_state:
            return
        source_class = self.class_name
        source_method = 'nxos_feature_verify_state'
        expectation = ','.join(self.nxos_feature_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def feature(self):
        return self.properties['feature']
    @feature.setter
    def feature(self, x):
        parameter = 'feature'
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
        self.nxos_feature_verify_state(x, parameter)
        self.properties[parameter] = x
