# NxosLagInterfaces() - cisco/nxos/nxos_lag_interfaces.py
our_version = 106

from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosLagInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosLagInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lag_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_lag_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_lag_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_lag_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_lag_interfaces.py>`_


|

================    ==================================================
User Methods        Description
================    ==================================================
add_member()        Append a member interface to the task and reset
                    member properties to None to allow configuration
                    of another member interface. See
                    ``ScriptKit Example`` above for usage.

add_lag()           Append a lag interface, and its members (if any)
                    to the task and reset lag properties to None to
                    allow configuration of another lag interface. See
                    ``ScriptKit Example`` above for usage.
================    ==================================================


|
|

====================    ==============================================
Property                Description
====================    ==============================================
force                   When ``True`` adds the ``force`` keyword to the
                        NX-OS channel-group CLI::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.member = 'Ethernet1/1'
                                task.force = True
                                task.add_member()
                                task.name = 'port-channel20'
                                task.add_lag()
                            - Resulting Ansible task:
                                config:
                                - name: port-channel20
                                  members:
                                  - member: Ethernet1/1
                                    force: true
                            - Resulting NX-OS CLI:
                                interface Ethernet1/1
                                   channel-group 20 force

member                  The full name of the member ethernet interface::

                            - Type: str()
                            - Valid values: An ethernet interface name
                            - Example:
                                task.member = 'Ethernet1/1'

mode                    Member interface link aggregation mode::

                            - Type: str()
                            - Valid values:
                                - active
                                    Initiate negotiation with the remote end
                                    by sending LACP PDUs
                                - on
                                    Do not participate in LACP. This forces
                                    the interface's membership in the port-channel
                                    regardless of the state of the remote end
                                - passive
                                    Participate in LACP, by responding to received
                                    LACP PDUs, but do not initiate the negotiation
                            - Example:
                                task.member = 'Ethernet1/1'
                                task.mode = 'active'
                                task.add_member()

name                    Name of the port-channel interface::

                            - Type: str()
                            - Valid values: A port-channel interface name
                            - Example:
                                task.name = 'port-channel3'

register                Ansible variable to save output to::

                            - Type: str()
                            - Examples:
                                task.register = 'result'

running_config          Full path to a file containing the output of
                        ``show running-config | section ^interface``.
                        ``running_config`` is mutually-exclusive with
                        every other property except ``state`` and
                        ``register``.  ``state`` must be set to ``parsed``
                        if ``running_config`` is set.::

                            - Type: str()
                            - Examples:
                                task.state = 'parsed'
                                task.running_config = '/tmp/running.cfg'

state                   Desired state after task has run::

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

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'configure lag'

====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosLagInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_lag_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.config = list()
        self.lag = list()
        self.lag_members = list()

        self.nxos_lag_interfaces_valid_state = set()
        self.nxos_lag_interfaces_valid_state.add('deleted')
        self.nxos_lag_interfaces_valid_state.add('gathered')
        self.nxos_lag_interfaces_valid_state.add('merged')
        self.nxos_lag_interfaces_valid_state.add('overridden')
        self.nxos_lag_interfaces_valid_state.add('parsed')
        self.nxos_lag_interfaces_valid_state.add('rendered')
        self.nxos_lag_interfaces_valid_state.add('replaced')

        self.nxos_lag_interfaces_valid_mode = set()
        self.nxos_lag_interfaces_valid_mode.add('active')
        self.nxos_lag_interfaces_valid_mode.add('on')
        self.nxos_lag_interfaces_valid_mode.add('passive')

        self.properties_set = set()
        self.properties_set.add('force')
        self.properties_set.add('member')
        self.properties_set.add('mode')
        self.properties_set.add('name')
        self.properties_set.add('register')
        self.properties_set.add('running_config')
        self.properties_set.add('state')

        self.properties_lag = set()
        self.properties_lag.add('name')

        self.properties_member = set()
        self.properties_member.add('force')
        self.properties_member.add('member')
        self.properties_member.add('mode')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def running_config_verification(self):
        if self.state != 'parsed':
            self.task_log.error('exiting. if running_config is set, state must be set to parsed')
            exit(1)
        if len(self.config) != 0:
            self.task_log.error('exiting. Cannot mix running_config with interface configuration.')
            self.task_log.error('Instantiate a separate NxosLagInterfaces() instance and configure it solely for running_config.')
            exit(1)

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.running_config != None:
            self.running_config_verification()
        if self.running_config == None:
            if len(self.config) == 0:
                self.task_log.error('exiting. call instance.add_lag() at least once before calling self.update()')
                exit(1)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()

        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        if self.register != None:
            self.ansible_task['register'] = self.register
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.running_config != None:
            self.ansible_task[self.ansible_module]['running_config'] = self.make_running_config()
        else:
            self.ansible_task[self.ansible_module]['config'] = deepcopy(self.config)

    def make_running_config(self):
        return r'{{' +  " lookup(" + r'"file"' + ',' + r'"' + self.running_config + r'"' + ')' + r' }}'

    def verify_lag(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling add_lag()')
            exit(1)
    def init_lag(self):
        for p in self.properties_lag:
            self.properties[p] = None
        self.lag_members = list()
    def add_lag(self):
        self.verify_lag()
        d = dict()
        d['name'] = self.name
        if len(self.lag_members) != 0:
            d['members'] = deepcopy(self.lag_members)
        self.config.append(deepcopy(d))
        self.init_lag()

    def verify_member(self):
         if self.member == None:
            self.task_log.error('exiting. set instance.member to a valid ethernet interface name before calling add_member()')
            exit(1)
    def init_member(self):
        for p in self.properties_member:
            self.properties[p] = None
    def add_member(self):
        d = dict()
        d['member'] = self.member
        if self.mode != None:
            d['mode'] = self.mode
        if self.force != None:
            d['force'] = self.force
        self.lag_members.append(deepcopy(d))
        self.init_member()

    def verify_nxos_lag_interfaces_mode(self, x, parameter='mode'):
        verify_set = self.nxos_lag_interfaces_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lag_interfaces_mode'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lag_interfaces_member(self, x, parameter='member'):
        if self.is_ethernet_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lag_interfaces_member'
        expectation = 'valid LAG member interface name e.g.: Ethernet1/1, Ethernet1/2/1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lag_interfaces_name(self, x, parameter='name'):
        if self.is_port_channel_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lag_interfaces_name'
        expectation = 'port-channel interface name e.g.: port-channel3'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lag_interfaces_state(self, x, parameter='state'):
        verify_set = self.nxos_lag_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lag_interfaces_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def force(self):
        return self.properties['force']
    @force.setter
    def force(self, x):
        parameter = 'force'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def member(self):
        return self.properties['member']
    @member.setter
    def member(self, x):
        parameter = 'member'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lag_interfaces_member(x, parameter)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lag_interfaces_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lag_interfaces_name(x, parameter)
        self.properties[parameter] = x

    @property
    def register(self):
        return self.properties['register']
    @register.setter
    def register(self, x):
        parameter = 'register'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def running_config(self):
        return self.properties['running_config']
    @running_config.setter
    def running_config(self, x):
        parameter = 'running_config'
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
        self.verify_nxos_lag_interfaces_state(x, parameter)
        self.properties[parameter] = x

    @property
    def task_name(self):
        return self.properties['task_name']
    @task_name.setter
    def task_name(self, x):
        parameter = 'task_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
