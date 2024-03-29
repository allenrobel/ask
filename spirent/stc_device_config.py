# StcDeviceConfig() - spirent/stc_device_config.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
*****************************************************************************
StcDeviceConfigIPv4() - spirent/stc_device_config.py
*****************************************************************************

*****************************************************************************
StcDeviceConfigIPv6() - spirent/stc_device_config.py
*****************************************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcDeviceConfigIPv4() and StcDeviceConfigIPv6() are subclasses of
tcDeviceConfig() and generate Ansible task instances conformant with
Spirent Ansible implementation for their LabServer + TestCenter
products.

These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run playbooks generated by StcDeviceConfigIPv4() and
        StcDeviceConfigIPv6()
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_device_config.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_device_config.py>`_

Properties
----------

====================================    ==================================================
Property                                Description
====================================    ==================================================
device_name                             Emulated device name under which to configure ipv6
                                        link local. This is used to populate the Spirent
                                        'under' parameter with a Spirent ref which points 
                                        to the emulated device.::

                                            - Type: str()
                                            - Spirent name: none
                                            - Examples:
                                                - task.device_name = '411_ipv4_device'
                                                - task.device_name = '611_ipv6_device'
                                            - Required

                                            The above populates the following required Spirent 
                                            parameter:

                                            objects: ref:/Emulateddevice[@Name='411_ipv4_device']
                                            objects: ref:/Emulateddevice[@Name="611_ipv6_device"]/Ipv6If[name!="611_ipv6_device_linklocal"]

address                                 Emulated device address. Depending on the specific subclass
                                        instantiated, this will be an IPv4 or IPv6 address::

                                            - Type: str()
                                            - Spirent name: Address
                                            - Examples:
                                                - task.address = '10.1.1.2'
                                                - task.address = '2001:a::2'

gateway                                 Emulated device gateway. Depending on the specific subclass
                                        instantiated, this will be an IPv4 or IPv6 address::

                                            - Type: str()
                                            - Spirent name: Gateway
                                            - Default: '::1'
                                            - Examples:
                                                - task.gateway = '10.1.1.1'
                                                - task.gateway = '2001:a::1'

prefixlen                               Emulated device address prefix length. Depending on the 
                                        specific subclass instantiated, this will be an IPv4 or IPv6
                                        prefix length::

                                            - Type: str()
                                            - Spirent name: Gateway
                                            - Default: '::1'
                                            - Examples:
                                                - task.prefixlen = 24
                                                - task.prefixlen = 120

====================================    ==================================================
'''

class StcDeviceConfig(Task):
    def __init__(self, task_log):
        ansible_module = 'stc'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.action = 'config'

        self.stc_command_properties_set = set()
        self.stc_command_properties_set.add('count')
        self.stc_command_properties_set.add('device')

        self.stc_device_properties_set = set()
        self.stc_device_properties_set.add('address')
        self.stc_device_properties_set.add('gateway')
        self.stc_device_properties_set.add('prefixlen')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.stc_command_properties_set)
        self.scriptkit_properties.update(self.stc_device_properties_set)

        # used in self.update() to map between this class's property names
        # and Spirent's property names. This dict() is keyed on the items in
        # self.stc_device_properties_set, and MUST contain all of these items.
        self.property_map = dict()
        self.property_map['address']    = 'Address'
        self.property_map['gateway']    = 'Gateway'
        self.property_map['prefixlen']  = 'PrefixLength'

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.stc_device_properties_set:
            self.properties[p] = None
        for p in self.stc_command_properties_set:
            self.properties[p] = None

    def final_verification(self):
        if self.device_name == None:
            self.task_log.error('exiting. call instance.device_name before calling instance.update()')
            exit(1)
        if self.address == None:
            self.task_log.error('exiting. call instance.address before calling instance.update()')
            exit(1)
        if self.gateway == None:
            self.task_log.error('exiting. call instance.gateway before calling instance.update()')
            exit(1)
        if self.prefixlen == None:
            self.task_log.error('exiting. call instance.prefixlen before calling instance.update()')
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
        d['action'] = self.action
        d['count'] = self.count
        d['objects'] = self.get_device_ref()
        d['properties'] = dict()
        stc_ip_version = 'Ipv{}If'.format(self.ip_version)
        d['properties'][stc_ip_version] = dict()
        for p in self.stc_device_properties_set:
            mapped_property = self.property_map[p]
            d['properties'][stc_ip_version][mapped_property] = self.properties[p]

        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def verify_stc_device_config_count(self, x, parameter='count'):
        if self.is_digits(x):
            return
        source_method = 'verify_stc_device_config_count'
        expectation = 'int()'
        self.fail(self.class_name, source_method, x, parameter, expectation)

    @property
    def count(self):
        return self.properties['count']
    @count.setter
    def count(self, x):
        parameter = 'count'
        if self.set_none(x, parameter):
            return
        self.verify_stc_device_config_count(x, parameter)
        self.properties[parameter] = x

    @property
    def device_name(self):
        return self.properties['device']
    @device_name.setter
    def device_name(self, x):
        '''
        device_name is used to complete the value for the objects key
        required by Spirent Ansible.  See Resulting playbook section of 
        the docstring above.

        For ipv4:

        instance.device_name = '711_ipv4'

        Results in:

        d['objects'] = "ref:/EmulatedDevice[@Name='711_ipv4]"

        For ipv6:

        instance.device_name = '611_ipv6'

        Results in:

        d['objects'] = "ref:/EmulatedDevice[@Name='611_ipv6]/Ipv6If[address!="fe80::*"]"
        '''
        parameter = 'device'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def address(self):
        return self.properties['address']
    @address.setter
    def address(self, x):
        parameter = 'address'
        if self.set_none(x, parameter):
            return
        self.verify_stc_device_config_address(x, parameter)
        self.properties[parameter] = x

    @property
    def gateway(self):
        return self.properties['gateway']
    @gateway.setter
    def gateway(self, x):
        parameter = 'gateway'
        if self.set_none(x, parameter):
            return
        self.verify_stc_device_config_gateway(x, parameter)
        self.properties[parameter] = x

    @property
    def prefixlen(self):
        return self.properties['prefixlen']
    @prefixlen.setter
    def prefixlen(self, x):
        parameter = 'prefixlen'
        if self.set_none(x, parameter):
            return
        self.verify_stc_device_config_prefixlen(x, parameter)
        self.properties[parameter] = x

class StcDeviceConfigIpv4(StcDeviceConfig):
    def __init__(self, log):
        super().__init__(log)
        self.ip_version = 4

    def get_device_ref(self):
        if self.device_name == None:
            self.task_log.error('exiting. call instance.device_name before calling instance.update()')
            exit(1)
        return "ref:/Emulateddevice[@Name='" + self.device_name + "']"

    def verify_stc_device_config_address(self, x, parameter='address'):
        if self.is_ipv4_unicast_address(x):
            return
        source_method = 'verify_stc_device_config_ipv4_address'
        expectation = 'ipv4 unicast address e.g. 10.1.1.1'
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_device_config_gateway(self, x, parameter='gateway'):
        if self.is_ipv4_unicast_address(x):
            return
        source_method = 'verify_stc_device_config_gateway'
        expectation = 'ipv4 unicast address e.g. 10.1.1.1'
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_device_config_prefixlen(self, x, parameter='prefixlen'):
        self.verify_integer_range(x, 8, 32, self.class_name, parameter)


class StcDeviceConfigIpv6(StcDeviceConfig):
    def __init__(self, log):
        super().__init__(log)
        self.ip_version = 6

    def get_device_ref(self):
        if self.device_name == None:
            self.task_log.error('exiting. call instance.device_name before calling instance.update()')
            exit(1)
        return 'ref:/Emulateddevice[@Name="{}"]/Ipv6If[name!="{}_linklocal"]'.format(self.device_name, self.device_name)

    def verify_stc_device_config_address(self, x, parameter='address'):
        if not self.is_ipv6_address(x):
            source_method = 'verify_stc_device_config_address'
            expectation = 'ipv6 unicast address e.g. 2001:a::1'
            self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_device_config_gateway(self, x, parameter='gateway'):
        if self.is_ipv6_address(x):
            return
        source_method = 'verify_stc_device_config_gateway'
        expectation = 'ipv6 unicast address e.g. 2001:a::1'
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_device_config_prefixlen(self, x, parameter='prefixlen'):
        self.verify_integer_range(x, 8, 128, self.class_name, parameter)

