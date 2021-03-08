# NxosStaticRoutes() - cisco/nxos/nxos_static_routes.py
our_version = 103
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosStaticRoutes()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosStaticRoutes() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_static_routes
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_static_routes <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_static_routes_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_static_routes.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_static_routes.py>`_

|

========================    ==============================================
Property                    Description
========================    ==============================================
afi                         Specifies the top level address family 
                            indicator::

                                - Type: str()
                                - Valid values: ipv4, ipv6
                                - Example
                                    task.afi = 'ipv4'
                                - Required

dest                        Destination prefix of static route::

                                - Type: str()
                                - Valid values:
                                    - IPv4 address with prefixlen
                                        - prefixlen range: 0-32
                                    - IPv6 address with prefixlen
                                        - prefixlen range: 0-128
                                Examples:
                                    task.dest = '10.1.0.0/16'
                                    task.dest = '2001:aaaa:bbbb::/48'
                                - Required

admin_distance              Preference or administrative distance of
                            route::

                                - Type: int()
                                - Valid values: range 1-255
                                - Example:
                                    task.admin_distance = 100

dest_vrf                    VRF of the destination::

                                - Type: str()
                                - Example:
                                    task.dest_vrf = "ENG"

forward_router_address      IP address of the next hop router::

                                - Type: str()
                                - Valid values:
                                    - ip address in same address-family as dest/afi
                                - Examples:
                                    task.forward_router_address = '10.2.1.1'
                                    task.forward_router_address = '2001:aaaa::3'

interface                   Outgoing interface of next-hop::

                                - Type: str()
                                - Valid values:
                                    - Full interface name
                                    - Null0
                                - Examples:
                                    task.interface = 'Null0'
                                    task.interface = 'Ethernet1/1'

route_name                  Name of the static route::

                                - Type: str()
                                - Example:
                                    task.route_name = 'POD_2'

tag                         Route tag value::

                                - Type: int()
                                - Example:
                                    task.tag = 5000

track                       Track value::

                                - Type: int()
                                - Valid values: range 1-512
                                - Example:
                                    task.track = 100
                                - NOTES:
                                    - Track must already be configured on
                                      the device before adding the route.

vrf                         The VRF to which the static route(s) belong::

                                - Type: str()
                                - Example:
                                    task.vrf = 'ENG'

state                       Desired state after task has completed::

                                - Type: str()
                                - Valid values:
                                    - deleted
                                    - gathered
                                    - merged
                                    - overridden
                                    - parsed  (not currently supported by ScriptKit)
                                    - rendered
                                    - replaced

task_name                   Name of the task. Ansible will display this
                            when the playbook is run::

                                - Type: str()
                                - Example:
                                    - task.task_name = 'my task'

========================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
'''

class NxosStaticRoutes(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_static_routes'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()

        self.ipv4_routes = dict()
        self.ipv6_routes = dict()

        self.nxos_static_routes_valid_afi = set()
        self.nxos_static_routes_valid_afi.add('ipv4')
        self.nxos_static_routes_valid_afi.add('ipv6')

        self.nxos_static_routes_valid_state = set()
        self.nxos_static_routes_valid_state.add('deleted')
        self.nxos_static_routes_valid_state.add('gathered')
        self.nxos_static_routes_valid_state.add('merged')
        self.nxos_static_routes_valid_state.add('overridden')
        self.nxos_static_routes_valid_state.add('replaced')
        self.nxos_static_routes_valid_state.add('rendered')
        self.nxos_static_routes_valid_state.add('parsed')

        self.address_family_set = set()
        self.address_family_set.add('afi')

        self.route_set = set()
        self.route_set.add('dest')

        self.next_hop_set = set()
        self.next_hop_set.add('admin_distance')
        self.next_hop_set.add('dest_vrf')
        self.next_hop_set.add('forward_router_address')
        self.next_hop_set.add('interface')
        self.next_hop_set.add('route_name')
        self.next_hop_set.add('tag')
        self.next_hop_set.add('track')

        self.nxos_static_routes_admin_distance_min = 1
        self.nxos_static_routes_admin_distance_max = 255

        self.nxos_static_routes_track_min = 1
        self.nxos_static_routes_track_max = 512

        # properties_set is not currently used in this class,
        # but it can be used by scripts to set task_name.
        # See Task().append_to_task_name() method in common/task.py
        self.properties_set = set()
        self.properties_set.add('afi')
        self.properties_set.add('dest')
        self.properties_set.add('admin_distance')
        self.properties_set.add('dest_vrf')
        self.properties_set.add('forward_router_address')
        self.properties_set.add('interface')
        self.properties_set.add('route_name')
        self.properties_set.add('tag')
        self.properties_set.add('track')
        self.properties_set.add('vrf')
        self.properties_set.add('state')

        self.init_properties()

    def init_properties_address_family(self):
        for p in self.address_family_set:
            self.properties[p] = None

    def init_properties_route(self):
        for p in self.route_set:
            self.properties[p] = None

    def init_properties_next_hop(self):
        for p in self.next_hop_set:
            self.properties[p] = None

    def init_properties(self):
        self.properties = dict()
        self.properties['vrf'] = None
        self.properties['state'] = None
        self.init_properties_address_family()
        self.init_properties_route()
        self.init_properties_next_hop()

    def verify_next_hop(self):
        if self.afi == None:
            self.task_log.error('exiting. instance.afi must be set prior to calling instance.add_next_hop()')
            exit(1)
        if self.dest == None:
            self.task_log.error('exiting. instance.dest must be set prior to calling instance.add_next_hop()')
            exit(1)
        # TODO: Per RFC5549 ipv4 AFI can use ipv6 destination for next-hop and vice-versa
        # As of 9.3(6), NXOS does not support static routes with other AFI as next-hop
        # But, if it ever does, these checks will need to be removed. 
        if self.afi == 'ipv4' and not self.is_ipv4_address_with_prefix(self.dest):
            self.task_log.error('exiting. instance.afi {} does not match dest {}'.format(self.afi, self.dest))
            exit(1)
        if self.afi == 'ipv6' and not self.is_ipv6_interface(self.dest):
            self.task_log.error('exiting. instance.afi {} does not match dest {}'.format(self.afi, self.dest))
            exit(1)

    def add_next_hop_ipv4(self, nh):
        if self.dest not in self.ipv4_routes:
            self.ipv4_routes[self.dest] = dict()
        if len(nh) != None:
            try:
                self.ipv4_routes[self.dest]['next_hops'].append(deepcopy(nh))
            except:
                self.ipv4_routes[self.dest]['next_hops'] = list()
                self.ipv4_routes[self.dest]['next_hops'].append(deepcopy(nh))
    def add_next_hop_ipv6(self, nh):
        if self.dest not in self.ipv6_routes:
            self.ipv6_routes[self.dest] = dict()
        if len(nh) != None:
            try:
                self.ipv6_routes[self.dest]['next_hops'].append(deepcopy(nh))
            except:
                self.ipv6_routes[self.dest]['next_hops'] = list()
                self.ipv6_routes[self.dest]['next_hops'].append(deepcopy(nh))

    def add_next_hop(self):
        self.verify_next_hop()
        nh = dict()
        for p in self.next_hop_set:
            if self.properties[p] != None:
                nh[p] = self.properties[p]
        if self.afi == 'ipv4':
            self.add_next_hop_ipv4(nh)
        if self.afi == 'ipv6':
            self.add_next_hop_ipv6(nh)
        self.init_properties_next_hop()

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        d = dict()
        d['address_families'] = list()
        if len(self.ipv4_routes) != 0:
            d4 = dict()
            d4['afi'] = 'ipv4'
            d4['routes'] = list()
            for dest in self.ipv4_routes:
                route = dict()
                route['dest'] = dest
                if 'next_hops' in self.ipv4_routes[dest]:
                     route['next_hops'] = list()
                     for next_hop in self.ipv4_routes[dest]['next_hops']:
                        route['next_hops'].append(next_hop)
                d4['routes'].append(deepcopy(route))
            d['address_families'].append(deepcopy(d4))

        if len(self.ipv6_routes) != 0:
            d6 = dict()
            d6['afi'] = 'ipv6'
            d6['routes'] = list()
            for dest in self.ipv6_routes:
                route = dict()
                route['dest'] = dest
                if 'next_hops' in self.ipv6_routes[dest]:
                     route['next_hops'] = list()
                     for next_hop in self.ipv6_routes[dest]['next_hops']:
                        route['next_hops'].append(next_hop)
                d6['routes'].append(deepcopy(route))
            d['address_families'].append(deepcopy(d6))
        
        if self.vrf != None:
            d['vrf'] = self.vrf
        if len(d['address_families']) != 0:
            self.ansible_task[self.ansible_module]['config'].append(deepcopy(d))

        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_static_routes_admin_distance(self, x):
        source_class = self.class_name
        source_method = 'verify_nxos_static_routes_admin_distance'
        self.verify_integer_range(x, self.nxos_static_routes_admin_distance_min, self.nxos_static_routes_admin_distance_max, source_class, source_method)

    def verify_nxos_static_routes_afi(self, x, parameter='receive'):
        verify_set = self.nxos_static_routes_valid_afi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_static_routes_afi'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_static_routes_dest(self, x, parameter='dest'):
        if self.is_ipv4_address_with_prefix(x):
            return
        if self.is_ipv6_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_static_routes_dest'
        expectation = 'ipv4 or ipv6 address with prefix e.g. 1.1.0.0/16, 2001:10:a:b::/64'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_static_routes_forward_router_address(self, x, parameter='forward_router_address'):
        if self.is_ipv4_address(x):
            return
        if self.is_ipv6_address(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_static_routes_forward_router_address'
        expectation = 'ipv4 or ipv6 address without prefix e.g. 1.1.1.3, 2001:10:a:b::3'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_static_routes_interface(self, x, parameter='interface'):
        if x == 'Null0':
            return
        if self.is_ethernet_interface(x):
            return
        if self.is_ethernet_subinterface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_pim_interface_interface'
        expectation = ','.join(self.valid_ip_pim_interface)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_static_routes_state(self, x, parameter='state'):
        verify_set = self.nxos_static_routes_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_static_routes_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_static_routes_tag(self, x, parameter='tag'):
        if self.is_digits(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_static_routes_tag'
        expectation = 'int()'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_static_routes_track(self, x):
        source_class = self.class_name
        source_method = 'verify_nxos_static_routes_track'
        self.verify_integer_range(x, self.nxos_static_routes_track_min, self.nxos_static_routes_track_max, source_class, source_method)

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_static_routes_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def dest(self):
        return self.properties['dest']
    @dest.setter
    def dest(self, x):
        parameter = 'dest'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_static_routes_dest(x, parameter)
        self.properties[parameter] = x

    @property
    def admin_distance(self):
        return self.properties['admin_distance']
    @admin_distance.setter
    def admin_distance(self, x):
        parameter = 'admin_distance'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_static_routes_admin_distance(x)
        self.properties[parameter] = x

    @property
    def dest_vrf(self):
        return self.properties['dest_vrf']
    @dest_vrf.setter
    def dest_vrf(self, x):
        parameter = 'dest_vrf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def forward_router_address(self):
        return self.properties['forward_router_address']
    @forward_router_address.setter
    def forward_router_address(self, x):
        parameter = 'forward_router_address'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_static_routes_forward_router_address(x, parameter)
        self.properties[parameter] = x

    @property
    def interface(self):
        return self.properties['interface']
    @interface.setter
    def interface(self, x):
        parameter = 'interface'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_static_routes_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def route_name(self):
        return self.properties['route_name']
    @route_name.setter
    def route_name(self, x):
        parameter = 'route_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def tag(self):
        return self.properties['tag']
    @tag.setter
    def tag(self, x):
        parameter = 'tag'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_static_routes_tag(x, parameter)
        self.properties[parameter] = x

    @property
    def track(self):
        return self.properties['track']
    @track.setter
    def track(self, x):
        parameter = 'track'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_static_routes_track(x, parameter)
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
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_static_routes_state(x, parameter)
        self.properties[parameter] = x
