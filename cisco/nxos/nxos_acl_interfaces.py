# NxosAclInterfaces() - cisco/nxos/nxos_acl_interfaces.py
our_version = 104
from copy import deepcopy
from ask.common.task import Task
'''
******************************************
NxosAclInterfaces()
******************************************

ScriptKit Synopsis
------------------
NxosAclInterfaces() generates Ansible task instances conformant with cisco.nxos.nxos_acl_interfaces.
These task instances can then be passed to Playbook().add_task()

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_acl_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_acl_interfaces.py>`_

Ansible Module Documentation
----------------------------
- `nxos_acl_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_acl_interfaces_module.rst>`_

|

============================    ==============================================
Property                        Description
============================    ==============================================
acl_direction                   Direction to be applied for the ACL::

                                    - Type: str()
                                    - Valid values:
                                        - in
                                        - out
                                    - Example:
                                        task.acl_direction = 'out'
                                    - Required

acl_name                        Name of the ACL to be added/removed::

                                    - Type: str()
                                    - Example:
                                        task.acl_name = 'TOR_OUT'
                                    - Required

acl_port                        Use ACL as port policy. If True, ``name``
                                must be a (L2) switchport.  If False, ``name``
                                must be a (L3) routed port::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.acl_port = True

afi                             Address Family Indicator of the ACLs to be configured::

                                    - Type: str()
                                    - Valid values:
                                        - ipv4
                                        - ipv6
                                    - Example:
                                        task.afi = 'ipv4'
                                    - Required

name                            Name of the interface on which the ACL is applied::

                                    - Type: str()
                                    - Examples:
                                        - task.name = 'Ethernet1/1'
                                        - task.name = 'Vlan10'
                                    - Required

state                           The state after playbook has executed::

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

task_name                       Name of the task. Ansible will display this when
                                executing the playbook::

                                    - Type: str()
                                    - Default: Task name is not displayed
                                    - Example:
                                        task.task_name = 'my task'

============================    ==============================================

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

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
        populate self.ansible_task
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
        self.verify_boolean(x, parameter)
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
