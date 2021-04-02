# NxosPim() - cisco/nxos/nxos_pim.py
our_version = 108
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosPim()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosPim() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_pim
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_pim <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_pim_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_pim.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_pim.py>`_

Dependencies
------------
The following must be enabled prior to applying nxos_pim playbook::

  feature pim

|

================    ==============================================
Property            Description
================    ==============================================
bfd                 Enables BFD on all PIM interfaces::

                        - Type: str()  
                        - Valid values:
                            - disable
                            - enable
                        - Dependency: 'feature bfd
                        - Example:
                            task.bfd = 'enable'

ssm_range           Configure group ranges for Source Specific Multicast (SSM)::

                        - Type: list() or str()
                        - Valid values:
                            - default
                                - set ssm_range to 232.0.0.0/8
                            - none
                                - remove all ssm group ranges
                            - list()
                                - list of multicast group ranges
                        - Examples:
                            task.ssm_range = 'default'
                            task.ssm_range = 'none'

                            ssm = list()
                            ssm.append('225.1.0.0/16')
                            ssm.append('225.4.1.0/24')
                            task.ssm_range = ssm

================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

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

    def ssm_range_list_ok(self, x):
        if type(x) != type(list()):
            return False
        for r in x:
            if not self.is_ipv4_multicast_range(r):
                return False
        return True

    def verify_ssm_range(self, x, parameter='ssm_range'):
        if x == 'default':
            return
        if x == 'none':
            return
        if self.ssm_range_list_ok(x):
            return
        source_class = self.class_name
        source_method = 'verify_ssm_range'
        expectation = "default, none, or python list() of ipv4_multicast_address/prefixlen e.g. ['232.1.1.0/24', '225.1.0.0/16']"
        self.fail(source_class, source_method, x, parameter, expectation)

    def final_verification(self):
        if self.ssm_range == None:
            self.task_log.error('exiting. instance.ssm_range is mandatory. call instance.ssm_range before calling instance.commit()')
            exit(1)

    def commit(self):
        self.update()
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
