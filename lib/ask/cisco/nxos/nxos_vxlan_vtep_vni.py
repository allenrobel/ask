# NxosVxlanVtepVni() - cisco/nxos/nxos_vxlan_vtep_vni.py
our_version = 108
from copy import deepcopy
from ask.common.task import Task
'''
*******************************************
NxosVxlanVtepVni() - nxos_vxlan_vtep_vni.py
*******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVxlanVtepVni() generates Ansible task instances conformant with cisco.nxos.nxos_vxlan_vtep_vni.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vxlan_vtep_vni <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vxlan_vtep_vni_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vxlan_vtep_vni.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vxlan_vtep_vni.py>`_

Properties
----------

================================    ==================================================
Property                            Description
================================    ==================================================
assoc_vrf                           Used to identify and separate processing VNIs that 
                                    are associated with a VRF and used for routing.
                                    The VRF and VNI specified with this command must
                                    match the configuration of the VNI under the VRF.::

                                        - Type: str()
                                        - Valid values: no, yes
                                        - Examples:
                                            - task.assoc_vrf = 'no'

ingress_replication                 Specifies mechanism for host reachability
                                    advertisement.::

                                        - Type: str()
                                        - Valid values: bgp, static, default
                                        - Examples:
                                            - task.ingress_replication = 'bgp'

interface                           Interface name for the VXLAN Network
                                    Virtualization Endpoint.::

                                        - Type: str()
                                        - Examples:
                                            - task.interface = 'nve1'
                                        - Required

multicast_group                     The multicast group (range) of the VNI.::

                                        - Type: str()
                                        - Valid values: A multicast group address,
                                          or the keyword 'default'
                                        - Examples:
                                            - task.multicast_group = '225.1.2.3'
                                            - task.multicast_group = 'default'

multisite_ingress_replication       Enables multisite ingress replication.::

                                        - Type: str()
                                        - Valid values: disable, enable, optimized
                                        - Examples:
                                            - task.multisite_ingress_replication = 'disable'
                                            - task.multisite_ingress_replication = 'optimized'

peer_list                           Set the ingress-replication static peer list.::

                                        - Type: list()
                                        - Valid values: A python list() of ipv4 addresses
                                        - Examples:
                                            - task.peer_list = ['1.1.2.1', '10.2.3.4']

state                               Determines whether the config should be present or 
                                    not on the device.::

                                        - Type: str()
                                        - Valid values: absent, present
                                        - Examples:
                                            - task.state = 'present'
                                        - Required

suppress_arp                        Suppress arp under layer 2 VNI.::

                                        - Type: str()
                                        - Valid values: no, yes
                                        - Examples:
                                            - task.suppress_arp = 'yes'

suppress_arp_disable                Overrides the global ARP suppression config. 
                                    Available on NX-OS 9K series running 9.2.x 
                                    or higher.::

                                        - Type: str()
                                        - Valid values: no, yes
                                        - Examples:
                                            - task.suppress_arp_disable = 'no'

task_name                           Freeform name for the task (ansible-playbook will
                                    print this when the task is run)::

                                        - Type: str()
                                        - Examples:
                                            - task.task_name = 'configure vni'

vni                                 Virtual Network Identifier.::

                                        - Type: int()
                                        - Valid values: int() range: 1-16777214
                                        - Examples:
                                            - task.vni = 10111
                                        - Required

================================    ==================================================

'''
class NxosVxlanVtepVni(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vxlan_vtep_vni'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.valid_nxos_vxlan_vtep_vni_state = set()
        self.valid_nxos_vxlan_vtep_vni_state.add('present')
        self.valid_nxos_vxlan_vtep_vni_state.add('absent')

        self.valid_nxos_vxlan_vtep_vni_ingress_replication = set()
        self.valid_nxos_vxlan_vtep_vni_ingress_replication.add('bgp')
        self.valid_nxos_vxlan_vtep_vni_ingress_replication.add('static')
        self.valid_nxos_vxlan_vtep_vni_ingress_replication.add('default')

        self.valid_nxos_vxlan_vtep_vni_multisite_ingress_replication = set()
        self.valid_nxos_vxlan_vtep_vni_multisite_ingress_replication.add('disable')
        self.valid_nxos_vxlan_vtep_vni_multisite_ingress_replication.add('enable')
        self.valid_nxos_vxlan_vtep_vni_multisite_ingress_replication.add('optimized')

        self.vni_min = 1
        self.vni_max = 16777214

        self.properties_set = set()
        self.properties_set.add('assoc_vrf')
        self.properties_set.add('ingress_replication')
        self.properties_set.add('interface')
        self.properties_set.add('multicast_group')
        self.properties_set.add('multisite_ingress_replication')
        self.properties_set.add('peer_list')
        self.properties_set.add('state')
        self.properties_set.add('suppress_arp')
        self.properties_set.add('suppress_arp_disable')
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
        self.property_map['assoc_vrf'] = 'assoc_vrf'
        self.property_map['ingress_replication'] = 'ingress_replication'
        self.property_map['interface'] = 'interface'
        self.property_map['multicast_group'] = 'multicast_group'
        self.property_map['multisite_ingress_replication'] = 'multisite_ingress_replication'
        self.property_map['peer_list'] = 'peer_list'
        self.property_map['state'] = 'state'
        self.property_map['suppress_arp'] = 'suppress_arp'
        self.property_map['suppress_arp_disable'] = 'suppress_arp_disable'
        self.property_map['vni'] = 'vni'
        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        '''
        '''
        if self.interface == None:
            self.task_log.error('exiting. call instance.interface before calling instance.commit()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if self.vni == None:
            self.task_log.error('exiting. call instance.vni before calling instance.commit()')
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
        for p in self.properties_set:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_ingress_replication(self, x, parameter='ingress_replication'):
        verify_set = self.valid_nxos_vxlan_vtep_vni_ingress_replication
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_ingress_replication'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_multisite_ingress_replication(self, x, parameter='multisite_ingress_replication'):
        verify_set = self.valid_nxos_vxlan_vtep_vni_multisite_ingress_replication
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_multisite_ingress_replication'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_peer_list(self, x, parameter='peer_list'):
        source_class = self.class_name
        source_method = 'verify_peer_list'
        expectation = 'python list of ipv4 addresses with format: A.B.C.D'
        if type(x) != type(list()):
            self.fail(source_class, source_method, x, parameter, expectation)
        for item in x:
            if not self.is_ipv4_unicast_address(item):
                self.fail(source_class, source_method, x, parameter, expectation)
        return

    def verify_nxos_vxlan_vtep_vni_interface(self, x, parameter='interface'):
        if self.is_nve_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vxlan_vtep_vni_interface'
        expectation = 'An NVE interface name, e.g. nve1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vxlan_vtep_vni_state(self, x, parameter='state'):
        verify_set = self.valid_nxos_vxlan_vtep_vni_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vxlan_vtep_vni_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def assoc_vrf(self):
        return self.properties['assoc_vrf']
    @assoc_vrf.setter
    def assoc_vrf(self, x):
        parameter = 'assoc_vrf'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def ingress_replication(self):
        return self.properties['ingress_replication']
    @ingress_replication.setter
    def ingress_replication(self, x):
        parameter = 'ingress_replication'
        if self.set_none(x, parameter):
            return
        self.verify_ingress_replication(x, parameter)
        self.properties[parameter] = x

    @property
    def interface(self):
        return self.properties['interface']
    @interface.setter
    def interface(self, x):
        parameter = 'interface'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vxlan_vtep_vni_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def multicast_group(self):
        return self.properties['multicast_group']
    @multicast_group.setter
    def multicast_group(self, x):
        parameter = 'multicast_group'
        if self.set_none(x, parameter):
            return
        self.verify_ipv4_multicast_address(x, parameter)
        self.properties[parameter] = x

    @property
    def multisite_ingress_replication(self):
        return self.properties['multisite_ingress_replication']
    @multisite_ingress_replication.setter
    def multisite_ingress_replication(self, x):
        parameter = 'multisite_ingress_replication'
        if self.set_none(x, parameter):
            return
        self.verify_multisite_ingress_replication(x, parameter)
        self.properties[parameter] = x

    @property
    def peer_list(self):
        return self.properties['peer_list']
    @peer_list.setter
    def peer_list(self, x):
        parameter = 'peer_list'
        if self.set_none(x, parameter):
            return
        self.verify_peer_list(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vxlan_vtep_vni_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_arp(self):
        return self.properties['suppress_arp']
    @suppress_arp.setter
    def suppress_arp(self, x):
        parameter = 'suppress_arp'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_arp_disable(self):
        return self.properties['suppress_arp_disable']
    @suppress_arp_disable.setter
    def suppress_arp_disable(self, x):
        parameter = 'suppress_arp_disable'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def vni(self):
        return self.properties['vni']
    @vni.setter
    def vni(self, x):
        parameter = 'vni'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(x, self.vni_min, self.vni_max, self.class_name, parameter)
        self.properties[parameter] = str(x)
