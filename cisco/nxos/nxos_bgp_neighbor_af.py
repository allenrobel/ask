# NxosBgpNeighborAf() - cisco/nxos/nxos_bgp_neighbor_af.py
our_version = 110

# standard library
from copy import deepcopy
import re
# scriptkit library
from ask.common.task import Task

'''
Name: nxos_bgp_neighbor_af.py

Description:

NxosBgpNeighborAf() generates Ansible Playbook tasks conformant with nxos_bgp_neighbor_af
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_af.py

Properties:
    additional_paths_receive        Valid values: enable, disable, inherit
    additional_paths_send           Valid values: enable, disable, inherit
    advertise_map_exist             Valid values: ['my_advertise_map', 'my_exist_map'], or default
                                        mutually-exclusive with advertise_map_non_exist
    advertise_map_non_exist         Valid values: ['my_advertise_map', 'my_exist_map'], or default
                                        mutually-exclusive with advertise_map_exist
    afi                             Valid values: ipv4, ipv6, vpnv4, vpnv6, l2vpn
    allowas_in                      Valid values: no, yes
                                        mutually-exclusive with allowas_in_max
    allowas_in_max                  Valid values: int(), or default
                                        mutually-exclusive with allowas_in
    asn                             Valid values: digits, digits.digits
    as_override                     Valid values: no, yes
    default_originate               Valid values: no, yes
    default_originate_route_map     Valid values: str() or 'default' route-map name.
                                        mutually-exclusive with default_originate(?)
    disable_peer_as_check           Valid values: no, yes
    filter_list_in                  Valid values: str(), or 'default'
    filter_list_out                 Valid values: str(), or 'default'
    max_prefix_interval             Valid values: int()
                                        If present, max_prefix_limit must also be present.
    max_prefix_limit                Valid values: int(), or default
    max_prefix_threshold            Valid values: int()
                                        If present, max_prefix_limit must also be present.
    max_prefix_warning              Valid values: no, yes.  
                                        If present, max_prefix_limit must also be present.
                                        mutually-exclusive with max_prefix_interval
    neighbor                        Valid values: ipv4, ipv6 address. With or without prefix length.
                                        Required  
    next_hop_self                   Valid values: no, yes
    next_hop_third_party            Valid values: no, yes
    prefix_list_in                  Valid values: str(), or 'default'
    prefix_list_out                 Valid values: str(), or 'default'
    route_map_in                    Valid values: str(), or 'default'
    route_map_out                   Valid values: str(), or 'default'
    route_reflector_client          Valid values: no, yes
    safi                            Valid values: str() unicast, multicast, evpn
    send_community                  Valid values: none, both, extended, standard, default
    soft_reconfiguration_in         Valid values: enable, always, inherit
    soo                             Valid values: str(), or 'default'
    suppress_inactive               Valid values: no, yes
    unsuppress_map                  Valid values: str(), or 'default'
    weight                          Valid values: int(), or default

'''

class NxosBgpNeighborAf(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp_neighbor_af'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.properties_set = set()
        self.properties_set.add('additional_paths_receive')
        self.properties_set.add('additional_paths_send')
        self.properties_set.add('advertise_map_exist')
        self.properties_set.add('advertise_map_non_exist')
        self.properties_set.add('afi')
        self.properties_set.add('allowas_in')
        self.properties_set.add('allowas_in_max')
        self.properties_set.add('asn')
        self.properties_set.add('as_override')
        self.properties_set.add('default_originate')
        self.properties_set.add('default_originate_route_map')
        self.properties_set.add('disable_peer_as_check')
        self.properties_set.add('filter_list_in')
        self.properties_set.add('filter_list_out')
        self.properties_set.add('max_prefix_interval')
        self.properties_set.add('max_prefix_limit')
        self.properties_set.add('max_prefix_threshold')
        self.properties_set.add('max_prefix_warning')
        self.properties_set.add('neighbor')
        self.properties_set.add('next_hop_self')
        self.properties_set.add('next_hop_third_party')
        self.properties_set.add('prefix_list_in')
        self.properties_set.add('prefix_list_out')
        self.properties_set.add('route_map_in')
        self.properties_set.add('route_map_out')
        self.properties_set.add('route_reflector_client')
        self.properties_set.add('safi')
        self.properties_set.add('send_community')
        self.properties_set.add('soft_reconfiguration_in')
        self.properties_set.add('soo')
        self.properties_set.add('state')
        self.properties_set.add('suppress_inactive')
        self.properties_set.add('unsuppress_map')
        self.properties_set.add('weight')

        self.nxos_bgp_neighbor_af_valid_additional_paths_receive = set()
        self.nxos_bgp_neighbor_af_valid_additional_paths_receive.add('enable')
        self.nxos_bgp_neighbor_af_valid_additional_paths_receive.add('disable')
        self.nxos_bgp_neighbor_af_valid_additional_paths_receive.add('inherit')

        self.nxos_bgp_neighbor_af_valid_afi = set()
        self.nxos_bgp_neighbor_af_valid_afi.add('ipv4')
        self.nxos_bgp_neighbor_af_valid_afi.add('ipv6')
        self.nxos_bgp_neighbor_af_valid_afi.add('vpnv4')
        self.nxos_bgp_neighbor_af_valid_afi.add('vpnv6')
        self.nxos_bgp_neighbor_af_valid_afi.add('l2vpn')

        self.nxos_bgp_neighbor_af_valid_safi = set()
        self.nxos_bgp_neighbor_af_valid_safi.add('unicast')
        self.nxos_bgp_neighbor_af_valid_safi.add('multicast')
        self.nxos_bgp_neighbor_af_valid_safi.add('evpn')

        self.nxos_bgp_neighbor_af_valid_send_community = set()
        self.nxos_bgp_neighbor_af_valid_send_community.add('none')
        self.nxos_bgp_neighbor_af_valid_send_community.add('both')
        self.nxos_bgp_neighbor_af_valid_send_community.add('extended')
        self.nxos_bgp_neighbor_af_valid_send_community.add('standard')
        self.nxos_bgp_neighbor_af_valid_send_community.add('default')

        self.nxos_bgp_neighbor_af_valid_soft_reconfiguration_in = set()
        self.nxos_bgp_neighbor_af_valid_soft_reconfiguration_in.add('enable')
        self.nxos_bgp_neighbor_af_valid_soft_reconfiguration_in.add('always')
        self.nxos_bgp_neighbor_af_valid_soft_reconfiguration_in.add('inherit')

        self.nxos_bgp_neighbor_af_valid_state = set('')
        self.nxos_bgp_neighbor_af_valid_state.add('present')
        self.nxos_bgp_neighbor_af_valid_state.add('absent')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.afi == None:
            self.task_log.error('exiting. call instance.afi before calling instance.update()')
            exit(1)
        if self.safi == None:
            self.task_log.error('exiting. call instance.safi before calling instance.update()')
            exit(1)
        if self.allowas_in != None and self.allowas_in_max != None:
            self.task_log.error('exiting. allowas_in is mutually-exclusive with allowas_in_max')
            exit(1)
        if self.any_defined([self.max_prefix_warning, self.max_prefix_limit]):
            if not self.all_defined([self.max_prefix_warning, self.max_prefix_limit]):
                self.task_log.error('exiting. either define both max_prefix_warning and max_prefix_limit, or neither.')
                self.task_log.error('max_prefix_warning {}'.format(self.max_prefix_warning))
                self.task_log.error('max_prefix_limit {}'.format(self.max_prefix_limit))
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
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.init_properties()

    def verify_nxos_bgp_neighbor_af_state(self, x, parameter='state'):
        if x in self.nxos_bgp_neighbor_af_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_af_state'
        expectation = ','.join(self.nxos_bgp_neighbor_af_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_af_verify_additional_paths_receive(self, x, parameter='additional_paths_receive'):
        if x in self.nxos_bgp_neighbor_af_valid_additional_paths_receive:
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_neighbor_af_verify_additional_paths_receive'
        expectation = self.nxos_bgp_neighbor_af_valid_additional_paths_receive 
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_af_verify_afi(self, x, parameter='afi'):
        if x in self.nxos_bgp_neighbor_af_valid_afi:
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_neighbor_af_verify_afi'
        expectation = self.nxos_bgp_neighbor_af_valid_afi
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_af_verify_asn(self, x, parameter='asn'):
        if self.is_digits(x):
            return
        if re.search('^\d+\.\d+$', str(x)):
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_neighbor_af_verify_asn'
        expectation = '["digits", "digits.digits", "digits:digits"]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_af_verify_neighbor(self, x, parameter='neighbor'):
        _expectation = "[IPv4 Address, IPv6 Address]"
        if self.is_ipv4_address(x):
            return
        if self.is_ipv6_address(x):
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_neighbor_af_verify_neighbor'
        self.fail(source_class, source_method, x, parameter, _expectation)

    def nxos_bgp_neighbor_af_verify_safi(self, x, parameter='safi'):
        if x in self.nxos_bgp_neighbor_af_valid_safi:
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_neighbor_af_verify_safi'
        expectation = self.nxos_bgp_neighbor_af_valid_safi
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_af_verify_send_community(self, x, parameter='send_community'):
        if x in self.nxos_bgp_neighbor_af_valid_send_community:
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_neighbor_af_verify_send_community'
        expectation = self.nxos_bgp_neighbor_af_valid_send_community
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bgp_neighbor_af_verify_soft_reconfiguration_in(self, x, parameter='soft_reconfiguration_in'):
        if x in self.nxos_bgp_neighbor_af_valid_soft_reconfiguration_in:
            return
        source_class = self.class_name
        source_method = 'nxos_bgp_neighbor_af_verify_soft_reconfiguration_in'
        expectation = self.nxos_bgp_neighbor_af_valid_soft_reconfiguration_in
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def additional_paths_receive(self):
        return self.properties['additional_paths_receive']
    @additional_paths_receive.setter
    def additional_paths_receive(self, x):
        parameter = 'additional_paths_receive'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_af_verify_additional_paths_receive(x, parameter)
        self.properties[parameter] = x

    @property
    def additional_paths_install(self):
        return self.properties['additional_paths_install']
    @additional_paths_install.setter
    def additional_paths_install(self, x):
        parameter = 'additional_paths_install'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def additional_paths_send(self):
        return self.properties['additional_paths_send']
    @additional_paths_send.setter
    def additional_paths_send(self, x):
        parameter = 'additional_paths_send'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_af_verify_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def asn(self):
        return self.properties['asn']
    @asn.setter
    def asn(self, x):
        parameter = 'asn'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_af_verify_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def advertise_map_exist(self):
        return self.properties['advertise_map_exist']
    @advertise_map_exist.setter
    def advertise_map_exist(self, x):
        parameter = 'advertise_map_exist'
        if self.set_none(x, parameter):
            return
        self.verify_list_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def advertise_map_non_exist(self):
        return self.properties['advertise_map_non_exist']
    @advertise_map_non_exist.setter
    def advertise_map_non_exist(self, x):
        parameter = 'advertise_map_non_exist'
        if self.set_none(x, parameter):
            return
        self.verify_list_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def allowas_in(self):
        return self.properties['allowas_in']
    @allowas_in.setter
    def allowas_in(self, x):
        parameter = 'allowas_in'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def allowas_in_max(self):
        return self.properties['allowas_in_max']
    @allowas_in_max.setter
    def allowas_in_max(self, x):
        parameter = 'allowas_in_max'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def as_override(self):
        return self.properties['as_override']
    @as_override.setter
    def as_override(self, x):
        parameter = 'as_override'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def default_originate(self):
        return self.properties['default_originate']
    @default_originate.setter
    def default_originate(self, x):
        parameter = 'default_originate'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def default_originate_route_map(self):
        return self.properties['default_originate_route_map']
    @default_originate_route_map.setter
    def default_originate_route_map(self, x):
        parameter = 'default_originate_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def disable_peer_as_check(self):
        return self.properties['disable_peer_as_check']
    @disable_peer_as_check.setter
    def disable_peer_as_check(self, x):
        parameter = 'disable_peer_as_check'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def filter_list_in(self):
        return self.properties['filter_list_in']
    @filter_list_in.setter
    def filter_list_in(self, x):
        parameter = 'filter_list_in'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def filter_list_out(self):
        return self.properties['filter_list_out']
    @filter_list_out.setter
    def filter_list_out(self, x):
        parameter = 'filter_list_out'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def max_prefix_interval(self):
        return self.properties['max_prefix_interval']
    @max_prefix_interval.setter
    def max_prefix_interval(self, x):
        parameter = 'max_prefix_interval'
        if self.set_none(x, parameter):
            return
        if self.max_prefix_warning != None:
            self.task_log.error('exiting. {} is mutually-exclusive with max_prefix_warning.'.format(parameter))
            exit(1)
        self.verify_digits(x, parameter)
        self.properties[parameter] = x

    @property
    def max_prefix_limit(self):
        return self.properties['max_prefix_limit']
    @max_prefix_limit.setter
    def max_prefix_limit(self, x):
        parameter = 'max_prefix_limit'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def max_prefix_threshold(self):
        return self.properties['max_prefix_threshold']
    @max_prefix_threshold.setter
    def max_prefix_threshold(self, x):
        parameter = 'max_prefix_threshold'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = x

    @property
    def max_prefix_warning(self):
        return self.properties['max_prefix_warning']
    @max_prefix_warning.setter
    def max_prefix_warning(self, x):
        parameter = 'max_prefix_warning'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor(self):
        return self.properties['neighbor']
    @neighbor.setter
    def neighbor(self, x):
        parameter = 'neighbor'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_af_verify_neighbor(x)
        self.properties[parameter] = x

    @property
    def next_hop_self(self):
        return self.properties['next_hop_self']
    @next_hop_self.setter
    def next_hop_self(self, x):
        parameter = 'next_hop_self'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def next_hop_third_party(self):
        return self.properties['next_hop_third_party']
    @next_hop_third_party.setter
    def next_hop_third_party(self, x):
        parameter = 'next_hop_third_party'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def prefix_list_in(self):
        return self.properties['prefix_list_in']
    @prefix_list_in.setter
    def prefix_list_in(self, x):
        parameter = 'prefix_list_in'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def prefix_list_out(self):
        return self.properties['prefix_list_out']
    @prefix_list_out.setter
    def prefix_list_out(self, x):
        parameter = 'prefix_list_out'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def route_map_in(self):
        return self.properties['route_map_in']
    @route_map_in.setter
    def route_map_in(self, x):
        parameter = 'route_map_in'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def route_map_out(self):
        return self.properties['route_map_out']
    @route_map_out.setter
    def route_map_out(self, x):
        parameter = 'route_map_out'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def route_reflector_client(self):
        return self.properties['route_reflector_client']
    @route_reflector_client.setter
    def route_reflector_client(self, x):
        parameter = 'route_reflector_client'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def safi(self):
        return self.properties['safi']
    @safi.setter
    def safi(self, x):
        parameter = 'safi'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_af_verify_safi(x, parameter)
        self.properties[parameter] = x

    @property
    def send_community(self):
        return self.properties['send_community']
    @send_community.setter
    def send_community(self, x):
        parameter = 'send_community'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_af_verify_send_community(x, parameter)
        self.properties[parameter] = x

    @property
    def soft_reconfiguration_in(self):
        return self.properties['soft_reconfiguration_in']
    @soft_reconfiguration_in.setter
    def soft_reconfiguration_in(self, x):
        parameter = 'soft_reconfiguration_in'
        if self.set_none(x, parameter):
            return
        self.nxos_bgp_neighbor_af_verify_soft_reconfiguration_in(x, parameter)
        self.properties[parameter] = x

    @property
    def soo(self):
        return self.properties['soo']
    @soo.setter
    def soo(self, x):
        parameter = 'soo'
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
        self.verify_nxos_bgp_neighbor_af_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_inactive(self):
        return self.properties['suppress_inactive']
    @suppress_inactive.setter
    def suppress_inactive(self, x):
        parameter = 'suppress_inactive'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def unsuppress_map(self):
        return self.properties['unsuppress_map']
    @unsuppress_map.setter
    def unsuppress_map(self, x):
        parameter = 'unsuppress_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def weight(self):
        return self.properties['weight']
    @weight.setter
    def weight(self, x):
        parameter = 'weight'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x
