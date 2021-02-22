# NxosBgpAf() - cisco/nxos/nxos_bgp_af.py
our_version = 112

from copy import deepcopy
import re
from ask.common.task import Task
'''
**************************************
NxosBgpAf()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosBgpAf() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp_af
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp_af <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_af_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp_af.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp_af.py>`_


|

=============================   ==============================================
Property                        Description
=============================   ==============================================
additional_paths_install        Install a backup path into the forwarding table::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_install = False

additional_paths_receive        Advertise the capability to receive additional
                                paths from the neighbors under this
                                address family (afi) for which the capability
                                has not been disabled::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_receive = True

additional_paths_selection      Determines which prefix(es) are eligible for installation
                                of additional paths::

                                    - Type: str()
                                    - Valid values: route-map name
                                    - Example:
                                        task.additional_paths_selection = 'ADD_PATH_SEL'

additional_paths_send           Advertise the capability to send additional
                                paths to all of the neighbors under this
                                address family (afi) for which the capability
                                has not been disabled::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_send = False

advertise_l2vpn_evpn            Advertise L2 EVPN routes::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.advertise_l2vpn_evpn = False

afi                             Address Family Identifier::

                                    - Type: str()
                                    - Valid values:
                                        - ipv4
                                        - ipv6
                                        - vpnv4
                                        - vpnv6
                                        - l2vpn
                                    - Example:
                                        task.afi = 'ipv4'
                                    - Required

asn                             BGP autonomous system number, in ASPLAIN or ASDOT notation::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-4294967295
                                        - <1-65535>.<0-65535>
                                    - Examples:
                                        task.asn = 64512
                                        task.asn = 4200000000
                                        task.asn = '2301.0'
                                    - NOTES:
                                        - private asn ranges
                                            - 64512 to 65534
                                            - 4200000000 to 4294967294
                                    - Required

client_to_client                Configure client-to-client route reflection::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.client_to_client = False

dampen_igp_metric               Duration, in seconds, to dampen IGP
                                metric-related changes::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 20-3600
                                        - keyword: 'default'
                                    - Default: 600
                                    - Units: seconds
                                    - Example:
                                        task.dampen_igp_metric = 1200

dampening_half_time             Decay half life::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-45
                                        - keyword: 'default'
                                    - Units: minutes
                                    - Examples:
                                        task.dampening_half_time = 2

dampening_max_suppress_time     Maximum suppress time for stable route::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-255
                                        - keyword: 'default'
                                    - Units: minutes
                                    - NOTES:
                                        - higher values require higher dampening_half_time values
                                    - Examples:
                                        task.dampening_max_suppress_time = 10

dampening_reuse_time            Value to start reusing a route::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-20000
                                        - keyword: 'default'
                                    - Units: int()
                                    - Examples:
                                        task.dampening_reuse_time = 20
                                    - NOTES:
                                        - dampening_reuse_time must be less than dampening_suppress_time

dampening_routemap              Specify which prefix(es) are subject to route-flap dampening::

                                    - Type: str()
                                    - Example:
                                        task.dampening_routemap = 'DAMPEN_THESE'

dampening_state                 Enable/disable route-flap dampening::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.dampening_state = True

dampening_suppress_time         Value to start suppressing a route::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Units: int()
                                    - NOTES:
                                        - dampening_suppress_time must be greater than dampening_reuse_time
                                    - Examples:
                                        task.dampening_suppress_time = 40
                                        task.dampening_suppress_time = 'default'

default_information_originate   Generate and inject the default route into the
                                BGP RIB, regardless of whether it is present in
                                the routing table::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.default_information_originate = True

default_metric                  Sets default metrics for routes redistributed into BGP::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Examples:
                                        task.default_metric = 400
                                        task.default_metric = 'default'

distance_ebgp                   Sets the administrative distance for eBGP routes::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Examples:
                                        task.distance_ebgp = 300
                                        task.distance_ebgp = 'default'

distance_ibgp                   Sets the administrative distance for iBGP routes::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Examples:
                                        task.distance_ibgp = 200
                                        task.distance_ibgp = 'default'

distance_local                  Sets the administrative distance for local BGP routes::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int()
                                        - keyword: 'default'
                                    - Examples:
                                        task.distance_local = 100
                                        task.distance_local = 'default'

inject_map                      An array of route-map names which will specify
                                prefixes to inject. Each array entry must first
                                specify the ``inject-map`` name, secondly an ``exist-map``
                                name, and optionally the ``copy-attributes`` keyword,
                                which indicates that attributes should be copied from
                                the aggregate::

                                    - Type: list() of list()
                                    - Example:
                                        inject_map_list = list()
                                        inject_map_list.append(['INJECT_1', 'EXIST_1', 'copy-attributes'])
                                        inject_map_list.append(['INJECT_2', 'EXIST_2'])
                                        task.inject_map = inject_map_list.copy()

maximum_paths                   Maximum number of equal-cost paths for load sharing::

                                    - Type: int()
                                    - Valid values: int() range: 1-64
                                    - Example:
                                        task.maximum_paths = 16

maximum_paths_ibgp              Maximum number of ibgp equal-cost paths for load sharing::

                                    - Type: int()
                                    - Valid values: int() range: 1-64
                                    - Example:
                                        task.maximum_paths_ibgp = 16

networks                        Networks to configure.  Specified as a list() of list().
                                Each list contains network/prefix and, optionally, a 
                                route-map name::

                                    - Type: list() of list()
                                    - Example:
                                        network_list = list()
                                        network_list.append(['10.0.0.0/16', 'routemap_LA'])
                                        network_list.append(['192.168.2.0/24'])
                                        task.networks = network_list.copy()

next_hop_route_map              A route-map which specifies/selects valid nexthops::

                                    - Type: str()
                                    - Examples:
                                        - task.next_hop_route_map = 'NEXT_HOP_RM'

redistribute                    A list of redistribute directives.
                                Multiple redistribute entries are allowed.
                                The list must be in the form of a nested array.
                                The first element of each array specifies the 
                                source-protocol from which to redistribute.
                                The second element specifies a route-map name.
                                A route-map is advised but may be optional
                                on some platforms, in which case it may be
                                omitted from the list::

                                    - Type: list() of list()
                                    - Example:
                                        redistribute_list = list()
                                        redistribute_list.append(['direct'])
                                        redistribute_list.append(['ospf', 'ROUTE_MAP_OSPF'])
                                        task.redistribute = redistribute_list.copy()

retain_route_target             Retains all of the routes or the routes which are
                                part of configured route-map::

                                    - Valid values:
                                        - route-map name
                                            - selectively retain routes
                                            - route-map name cannot be 'all' or 'default'
                                        - keyword: all
                                            -  retain all routes regardless of
                                               Target-VPN community
                                        - keyword: default
                                            - disable the retain route target option
                                        - Examples:
                                            task.retain_route_target = 'RRT_RMAP'
                                            task.retain_route_target = 'all'
                                            task.retain_route_target = 'default'

safi                            Sub Address Family Identifier::

                                    - Type: str()
                                    - Valid values: unicast, multicast, evpn
                                    - Examples:
                                        - task.safi = 'unicast'
                                    - Required

state                           Determines whether the config should be present or
                                not on the remote device::

                                    - Type: str()
                                    - Valid values: absent, present
                                    - Examples:
                                        - task.state = 'present'
                                    - Required

suppress_inactive               Advertise only active routes to peers::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.suppress_inactive = True

table_map                       Apply table-map to filter routes downloaded into URIB::

                                    - Type: str()
                                    - Examples:
                                        - task.table_map = 'PRIO_1'

table_map_filter                Filters routes rejected by the route-map and
                                does not download them to the RIB::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.table_map_filter = True

vrf                             VRF name::

                                    - Type: str()
                                    - Default: 'default'
                                    - Examples:
                                        - task.vrf = 'default'
                                        - task.vrf = 'PROD'

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Examples:
                                        - task.task_name = 'my task'

=============================   ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosBgpAf(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp_af'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.nxos_bgp_af_valid_additional_paths_receive = set()
        self.nxos_bgp_af_valid_additional_paths_receive.add('no')
        self.nxos_bgp_af_valid_additional_paths_receive.add('yes')

        self.nxos_bgp_af_valid_afi = set()
        self.nxos_bgp_af_valid_afi.add('ipv4')
        self.nxos_bgp_af_valid_afi.add('ipv6')
        self.nxos_bgp_af_valid_afi.add('vpnv4')
        self.nxos_bgp_af_valid_afi.add('vpnv6')
        self.nxos_bgp_af_valid_afi.add('l2vpn')

        self.nxos_bgp_af_valid_safi = set()
        self.nxos_bgp_af_valid_safi.add('unicast')
        self.nxos_bgp_af_valid_safi.add('multicast')
        self.nxos_bgp_af_valid_safi.add('evpn')

        self.nxos_bgp_af_valid_state = set()
        self.nxos_bgp_af_valid_state.add('present')
        self.nxos_bgp_af_valid_state.add('absent')

        self.properties_set = set()
        self.properties_set.add('additional_paths_install')
        self.properties_set.add('additional_paths_receive')
        self.properties_set.add('additional_paths_selection')
        self.properties_set.add('additional_paths_send')
        self.properties_set.add('advertise_l2vpn_evpn')
        self.properties_set.add('afi')
        self.properties_set.add('asn')
        self.properties_set.add('client_to_client')
        self.properties_set.add('dampen_igp_metric')
        self.properties_set.add('dampening_half_time')
        self.properties_set.add('dampening_max_suppress_time')
        self.properties_set.add('dampening_reuse_time')
        self.properties_set.add('dampening_routemap')
        self.properties_set.add('dampening_state')
        self.properties_set.add('dampening_suppress_time')
        self.properties_set.add('default_information_originate')
        self.properties_set.add('default_metric')
        self.properties_set.add('distance_ebgp')
        self.properties_set.add('distance_ibgp')
        self.properties_set.add('distance_local')
        self.properties_set.add('inject_map')
        self.properties_set.add('maximum_paths')
        self.properties_set.add('maximum_paths_ibgp')
        self.properties_set.add('networks')
        self.properties_set.add('next_hop_route_map')
        self.properties_set.add('redistribute')
        self.properties_set.add('safi')
        self.properties_set.add('suppress_inactive')
        self.properties_set.add('table_map')
        self.properties_set.add('table_map_filter')
        self.properties_set.add('vrf')
        self.properties_set.add('state')
        self.init_properties()

        self.nxos_bgp_af_maximum_paths_min = 1
        self.nxos_bgp_af_maximum_paths_max = 64

        self.nxos_bgp_af_maximum_paths_ibgp_min = 1
        self.nxos_bgp_af_maximum_paths_ibgp_max = 64

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.asn == None:
            self.task_log.error('exiting. call instance.asn before calling instance.update()')
            exit(1)
        if self.afi == None:
            self.task_log.error('exiting. call instance.afi before calling instance.update()')
            exit(1)
        if self.safi == None:
            self.task_log.error('exiting. call instance.safi before calling instance.update()')
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
                d[p] = self.properties[p]
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def verify_nxos_bgp_af_additional_paths_receive(self, x, parameter='unspecified'):
        verify_set = self.nxos_bgp_af_valid_additional_paths_receive
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_af_additional_paths_receive'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_af_afi(self, x, parameter=''):
        verify_set = self.nxos_bgp_af_valid_afi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_af_afi'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_af_asn(self, x, parameter='asn'):
        if self.is_bgp_asn(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_af_asn'
        expectation = '[digits, digits.digits]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_af_maximum_paths(self, x, parameter='maximum_paths'):
        source_class = self.class_name
        range_min = self.nxos_bgp_af_maximum_paths_min
        range_max = self.nxos_bgp_af_maximum_paths_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_bgp_af_maximum_paths_ibgp(self, x, parameter='maximum_paths_ibgp'):
        source_class = self.class_name
        range_min = self.nxos_bgp_af_maximum_paths_ibgp_min
        range_max = self.nxos_bgp_af_maximum_paths_ibgp_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_bgp_af_safi(self, x, parameter='safi'):
        verify_set = self.nxos_bgp_af_valid_safi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_af_safi'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_af_state(self, x, parameter='state'):
        verify_set = self.nxos_bgp_af_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_af_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)


    @property
    def additional_paths_install(self):
        return self.properties['additional_paths_install']
    @additional_paths_install.setter
    def additional_paths_install(self, x):
        parameter = 'additional_paths_install'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def additional_paths_receive(self):
        return self.properties['additional_paths_receive']
    @additional_paths_receive.setter
    def additional_paths_receive(self, x):
        parameter = 'additional_paths_receive'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_af_additional_paths_receive(x, parameter)
        self.properties[parameter] = x

    @property
    def additional_paths_selection(self):
        return self.properties['additional_paths_selection']
    @additional_paths_selection.setter
    def additional_paths_selection(self, x):
        parameter = 'additional_paths_selection'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def additional_paths_send(self):
        return self.properties['additional_paths_send']
    @additional_paths_send.setter
    def additional_paths_send(self, x):
        parameter = 'additional_paths_send'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def advertise_l2vpn_evpn(self):
        return self.properties['advertise_l2vpn_evpn']
    @advertise_l2vpn_evpn.setter
    def advertise_l2vpn_evpn(self, x):
        parameter = 'advertise_l2vpn_evpn'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_af_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def asn(self):
        return self.properties['asn']
    @asn.setter
    def asn(self, x):
        parameter = 'asn'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_af_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def client_to_client(self):
        return self.properties['client_to_client']
    @client_to_client.setter
    def client_to_client(self, x):
        parameter = 'client_to_client'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def dampen_igp_metric(self):
        return self.properties['dampen_igp_metric']
    @dampen_igp_metric.setter
    def dampen_igp_metric(self, x):
        parameter = 'dampen_igp_metric'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_half_time(self):
        return self.properties['dampening_half_time']
    @dampening_half_time.setter
    def dampening_half_time(self, x):
        parameter = 'dampening_half_time'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_max_suppress_time(self):
        return self.properties['dampening_max_suppress_time']
    @dampening_max_suppress_time.setter
    def dampening_max_suppress_time(self, x):
        parameter = 'dampening_max_suppress_time'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_reuse_time(self):
        return self.properties['dampening_reuse_time']
    @dampening_reuse_time.setter
    def dampening_reuse_time(self, x):
        parameter = 'dampening_reuse_time'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_routemap(self):
        return self.properties['dampening_routemap']
    @dampening_routemap.setter
    def dampening_routemap(self, x):
        parameter = 'dampening_routemap'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def dampening_state(self):
        return self.properties['dampening_state']
    @dampening_state.setter
    def dampening_state(self, x):
        parameter = 'dampening_state'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_suppress_time(self):
        return self.properties['dampening_suppress_time']
    @dampening_suppress_time.setter
    def dampening_suppress_time(self, x):
        parameter = 'dampening_suppress_time'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def default_information_originate(self):
        return self.properties['default_information_originate']
    @default_information_originate.setter
    def default_information_originate(self, x):
        parameter = 'default_information_originate'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def default_metric(self):
        return self.properties['default_metric']
    @default_metric.setter
    def default_metric(self, x):
        parameter = 'default_metric'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def distance_ebgp(self):
        return self.properties['distance_ebgp']
    @distance_ebgp.setter
    def distance_ebgp(self, x):
        parameter = 'distance_ebgp'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def distance_ibgp(self):
        return self.properties['distance_ibgp']
    @distance_ibgp.setter
    def distance_ibgp(self, x):
        parameter = 'distance_ibgp'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def distance_local(self):
        return self.properties['distance_local']
    @distance_local.setter
    def distance_local(self, x):
        parameter = 'distance_local'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def inject_map(self):
        return self.properties['inject_map']
    @inject_map.setter
    def inject_map(self, x):
        parameter = 'inject_map'
        if self.set_none(x, parameter):
            return
        self.verify_list_of_list(x, parameter)
        self.properties[parameter] = x

    @property
    def maximum_paths(self):
        return self.properties['maximum_paths']
    @maximum_paths.setter
    def maximum_paths(self, x):
        parameter = 'maximum_paths'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_af_maximum_paths(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def maximum_paths_ibgp(self):
        return self.properties['maximum_paths_ibgp']
    @maximum_paths_ibgp.setter
    def maximum_paths_ibgp(self, x):
        parameter = 'maximum_paths_ibgp'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_af_maximum_paths_ibgp(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def networks(self):
        return self.properties['networks']
    @networks.setter
    def networks(self, x):
        parameter = 'networks'
        if self.set_none(x, parameter):
            return
        self.verify_list_of_list(x, parameter)
        self.properties[parameter] = x

    @property
    def next_hop_route_map(self):
        return self.properties['next_hop_route_map']
    @next_hop_route_map.setter
    def next_hop_route_map(self, x):
        parameter = 'next_hop_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def redistribute(self):
        return self.properties['redistribute']
    @redistribute.setter
    def redistribute(self, x):
        '''
        where x is a list_of_list
        Each list contains source-protocol, route-map

        Example:
        task.redistribute = [['direct', 'rm_direct'], ['ospf', 'rm_ospf']]

        '''
        parameter = 'redistribute'
        if self.set_none(x, parameter):
            return
        self.verify_list_of_list(x, parameter)
        self.properties[parameter] = x

    @property
    def safi(self):
        return self.properties['safi']
    @safi.setter
    def safi(self, x):
        parameter = 'safi'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_af_safi(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_inactive(self):
        return self.properties['suppress_inactive']
    @suppress_inactive.setter
    def suppress_inactive(self, x):
        parameter = 'suppress_inactive'
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
        self.verify_nxos_bgp_af_state(x, parameter)
        self.properties[parameter] = x

    @property
    def table_map(self):
        return self.properties['table_map']
    @table_map.setter
    def table_map(self, x):
        parameter = 'table_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def table_map_filter(self):
        return self.properties['table_map_filter']
    @table_map_filter.setter
    def table_map_filter(self, x):
        parameter = 'table_map_filter'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
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
