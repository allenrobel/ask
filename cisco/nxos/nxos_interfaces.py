# NxosInterfaces() - cisco/nxos/nxos_interfaces.py
our_version = 124
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosInterfaces()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
123

ScriptKit Synopsis
------------------
- NxosInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_interfaces_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_interfaces.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_interfaces.py>`_


|

====================================    ==============================================
Method                                  Description
====================================    ==============================================
add_interface()                         Add an interface to the configuration::

                                            - Type: function()
                                            - Example:
                                                #!/usr/bin/env python3
                                                # Configure one ethernet and one SVI interface
                                                from ask.cisco.nxos.nxos_interfaces import NxosInterfaces
                                                from ask.common.log import Log
                                                from ask.common.playbook import Playbook
                                                log_level_console = 'INFO'
                                                log_level_file = 'DEBUG'
                                                log = Log('my_log', log_level_console, log_level_file)
                                                pb = Playbook(log)
                                                pb.profile_nxos()
                                                pb.ansible_password = 'mypassword'
                                                pb.name = 'Example nxos_interfaces'
                                                pb.add_host('dc-101')
                                                pb.file = '/tmp/nxos_interfaces.yaml'
                                                task = NxosInterfaces(log)
                                                task.name = 'Ethernet1/1'
                                                task.enabled = True
                                                task.mode = 'layer3'
                                                task.mtu = 9216
                                                task.add_interface()
                                                task.name = 'Vlan2'
                                                task.enabled = True
                                                task.add_interface()
                                                task.state = 'merged'
                                                task.commit()
                                                pb.add_task(task)
                                                pb.append_playbook()
                                                pb.write_playbook()

====================================    ==============================================

|

====================================    ==============================================
Property                                Description
====================================    ==============================================
description                             Interface description::

                                            - Type: str()
                                            - Example:
                                                task.description = 'Here be dragons'

duplex                                  Interface duplex. Applicable for Ethernet
                                        interfaces only.  If set, ``speed`` must
                                        also be set::

                                            - Type: str()
                                            - Valid values:
                                                - auto
                                                - full
                                                - half
                                            - Example:
                                                task.speed = 40000
                                                task.duplex = 'auto'

enabled                                 Administrative state of the interface. Set
                                        the value to ``True`` to administratively
                                        enable the interface or  ``False`` to disable
                                        it::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Example:
                                                task.enabled = True

fabric_forwarding_anycast_gateway       Associate SVI with anycast gateway under VLAN
                                        configuration mode. Applicable for SVI interfaces
                                        only::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Prerequisites:
                                                - feature fabric forwarding must be enabled
                                                    task = NxosFeature(log)
                                                    task.feature = 'fabric forwarding'
                                                    task.state = 'enabled'
                                                    task.commit()
                                                    pb.add_task(task)
                                                - fabric forwarding anycast-gateway-mac
                                                  must be configured
                                                    task = NxosConfig(log)
                                                    cfg = list()
                                                    cfg.append('fabric forwarding anycast-gateway-mac 0000.0000.1111')
                                                    task.lines = cfg
                                                    task.commit()
                                                    pb.add_task(task)
                                            - Example:
                                                task = NxosInterfaces(log)
                                                task.name = 'Vlan222'
                                                task.fabric_forwarding_anycast_gateway = True
                                                task.commit()
                                                pb.add_task(task)

ip_forward                              Disable ``False`` or enable ``True`` IP forward
                                        feature on the interface::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Example:
                                                task.ip_forward = False

mode                                    Layer2 or Layer3 state of the interface.
                                        Applicable for Ethernet and port channel
                                        interfaces only::

                                            - Type: str()
                                            - Valid values:
                                                - layer2
                                                - layer3
                                            - Example:
                                                task.mode = 'layer2'

mtu                                     Maximum transfer unit (MTU) for a specific
                                        interface::

                                            - Type: int()
                                            - Valid values:
                                                - range:  68-9216  SVI
                                                - range: 576-9216  port-channel
                                                - range: 576-9216  Ethernet
                                            - Example:
                                                task.mtu = 9216

name                                    Full name of interface::

                                            - Type: str()
                                            - Examples:
                                                task.name = 'Ethernet1/1'
                                                task.name = 'Ethernet1/1.23'
                                                task.name = 'Loopback4'
                                                task.name = 'mgmt0'
                                                task.name = 'port-channel22'
                                                task.name = 'Vlan3'

speed                                   Interface link speed. Applicable for Ethernet
                                        interfaces only::

                                            - Type: int()
                                            - Valid values: digits
                                            - Example:
                                                task.speed = 100000

state                                   Desired state after task has run::

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

task_name                               Name of the task. Ansible will display this
                                        when the playbook is run::

                                            - Type: str()
                                            - Example:
                                                - task.task_name = 'Create Vlan10'
                                        
====================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.interface_list = list()

        self.interface_properties = set()
        self.interface_properties.add('description')
        self.interface_properties.add('duplex')
        self.interface_properties.add('enabled')
        self.interface_properties.add('fabric_forwarding_anycast_gateway')
        self.interface_properties.add('ip_forward')
        self.interface_properties.add('mode')
        self.interface_properties.add('mtu')
        self.interface_properties.add('name')
        self.interface_properties.add('speed')

        self.properties_set = set()
        self.properties_set.update(self.interface_properties)
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_interfaces_valid_duplex = set()
        self.nxos_interfaces_valid_duplex.add('full')
        self.nxos_interfaces_valid_duplex.add('half')
        self.nxos_interfaces_valid_duplex.add('auto')

        self.nxos_interfaces_valid_mode = set()
        self.nxos_interfaces_valid_mode.add('layer2')
        self.nxos_interfaces_valid_mode.add('layer3')

        self.nxos_interfaces_valid_state = set()
        self.nxos_interfaces_valid_state.add('deleted')
        self.nxos_interfaces_valid_state.add('gathered')
        self.nxos_interfaces_valid_state.add('merged')
        self.nxos_interfaces_valid_state.add('overridden')
        self.nxos_interfaces_valid_state.add('parsed')
        self.nxos_interfaces_valid_state.add('rendered')
        self.nxos_interfaces_valid_state.add('replaced')

        self.nxos_interfaces_mtu_min = 576
        self.nxos_interfaces_mtu_max = 9216

        self.nxos_interfaces_svi_mtu_min = 68
        self.nxos_interfaces_svi_mtu_max = 9216

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None

    def final_verification_mtu(self):
        if self.mtu == None:
            return
        if 'Loopback' in self.name:
            self.task_log.warning('mtu not valid for {}. Changing mtu to None.'.format(self.name))
            self.mtu = None
            return
        if 'nve' in self.name:
            self.task_log.warning('mtu not valid for {}. Changing mtu to None.'.format(self.name))
            self.mtu = None
            return
        if self.is_vlan_interface(self.name):
            self.verify_nxos_interfaces_svi_mtu(self.mtu, 'mtu')
        else:
            self.verify_nxos_interfaces_mtu(self.mtu, 'mtu')

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
        populate ansible_task dict()
        '''
        self.final_verification()

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = self.state
        self.ansible_task[self.ansible_module]['config'] = deepcopy(self.interface_list)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_interface_properties(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.add_interface()')
            exit(1)
        if self.mode == 'layer2' and self.ip_forward == 'enable':
            self.task_log.error('exiting. mode is layer2 and ip_forward is enabled.  Either set mode to layer3 or set ip_forward to either None or no')
            exit(1)
        if self.duplex != None and self.speed == None:
            self.task_log.error('exiting. If duplex is set, speed must also be set.')
            exit(1)
        if self.fabric_forwarding_anycast_gateway != None and not self.is_vlan_interface(self.name):
            self.task_log.error('exiting. If fabric_forwarding_anycast_gateway is set, name must be an SVI.')
            exit(1)
        self.final_verification_mtu()
        if self.speed != None and not self.is_ethernet_interface(self.name):
            self.task_log.error('exiting. If instance.speed is set, instance.name must be an ethernet interface.')
            exit(1)

    def init_interface_properties(self):
        for p in self.interface_properties:
            self.properties[p] = None
    def add_interface(self):
        self.verify_interface_properties()
        d = dict()
        for p in self.interface_properties:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        if len(d) == 0:
            self.task_log.error('exiting. Set at least instance.name before calling task.add_interface().')
            exit(1)
        self.interface_list.append(deepcopy(d))
        self.init_interface_properties()

    def verify_nxos_interfaces_state(self, x, parameter='state'):
        verify_set = self.nxos_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interfaces_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interfaces_duplex(self, x, parameter='duplex'):
        verify_set = self.nxos_interfaces_valid_duplex
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interfaces_duplex'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interfaces_mode(self, x, parameter='mode'):
        verify_set = self.nxos_interfaces_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interfaces_mode'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interfaces_mtu(self, x, parameter='verify_nxos_interfaces_mtu'):
        range_min = self.nxos_interfaces_mtu_min
        range_max = self.nxos_interfaces_mtu_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_nxos_interfaces_svi_mtu(self, x, parameter='verify_nxos_interfaces_svi_mtu'):
        range_min = self.nxos_interfaces_svi_mtu_min
        range_max = self.nxos_interfaces_svi_mtu_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    @property
    def description(self):
        return self.properties['description']
    @description.setter
    def description(self, x):
        parameter = 'description'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def duplex(self):
        return self.properties['duplex']
    @duplex.setter
    def duplex(self, x):
        parameter = 'duplex'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interfaces_duplex(x, parameter)
        self.properties[parameter] = x

    @property
    def enabled(self):
        return self.properties['enabled']
    @enabled.setter
    def enabled(self, x):
        parameter = 'enabled'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def fabric_forwarding_anycast_gateway(self):
        return self.properties['fabric_forwarding_anycast_gateway']
    @fabric_forwarding_anycast_gateway.setter
    def fabric_forwarding_anycast_gateway(self, x):
        parameter = 'fabric_forwarding_anycast_gateway'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def ip_forward(self):
        return self.properties['ip_forward']
    @ip_forward.setter
    def ip_forward(self, x):
        parameter = 'ip_forward'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interfaces_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def mtu(self):
        return self.properties['mtu']
    @mtu.setter
    def mtu(self, x):
        parameter = 'mtu'
        if self.set_none(x, parameter):
            return
        # Additional mtu verification in final_verification()
        # once we know the type of interface
        self.verify_digits(x, parameter)
        self.properties[parameter] = str(x)

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
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interfaces_state(x, parameter)
        self.properties[parameter] = x

    @property
    def speed(self):
        return self.properties['speed']
    @speed.setter
    def speed(self, x):
        parameter = 'speed'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = str(x)
