# NxosVxlanVtep() - python/lib3/nxos_vxlan_vtep.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
*******************************************
NxosVxlanVtep() - nxos_vxlan_vtep.py
*******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVxlanVtep() generates Ansible task instances conformant with cisco.nxos.nxos_vxlan_vtep.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vxlan_vtep <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vxlan_vtep_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vxlan_vtep.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vxlan_vtep.py>`_

Properties
----------

================================        ==================================================
Property                                Description
================================        ==================================================
description                             Description of the NVE interface::

                                            - Type: str()
                                            - Examples:
                                                - task.description = 'my nve'

global_ingress_replication_bgp          Configures ingress replication protocol as bgp for
                                        all VNIs.::

                                            - Type: str()
                                            - Valid values: no, yes
                                            - Examples:
                                                - task.global_ingress_replication_bgp = 'no'
                                            - Availability:
                                                - Platform: Nexus 9000
                                                - Software: NX-OS 9.2(x) or higher

global_mcast_group_L2                   Global multicast IP prefix for L2 VNIs or the
                                        keyword 'default'.::

                                            - Type: str()
                                            - Valid values: An ipv4 multicast ip address
                                            - Examples:
                                                - task.global_mcast_group_L2 = '225.1.2.3'
                                            - Availability:
                                                - Platform: Nexus 9000
                                                - Software: NX-OS 9.2(x) or higher

global_mcast_group_L2                   Global multicast IP prefix for L3 VNIs or the
                                        keyword 'default'.

                                            - Type: str()
                                            - Valid values: An ipv4 multicast ip address
                                            - Examples:
                                                - task.global_mcast_group_L2 = '225.1.2.3'
                                            - Availability:
                                                - Platform: Nexus 9000
                                                - Software: NX-OS 9.2(x) or higher

global_suppress_arp                     Enables ARP suppression for all VNIs.::

                                            - Type: str()
                                            - Valid values: no, yes
                                            - Examples:
                                                - task.global_suppress_arp = 'no'
                                            - Availability:
                                                - Platform: Nexus 9000
                                                - Software: NX-OS 9.2(x) or higher

host_reachability                       Specify mechanism for host reachability advertisement.::

                                            - 'yes' indicates that BGP will be used for host
                                              reachability advertisement.
                                            - 'no' indicates that no protocol is used for host
                                              reachability advertisement.
                                            - Other host reachability advertisement protocols 
                                              (e.g. OpenFlow, controller, etc.) are not
                                              supported.::

                                            - Type: str()
                                            - Valid values: no, yes
                                            - Examples:
                                                - task.host_reachability = 'yes'

interface                               Interface name for the VXLAN Network
                                        Virtualization Endpoint.::

                                            - Type: str()
                                            - Examples:
                                                - task.interface = 'nve1'
                                            - Required

multisite_border_gateway_interface      The loopback interface whose IP address should be
                                        used for the NVE Multisite Border-gateway Interface.::

                                            - Type: str()
                                            - Valid values:
                                                - A loopback interface name
                                                - The keyword 'default'
                                            - Examples:
                                                - task.multisite_border_gateway_interface = 'Loopback2'
                                                - task.multisite_border_gateway_interface = 'default'
                                            - Availability:
                                                - Platform: Subset of Nexus 9000
                                                - Software: NX-OS 7.0(3)I7(x) or higher

shutdown                                Administratively shutdown the NVE interface.::

                                            - Type: str()
                                            - Valid values: no, yes
                                            - Examples:
                                                - task.shutdown = 'yes'

source_interface                        The loopback interface whose IP address should be
                                        used for the NVE interface::

                                            - Type: str()
                                            - Valid values: A loopback interface name
                                            - Examples:
                                                - task.source_interface = 'loopback2'

source_interface_hold_down_time         Suppresses advertisement of the NVE loopback address
                                        until the overlay has converged.::

                                            - Type: int()
                                            - Valid values: int() range: 1-1500
                                            - Units: seconds
                                            - Examples:
                                                - task.source_interface_hold_down_time = 300

state                                   Determines whether the config should be present or 
                                        not on the device.::

                                            - Type: str()
                                            - Valid values: absent, present
                                            - Examples:
                                                - task.state = 'present'
                                            - Required

task_name                               Freeform name for the task (ansible-playbook will
                                        print this when the task is run)::

                                            - Type: str()
                                            - Examples:
                                                - task.task_name = 'configure vni'

================================    ==================================================

'''
class NxosVxlanVtep(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vxlan_vtep'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.source_interface_hold_down_time_min = 1
        self.source_interface_hold_down_time_max = 1500

        self.nxos_vxlan_vtep_valid_state = set()
        self.nxos_vxlan_vtep_valid_state.add('present')
        self.nxos_vxlan_vtep_valid_state.add('absent')

        self.properties_set = set()
        self.properties_set.add('description')
        self.properties_set.add('global_ingress_replication_bgp')
        self.properties_set.add('global_mcast_group_L2')
        self.properties_set.add('global_mcast_group_L3')
        self.properties_set.add('global_suppress_arp')
        self.properties_set.add('host_reachability')
        self.properties_set.add('interface')
        self.properties_set.add('multisite_border_gateway_interface')
        self.properties_set.add('shutdown')
        self.properties_set.add('source_interface')
        self.properties_set.add('source_interface_hold_down_time')
        self.properties_set.add('state')

        # used in update() to resolve any disambiguated property
        # names back into the names used by the Ansible module.
        # In this case, there are currently no property names
        # that needed disambiguation, so property_map is essentially
        # a noop so update() is consistant with other ScriptKit
        # classes.  Any future ambiguous properties would be added
        # here.
        self.property_map = dict()
        for p in self.properties_set:
            self.property_map[p] = p

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.interface == None:
            self.task_log.error('exiting. Set instance.interface before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. Set instance.state before calling instance.update()')
            exit(1)

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

    def verify_nxos_vxlan_vtep_interface(self, x, parameter='interface'):
        if self.is_nve_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vxlan_vtep_interface'
        expectation = 'An NVE interface name, e.g. nve1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vxlan_vtep_multisite_border_gateway_interface(self, x, parameter='multisite_border_gateway_interface'):
        if x == 'default':
            return
        if self.is_loopback_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vxlan_vtep_multisite_border_gateway_interface'
        expectation = 'A loopback interface e.g. loopback2'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vxlan_vtep_global_mcast_group_L2(self, x, parameter='global_mcast_group_L2'):
        if x == 'default':
            return
        self.verify_ipv4_multicast_address(x, parameter)

    def verify_nxos_vxlan_vtep_global_mcast_group_L3(self, x, parameter='global_mcast_group_L3'):
        if x == 'default':
            return
        self.verify_ipv4_multicast_address(x, parameter)

    def verify_nxos_vxlan_vtep_source_interface(self, x, parameter='source_interface'):
        if self.is_loopback_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vxlan_vtep_source_interface'
        expectation = 'A loopback interface e.g. loopback2'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vxlan_vtep_source_interface_hold_down_time(self, x, parameter='source_interface_hold_down_time'):
        source_class = self.class_name
        range_min = self.source_interface_hold_down_time_min
        range_max = self.source_interface_hold_down_time_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_vxlan_vtep_state(self, x, parameter='state'):
        verify_set = self.nxos_vxlan_vtep_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vxlan_vtep_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

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
    def global_ingress_replication_bgp(self):
        return self.properties['global_ingress_replication_bgp']
    @global_ingress_replication_bgp.setter
    def global_ingress_replication_bgp(self, x):
        parameter = 'global_ingress_replication_bgp'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def global_mcast_group_L2(self):
        return self.properties['global_mcast_group_L2']
    @global_mcast_group_L2.setter
    def global_mcast_group_L2(self, x):
        parameter = 'global_mcast_group_L2'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vxlan_vtep_global_mcast_group_L2(x, parameter)
        self.properties[parameter] = x

    @property
    def global_mcast_group_L3(self):
        return self.properties['global_mcast_group_L3']
    @global_mcast_group_L3.setter
    def global_mcast_group_L3(self, x):
        parameter = 'global_mcast_group_L3'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vxlan_vtep_global_mcast_group_L3(x, parameter)
        self.properties[parameter] = x

    @property
    def global_suppress_arp(self):
        return self.properties['global_suppress_arp']
    @global_suppress_arp.setter
    def global_suppress_arp(self, x):
        parameter = 'global_suppress_arp'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def host_reachability(self):
        return self.properties['host_reachability']
    @host_reachability.setter
    def host_reachability(self, x):
        parameter = 'host_reachability'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def interface(self):
        return self.properties['interface']
    @interface.setter
    def interface(self, x):
        parameter = 'interface'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vxlan_vtep_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def multisite_border_gateway_interface(self):
        return self.properties['multisite_border_gateway_interface']
    @multisite_border_gateway_interface.setter
    def multisite_border_gateway_interface(self, x):
        parameter = 'multisite_border_gateway_interface'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vxlan_vtep_multisite_border_gateway_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def shutdown(self):
        return self.properties['shutdown']
    @shutdown.setter
    def shutdown(self, x):
        parameter = 'shutdown'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def source_interface(self):
        return self.properties['source_interface']
    @source_interface.setter
    def source_interface(self, x):
        parameter = 'source_interface'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vxlan_vtep_source_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def source_interface_hold_down_time(self):
        return self.properties['source_interface_hold_down_time']
    @source_interface_hold_down_time.setter
    def source_interface_hold_down_time(self, x):
        parameter = 'source_interface_hold_down_time'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vxlan_vtep_source_interface_hold_down_time(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vxlan_vtep_state(x, parameter)
        self.properties[parameter] = x

