# NxosPim() - cisco/nxos/nxos_pim.py
our_version = 106
from copy import deepcopy
from ask.common.task import Task
'''
=======================
NxosPim() - nxos_pim.py
=======================

Description
-----------
NxosPim() generates Ansible tasks conformant with Ansible module nxos_pim
These can then be passed to Playbook().add_task()

Example usage
-------------
unit_test/cisco/nxos/unit_test_nxos_pim.py

Properties
----------

bfd         -   Valid values: enable, disable
ssm_range   -   Valid values: default, none, ipv4 multicast group range e.g. 225.1.0.0/16
'''

class NxosPim(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_pim'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.properties_set = set()
        self.properties_set.add('bfd')
        self.properties_set.add('ssm_range')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name']    = None

    def verify_ssm_range(self, x, parameter='ssm_range'):
        if x == 'none':
            return
        if x == 'default':
            return
        if self.is_ipv4_multicast_range(x):
            return
        source_class = self.class_name
        source_method = 'verify_ssm_range'
        expectation = '[default, none, or ipv4_multicast_address/prefixlen e.g. 232.1.1.0/24]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def final_verification(self):
        if self.ssm_range == None:
            self.task_log.error('exiting. instance.ssm_range is mandatory. call instance.ssm_range before calling instance.update()')
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
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = d.copy()

    @property
    def bfd(self):
        return self.properties['bfd']
    @bfd.setter
    def bfd(self, x):
        parameter = 'bfd'
        if self.set_none(x, parameter):
            return
        self.verify_enable_disable(x, parameter)
        self.properties[parameter] = x

    @property
    def ssm_range(self):
        return self.properties['ssm_range']
    @ssm_range.setter
    def ssm_range(self, x):
        parameter = 'ssm_range'
        if self.set_none(x, parameter):
            return
        self.verify_ssm_range(x, parameter)
        self.properties[parameter] = x
