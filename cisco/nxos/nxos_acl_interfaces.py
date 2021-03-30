# NxosAclInterfaces() - cisco/nxos/nxos_acl_interfaces.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
******************************************
NxosAclInterfaces()
******************************************

Version
-------
107

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

====================    ============================================
Method                  Description
====================    ============================================
add_access_group()      Add access_group configuration to the list
                        of access-groups to apply to ``name`` when
                        ``add_interface()`` is called.  access-group
                        configuration consists of ``afi`` and the
                        list of ACLs built by calling ``add_acl()``::

                            - Type: function()
                            - Example:
                                See commit() in this table for a short example
                                See ScriptKit Example above for a full script

add_acl()               Add ACL configuration to the list of ACLs
                        to apply to access-group when ``add_access_group()``
                        is called.  ACL configuration consists of ``acl_name``,
                        ``acl_direction`` and, optionally, ``acl_port``::

                            - Type: function()
                            - Example:
                                See commit() in this table for a short example
                                See ScriptKit Example above for a full script

add_interface()         Add interface configuration to the list of interfaces
                        to apply when ``commit()`` is called.  Interface 
                        configuration consists of ``name``::

                            - Type: function()
                            - Example:
                                See commit() in this table for a short example
                                See ScriptKit Example above for a full script

commit()                Perform final verification and commit the current task::

                            - Type: function()
                            - Alias: update()
                            - Example (See also: ScriptKit Example above):
                                #!/usr/bin/env python3
                                # Configure an ipv4 access-group with two ACLs on interface Eth1/3
                                from ask.cisco.nxos.nxos_acl_interfaces import NxosAclInterfaces
                                from ask.common.log import Log
                                from ask.common.playbook import Playbook

                                log_level_console = 'INFO'
                                log_level_file = 'DEBUG'
                                log = Log('my_log', log_level_console, log_level_file)

                                pb = Playbook(log)
                                pb.profile_nxos()
                                pb.ansible_password = 'mypassword'
                                pb.name = 'Example nxos_acl_interfaces'
                                pb.add_host('dc-101')
                                pb.file = '/tmp/nxos_acl_interfaces.yaml'

                                task = NxosAclInterfaces(log)
                                task.acl_name = 'IPv4_ACL_IN'
                                task.acl_port = False
                                task.acl_direction = 'in'
                                task.add_acl()
                                task.acl_name = 'IPv4_ACL_OUT'
                                task.acl_port = False
                                task.acl_direction = 'out'
                                task.add_acl()
                                task.afi = 'ipv4'
                                task.add_access_group()
                                task.name = 'Ethernet1/3'
                                task.add_interface()
                                task.state = 'merged'
                                task.commit()

                                pb.add_task(task)
                                pb.append_playbook()
                                pb.write_playbook()

                            - Resulting task (full playbook not shown):

                                tasks:
                                -   cisco.nxos.nxos_acl_interfaces:
                                        config:
                                        -   access_groups:
                                            -   acls:
                                                -   direction: in
                                                    name: IPv4_ACL_IN
                                                    port: false
                                                -   direction: out
                                                    name: IPv4_ACL_OUT
                                                    port: false
                                                afi: ipv4
                                            name: Ethernet1/3
                                        state: merged

                            - Resulting config on remote device:

                                interface Ethernet1/3
                                  ip access-group IPv4_ACL_IN in
                                  ip access-group IPv4_ACL_OUT out

====================    ============================================

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

        self.acl_list = list()
        self.access_group_list = list()
        self.interface_list = list()

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

        self.interface_properties = set()
        self.interface_properties.add('name')

        self.access_group_properties = set()
        self.access_group_properties.add('afi')

        self.acl_properties = set()
        self.acl_properties.add('acl_direction')
        self.acl_properties.add('acl_name')
        self.acl_properties.add('acl_port')

        self.properties_set = set()
        self.properties_set.add('acl_direction')
        self.properties_set.add('acl_name')
        self.properties_set.add('acl_port')
        self.properties_set.add('afi')
        self.properties_set.add('name')
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.property_map = dict()
        self.property_map['acl_direction'] = 'direction'
        self.property_map['acl_name'] = 'name'
        self.property_map['acl_port'] = 'port'
        self.property_map['afi'] = 'afi'
        self.property_map['name'] = 'name'

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if len(self.interface_list) == 0:
            self.task_log.error('exiting. call instance.add_interface() at least once before calling instance.commit()')
            exit(1)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        populate self.ansible_task
        '''
        self.final_verification()

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['config'] = deepcopy(self.interface_list)
        self.ansible_task[self.ansible_module]['state'] = self.state

    def init_interface(self):
        for p in self.interface_properties:
            self.properties[p] = None
        self.access_group_list = list()
    def verify_interface(self):
        if self.name == None:
            self.task_log.error('exiting. Set instance.name before calling instance.add_interface()')
            exit(1)
        if len(self.access_group_list) == 0:
            self.task_log.error('exiting. Call instance.add_access_group() at least once before calling instance.add_interface()')
            exit(1)
    def add_interface(self):
        self.verify_interface()
        d = dict()
        d['name'] = self.name
        d['access_groups'] = deepcopy(self.access_group_list)
        self.interface_list.append(deepcopy(d))
        self.init_interface()

    def init_access_group(self):
        for p in self.access_group_properties:
            self.properties[p] = None
        self.acl_list = list()
    def verify_access_group(self):
        if self.afi == None:
            self.task_log.error('exiting. Set instance.afi before calling instance.add_access_group()')
            exit(1)
        if len(self.acl_list) == 0:
            self.task_log.error('exiting. Call instance.add_acl() at least once before calling instance.add_access_group()')
            exit(1)
    def add_access_group(self):
        self.verify_access_group()
        d = dict()
        d['afi'] = self.afi
        d['acls'] = deepcopy(self.acl_list)
        self.access_group_list.append(deepcopy(d))
        self.init_access_group()

    def init_acl(self):
        for p in self.acl_properties:
            self.properties[p] = None
    def verify_acl(self):
        if self.acl_name == None:
            self.task_log.error('exiting. Set instance.acl_name before calling instance.add_acl()')
            exit(1)
        if self.acl_direction == None:
            self.task_log.error('exiting. call instance.acl_direction before calling instance.add_acl()')
            exit(1)
    def add_acl(self):
        self.verify_acl()
        d = dict()
        for p in self.acl_properties:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.acl_list.append(deepcopy(d))
        self.init_acl()

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
