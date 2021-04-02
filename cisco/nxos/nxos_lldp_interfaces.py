# NxosLldpInterfaces() - cisco/nxos/nxos_lldp_interfaces.py
our_version = 106

from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosLldpInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosLldpInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lldp_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_lldp_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_lldp_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_lldp_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_lldp_interfaces.py>`_


|

================    ==================================================
User Methods        Description
================    ==================================================
add_interface()     Append an LLDP interface to the task and reset
                    lldp interface properties to None to allow 
                    configuration of another interface. See
                    ``ScriptKit Example`` above for example usage.
================    ==================================================


|
|

============================    ==============================================
Property                        Description
============================    ==============================================
name                            Full name of the interface on which to
                                configure LLDP::

                                    - Type: str()
                                    - Valid values: An LLDP-capable interface name
                                    - Required (if running_config is not set)
                                    - Example:
                                        task.name = 'Ethernet1/1'

receive                         Enable ``True`` or disable ``False``
                                reception of LLDP packets on ``name``.
                                By default, this is enabled after LLDP is
                                enabled globally::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.receive = True

tlv_set_management_address      Advertise the IPv4 or IPv6 management address 
                                associated with ``name``::

                                    - Type: str()
                                    - Valid values: an IPv4 or IPv6 address
                                    - Example:
                                        task.tlv_set_management_address = '10.1.2.3'

tlv_set_vlan                    Advertise the VLAN ID associated with ``name``::

                                    - Type: str()
                                    - Valid values: range 1-4094
                                    - Example:
                                        task.tlv_set_vlan = 30

transmit                        Enable ``True`` or Disable ``False``
                                transmission of LLDP packets on ``name``.
                                By default, this is enabled after LLDP is
                                enabled globally::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.transmit = True

register                        Ansible variable to save output to::

                                    - Type: str()
                                    - Examples:
                                        task.register = 'result'

running_config                  Full path to a file containing the output of
                                ``show running-config | section ^interface``.
                                ``running_config`` is mutually-exclusive with
                                every other property except ``state`` and
                                ``register``.  ``state`` must be set to ``parsed``
                                if ``running_config`` is set.::

                                    - Type: str()
                                    - Examples:
                                        task.state = 'parsed'
                                        task.running_config = '/tmp/running.cfg'

state                           Desired state after the task has run::

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

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Example:
                                        - task.task_name = 'configure lldp interfaces'

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosLldpInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_lldp_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.config = list()

        self.nxos_lldp_interfaces_valid_state = set()
        self.nxos_lldp_interfaces_valid_state.add('deleted')
        self.nxos_lldp_interfaces_valid_state.add('gathered')
        self.nxos_lldp_interfaces_valid_state.add('merged')
        self.nxos_lldp_interfaces_valid_state.add('overridden')
        self.nxos_lldp_interfaces_valid_state.add('parsed')
        self.nxos_lldp_interfaces_valid_state.add('rendered')
        self.nxos_lldp_interfaces_valid_state.add('replaced')

        self.min_vlan = 1
        self.max_vlan = 4094

        self.properties_set = set()
        self.properties_set.add('name')
        self.properties_set.add('receive')
        self.properties_set.add('register')
        self.properties_set.add('running_config')
        self.properties_set.add('state')
        self.properties_set.add('tlv_set_management_address')
        self.properties_set.add('tlv_set_vlan')
        self.properties_set.add('transmit')

        self.config_properties_set = set()
        self.config_properties_set.add('name')
        self.config_properties_set.add('receive')
        self.config_properties_set.add('tlv_set_management_address')
        self.config_properties_set.add('tlv_set_vlan')
        self.config_properties_set.add('transmit')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)
        self.scriptkit_properties.update(self.config_properties_set)
        self.scriptkit_properties.add('state')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def init_config_properties(self):
        for p in self.config_properties_set:
            self.properties[p] = None

    def interface_verification(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.add_iterface()')
            exit(1)

    def add_interface(self):
        self.interface_verification()
        d = dict()
        tlv_set = dict()
        d['name'] = self.name
        if self.transmit != None:
            d['transmit'] = self.transmit
        if self.receive != None:
            d['receive'] = self.receive
        if self.tlv_set_management_address != None:
            tlv_set['management_address'] = self.tlv_set_management_address
        if self.tlv_set_vlan != None:
            tlv_set['vlan'] = self.tlv_set_vlan
        if len(tlv_set) != 0:
            d['tlv_set'] = deepcopy(tlv_set)
        self.config.append(deepcopy(d))
        self.init_config_properties()

    def final_verification_running_config(self):
        if self.state != 'parsed':
            self.task_log.error('exiting. if running_config is set, state must be set to parsed')
            exit(1)
    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if self.running_config != None:
            self.final_verification_running_config()
        else:
            if len(self.config) == 0 and self.state != 'deleted':
                self.task_log.error('exiting. call intance.add_interface() at least once before calling instance.commit().')
                exit(1)

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

    def add_interface(self):
        d = dict()
        tlv_set = dict()
        d['name'] = self.name
        if self.transmit != None:
            d['transmit'] = self.transmit
        if self.receive != None:
            d['receive'] = self.receive
        if self.tlv_set_management_address != None:
            tlv_set['management_address'] = self.tlv_set_management_address
        if self.tlv_set_vlan != None:
            tlv_set['vlan'] = self.tlv_set_vlan
        if len(tlv_set) != 0:
            d['tlv_set'] = deepcopy(tlv_set)
        self.config.append(deepcopy(d))
        self.init_config_properties()

    def verify_nxos_lldp_interfaces_tlv_set_management_address(self, x, parameter='tlv_set_management_address'):
        if self.is_ipv6_address(x):
            return
        if self.is_ipv4_unicast_address(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lldp_interfaces_tlv_set_management_address'
        expectation = 'ipv4 or ipv6 unicast address without prefixlen/mask e.g. 1.1.1.1, 2001::1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lldp_interfaces_state(self, x, parameter='state'):
        if x in self.nxos_lldp_interfaces_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lldp_interfaces_state'
        expectation = ','.join(self.nxos_lldp_interfaces_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lldp_interfaces_tlv_set_vlan(self, x, parameter='tlv_set_vlan'):
        source_class = self.class_name
        source_method = 'verify_nxos_lldp_interfaces_tlv_set_vlan'
        self.verify_integer_range(x, self.min_vlan, self.max_vlan, source_class, source_method)

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def receive(self):
        return self.properties['receive']
    @receive.setter
    def receive(self, x):
        parameter = 'receive'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
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
        self.verify_nxos_lldp_interfaces_state(x, parameter)
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

    @property
    def tlv_set_management_address(self):
        return self.properties['tlv_set_management_address']
    @tlv_set_management_address.setter
    def tlv_set_management_address(self, x):
        parameter = 'tlv_set_management_address'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lldp_interfaces_tlv_set_management_address(x, parameter)
        self.properties[parameter] = x

    @property
    def tlv_set_vlan(self):
        return self.properties['tlv_set_vlan']
    @tlv_set_vlan.setter
    def tlv_set_vlan(self, x):
        parameter = 'tlv_set_vlan'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lldp_interfaces_tlv_set_vlan(x, parameter)
        self.properties[parameter] = x

    @property
    def transmit(self):
        return self.properties['transmit']
    @transmit.setter
    def transmit(self, x):
        parameter = 'transmit'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x
