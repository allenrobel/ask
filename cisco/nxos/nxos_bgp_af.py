# NxosBgpAf() - cisco/nxos/nxos_bgp_af.py
our_version = 111

# standard library
from copy import deepcopy
import re
# scriptkit library
from ask.common.task import Task
'''
Name: nxos_bgp_af.py

Description:

AskNxosBgpAf() generates Ansible Playbook tasks conformant with nxos_bgp_af
which can be fed to AnsPlaybook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_bgp_af.py

Properties:

    additional_paths_install        Valid values: no, yes
    additional_paths_receive        Valid values: no, yes      
    additional_paths_selection      route-map name
    additional_paths_send           Valid values: no, yes
    advertise_l2vpn_evpn            Value values: no, yes
    afi                             Valid values: ipv4, ipv6, vpnv4, vpnv6, l2vpn
    asn                             Valid values: digits, digits.digits
    client_to_client                Valid values: no, yes
    dampen_igp_metric               Valid values: int(), 'default'
    dampening_half_time             Valid values: int(), 'default'
    dampening_max_suppress_time     Valid values: int(), 'default'
    dampening_reuse_time            Valid values: int(), 'default'
    dampening_routemap              route-map name
    dampening_state                 Valid values: no, yes
    dampening_suppress_time         Valid values: int(), 'default'
    default_information_originate   Valid values: no, yes
    default_metric'] = None         Valid values: int(), 'default'
    distance_ebgp'] = None          Valid values: int(), 'default'
    distance_ibgp'] = None          Valid values: int(), 'default'
    distance_local'] = None         Valid values: int(), 'default'
    inject_map                      list_of_list
                                        Each list contains route-map, exists-map, plus optional keyword 'copy-attributes'
                                        Example:
                                            [['my_imap1', 'my_emap1', 'copy-attributes'], ['my_imap2', 'my_emap2']]
    maximum_paths                   Valid values: int() range: 1-64
    maximum_paths_ibgp              Valid values: int() range: 1-64
    networks                        list_of_list
                                        Each list contains network/prefix and optionally, route-map name
                                        [['network/prefix'], ['network/prefix', 'route-map name'], ...]
                                        Example:
                                            [['10.0.0.0/16', 'routemap_LA'], ['192.168.2.0/24']]
    next_hop_route_map              route-map name  
    redistribute                    list_of_list
                                        Each list contains source-protocol, route-map
                                        Example:
                                            [['direct', 'rm_direct'], ['ospf', 'rm_ospf']].
    safi                            Valid values: unicast, multicast, evpn
    suppress_inactive               Valid values: no, yes
    table_map                       route-map name
    table_map_filter                Valid values: no, yes
    vrf                             vrf name
    state                           Valid values: present, absent
                                        Mandatory
    task_name                       Name of the task
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

    def nxos_bgp_af_verify_additional_paths_receive(self, x, parameter='unspecified'):
        #       self.nxos_bgp_af_valid_additional_paths_receive is the respective subclasses
        if x in self.nxos_bgp_af_valid_additional_paths_receive:
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_af_verify_additional_paths_receive'
        expectation = self.nxos_bgp_af_valid_additional_paths_receive 
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_af_verify_afi(self, x, parameter=''):
        if x in self.nxos_bgp_af_valid_afi:
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_af_verify_afi'
        expectation = self.nxos_bgp_af_valid_afi
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_af_verify_asn(self, x, parameter=''):
        if self.is_digits(x):
            return
        if re.search('^\d+\.\d+$', str(x)):
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_af_verify_asn'
        expectation = '["digits", "digits.digits", "digits:digits"]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_af_verify_safi(self, x, parameter='safi'):
        if x in self.nxos_bgp_af_valid_safi:
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_af_verify_safi'
        expectation = self.nxos_bgp_af_valid_safi
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_af_verify_state(self, x, parameter='state'):
        if x in self.nxos_bgp_af_valid_state:
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_af_verify_state'
        expectation = ','.join(self.nxos_bgp_neighbor_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)


    @property
    def additional_paths_install(self):
        return self.properties['additional_paths_install']
    @additional_paths_install.setter
    def additional_paths_install(self, x):
        '''
        '''
        parameter = 'additional_paths_install'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def additional_paths_receive(self):
        return self.properties['additional_paths_receive']
    @additional_paths_receive.setter
    def additional_paths_receive(self, x):
        '''
        '''
        parameter = 'additional_paths_receive'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_af_verify_additional_paths_receive(x, parameter)
        self.properties[parameter] = x


    @property
    def additional_paths_selection(self):
        return self.properties['additional_paths_selection']
    @additional_paths_selection.setter
    def additional_paths_selection(self, x):
        '''
        '''
        parameter = 'additional_paths_selection'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def additional_paths_send(self):
        return self.properties['additional_paths_send']
    @additional_paths_send.setter
    def additional_paths_send(self, x):
        '''
        '''
        parameter = 'additional_paths_send'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def advertise_l2vpn_evpn(self):
        return self.properties['advertise_l2vpn_evpn']
    @advertise_l2vpn_evpn.setter
    def advertise_l2vpn_evpn(self, x):
        '''
        '''
        parameter = 'advertise_l2vpn_evpn'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        '''
        '''
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_af_verify_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def asn(self):
        return self.properties['asn']
    @asn.setter
    def asn(self, x):
        '''
        '''
        parameter = 'asn'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_af_verify_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def client_to_client(self):
        return self.properties['client_to_client']
    @client_to_client.setter
    def client_to_client(self, x):
        '''
        '''
        parameter = 'client_to_client'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def dampen_igp_metric(self):
        return self.properties['dampen_igp_metric']
    @dampen_igp_metric.setter
    def dampen_igp_metric(self, x):
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
        parameter = 'dampening_routemap'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def dampening_state(self):
        return self.properties['dampening_state']
    @dampening_state.setter
    def dampening_state(self, x):
        '''
        '''
        parameter = 'dampening_state'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def dampening_suppress_time(self):
        return self.properties['dampening_suppress_time']
    @dampening_suppress_time.setter
    def dampening_suppress_time(self, x):
        '''
        '''
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
        '''
        '''
        parameter = 'default_information_originate'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def default_metric(self):
        return self.properties['default_metric']
    @default_metric.setter
    def default_metric(self, x):
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
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
        '''
        '''
        parameter = 'maximum_paths'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        x = int(str(x))
        if x not in list(range(1,65)):
            _expectation = "int() in range 1-64"
            self.fail(self.class_name, parameter, x, parameter, _expectation)
        self.properties[parameter] = x

    @property
    def maximum_paths_ibgp(self):
        return self.properties['maximum_paths_ibgp']
    @maximum_paths_ibgp.setter
    def maximum_paths_ibgp(self, x):
        '''
        '''
        parameter = 'maximum_paths_ibgp'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        x = int(str(x))
        if x not in list(range(1,65)):
            _expectation = "int() in range 1-64"
            self.fail(self.class_name, parameter, x, parameter, _expectation)
        self.properties[parameter] = x

    @property
    def networks(self):
        return self.properties['networks']
    @networks.setter
    def networks(self, x):
        '''
        '''
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
        '''
        '''
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
        '''
        '''
        parameter = 'safi'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_af_verify_safi(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_inactive(self):
        return self.properties['suppress_inactive']
    @suppress_inactive.setter
    def suppress_inactive(self, x):
        '''
        '''
        parameter = 'suppress_inactive'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        '''
        '''
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_af_verify_state(x, parameter)
        self.properties[parameter] = x

    @property
    def table_map(self):
        return self.properties['table_map']
    @table_map.setter
    def table_map(self, x):
        '''
        '''
        parameter = 'table_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def table_map_filter(self):
        return self.properties['table_map_filter']
    @table_map_filter.setter
    def table_map_filter(self, x):
        '''
        '''
        parameter = 'table_map_filter'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def vrf(self):
        return self.properties['vrf']
    @vrf.setter
    def vrf(self, x):
        '''
        '''
        parameter = 'vrf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
