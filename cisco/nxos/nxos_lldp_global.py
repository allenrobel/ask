# NxosLldpGlobal() - cisco/nxos/nxos_lldp_global.py
our_version = 104
import re
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosLldpGlobal()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosLldpGlobal() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lldp_global
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_lldp_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_lldp_global_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_lldp_global.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_lldp_global.py>`_

Dependencies
------------

1. ``feature lldp`` must enabled on the target before using this module

|

========================    ==============================================
Property                    Description
========================    ==============================================
dcbxp                       Enable ``True`` or disable ``False``
                            Data Center Bridging Exchange Protocol TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.dcbxp = False

holdtime                    Amount of time the receiving device should
                            hold the information::

                                - Type: int()
                                - Valid values: range: 0-65535
                                - Units: seconds
                                - Example:
                                    task.holdtime = 300

management_address_v4       Enable ``True`` or disable ``False``
                            Management address with TLV ipv4::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.management_address_v4 = True

management_address_v6       Enable ``True`` or disable ``False``
                            Management address with TLV ipv6::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.management_address_v6 = False

port_description            Enable ``True`` or disable ``False``
                            port description TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.port_description = False

port_id                     Advertise interface names in the long(0)
                            or short(1) form::

                                - Type: int()
                                - Valid values: 0, 1
                                - Example:
                                    task.port_id = 0

port_vlan                   Enable ``True`` or disable ``False``
                            port VLAN ID TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.port_vlan = False

power_management            Enable ``True`` or disable ``False``
                            IEEE 802.3 DTE Power via MDI TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.power_management = False

register                    Ansible variable to save output to::

                                - Type: str()
                                - Examples:
                                    task.register = 'result'

reinit                      Amount of time to delay the initialization
                            of LLDP on any interface::

                                - Type: int()
                                - Valid values: range: 0-65535
                                - Units: seconds
                                - Example:
                                    task.reinit = 30

running_config              Full path to a file containing the output of
                            ``show running-config | include lldp``.
                            ``running_config`` is mutually-exclusive with
                            every other property except ``state`` and
                            ``register``.  ``state`` must be set to ``parsed``
                            if ``running_config`` is set.::

                                - Type: str()
                                - Examples:
                                    task.state = 'parsed'
                                    task.running_config = '/tmp/running.cfg'

state                       Desired state after task has run::

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

system_capabilities         Enable ``True`` or disable ``False``
                            system capabilities TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.system_capabilities = False

system_description          Enable ``True`` or disable ``False``
                            system description TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.system_description = False

system_name                 Enable ``True`` or disable ``False``
                            system name TLV::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.system_name = False

task_name                   Name of the task. Ansible will display this
                            when the playbook is run::

                                - Type: str()
                                - Example:
                                    - task.task_name = 'configure lldp global'

timer                       LLDP update transmission frequency::

                                - Type: int()
                                - Valid values: range: 0-65535
                                - Units: seconds
                                - Example:
                                    task.timer = 30

========================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)


'''
class NxosLldpGlobal(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_lldp_global'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_global = set()
        self.properties_global.add('holdtime')
        self.properties_global.add('port_id')
        self.properties_global.add('reinit')
        self.properties_global.add('timer')

        self.properties_tlv_select = set()
        self.properties_tlv_select.add('dcbxp') 
        self.properties_tlv_select.add('power_management')

        self.properties_tlv_select_management_address = set()
        self.properties_tlv_select_management_address.add('management_address_v4')
        self.properties_tlv_select_management_address.add('management_address_v6')

        self.properties_tlv_select_port = set()
        self.properties_tlv_select_port.add('port_description')
        self.properties_tlv_select_port.add('port_vlan')

        self.properties_tlv_select_system = set()
        self.properties_tlv_select_system.add('system_capabilities')
        self.properties_tlv_select_system.add('system_description')
        self.properties_tlv_select_system.add('system_name')

        self.properties_set = set()
        self.properties_set = self.properties_set.union(self.properties_global)
        self.properties_set = self.properties_set.union(self.properties_tlv_select)
        self.properties_set = self.properties_set.union(self.properties_tlv_select_management_address)
        self.properties_set = self.properties_set.union(self.properties_tlv_select_port)
        self.properties_set = self.properties_set.union(self.properties_tlv_select_system)

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)
        self.scriptkit_properties.add('name')
        self.scriptkit_properties.add('register')
        self.scriptkit_properties.add('running_config')
        self.scriptkit_properties.add('state')

        # property_map is used to:
        #    1. Map between disambiguated property names and the ambiguous Ansible
        #       property names used in the Ansible playbook
        #    2. Map between property names that we have chosen to make clearer
        #       and the corresponding properties names used in the Ansible playbook
        # For example, in the case of #1, the property names for port and system tlv_select
        # descriptioni are ambiguous (they are both 'description').  We disambiguate these
        # by providing properties for system_description and port_description.
        # Later, we use property_map to apply the correct property name/values when populating
        # the playbook.
        #     system_description -> description
        #     port_description   -> description
        #
        # In the case of #2, property names of 'v4' and 'v6' would not be descriptive enough
        # (v4 for what?) so we change these to management_address_v4 and management_address_v6.
        # It's also feasible that, in the future, we may gain a TLV for some other object that
        # has values for v4 and v6, hence, a bit of future-proofing.
        self.property_map = dict()
        for p in self.properties_tlv_select_management_address:
            mapped_p = re.sub('management_address_', '', p)
            self.property_map[p] = mapped_p
        for p in self.properties_tlv_select_port:
            mapped_p = re.sub('port_', '', p)
            self.property_map[p] = mapped_p
        for p in self.properties_tlv_select_system:
            self.property_map[p] = re.sub('system_', '', p)

        self.nxos_lldp_global_valid_state = set()
        self.nxos_lldp_global_valid_state.add('merged')
        self.nxos_lldp_global_valid_state.add('replaced')
        self.nxos_lldp_global_valid_state.add('overridden')
        self.nxos_lldp_global_valid_state.add('deleted')
        self.nxos_lldp_global_valid_state.add('gathered')
        self.nxos_lldp_global_valid_state.add('rendered')
        self.nxos_lldp_global_valid_state.add('parsed')

        self.lldp_port_id_min = 0
        self.lldp_port_id_max = 1

        self.lldp_holdtime_min = 1
        self.lldp_holdtime_max = 255

        self.lldp_reinit_min = 1
        self.lldp_reinit_max = 10

        self.lldp_timer_min = 1
        self.lldp_timer_max = 254

        self.init_properties()

    def get_mapped_property(self, x):
        '''
        return either a mapped property, if one exists, or x
        '''
        if x in self.property_map:
            return self.property_map[x]
        return x

    def init_properties_tlv_select_management_address(self):
        for p in self.properties_tlv_select_management_address:
            self.properties[p] = None

    def init_properties_tlv_select_port(self):
        for p in self.properties_tlv_select_port:
            self.properties[p] = None

    def init_properties_tlv_select_system(self):
        for p in self.properties_tlv_select_system:
            self.properties[p] = None

    def init_properties_tlv_select(self):
        for p in self.properties_tlv_select:
            self.properties[p] = None
        self.init_properties_tlv_select_management_address()
        self.init_properties_tlv_select_port()
        self.init_properties_tlv_select_system()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_global:
            self.properties[p] = None
        self.init_properties_tlv_select()
        self.properties['register'] = None
        self.properties['running_config'] = None
        self.properties['task_name'] = None

    def running_config_verification(self):
        if self.state != 'parsed':
            self.task_log.error('exiting. if running_config is set, state must be set to parsed')
            exit(1)
        for p in self.properties_set:
            if self.properties[p] != None:
                self.task_log.error('exiting. Cannot mix running_config with lldp global configuration.')
                self.task_log.error('Instantiate a separate NxosLldpGlobal() instance and configure it solely for running_config.')
                exit(1)

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.running_config != None:
            self.running_config_verification()

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        if self.register != None:
            self.ansible_task['register'] = self.register
        if self.running_config != None:
            self.ansible_task[self.ansible_module]['running_config'] = self.make_running_config()
            return

        d = dict()
        for p in self.properties_global:
            if self.properties[p] != None:
                d[p] = self.properties[p]

        tlv_select_dict = dict()
        for p in self.properties_tlv_select:
            if self.properties[p] != None:
                tlv_select_dict[p] = self.properties[p]

        management_address_dict = dict()
        for p in self.properties_tlv_select_management_address:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                management_address_dict[mapped_p] = self.properties[p]

        port_dict = dict()
        for p in self.properties_tlv_select_port:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                port_dict[mapped_p] = self.properties[p]

        system_dict = dict()
        for p in self.properties_tlv_select_system:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                system_dict[mapped_p] = self.properties[p]

        if len(management_address_dict) != 0:
            tlv_select_dict['management_address'] = deepcopy(management_address_dict)
        if len(port_dict) != 0:
            tlv_select_dict['port'] = deepcopy(port_dict)
        if len(system_dict) != 0:
            tlv_select_dict['system'] = deepcopy(system_dict)

        if len(tlv_select_dict) != 0:
            d['tlv_select'] = deepcopy(tlv_select_dict)

        self.ansible_task[self.ansible_module]['config'] = deepcopy(d)

    def make_running_config(self):
        return r'{{' +  " lookup(" + r'"file"' + ',' + r'"' + self.running_config + r'"' + ')' + r' }}'

    def verify_nxos_lldp_global_state(self, x, parameter='state'):
        verify_set = self.nxos_lldp_global_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_lldp_global_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_lldp_global_holdtime(self, x, source_method='verify_nxos_lldp_global_holdtime'):
        self.verify_integer_range(x, self.lldp_holdtime_min, self.lldp_holdtime_max, self.class_name, source_method)
    def verify_nxos_lldp_global_port_id(self, x, source_method='verify_nxos_lldp_global_port_id'):
        self.verify_integer_range(x, self.lldp_port_id_min, self.lldp_port_id_max, self.class_name, source_method)
    def verify_nxos_lldp_global_reinit(self, x, source_method='verify_nxos_lldp_global_reinit'):
        self.verify_integer_range(x, self.lldp_reinit_min, self.lldp_reinit_max, self.class_name, source_method)
    def verify_nxos_lldp_global_timer(self, x, source_method='verify_nxos_lldp_global_timer'):
        self.verify_integer_range(x, self.lldp_timer_min, self.lldp_timer_max, self.class_name, source_method)

    @property
    def dcbxp(self):
        return self.properties['dcbxp']
    @dcbxp.setter
    def dcbxp(self, x):
        parameter = 'dcbxp'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def holdtime(self):
        return self.properties['holdtime']
    @holdtime.setter
    def holdtime(self, x):
        parameter = 'holdtime'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lldp_global_holdtime(x, parameter)
        self.properties[parameter] = x

    @property
    def management_address_v4(self):
        return self.properties['management_address_v4']
    @management_address_v4.setter
    def management_address_v4(self, x):
        parameter = 'management_address_v4'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def management_address_v6(self):
        return self.properties['management_address_v6']
    @management_address_v6.setter
    def management_address_v6(self, x):
        parameter = 'management_address_v6'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def port_description(self):
        return self.properties['port_description']
    @port_description.setter
    def port_description(self, x):
        parameter = 'port_description'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def port_id(self):
        return self.properties['port_id']
    @port_id.setter
    def port_id(self, x):
        parameter = 'port_id'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lldp_global_port_id(x, parameter)
        self.properties[parameter] = x

    @property
    def port_vlan(self):
        return self.properties['port_vlan']
    @port_vlan.setter
    def port_vlan(self, x):
        parameter = 'port_vlan'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def power_management(self):
        return self.properties['power_management']
    @power_management.setter
    def power_management(self, x):
        parameter = 'power_management'
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
    def reinit(self):
        return self.properties['reinit']
    @reinit.setter
    def reinit(self, x):
        parameter = 'reinit'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lldp_global_reinit(x, parameter)
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
    def system_capabilities(self):
        return self.properties['system_capabilities']
    @system_capabilities.setter
    def system_capabilities(self, x):
        parameter = 'system_capabilities'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def system_description(self):
        return self.properties['system_description']
    @system_description.setter
    def system_description(self, x):
        parameter = 'system_description'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def system_name(self):
        return self.properties['system_name']
    @system_name.setter
    def system_name(self, x):
        parameter = 'system_name'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lldp_global_state(x, parameter)
        self.properties[parameter] = x

    @property
    def timer(self):
        return self.properties['timer']
    @timer.setter
    def timer(self, x):
        parameter = 'timer'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_lldp_global_timer(x, parameter)
        self.properties[parameter] = x

