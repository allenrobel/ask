# NxosSnmpHost() - cisco/nxos/nxos_snmp_host.py
our_version = 106
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosSnmpHost()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosSnmpHost() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_snmp_host
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_snmp_host <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_snmp_host_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_snmp_host.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_snmp_host.py>`_

|

============    ==============================================
Property        Description
============    ==============================================
community       Community string or v3 username::

                    - Type: str()
                    - Example:
                        task.community = 'public'

snmp_host       Address of SNMP receiver host::

                    - Type: str()
                    - Value values:
                        - IPv4 address without prefix
                        - IPv6 address without prefix
                        - domain name
                    - Examples:
                        task.snmp_host = '10.1.1.1'
                        task.snmp_host = '2000:aaaa::3a'
                        task.snmp_host = 'snmp.foo.com'
                    - Required

snmp_type       Type of message to send to snmp_host::

                    - Type: str()
                    - Valid values:
                        - inform
                        - trap
                    - Default: trap
                    - Example:
                        task.snmp_type = 'inform'

src_intf        Source interface. Must be fully qualified
                interface name::

                    - Type: str()
                    - Examples:
                        task.src_intf = 'mgmt0'
                        task.src_intf = 'Ethernet1/1'

state           Manage the state of the resource::

                    - Type: str()
                    - Value values:
                        - absent
                        - present
                    - Example:
                        task.state = 'present'
                    - NOTES:
                        - If state == present, the host is added to the
                          configuration
                        - If only vrf and/or vrf_filter and/or src_intf
                          are given, they will be added to the existing
                          host configuration
                        - If state == absent, the host is removed if
                          community parameter is given
                        - It is possible to remove only vrf and/or src_int
                          and/or vrf_filter by providing only those parameters
                          and no community parameter

udp             UDP port number::

                    - Type: int()
                    - Valid values:
                        - range: 0-65535
                    - Default: 162
                    - Example:
                        task.udp = 8162

v3              SNMPv3 Security level.  Valid when ``version`` is v3::

                    - Type: str()
                    - Valid values:
                        - auth
                        - noauth
                        - priv
                    - Example:
                        task.v3 = 'priv'

version         SNMP version. If this is not specified, v1 is used::

                    - Type: str()
                    - Valid values:
                        - v1
                        - v2c
                        - v3
                    - Example:
                        task.version = 'v3'

vrf             VRF in which SNMP traffic is originated::

                    - Type: str()
                    - Example:
                        task.vrf = 'management'

vrf_filter      Filters notifications to the notification host
                receiver based on the configured VRF::

                    - Type: str()
                    - Valid values:
                        - A VRF name
                    - Example:
                        task.vrf_filter = 'management'
                    - NOTES:
                        - If state == absent, the vrf is removed from the filter

task_name       Name of the task. Ansible will display this
                when the playbook is run::

                    - Type: str()
                    - Example:
                        - task.task_name = 'my task'

============    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosSnmpHost(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_snmp_host'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.nxos_snmp_host_valid_state = set()
        self.nxos_snmp_host_valid_state.add('present')
        self.nxos_snmp_host_valid_state.add('absent')

        self.nxos_snmp_host_valid_snmp_type = set()
        self.nxos_snmp_host_valid_snmp_type.add('inform')
        self.nxos_snmp_host_valid_snmp_type.add('trap')

        self.nxos_snmp_host_valid_v3 = set()
        self.nxos_snmp_host_valid_v3.add('auth')
        self.nxos_snmp_host_valid_v3.add('noauth')
        self.nxos_snmp_host_valid_v3.add('priv')

        self.nxos_snmp_host_valid_version = set()
        self.nxos_snmp_host_valid_version.add('v1')
        self.nxos_snmp_host_valid_version.add('v2c')
        self.nxos_snmp_host_valid_version.add('v3')

        self.properties_set = set()
        self.properties_set.add('community')
        self.properties_set.add('snmp_host')
        self.properties_set.add('snmp_type')
        self.properties_set.add('src_intf')
        self.properties_set.add('state')
        self.properties_set.add('udp')
        self.properties_set.add('v3')
        self.properties_set.add('version')
        self.properties_set.add('vrf')
        self.properties_set.add('vrf_filter')

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

    def final_verification(self):
        if self.community == None:
            self.task_log.error('exiting. Set instance.community before calling instance.update()')
            exit(1)
        if self.snmp_host == None:
            self.task_log.error('exiting. Set instance.snmp_host before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. Set instance.state before calling instance.update()')
            exit(1)
        if self.task_name == None:
            self.task_name = 'NxosSnmpHost {}'.format(self.snmp_host)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_snmp_host_state(self, x, parameter='state'):
        verify_set = self.nxos_snmp_host_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_host_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_snmp_host_snmp_type(self, x, parameter='snmp_type'):
        verify_set = self.nxos_snmp_host_valid_snmp_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_host_snmp_type'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_snmp_host_snmp_host(self, x, parameter='snmp_host'):
        if self.is_ipv4_unicast_address(x):
            return
        if self.is_ipv6_address(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_host_snmp_host'
        expectation = 'ipv4 or ipv6 address e.g. 10.1.1.1, 2001::1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_snmp_host_src_intf(self, x, parameter='src_intf'):
        if self.is_ethernet_interface(x):
            return
        if self.is_loopback_interface(x):
            return
        if self.is_management_interface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_host_src_intf'
        expectation = ','.join(sorted(self.nxos_snmp_host_valid_snmp_src_intf))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_snmp_host_udp(self, x, parameter='udp'):
        if x in range(0,65536):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_host_udp'
        expectation = 'int() in range 0-65535'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_snmp_host_v3(self, x, parameter='v3'):
        verify_set = self.nxos_snmp_host_valid_v3
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_host_v3'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_snmp_host_version(self, x, parameter='version'):
        verify_set = self.nxos_snmp_host_valid_version
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_snmp_host_version'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def community(self):
        return self.properties['community']
    @community.setter
    def community(self, x):
        parameter = 'community'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def snmp_host(self):
        return self.properties['snmp_host']
    @snmp_host.setter
    def snmp_host(self, x):
        parameter = 'snmp_host'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_snmp_host_snmp_host(x, parameter)
        self.properties[parameter] = x

    @property
    def snmp_type(self):
        return self.properties['snmp_type']
    @snmp_type.setter
    def snmp_type(self, x):
        parameter = 'snmp_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_snmp_host_snmp_type(x, parameter)
        self.properties[parameter] = x

    @property
    def src_intf(self):
        return self.properties['src_intf']
    @src_intf.setter
    def src_intf(self, x):
        parameter = 'src_intf'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_snmp_host_src_intf(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_snmp_host_state(x, parameter)
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
    def udp(self):
        return self.properties['udp']
    @udp.setter
    def udp(self, x):
        parameter = 'udp'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_snmp_host_udp(x, parameter)
        self.properties[parameter] = x

    @property
    def v3(self):
        return self.properties['v3']
    @v3.setter
    def v3(self, x):
        parameter = 'v3'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_snmp_host_v3(x, parameter)
        self.properties[parameter] = x

    @property
    def version(self):
        return self.properties['version']
    @version.setter
    def version(self, x):
        parameter = 'version'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_snmp_host_version(x, parameter)
        self.properties[parameter] = x

    @property
    def vrf(self):
        return self.properties['vrf']
    @vrf.setter
    def vrf(self, x):
        parameter = 'vrf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def vrf_filter(self):
        return self.properties['vrf_filter']
    @vrf_filter.setter
    def vrf_filter(self, x):
        parameter = 'vrf_filter'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
