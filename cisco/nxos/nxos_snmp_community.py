# NxosSnmpCommunity() - cisco/nxos/nxos_snmp_community.py
our_version = 105
from copy import deepcopy
from ask.common.task import Task
'''
============================================
NxosSnmpCommunity() - nxos_snmp_community.py
============================================

Description
-----------
NxosSnmpCommunity() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Example usage
-------------

unit_test/cisco/nxos/unit_test_nxos_snmp_community.py

Properties
----------

=========== ===========
Property    Description
=========== ===========
access      Access type for community::

                - Type: str()
                - Valid values: ro, rw
acl         ACL name to filter snmp requests::

                - Type: str()
                - Value values: str() or keyword 'default'
community   Case-sensitive community string::

                - Type: str()
                - Value values: str()
                - Required
group       Group to which the community belongs::

                - Type: str()
                - Value values: str()
state       Manage the state of the resource::

                - Type: str()
                - Value values: absent, present
=========== ===========

'''

class NxosSnmpCommunity(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_snmp_community'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('access')
        self.properties_set.add('acl')
        self.properties_set.add('community')
        self.properties_set.add('group')
        self.properties_set.add('state')

        self.nxos_snmp_community_valid_state = set()
        self.nxos_snmp_community_valid_state.add('present')
        self.nxos_snmp_community_valid_state.add('absent')

        self.nxos_snmp_community_valid_access = set()
        self.nxos_snmp_community_valid_access.add('ro')
        self.nxos_snmp_community_valid_access.add('rw')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.access == None:
            self.task_log.error('exiting. Set instance.access to ro or rw before calling instance.update()')
            exit(1)
        if self.community == None:
            self.task_log.error('exiting. Set instance.community before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. Set instance.state before calling instance.update()')
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
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_snmp_community_state(self, x, parameter='state'):
        verify_set = self.nxos_snmp_community_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_community_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_snmp_community_access(self, x, parameter='access'):
        verify_set = self.nxos_snmp_community_valid_access
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_community_access'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def access(self):
        return self.properties['access']
    @access.setter
    def access(self, x):
        parameter = 'access'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_snmp_community_access(x, parameter)
        self.properties[parameter] = x

    @property
    def acl(self):
        return self.properties['acl']
    @acl.setter
    def acl(self, x):
        parameter = 'acl'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def community(self):
        return self.properties['community']
    @community.setter
    def community(self, x):
        parameter = 'community'
        if self.set_none(x, parameter):
            return
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
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_snmp_community_state(x, parameter)
        self.properties[parameter] = x
