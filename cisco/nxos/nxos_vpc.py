# NxosVpc() - cisco/nxos/nxos_vpc.py
our_version = 108
from copy import deepcopy
from ask.common.task import Task
'''
******************************************
NxosVpc() - nxos_vpc.py
******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVpc() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vpc <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vpc.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vpc.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vpc.py>`_

|

============================    ===========
Property                        Description
============================    ===========
auto_recovery                   Enables/Disables auto recovery on platforms that support disable
                                timers are not modifiable with this attribute
                                mutually exclusive with auto_recovery_reload_delay::

                                    - Type: bool()
                                    - Valid values: no, yes
                                    - Example: task.auto_recovery = 'no'
auto_recovery_reload_delay      Group number of the portchannel that will be configured::

                                    - Type: str()
                                    - Valid values: int() range: 1-4096
                                    - Example: task.portchannel = 10
                                    - Required
delay_restore                   Delay in bringing up the vPC links (in seconds).
                                NxosVpc() converts this to str() prior to adding to the playbook::

                                    - Type: int() converted to str()
                                    - Valid values: int() range: 1-3600
                                    - Example: task.delay_restore = 300
delay_restore_interface_vlan    Delay in bringing-up interface-vlan, in seconds.
                                NxosVpc() converts this to str() prior to adding to the playbook::

                                    - Type: int() converted to str()
                                    - Valid values: int() range: 1-3600
                                    - Example: task.delay_restore_interface_vlan = 150
delay_restore_orphan_port       vPC orphan-port delay bring-up timer, in seconds.
                                NxosVpc() converts this to str() prior to adding to the playbook::

                                    - Type: int() converted to str()
                                    - Valid values: int() range: 0-300
                                    - Example: task.delay_restore_orphan_port = 150
domain                          vPC domain.
                                NxosVpc() converts this to str() prior to adding to the playbook::

                                    - Type: int() converted to str()
                                    - Valid values: int() range: 1-1000
                                    - Example: task.domain = 1
peer_gw                         Enables/Disables peer gateway::

                                    - Type: bool()
                                    - Valid values: no, yes
                                    - Example: task.peer_gw = 'yes'
pkl_dest                        Destination (remote) IP address used for peer keepalive link.
                                pkl_dest is required whenever pkl options are used::

                                    - Type: str()
                                    - Valid values: ipv4 address without prefix
                                    - Example: task.pkl_dest = '1.1.1.2'
pkl_src                         Source IP address used for peer keepalive link::

                                    - Type: str()
                                    - Valid values: ipv4 address without prefix
                                    - Example: task.pkl_src = '1.1.1.1'
pkl_vrf                         VRF used for peer keepalive link.
                                The VRF must exist on the device before using pkl_vrf.
                                (Note) 'default' is an overloaded term: Default vrf 
                                context for pkl_vrf is 'management'; 'pkl_vrf: default'
                                refers to the literal 'default' rib.::

                                    - Type: str()
                                    - Valid values: vrf name
                                    - Example: task.pkl_vrf = 'myVrf'
role_priority                   Priority to be used during vPC role (primary/secondary) election.
                                Lower value will become vpc primary::

                                    - Type: int()
                                    - Valid values: int() range: 1-65535
                                    - Example: task.role_priority = 100

state                           The state of the configuration after module completion.::

                                - Type: str()
                                - Valid values: absent, present
                                - Example: task.state = 'present'

system_priority                 System device priority. Value must match on both vpc peers.::

                                - Type: int()
                                - Valid values: int() range: 1-65535
                                - Example: task.system_priority = 2000
============================    ===========


Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''
class NxosVpc(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vpc'
        super().__init__(ansible_module, task_log)
        self._version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()

        self.auto_recovery_reload_delay_min = 60
        self.auto_recovery_reload_delay_max = 3600

        self.delay_restore_min = 1
        self.delay_restore_max = 3600

        self.delay_restore_interface_vlan_min = 1
        self.delay_restore_interface_vlan_max = 3600

        self.delay_restore_orphan_port_min = 0
        self.delay_restore_orphan_port_max = 300

        self.domain_min = 1
        self.domain_max = 1000

        self.role_priority_min = 1
        self.role_priority_max = 65535

        self.system_priority_min = 1
        self.system_priority_max = 65535

        self.nxos_vpc_valid_state = set()
        self.nxos_vpc_valid_state.add('absent')
        self.nxos_vpc_valid_state.add('present')

        self.properties_set = set()
        self.properties_set.add('auto_recovery')
        self.properties_set.add('auto_recovery_reload_delay')
        self.properties_set.add('delay_restore')
        self.properties_set.add('delay_restore_interface_vlan')
        self.properties_set.add('delay_restore_orphan_port')
        self.properties_set.add('domain')
        self.properties_set.add('peer_gw')
        self.properties_set.add('pkl_dest')
        self.properties_set.add('pkl_src')
        self.properties_set.add('pkl_vrf')
        self.properties_set.add('role_priority')
        self.properties_set.add('state')
        self.properties_set.add('system_priority')

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
        if self.domain == None:
            self.task_log.error('exiting. call instance.domain before calling instance.update()')
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
                d[p] = str(self.properties[p])
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_vpc_auto_recovery_reload_delay(self, x, parameter='auto_recovery_reload_delay'):
        source_class = self.class_name
        range_min = self.auto_recovery_reload_delay_min
        range_max = self.auto_recovery_reload_delay_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_vpc_delay_restore(self, x, parameter='delay_restore'):
        source_class = self.class_name
        range_min = self.delay_restore_min
        range_max = self.delay_restore_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_vpc_delay_restore_interface_vlan(self, x, parameter='delay_restore_interface_vlan'):
        source_class = self.class_name
        range_min = self.delay_restore_interface_vlan_min
        range_max = self.delay_restore_interface_vlan_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_vpc_delay_restore_orphan_port(self, x, parameter='delay_restore_orphan_port'):
        source_class = self.class_name
        range_min = self.delay_restore_orphan_port_min
        range_max = self.delay_restore_orphan_port_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_vpc_domain(self, x, parameter='domain'):
        source_class = self.class_name
        range_min = self.domain_min
        range_max = self.domain_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_vpc_role_priority(self, x, parameter='role_priority'):
        source_class = self.class_name
        range_min = self.role_priority_min
        range_max = self.role_priority_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_vpc_system_priority(self, x, parameter='system_priority'):
        source_class = self.class_name
        range_min = self.system_priority_min
        range_max = self.system_priority_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_vpc_state(self, x, parameter='state'):
        verify_set = self.nxos_vpc_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vpc_state'
        expectation = ','.join(self.verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def auto_recovery(self):
        return self.properties['auto_recovery']
    @auto_recovery.setter
    def auto_recovery(self, x):
        parameter = 'auto_recovery'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def auto_recovery_reload_delay(self):
        return self.properties['auto_recovery_reload_delay']
    @auto_recovery_reload_delay.setter
    def auto_recovery_reload_delay(self, x):
        parameter = 'auto_recovery_reload_delay'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_auto_recovery_reload_delay(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def delay_restore(self):
        return self.properties['delay_restore']
    @delay_restore.setter
    def delay_restore(self, x):
        parameter = 'delay_restore'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_delay_restore(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def delay_restore_interface_vlan(self):
        return self.properties['delay_restore_interface_vlan']
    @delay_restore_interface_vlan.setter
    def delay_restore_interface_vlan(self, x):
        parameter = 'delay_restore_interface_vlan'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_delay_restore_interface_vlan(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def delay_restore_orphan_port(self):
        return self.properties['delay_restore_orphan_port']
    @delay_restore_orphan_port.setter
    def delay_restore_orphan_port(self, x):
        parameter = 'delay_restore_orphan_port'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_delay_restore_orphan_port(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def domain(self):
        return self.properties['domain']
    @domain.setter
    def domain(self, x):
        parameter = 'domain'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_domain(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def peer_gw(self):
        return self.properties['peer_gw']
    @peer_gw.setter
    def peer_gw(self, x):
        parameter = 'peer_gw'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def pkl_dest(self):
        return self.properties['pkl_dest']
    @pkl_dest.setter
    def pkl_dest(self, x):
        parameter = 'pkl_dest'
        if self.set_none(x, parameter):
            return
        self.verify_ipv4_ipv6(x, parameter)
        self.properties[parameter] = x

    @property
    def pkl_src(self):
        return self.properties['pkl_src']
    @pkl_src.setter
    def pkl_src(self, x):
        parameter = 'pkl_src'
        if self.set_none(x, parameter):
            return
        self.verify_ipv4_ipv6(x, parameter)
        self.properties[parameter] = x

    @property
    def pkl_vrf(self):
        return self.properties['pkl_vrf']
    @pkl_vrf.setter
    def pkl_vrf(self, x):
        parameter = 'pkl_vrf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def role_priority(self):
        return self.properties['role_priority']
    @role_priority.setter
    def role_priority(self, x):
        parameter = 'role_priority'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_role_priority(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_state(x, parameter)
        self.properties[parameter] = x

    @property
    def system_priority(self):
        return self.properties['system_priority']
    @system_priority.setter
    def system_priority(self, x):
        parameter = 'system_priority'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_system_priority(x, parameter)
        self.properties[parameter] = str(x)
