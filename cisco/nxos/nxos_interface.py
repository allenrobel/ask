# NxosInterface() - cisco/nxos/nxos_interface.py
our_version = 116
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosInterface()
**************************************

.. contents::
   :local:
   :depth: 1

Deprecation
-----------

- Status: ``DEPRECATED``
- Alternative: `nxos_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_interfaces_module.rst>`_
- 2020-06-01, deprecation date
- 2022-06-01, removal date (module may be removed after this date)

ScriptKit Synopsis
------------------
- NxosInterface() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_interface
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_interface <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_interface_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_interface.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_interface.py>`_


|

====================================    ==============================================
Property                                Description
====================================    ==============================================
admin_state                             Administrative state of the interface::

                                            - Type: str()
                                            - Valid values:
                                                - down
                                                - up
                                            - Example:
                                                task.admin_state = 'down'

delay                                   Time in seconds to wait before checking for the
                                        operational state on remote device. This wait
                                        is applicable for operational state arguments::

                                            - Type: int()
                                            - Units: seconds
                                            - Default: 10
                                            - Example:
                                                task.delay = 20

description                             Interface description::

                                            - Type: str()
                                            - Example:
                                                task.description = 'Eth1/1 : peer 101.Eth2.1'

duplex                                  Interface duplex. Applicable for ethernet
                                        interface only::

                                            - Type: str()
                                            - Valid values:
                                                - auto
                                                - full
                                                - half
                                            - Example:
                                                task.duplex = 'full'

fabric_forwarding_anycast_gateway       Associate SVI with anycast gateway under
                                        VLAN configuration mode. Applicable for 
                                        SVI interface only::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Example:
                                                task.fabric_forwarding_anycast_gateway = True

interface_type                          Interface type to be unconfigured from the device::

                                            - Type: str()
                                            - Valid values:
                                                - loopback
                                                - nve
                                                - portchannel
                                                - svi
                                            - Example:
                                                task.interface_type = 'loopback'

ip_forward                              Enable/Disable ip forward feature on SVIs::

                                            - Type: str()
                                            - Valid values:
                                                - disable
                                                - enable
                                            - Example:
                                                task.ip_forward = 'disable'

mode                                    Manage Layer 2 or Layer 3 state of the interface. 
                                        Applicable for ethernet and portchannel interface
                                        only::

                                            - Type: str()
                                            - Valid values:
                                                - layer2
                                                - layer3
                                            - Example:
                                                task.mode = 'layer3'

mtu                                     Maximum transfer unit (MTU) for the interface.
                                        Applicable for ethernet interface only::

                                            - Type: int()
                                            - Valid values:
                                                - even int() range: 576-9216
                                            - Example:
                                                task.mtu = 9118

name                                    Full name of interface::

                                            - Type: str()
                                            - Examples:
                                                task.name = 'Ethernet1/1'
                                                task.name = 'port-channel22'

neighbor_host                           An LLDP neighbor that should be present if the
                                        interface is fully operational.  If this neighbor
                                        is not present, Ansible will declare the port down.
                                        Can be combined with neighbor_port::

                                            - Type: str()
                                            - Example:
                                                task.neighbor_host = 'foo_neighbor'
                                                task.add_neighbors()
                                            - See also: neighbor_port

neighbor_port                           An LLDP neighbor port name that should be present
                                        if the interface is fully operational.  If this
                                        port name is not present, Ansible will declare the
                                        port down.  Can be combined with neighbor_host::

                                            - Type: str()
                                            - Example:
                                                task.neighbor_port = 'Ethernet1/1'
                                                task.add_neighbors()
                                            - See also: neighbor_host

rx_rate                                 state_check only. Ansible will ensure ingress rate is
                                        at least ``rx_rate`` bps before declaring the interface
                                        up::

                                            - Type: int()
                                            - Units: bits per second (bps)
                                            - Example:
                                                task.rx_rate = 500000

speed                                   Interface link speed. Applicable for ethernet
                                        interface only.  Specifying speed will enable
                                        ``no negotiate auto`` (unless ``auto`` is used)::

                                            - Type: int() or str()
                                            - Valid values:
                                                  - 100     100Mb/s
                                                  - 1000    1Gb/s
                                                  - 10000   10Gb/s
                                                  - 100000  100Gb/s
                                                  - 200000  200Gb/s
                                                  - 25000   25Gb/s
                                                  - 40000   40Gb/s
                                                  - 400000  400Gb/s
                                                  - auto    Auto negotiate speed
                                            - Examples:
                                                task.speed = 40000
                                                task.speed = 'auto'
                                            - NOTES:
                                                - Different platforms will support different
                                                  values.  And certainly transceivers will
                                                  not support all values.  ScriptKit allows
                                                  any int() value, or 'auto' keyword.

state                                   Desired state after task has run::

                                            - Type: str()
                                            - Valid values:
                                                - absent
                                                - default
                                                - present
                                            - Example:
                                                task.state = 'present'
                                            - Required

task_name                               Name of the task. Ansible will display this
                                        when the playbook is run::

                                            - Type: str()
                                            - Example:
                                                - task.task_name = 'enable lacp'

tx_rate                                 state_check only. Ansible will ensure egress rate is
                                        at least ``tx_rate`` bps before declaring the interface
                                        up::

                                            - Type: int()
                                            - Units: bits per second (bps)
                                            - Example:
                                                task.tx_rate = 500000

====================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosInterface(Task):
    def __init__(self, log):
        ansible_module = 'nxos_interface'
        super().__init__(ansible_module, log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.task_log.warning('*******************************************************************************************')
        self.task_log.warning('NxosInterface() is DEPRECATED as its Ansible module nxos_interface is DEPRECATED.')
        self.task_log.warning('NxosInterface() will be removed after 2022-06-01')
        self.task_log.warning('Use NxosInterfaces() (cisco/nxos/nxos_interfaces.py) instead.')
        self.task_log.warning('*******************************************************************************************')

        self.nxos_interface_valid_admin_state = set()
        self.nxos_interface_valid_admin_state.add('up')
        self.nxos_interface_valid_admin_state.add('down')

        self.nxos_interface_valid_duplex = set()
        self.nxos_interface_valid_duplex.add('full')
        self.nxos_interface_valid_duplex.add('half')
        self.nxos_interface_valid_duplex.add('auto')

        self.nxos_interface_valid_interface_type = set() # interfaces which support CLI 'no interface X'
        self.nxos_interface_valid_interface_type.add('loopback')
        self.nxos_interface_valid_interface_type.add('portchannel')
        self.nxos_interface_valid_interface_type.add('svi')
        self.nxos_interface_valid_interface_type.add('nve')

        self.nxos_interface_valid_ip_forward = set()
        self.nxos_interface_valid_ip_forward.add('enable')
        self.nxos_interface_valid_ip_forward.add('disable')

        self.nxos_interface_valid_mode = set()
        self.nxos_interface_valid_mode.add('layer2')
        self.nxos_interface_valid_mode.add('layer3')

        self.nxos_interface_valid_state = set()
        self.nxos_interface_valid_state.add('present')
        self.nxos_interface_valid_state.add('absent')
        self.nxos_interface_valid_state.add('default')

        self.nxos_interface_min_delay = 1
        self.nxos_interface_max_delay = 16777215
        self.nxos_interface_min_mtu = 576
        self.nxos_interface_max_mtu = 9216

        self.properties_set = set()
        self.properties_set.add('admin_state')
        self.properties_set.add('aggregate')
        self.properties_set.add('delay')
        self.properties_set.add('description')
        self.properties_set.add('duplex')
        self.properties_set.add('fabric_forwarding_anycast_gateway')
        self.properties_set.add('interface_type')
        self.properties_set.add('ip_forward')
        self.properties_set.add('mode')
        self.properties_set.add('mtu')
        self.properties_set.add('name')
        self.properties_set.add('speed')
        self.properties_set.add('rx_rate')
        self.properties_set.add('tx_rate')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['neighbors']    = list()
        self.properties['task_name']    = None
        self.properties['neighbor_port'] = None
        self.properties['neighbor_host'] = None

    def final_verification(self):
        '''
        final_verification is called by subclass.update() method
        It performs a final verification across the properties that the user has or hasn't set
        '''
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.update()')
            exit(1)
        if self.mode == 'layer2' and self.ip_forward == 'enable':
            self.task_log.error('exiting. mode is layer2 and ip_forward is enable.  Either set mode to layer3 or set ip_forward to either None or disable')
            exit(1)
        if 'loopback' in self.name.lower() and self.mtu != None:
            self.task_log.info('mtu not valid for {}. Changing mtu to None.'.format(self.name))
            self.properties['mtu'] = None

    def commit(self):
        self.update()
    def update(self):
        '''
        '''
        self.final_verification()
        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.add_neighbors()
        if len(self.properties['neighbors']) > 0:
            d['neighbors'] = self.properties['neighbors']
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)
        self.init_properties()

    def add_neighbors(self):
        '''
        If user has set either self.neighbor_port or self.neighbor_host
        Append dict() d to self.properties['neighbors']
        '''
        if not self.is_lldp_interface(self.name):
            self.task_log.info('skipping lldp state check for interface {}: not LLDP capable'.format(self.name))
            return
        d = dict()
        if self.neighbor_port != None:
            d['port'] = self.neighbor_port
        if self.neighbor_host != None:
            d['host'] = self.neighbor_host
        if len(d) != 0:
            self.properties['neighbors'].append(deepcopy(d))
        self.neighbor_host = None
        self.neighbor_port = None

    def verify_nxos_interface_admin_state(self, x, parameter='admin_state'):
        verify_set = self.nxos_interface_valid_admin_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_admin_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interface_duplex(self, x, parameter='duplex'):
        verify_set = self.nxos_interface_valid_duplex
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_duplex'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interface_interface_type(self, x, parameter='interface_type'):
        for interface_type in self.nxos_interface_valid_interface_type:
            if interface_type in x.lower():
                return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_interface_type'
        expectation = ','.join(self.nxos_interface_valid_interface_type)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interface_ip_forward(self, x, parameter='ip_forward'):
        verify_set = self.nxos_interface_valid_ip_forward
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_ip_forward'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interface_mode(self, x, parameter='mode'):
        verify_set = self.nxos_interface_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_mode'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_interface_verify_mtu(self, x, parameter='mtu'):
        self.verify_integer_range(x, self.nxos_interface_min_mtu, self.nxos_interface_max_mtu, self.class_name, parameter)

    def verify_nxos_interface_speed(self, x, parameter='speed'):
        if x == 'auto':
            return
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_speed'
        expectation = 'digits, or keyword: auto'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_interface_state(self, x, parameter='state'):
        verify_set = self.nxos_interface_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_interface_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def admin_state(self):
        return self.properties['admin_state']
    @admin_state.setter
    def admin_state(self, x):
        parameter = 'admin_state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_admin_state(x, parameter)
        self.properties[parameter] = x

    @property
    def delay(self):
        return self.properties['delay']
    @delay.setter
    def delay(self, x):
        parameter = 'delay'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, self.nxos_interface_min_delay, self.nxos_interface_max_delay, self.class_name, parameter)
        self.properties[parameter] = x

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
        self.verify_nxos_interface_duplex(x, parameter)
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
    def interface_type(self):
        return self.properties['interface_type']
    @interface_type.setter
    def interface_type(self, x):
        parameter = 'interface_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_interface_type(x, parameter)
        self.properties[parameter] = x

    @property
    def ip_forward(self):
        return self.properties['ip_forward']
    @ip_forward.setter
    def ip_forward(self, x):
        parameter = 'ip_forward'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_ip_forward(x, parameter)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def mtu(self):
        return self.properties['mtu']
    @mtu.setter
    def mtu(self, x):
        parameter = 'mtu'
        if self.set_none(x, parameter):
            return
        self.nxos_interface_verify_mtu(x, parameter)
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
    def neighbor_host(self):
        return self.properties['neighbor_host']
    @neighbor_host.setter
    def neighbor_host(self, x):
        parameter = 'neighbor_host'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def neighbor_port(self):
        return self.properties['neighbor_port']
    @neighbor_port.setter
    def neighbor_port(self, x):
        parameter = 'neighbor_port'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def rx_rate(self):
        return self.properties['rx_rate']
    @rx_rate.setter
    def rx_rate(self, x):
        parameter = 'rx_rate'
        if self.set_none(x, parameter):
            return
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits. Got {}'.format(x))
            exit(1)
        self.properties[parameter] = x

    @property
    def speed(self):
        return self.properties['speed']
    @speed.setter
    def speed(self, x):
        parameter = 'speed'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_speed(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_interface_state(x, parameter)
        self.properties[parameter] = x

    @property
    def tx_rate(self):
        return self.properties['tx_rate']
    @tx_rate.setter
    def tx_rate(self, x):
        parameter = 'tx_rate'
        if self.set_none(x, parameter):
            return
        if not self.is_digits(x):
            self.task_log.error('exiting. Expected digits. Got {}'.format(x))
            exit(1)
        self.properties[parameter] = x
