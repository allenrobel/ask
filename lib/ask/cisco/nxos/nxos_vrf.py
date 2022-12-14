# NxosVrf() - cisco/nxos/nxos_vrf.py
our_version = 106
from copy import deepcopy
import ipaddress
import re
from ask.common.task import Task
'''
*******************************************
NxosVrf()
*******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVrf() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vrf <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vrf_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vrf.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vrf.py>`_

Properties
----------

======================================  ==================================================
Properties / Methods                    Description
======================================  ==================================================
add_vrf()                               Append the currently-configured vrf to the vrf
                                        list, and clear all vrf-related properties so that
                                        another vrf can be configured.  See
                                        ``ScriptKit Example`` above for usage within
                                        a script::

                                            - Type: method
                                            - Example:
                                                task = NxosVrf(log_instance)
                                                task.name = 'vrf_1'
                                                task.description = 'ENG'
                                                task.interfaces = ['Ethernet1/1']
                                                task.rd = 'auto'
                                                task.add_vrf()
                                                task.name = 'vrf_2'
                                                task.description = 'SALES'
                                                task.interfaces = ['Ethernet1/2']
                                                task.rd = 'auto'
                                                task.add_vrf()
                                                etc...

admin_state                             Administrative state of the VRF::

                                            - Type: str()
                                            - Valid values:
                                                - down
                                                - up
                                            - Examples:
                                                task.admin_state = 'up'

aggregate                               list() of VRF definitions::

                                            This property is not accessed directly.
                                            Use ScriptKit's add_vrf() method to populate
                                            the aggregate list(). If ``add_vrf()`` is not
                                            called prior to ``update()``, then the task will
                                            contain a single vrf, and aggregate is not used.
                                            See ScriptKit Example above for example usage in
                                            a script.

associated_interfaces                   This is an intent option and checks the operational state
                                        of the interfaces for the given vrf name.  If the value
                                        in the associated_interfaces list() does not match the
                                        operational state of vrf interfaces on device the module
                                        will report a failure::

                                            - Type: list()
                                            - Valid values:
                                                - list() of interface names
                                                - keyword: default
                                            - Examples:
                                                task.associated_interfaces = 'default'

                                                interfaces = list()
                                                interfaces.append('Ethernet1/1')
                                                interfaces.append('port-channel44')
                                                task.associated_interfaces = interfaces

delay                                   Time in seconds to wait before checking for the operational
                                        state on the remote device::

                                            - Type: int()
                                            - Default: 10
                                            - Examples:
                                                task.delay = 20

description                             Description of the VRF::

                                            - Type: str()
                                            - Valid values:
                                                - freeform vrf description
                                                - keyword: default
                                            - Examples:
                                                task.description = 'no offsite access'
                                                task.description = 'default'

interfaces                              List of interfaces on which to configure VRF membership::

                                            - Type: list()
                                            - Valid values:
                                                - list() of interface names
                                                - keyword: default
                                            - Examples:
                                                task.interfaces = 'default'

                                                interfaces = list()
                                                interfaces.append('Ethernet1/1')
                                                interfaces.append('port-channel44')
                                                task.interfaces = interfaces

name                                    Name of the VRF to be managed::

                                            - Type: str()
                                            - Examples:
                                                - task.name = 'my_vrf'

purge                                   Purge VRFs not defined in the aggregate parameter::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Notes:
                                                1.  purge is recognized only when
                                                    NxosVrf().add_vrf() is used. For example,
                                                    the following purges all vrfs configured
                                                    on the remote device, except for vrf_1
                                                    and vrf_2::

                                                        task.name = 'vrf_1'
                                                        task.state = 'present'
                                                        task.add_vrf()
                                                        task.name = 'vrf_2'
                                                        task.state = 'present'
                                                        task.add_vrf()
                                                        task.purge = 'yes'
                                                        task.update()

rd                                      VPN Route Distinguisher (RD)::

                                            - Type: str()
                                            - Valid values:
                                                - ASN2:NN
                                                - ASN4:NN
                                                - IPV4:NN
                                                - keyword: auto
                                                - keyword: default
                                            - Examples:
                                                task.rd = 'auto'
                                                task.rd = 'default'
                                                task.rd = '65230:200'
                                                task.rd = '29123312:65000'
                                                task.rd = '10.1.1.1:65200'

state                                   Manages desired state of the resource::

                                            - Type: str()
                                            - Valid values:
                                                - absent
                                                - present
                                            - Examples:
                                                task.state = 'present'

task_name                               Freeform name for the task (ansible-playbook
                                        will print this when the task is run)::

                                            - Type: str()
                                            - Examples:
                                                task.task_name = 'configure vrf {}'.format(task.name)

vni                                     Virtual network identifier::

                                            - Type: int()
                                            - Valid values:
                                                - A VNI
                                                - keyword: default
                                            - Examples:
                                                task.vni = 10200
                                                task.vni = 'default'

======================================  ==================================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosVrf(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vrf'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.aggregate_list = list() # updated in add_vrf()

        self.nxos_vrf_valid_state = set()
        self.nxos_vrf_valid_state.add('present')
        self.nxos_vrf_valid_state.add('absent')

        self.properties_set = set()
        self.properties_set.add('associated_interfaces')
        self.properties_set.add('delay')
        self.properties_set.add('description')
        self.properties_set.add('interfaces')
        self.properties_set.add('name')
        self.properties_set.add('purge')
        self.properties_set.add('rd')
        self.properties_set.add('state')
        self.properties_set.add('vni')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        # used in update() to resolve any disambiguated property
        # names back into the names used by the Ansible module.
        # In this case, there are currently no property names
        # that needed disambiguation, so this is essentially
        # a noop to maintain consistency with other ScriptKit
        # classes.
        self.property_map = dict()
        self.property_map['associated_interfaces'] = 'associated_interfaces'
        self.property_map['delay'] = 'delay'
        self.property_map['description'] = 'description'
        self.property_map['interfaces'] = 'interfaces'
        self.property_map['name'] = 'name'
        self.property_map['purge'] = 'purge'
        self.property_map['rd'] = 'rd'
        self.property_map['state'] = 'state'
        self.property_map['vni'] = 'vni'

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.commit()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
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
        if len(self.aggregate_list) != 0:
            d['aggregate'] = deepcopy(self.aggregate_list)
            if self.purge != None:
                d['purge'] = self.purge
        else:
            for p in self.properties_set:
                if self.properties[p] != None:
                    mapped_p = self.property_map[p]
                    d[mapped_p] = self.properties[p]
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def add_vrf(self):
        d = dict()
        for p in self.properties_set:
            if p == 'purge': # purge not allowed in aggregate list
                continue
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.aggregate_list.append(deepcopy(d))

    def verify_nxos_vrf_delay(self, x, parameter='delay'):
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_delay'
        expectation = 'digits e.g. 10'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vrf_interfaces(self, x, parameter='interfaces'):
        if x == 'default':
            return
        interfaces_ok = True
        if type(x) == type(list()):
            for interface in x:
                if self.is_ethernet_interface(interface):
                    continue
                if self.is_ethernet_subinterface(interface):
                    continue
                if self.is_port_channel_interface(interface):
                    continue
                if self.is_vlan_interface(interface):
                    continue
                if self.is_management_interface(interface):
                    continue
                interfaces_ok = False
            if interfaces_ok == True:
                return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_interfaces'
        expectation = 'list of nxos interfaces or the keyword: default'
        self.fail(source_class, source_method, x, parameter, expectation)

    def is_asn_ipv4_nn(self,x):
        if ':' not in x:
            return False
        ipv4,nn = re.split(':', x)
        try:
            foo = ipaddress.IPv4Address(ipv4)
        except:
            return False
        try:
            nn = int(nn)
        except:
            return False
        if nn < 1:
            return False
        if nn > 65535:
            return False
        return True

    def is_asn4_nn(self,x):
        if ':' not in x:
            return False
        asn4,nn = re.split(':', x)
        try:
            asn4 = int(asn4)
        except:
            return False
        try:
            nn = int(nn)
        except:
            return False
        if asn4 < 1:
            return False
        if asn4 > 4294967295:
            return False
        if nn < 1:
            return False
        if nn > 65535:
            return False
        return True

    def is_asn2_nn(self,x):
        if ':' not in x:
            return False
        asn2,nn = re.split(':', x)
        try:
            asn2 = int(asn2)
        except:
            return False
        try:
            nn = int(nn)
        except:
            return False
        if asn2 < 1:
            return False
        if asn2 > 65535:
            return False
        if nn < 1:
            return False
        if nn > 65535:
            return False
        return True

    def verify_nxos_vrf_rd(self, x, parameter='rd'):
        if x == 'default':
            return
        if x == 'auto':
            return
        if self.is_asn_ipv4_nn(x):
            return
        if self.is_asn2_nn(x):
            return
        if self.is_asn4_nn(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_rd'
        expectation = 'ASN2:NN, ASN4:NN, IPV4:NN, or keyword: auto, default'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vrf_state(self, x, parameter='state'):
        verify_set = self.nxos_vrf_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vrf_vni(self, x, parameter='vni'):
        if x == 'default':
            return
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_vni'
        expectation = 'digits, or keyword: default'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def associated_interfaces(self):
        return self.properties['associated_interfaces']
    @associated_interfaces.setter
    def associated_interfaces(self, x):
        parameter = 'associated_interfaces'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_interfaces(x, parameter)
        self.properties[parameter] = x

    @property
    def delay(self):
        return self.properties['delay']
    @delay.setter
    def delay(self, x):
        parameter = 'delay'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_delay(x, parameter)
        self.properties[parameter] = x

    @property
    def interfaces(self):
        return self.properties['interfaces']
    @interfaces.setter
    def interfaces(self, x):
        parameter = 'interfaces'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_interfaces(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def purge(self):
        return self.properties['purge']
    @purge.setter
    def purge(self, x):
        parameter = 'purge'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def rd(self):
        return self.properties['rd']
    @rd.setter
    def rd(self, x):
        parameter = 'rd'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_rd(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_state(x, parameter)
        self.properties[parameter] = x

    @property
    def vni(self):
        return self.properties['vni']
    @vni.setter
    def vni(self, x):
        parameter = 'vni'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_vni(x, parameter)
        self.properties[parameter] = x
