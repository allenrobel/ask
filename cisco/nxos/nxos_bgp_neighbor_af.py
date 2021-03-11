# NxosBgpNeighborAf() - cisco/nxos/nxos_bgp_neighbor_af.py
our_version = 113

from copy import deepcopy
import re
from ask.common.task import Task

'''
**************************************
NxosBgpNeighborAf()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosBgpNeighborAf() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp_neighbor_af
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp_neighbor_af <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_neighbor_af_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_af.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_af.py>`_


|

=============================   ==============================================
Property                        Description
=============================   ==============================================
additional_paths_receive        Advertise the capability to receive additional
                                paths from the neighbors under this
                                address family ``afi`` for which the capability
                                has not been disabled::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_receive = True

additional_paths_send           Advertise the capability to send additional
                                paths to all of the neighbors under this
                                address family ``afi`` for which the capability
                                has not been disabled::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.additional_paths_send = False

advertise_map_exist             Conditional route advertisement. This property
                                requires two route maps, an ``advertise-map``
                                and an ``exist-map``. Valid values are an array
                                specifying both the ``advertise-map`` name and
                                the ``exist-map`` name, or simply the keyword
                                ``default``.  This property is mutually-exclusive
                                with ``advertise_map_non_exist``::

                                    - Type: list() or str()
                                        - str() if 'default' keyword is used
                                        - list() otherwise
                                    - Valid values:
                                        - 2-element list() containing:
                                            - a route-map name -> advertise-map
                                            - a route-map name -> exist-map
                                        - Keyword: default
                                    - Examples:
                                        - list()
                                            ame = list()
                                            ame.append('my_advertise_map')
                                            ame.append('my_exist_map')
                                            task.advertise_map_exist = ame.copy()
                                        - str()
                                            task.advertise_map_exist = 'default'
                                    - NOTES:
                                        - Mutually-exclusive with: advertise_map_non_exist

advertise_map_non_exist         Conditional route advertisement. This property
                                requires two route maps, an ``advertise-map``
                                and a ``non-exist-map``. Valid values are an array
                                specifying both the ``advertise-map name`` and
                                the ``non-exist-map`` name, or simply the keyword
                                ``default``. This property is mutually-exclusive
                                with ``advertise_map_exist``::

                                    - Type: list() or str()
                                        - str() if 'default' keyword is used
                                        - list() otherwise
                                    - Valid values:
                                        - 2-element list() containing:
                                            - a route-map name -> advertise-map
                                            - a route-map name -> non-exist-map
                                        - Keyword: default
                                    - Examples:
                                        - list()
                                            amne = list()
                                            amne.append('my_advertise_map')
                                            amne.append('my_exist_map')
                                            task.advertise_map_non_exist = amne.copy()
                                        - str()
                                            task.advertise_map_non_exist = 'default'
                                    - NOTES:
                                        - Mutually-exclusive with: advertise_map_exist

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

allowas_in                      Accept advertisements with our AS in the AS path.
                                Mutually-exclusive with allowas_in_max::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.allowas_in = False

allowas_in_max                  Max-occurrences value for allowas_in.
                                Mutually-exclusive with allowas_in::

                                    - Type: int()
                                    - Valid values:
                                        - int() range: 1-10
                                        - Keyword: default
                                    - Example:
                                        task.allowas_in_max = 2

as_override                     Activate the as-override feature::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.as_override = False


asn                             BGP autonomous system number, in ``ASPLAIN`` or ``ASDOT`` notation::

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

default_originate               Advertise the default route to this neighbor, regardless
                                of whether it is present in the routing table::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.default_originate = True

default_originate_route_map     Route-map for the ``default_originate`` property. 
                                Mutually-exclusive with ``default_originate``::

                                    - Valid values:
                                        - str() defining a route-map name
                                        - Keyword: default

disable_peer_as_check           Disable checking of peer AS-number while advertising::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.disable_peer_as_check = True

filter_list_in                  Inbound filter-list applied to this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - filter-list name
                                        - Keyword: default
                                    - Examples:
                                        task.filter_list_in = 'FILTER_IN'
                                        task.filter_list_in = 'default'

filter_list_out                 Outbound filter-list applied to this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - filter-list name
                                        - Keyword: default
                                    - Examples:
                                        task.filter_list_out = 'FILTER_OUT'
                                        task.filter_list_out = 'default'

max_prefix_interval             When the maximum number of prefixes is received from this
                                neighbor, restart the BGP connection after this interval::

                                    - Type: int()
                                    - Valid values: range 1-65535
                                    - Units: seconds
                                    - Example:
                                        task.max_prefix_interval = 300
                                    - NOTES:
                                        - Requires max_prefix_limit to be configured
                                        - Mutually-exclusive with max_prefix_warning

max_prefix_limit                Maximum number of prefixes allowed from this neighbor::

                                    - Type: int()
                                    - Example:
                                        task.max_prefix_limit = 12000

max_prefix_threshold            Optional threshold percentage at which to generate a warning::

                                    - Type: int()
                                    - Example:
                                        task.max_prefix_threshold = 85
                                    NOTES:
                                        - Requires max_prefix_limit to be configured

max_prefix_warning              Warn (via syslog) if the number of prefixes received
                                from this neighbor exceeds ``max_prefix_limit``::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.max_prefix_warning = True
                                    NOTES:
                                        - Requires max_prefix_limit to be configured
                                        - Mutually-exclusive with max_prefix_interval

neighbor                        IPv4 or IPv6 address of the neighbor.  May 
                                include a prefixlen for prefix-peering
                                scenarios::

                                    - Type: str()
                                    - Valid values:
                                        - IPv4 address
                                        - IPv4 address with prefixlen
                                        - IPv6 address
                                        - IPv6 address with prefixlen
                                    - Examples:
                                        task.neighbor = '10.1.1.1'
                                        task.neighbor = '10.1.1.0/24'
                                        task.neighbor = '2011:aaaa::1'
                                        task.neighbor = '2011:aaaa::/126'
                                    - Required

next_hop_self                   Advertise prefixes to this neighbor with our peering
                                interface as the next-hop::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.next_hop_self = True

next_hop_third_party            If the neighbor and the next-hop for a given prefix are both
                                on a common shared network (e.g. an L2 internet peering point
                                where the neighbor address falls within the same subnet as a
                                prefix's next-hop), ``next_hop_third_party`` determines whether
                                we advertise the prefix with the unaltered (3rd-party) next-hop
                                of the prefix, or no.  See RFC2283::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.next_hop_third_party = False

prefix_list_in                  Inbound prefix-list influencing acceptance of
                                prefixes from this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - prefix-list name
                                        - Keyword: default
                                    - Examples:
                                        task.prefix_list_in = 'PREFIX_IN'
                                        task.prefix_list_in = 'default'

prefix_list_out                 Outbound prefix-list influencing advertisement of
                                prefixes to this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - prefix-list name
                                        - Keyword: default
                                    - Examples:
                                        task.prefix_list_out = 'PREFIX_OUT'
                                        task.prefix_list_out = 'default'

rewrite_evpn_rt_asn             Auto generate route targets for EBGP neighbor::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.rewrite_evpn_rt_asn = True

route_map_in                    Inbound route-map for this neighbor which permits
                                and/or denies acceptance of prefixes from neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - route-map name
                                        - Keyword: default
                                    - Examples:
                                        task.route_map_in = 'TO_TOR'
                                        task.route_map_in = 'default'

route_map_out                   Outbound route-map for this neighbor which permits
                                and/or denies advertisement of prefixes::

                                    - Type: str()
                                    - Valid values:
                                        - route-map name
                                        - Keyword: default
                                    - Examples:
                                        task.route_map_out = 'TO_TOR'
                                        task.route_map_out = 'default'

route_reflector_client          Specify whether this neighbor is a route-reflector
                                client::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.route_reflector_client = True

safi                            Sub Address Family Identifier::

                                    - Type: str()
                                    - Valid values:
                                        - unicast
                                        - multicast
                                        - evpn
                                    - Example:
                                        - task.safi = 'unicast'
                                    - Required

send_community                  Send the BGP community attribute to this neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - none
                                        - both
                                        - extended
                                        - standard
                                        - default
                                    - Example:
                                        task.send_community = 'both'

soft_reconfiguration_in         Configure inbound soft-reconfiguration::

                                    - Type: str()
                                    - Valid values:
                                        - enable  (issues: soft-reconfiguration inbound)
                                        - always  (issues: soft-reconfiguration inbound always)
                                        - inherit (remove from neighbor config and inherit,
                                                   if present, from a template)
                                    - Example:
                                        task.soft_reconfiguration_in = 'always'

soo                             Site-of-origin::

                                    - Type: str()
                                    - Valid values:
                                        - str() defining a VPN extcommunity
                                        - str() Keyword: default
                                    - Examples:
                                        - task.soo = '65000:0'
                                        - task.soo = 'default'

state                           Determines whether the config should be present or
                                not on the remote device::

                                    - Type: str()
                                    - Valid values:
                                        - absent
                                        - present
                                    - Examples:
                                        - task.state = 'present'
                                    - Required

suppress_inactive               Advertise only active routes to peers::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Examples:
                                        - task.suppress_inactive = True

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Examples:
                                        - task.task_name = 'my task'

unsuppress_map                  In addition to active routes (see ``suppress_inactive``) advertise these
                                inactive routes::

                                    - Type: str()
                                    - Valid values:
                                        - A route-map name
                                        - Keyword: default
                                    - Examples:
                                        - task.unsuppress_map = 'DO_NOT_SUPPRESS_THESE'
                                        - task.unsuppress_map = 'default'

vrf                             Name of the VRF. The name ``default`` is a valid VRF representing
                                the global bgp table.::

                                    - Type: str()
                                    - Default: 'default'
                                    - Examples:
                                        - task.vrf = 'default'
                                        - task.vrf = 'PROD'

weight                          ``weight`` is a Cisco proprietary property and is not exchanged
                                with BGP neighbors.  Weight takes precedence over other BGP path
                                selection attributes (assuming all other attributes are equal 
                                between two or more neighbors). To prefer one neighbor over others
                                (again, assuming their other next-hop selection criteria are equal)
                                set the weight for that neighbor higher than the other neighbors)::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range: 0-65535
                                        - str() Keyword: default
                                    - Examples:
                                        - task.weight = 400
                                        - task.weight = 'default'

=============================   ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)


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

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

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
        self.verify_boolean(x, parameter)
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
        self.verify_boolean(x, parameter)
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
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def default_originate(self):
        return self.properties['default_originate']
    @default_originate.setter
    def default_originate(self, x):
        parameter = 'default_originate'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
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
        self.verify_boolean(x, parameter)
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
        self.verify_boolean(x, parameter)
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
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def next_hop_third_party(self):
        return self.properties['next_hop_third_party']
    @next_hop_third_party.setter
    def next_hop_third_party(self, x):
        parameter = 'next_hop_third_party'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
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
        self.verify_boolean(x, parameter)
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
        self.verify_boolean(x, parameter)
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
