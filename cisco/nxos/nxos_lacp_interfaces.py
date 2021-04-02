# NxosLacpInterfaces() - cisco/nxos/nxos_lacp_interfaces.py
our_version = 106
import re
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosLacpInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosLacpInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lacp_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_lacp_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_lacp_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_lacp_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_lacp_interfaces.py>`_


|

================    ==============================================
User Methods        Description
================    ==============================================
add_interface()     Append lacp interface properties to the task
                    config list and reset the properties to None to
                    allow configuration of another interface.
                    See ``ScriptKit Example`` above for usage.
================    ==============================================


|
|

====================    ==============================================
Property                Description
====================    ==============================================
graceful                port-channel lacp graceful convergence.
                        Disable this only with lacp ports connected to
                        Non-Nexus peer. Disabling this with Nexus peer
                        can lead to port suspension.  If ``graceful``
                        is set, ``name`` must refer to a port-channel
                        interface::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.name = 'port-channel3'
                                task.graceful = True

min                     Minimum number of member interfaces in the
                        port-channel that must be up before the
                        port-channel interface is brought up.
                        If ``min`` is set, ``name`` must refer to
                        a port-channel interface::

                            - Type: int()
                            - Valid values: range: 1-32
                            - Example:
                                task.name = 'port-channel3'
                                task.min = 8

max                     Maximum number of interfaces in the
                        port-channel.  Member interfaces above this
                        limit will be placed in hot-standby mode.
                        If ``max`` is set, ``name`` must refer to
                        a port-channel interface::

                            - Type: int()
                            - Valid values: range: 1-32
                            - Example:
                                task.name = 'port-channel3'
                                task.max = 16

mode                    Configure delayed lacp on the port-channel.
                        LACP port-channels exchange LACP PDUs for quick
                        bundling of links when connecting a server and
                        a switch. However, the links go into suspended
                        state when the PDUs are not received.  The delayed
                        LACP feature enables one port-channel member, the
                        delayed-LACP port, to come up first as a member of
                        a regular port-channel before LACP PDUs are received.
                        After it is connected in LACP mode, other members,
                        the auxiliary LACP ports, are brought up. This avoids
                        the links becoming suspended when PDUs are not
                        received.  If ``mode`` is set, ``name`` must refer to
                        a port-channel interface::

                            - Type: str()
                            - Valid values: delay
                            - Example:
                                task.name = 'port-channel3'
                                task.mode = 'delay'

name                    Name of the interface::

                            - Type: str()
                            - Valid values:
                                - port-channelX
                                - EthernetX/Y
                            - Examples:
                                task.name = 'port-channel3'
                                task.name = 'Ethernet1/1'
                            - Required
                            - NOTES:
                                - Depending on which properties
                                  are set, only one of port-channel
                                  or ethernet will be valid.  Refer
                                  to individual properties for
                                  details.

port_priority           LACP port priority assigned to the
                        member ethernet interface. A higher port
                        priority value increases the likelihood
                        that a member port will be chosen to be
                        active in a bundle in the event that the
                        ``max`` (max-bundle) value is exceeded. 
                        Applicable only for Ethernet.
                        If ``port_priority`` is set, ``name``
                        must refer to a member ethernet interface::

                            - Type: int()
                            - Valid values: range: 1-65535
                            - Example:
                                task.name = 'Ethernet1/1'
                                task.port_priority = 8216

rate                    Rate at which PDUs are sent by LACP.
                        Applicable only for Ethernet.  At fast
                        rate LACP is transmitted once every 1
                        second. At normal rate LACP is transmitted
                        every 30 seconds after the link is bundled.
                        If ``rate`` is set, ``name`` must refer to
                        a member ethernet interface::

                            - Type: str()
                            - Valid values:
                                - fast
                                - normal
                            - Example:
                                task.name 'Ethernet1/1'
                                task.rate = 'fast'

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

suspend_individual      Disabling this will cause lacp to place a
                        member port into individual state (rather than
                        suspend it) in the event the individual port 
                        does not receive LACP BPDUs from its peer port.
                        If ``suspend_individual`` is set, ``name`` must
                        refer to a port-channel interface::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.name = 'port-channel3'
                                task.suspend_individual = True

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'enable lacp'

vpc                     Enable lacp convergence for vPC port
                        channels. If ``vpc`` is set, ``name``
                        must refer to a port-channel interface::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.name = 'port-channel3'
                                task.vpc = True

====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
'''

class NxosLacpInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_lacp_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.re_lacp_interface = re.compile('^port-channel\d+$')

        self.config = list()
        self.nxos_lacp_interfaces_valid_state = set()
        self.nxos_lacp_interfaces_valid_state.add('deleted')
        self.nxos_lacp_interfaces_valid_state.add('gathered')
        self.nxos_lacp_interfaces_valid_state.add('merged')
        self.nxos_lacp_interfaces_valid_state.add('overridden')
        self.nxos_lacp_interfaces_valid_state.add('parsed')
        self.nxos_lacp_interfaces_valid_state.add('rendered')
        self.nxos_lacp_interfaces_valid_state.add('replaced')

        self.nxos_lacp_interfaces_valid_mode = set()
        self.nxos_lacp_interfaces_valid_mode.add('delay')

        self.nxos_lacp_interfaces_valid_rate = set()
        self.nxos_lacp_interfaces_valid_rate.add('fast')
        self.nxos_lacp_interfaces_valid_rate.add('normal')

        self.lacp_interfaces_max_bundle_min = 1
        self.lacp_interfaces_max_bundle_max = 32

        self.lacp_interfaces_min_links_min = 1
        self.lacp_interfaces_min_links_max = 32

        self.lacp_interfaces_port_priority_min = 1
        self.lacp_interfaces_port_priority_max = 65535

        self.properties_set = set()
        self.properties_set.add('convergence')
        self.properties_set.add('graceful')
        self.properties_set.add('links')
        self.properties_set.add('min')
        self.properties_set.add('max')
        self.properties_set.add('mode')
        self.properties_set.add('name')
        self.properties_set.add('port_priority')
        self.properties_set.add('rate')
        self.properties_set.add('register')
        self.properties_set.add('running_config')
        self.properties_set.add('state')
        self.properties_set.add('suspend_individual')
        self.properties_set.add('vpc')

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

    def running_config_verification(self):
        if self.state != 'parsed':
            self.task_log.error('exiting. if running_config is set, state must be set to parsed')
            exit(1)
        if len(self.config) != 0:
            self.task_log.error('exiting. Cannot mix running_config with interface configuration.')
            self.task_log.error('Instantiate a separate NxosLacpInterfaces() instance and configure it solely for running_config.')
            exit(1)

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if self.running_config != None:
            self.running_config_verification()
        if self.running_config == None:
            if len(self.config) == 0:
                self.task_log.error('exiting. call instance.add_interface() at least once before calling self.update()')
                exit(1)

    def interface_verification(self):
        if self.running_config != None:
            self.task_log.error('exiting. Cannot mix running_config with interface configuration.')
            self.task_log.error('Instantiate a separate NxosLacpInterfaces() instance and configure it solely for running_config.')
            exit(1)
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.add_interface()')
            exit(1)
        if self.graceful != None and self.is_ethernet_interface(self.name):
            self.task_log.error('exiting. instance.graceful is not applicable when instance.name is ethernet. Got instance.name: {}'.format(self.name))
            exit(1) 
        if self.vpc != None and self.is_ethernet_interface(self.name):
            self.task_log.error('exiting. instance.vpc is not applicable when instance.name is ethernet. Got instance.name: {}'.format(self.name))
            exit(1)
        if self.mode != None and self.is_ethernet_interface(self.name):
            self.task_log.error('exiting. instance.mode is not applicable when instance.name is ethernet. Got instance.name: {}'.format(self.name))
            exit(1)
        if self.rate != None and self.is_port_channel_interface(self.name):
            self.task_log.error('exiting. instance.rate is not applicable when instance.name is port-channel. Got instance.name: {}'.format(self.name))
            exit(1)
        if self.port_priority != None and self.is_port_channel_interface(self.name):
            self.task_log.error('exiting. instance.port_priority is not applicable when instance.name is port-channel. Got instance.name: {}'.format(self.name))
            exit(1)
        if self.suspend_individual != None and self.is_ethernet_interface(self.name):
            self.task_log.error('exiting. instance.suspend_individual is not applicable when instance.name is ethernet. Got instance.name: {}'.format(self.name))
            exit(1)

    def add_interface(self):
        self.interface_verification()
        d = dict()
        convergence = dict()
        links = dict()

        d['name'] = self.name
        if self.graceful != None:
            convergence['graceful'] = self.graceful
        if self.vpc != None:
            convergence['vpc'] = self.vpc
        if len(convergence) != 0:
            d['convergence'] = deepcopy(convergence)

        if self.min != None:
            links['min'] = self.min
        if self.max != None:
            links['max'] = self.max
        if len(links) != 0:
            d['links'] = deepcopy(links)
        if self.mode != None:
            d['mode'] = self.mode
        if self.port_priority != None:
            d['port_priority'] = self.port_priority
        if self.rate != None:
            d['rate'] = self.rate
        if self.suspend_individual != None:
            d['suspend_individual'] = self.suspend_individual
        self.config.append(deepcopy(d))
        self.init_properties()

    def commit(self):
        self.update()
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

    def verify_nxos_lacp_interfaces_mode(self, x, parameter='mode'):
        verify_set = self.nxos_lacp_interfaces_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lacp_interfaces_mode'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lacp_interfaces_name(self, x, parameter='name'):
        if self.is_ethernet_interface(x):
            return
        if self.is_port_channel_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lacp_interfaces_name'
        expectation = 'valid LACP interface name e.g.: Ethernet1/1, port-channel3'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lacp_interfaces_max_bundle(self, x, parameter='max'):
        source_class = self.class_name
        range_min = self.lacp_interfaces_max_bundle_min
        range_max = self.lacp_interfaces_max_bundle_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_lacp_interfaces_min_links(self, x, parameter='min'):
        source_class = self.class_name
        range_min = self.lacp_interfaces_min_links_min
        range_max = self.lacp_interfaces_min_links_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_lacp_interfaces_rate(self, x, parameter='rate'):
        verify_set = self.nxos_lacp_interfaces_valid_rate
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lacp_interfaces_rate'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lacp_interfaces_port_priority(self, x, parameter='port_priority'):
        source_class = self.class_name
        range_min = self.lacp_interfaces_port_priority_min
        range_max = self.lacp_interfaces_port_priority_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_lacp_interfaces_state(self, x, parameter='state'):
        verify_set = self.nxos_lacp_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lacp_interfaces_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def graceful(self):
        return self.properties['graceful']
    @graceful.setter
    def graceful(self, x):
        parameter = 'graceful'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def max(self):
        return self.properties['max']
    @max.setter
    def max(self, x):
        parameter = 'max'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lacp_interfaces_max_bundle(x, parameter)
        self.properties[parameter] = x

    @property
    def min(self):
        return self.properties['min']
    @min.setter
    def min(self, x):
        parameter = 'min'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lacp_interfaces_min_links(x, parameter)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lacp_interfaces_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lacp_interfaces_name(x, parameter)
        self.properties['name'] = x

    @property
    def port_priority(self):
        return self.properties['port_priority']
    @port_priority.setter
    def port_priority(self, x):
        parameter = 'port_priority'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lacp_interfaces_port_priority(x, parameter)
        self.properties[parameter] = x

    @property
    def rate(self):
        return self.properties['rate']
    @rate.setter
    def rate(self, x):
        parameter = 'rate'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lacp_interfaces_rate(x, parameter)
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
        self.verify_nxos_lacp_interfaces_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suspend_individual(self):
        return self.properties['suspend_individual']
    @suspend_individual.setter
    def suspend_individual(self, x):
        parameter = 'suspend_individual'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def vpc(self):
        return self.properties['vpc']
    @vpc.setter
    def vpc(self, x):
        parameter = 'vpc'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

