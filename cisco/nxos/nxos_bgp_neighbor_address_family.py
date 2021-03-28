# NxosBgpNeighborAddressFamily() - cisco/nxos/nxos_bgp_neighbor_address_family.py
our_version = 101
from copy import deepcopy
import re
from ask.common.task import Task
'''
**************************************
NxosBgpNeighborAddressFamily()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
100

Status
------

- BETA

- This library is in development and not yet complete, nor fully-tested.
- See TODO below for missing functionality.

TODO
----

1. Support for states ``parsed`` and ``rendered`` not yet included
    - Hence ``running_config`` property is not yet supported
2. Verification of property mutual-exclusion not complete
3. Verification of required properties not complete
4. Verification of missing/dependent properties not complete

ScriptKit Synopsis
------------------
- NxosBgpNeighborAddressFamily() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp_neighbor_address_family
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp_neighbor_address_family <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_neighbor_address_family_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_address_family.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_address_family.py>`_

NOTES
-----

1.  When ``task.add_vrf()`` is called, the following happens:

    a.  All currently-defined neighbor address-families that were added using
        ``instance.add_address_family()`` followed by ``instance.add_vrf_bgp_neighbor()``
        are added to the vrf specified with ``instance.vrf`` and the vrf bgp neighbor
        list is cleared so that a new set of neighbor address-families can be added
        to another non-default vrf.

2.  Based on the above note, below is an example which adds two bgp neighbors
    into the default vrf, one bgp neighbor into vrf VRF_1, and two bgp neighbors
    into vrf VRF_2::

        pb = Playbook(log)
        task = NxosBgpNeighborAddressFamily(log)
        task.as_number = '6202.0'

        # Add two AF to a neighbor in VRF_1
        task.afi = 'ipv4'
        task.safi = 'unicast'
        task.add_address_family()

        task.afi = 'ipv6'
        task.safi = 'unicast'
        task.add_address_family()

        task.neighbor_address = '10.1.1.1'
        task.add_vrf_bgp_neighbor()
        task.vrf = 'VRF_1'
        task.add_vrf()

        # Add an AF to a neighbor in the global/default vrf
        task.afi = 'ipv6'
        task.safi = 'unicast'
        task.add_address_family()
        task.neighbor_address = '10.2.1.1'
        task.add_bgp_neighbor()

        # Add an AF to two neighbors in VRF_2
        task.afi = 'ipv4'
        task.safi = 'multicast'
        task.neighbor_address = '10.3.1.1'
        task.add_address_family()
        task.add_vrf_bgp_neighbor()

        task.afi = 'ipv4'
        task.safi = 'unicast'
        task.add_address_family()
        task.neighbor_address = '10.3.1.3'
        task.add_vrf_bgp_neighbor()
        task.vrf = "VRF_2"
        task.add_vrf()

        # Add another bgp neighbor to the global/default vrf
        task.afi = 'ipv4'
        task.safi = 'unicast'
        task.add_address_family()
        task.neighbor_address = '10.1.1.1'
        task.add_bgp_neighbor()

        # update the task. This performs a final verification
        # and prepares the task to be added to a playbook
        task.task_name = 'bgp neighbor AFs under default vrf and non-default vrf'
        task.state = 'merged'
        task.update()

        # add the task to the playbook
        pb.add_task(task)

        # Append the playbook (more than one playbook, each
        # with more than one task, can be appended to a
        # given playbook file)
        pb.append_playbook()

        # write the playbook
        pb.file = '/tmp/nxos_bgp_neighbor_address_family.yaml'
        pb.write_playbook()

|

========================================    ==============================================
Method                                      Description
========================================    ==============================================
add_address_family()                        Add an address-family to the address-family
                                            list.::

                                                Example:
                                                    task = NxosBgpNeighborAddressFamily(log)
                                                    task.as_number = '12000.0'
                                                    task.afi = 'ipv4'
                                                    task.safi = 'unicast'
                                                    task.add_address_family()
                                                    task.afi = 'ipv6'
                                                    task.safi = 'unicast'
                                                    task.add_address_family()

add_bgp_neighbor()                          Add a bgp neighbor, along with the currrent
                                            address-family list, to the default/global vrf::

                                                Example:
                                                    task = NxosBgpNeighborAddressFamily(log)
                                                    task.as_number = '12000.0'
                                                    task.afi = 'ipv4'
                                                    task.safi = 'multicast'
                                                    task.add_address_family()
                                                    task.neighbor_address = '10.4.4.0/24'
                                                    task.add_bgp_neighbor()

add_vrf_bgp_neighbor()                      Add a bgp neighbor, along with the currrent
                                            address-family list, to a non-default vrf::

                                                Example:
                                                    task = NxosBgpNeighborAddressFamily(log)
                                                    task.as_number = '12000.0'
                                                    task.afi = 'ipv4'
                                                    task.safi = 'multicast'
                                                    task.add_address_family()
                                                    task.neighbor_address = '10.4.4.0/24'
                                                    task.add_vrf_bgp_neighbor()
                                                    task.vrf = 'MY_VRF'
                                                    task.add_vrf()

add_vrf()                                   Add all bgp neighbors onfigured up to this
                                            point with ``add_vrf_bgp_neighbor()``,
                                            to the current ``vrf``.::

                                                Example (add one neighbor with one
                                                address family to vrf VRF_1):

                                                    task = NxosBgpNeighborAddressFamily(log)
                                                    task.as_number = '12000.0'
                                                    task.afi = 'ipv4'
                                                    task.safi = 'unicast'
                                                    task.next_hop_self_all_routes = True
                                                    task.next_hop_self_set = True
                                                    task.as_override = True
                                                    task.add_address_family()
                                                    task.neighbor_address = '10.4.4.0/24'
                                                    task.add_vrf_bgp_neighbor()
                                                    task.vrf = 'VRF_1'
                                                    task.add_vrf()

========================================    ==============================================

|

=================================== ==============================================
Property                            Description
=================================== ==============================================
advertise_map_exist_map             Condition route-map to advertise only when
                                    prefix in condition exists::

                                        - Type: str()
                                        - Example:
                                            task.advertise_map_exist_map = 'RM_EXIST'

advertise_map_non_exist_map         Condition route-map to advertise only when
                                    prefix in condition does not exist::

                                        - Type: str()
                                        - Example:
                                            task.advertise_map_non_exist_map = 'RM_NON_EXIST'

advertise_map_route_map             Route-map name::

                                        - Type: str()
                                        - Required if other advertise_map_* are set
                                        - Example:
                                            task.advertise_map_route_map = 'AM_RM'

advertisement_interval              Minimum interval between sending BGP routing updates::

                                        - Type: int()
                                        - Valid values:
                                            - range 1-600
                                        - Units: seconds
                                        - Example:
                                            task.advertisement_interval = 10

afi                                 Address Family indicator::

                                        - Type: str()
                                        - Valid values:
                                            - ipv4
                                            - ipv6
                                            - link-state
                                            - vpnv4
                                            - vpnv6
                                            - l2vpn
                                        - Required
                                        - Example:
                                            task.afi = 'ipv4'

allowas_in_max_occurences           Number of occurrences of AS number to allow in
                                    inbound updates::

                                        - Type: int()
                                        - Valid values:
                                            - range 1-10
                                        - Default: 3
                                        - Example:
                                            task.allowas_in_max_occurences = 10

allowas_in_set                      Activate allowas-in property::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.allowas_in_set = True

as_number                           BGP autonomous system number of the router::

                                        - Type: int() or str()
                                        - Valid values:
                                            - int() range 1-4294967295
                                            - str() <1-65535>.<0-65535>
                                        - Required
                                        - Examples:
                                            task.as_number = 64512
                                            task.as_number = 4200000000
                                            task.as_number = '2301.0'
                                        - NOTES:
                                            - private asn ranges
                                                - 64512 to 65534
                                                - 4200000000 to 4294967294

as_override                         Override matching AS-number while sending update.::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.as_override = False

capability_additional_paths_receive Enable additional paths receive capability::

                                        - Type: str()
                                        - Valid values:
                                            - disable
                                            - enable
                                        - Example:
                                            task.capability_additional_paths_receive = 'disable'

capability_additional_paths_send    Enable additional paths send capability::

                                        - Type: str()
                                        - Valid values:
                                            - disable
                                            - enable
                                        - Example:
                                            task.capability_additional_paths_send = 'disable'

default_originate_route_map         Route-map to specify criteria for originating
                                    default::

                                        - Type: str()
                                        - Example:
                                            task.default_originate_route_map = 'DO_RM'

default_originate_set               Set default-originate attribute::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.allowas_in_set = True

disable_peer_as_check               Disable checking of peer AS-number while
                                    advertising::

                                        - Type: bool()
                                        - Valid values:
                                            - False
                                            - True
                                        - Example:
                                            task.disable_peer_as_check = True

filter_list_inbound                 Apply policy to incoming routes::

                                        - Type: str()
                                        - Example:
                                            task.filter_list_inbound = 'FL_IN'

filter_list_outbound                 Apply policy to outgoing routes::

                                        - Type: str()
                                        - Example:
                                            task.filter_list_inbound = 'FL_OUT'

inherit_sequence                    Sequence number::

                                        - Type: int()
                                        - Example:
                                            task.inherit_sequence = 10

inherit_template                    Template name::

                                        - Type: str()
                                        - Example:
                                            task.inherit_template = 'TOR_TEMPLATE'

=================================== ==============================================

|

============================================    =========================================
Property                                        Description
============================================    =========================================
maximum_prefix_generate_warning_threshold       Threshold percentage of 
                                                ``maximum_prefix_max_prefix_limit`` at
                                                which to generate a warning::

                                                    - Type: int()
                                                    - Valid values:
                                                        - range: 1-100
                                                    - Example:
                                                        task.maximum_prefix_generate_warning_threshold = 75

============================================    =========================================

====================================    =========================================
Property                                Description
====================================    =========================================
maximum_prefix_max_prefix_limit         Maximum prefix limit::

                                            - Type: int()
                                            - Valid values:
                                                - range: 1-4294967295
                                            - Example:
                                                task.maximum_prefix_max_prefix_limit = 12000

maximum_prefix_restart_interval         Restart bgp connection after limit is exceeded::

                                            - Type: int()
                                            - Units: minutes
                                            - Valid values:
                                                - range: 1-65535
                                            - Example:
                                                task.maximum_prefix_restart_interval = 5

maximum_prefix_warning_only             Only give a warning message when limit
                                        is exceeded::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.maximum_prefix_warning_only = True

next_hop_self_all_routes                Set our address as nexthop (non-reflected)
                                        for all routes::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.next_hop_self_all_routes = True

next_hop_self_set                       Set next-hop-self attribute::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.next_hop_self_set = True

next_hop_third_party                    Compute a third-party nexthop if possible::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.next_hop_third_party = True

prefix_list_inbound                     Apply policy to incoming routes via
                                        prefix-list::

                                            - Type: str()
                                            - Example:
                                                task.prefix_list_inbound = 'PL_IN'

prefix_list_outbound                    Apply policy to outgoing routes via::
                                        prefix-list::

                                            - Type: str()
                                            - Example:
                                                task.prefix_list_outbound = 'PL_OUT'

rewrite_evpn_rt_asn                     Auto generate RTs for EBGP neighbor::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.rewrite_evpn_rt_asn = False

route_map_inbound                       Apply policy to incoming routes via
                                        route-map::

                                            - Type: str()
                                            - Example:
                                                task.prefix_list_inbound = 'PL_IN'

route_map_outbound                      Apply policy to outgoing routes via
                                        route-map::

                                            - Type: str()
                                            - Example:
                                                task.prefix_list_outbound = 'PL_OUT'

route_reflector_client                  Configure a neighbor as Route reflector
                                        client::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.route_reflector_client = False

safi                                    Sub Address Family indicator::

                                            - Type: str()
                                            - Valid values:
                                                - evpn
                                                - multicast
                                                - mvpn
                                                - unicast
                                            - Required
                                            - Example:
                                                task.safi = 'unicast'

send_community_both                     Send Standard and Extended Community 
                                        attributes::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.send_community_both = False

send_community_extended                 Send only Extended Community attributes::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.send_community_extended = False

send_community_set                      Set send-community attribute::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.send_community_set = False

send_community_standard                 Send only Standard Community attributes::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.send_community_standard = False

soft_reconfiguration_inbound_always     Always perform inbound soft reconfiguration::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.soft_reconfiguration_inbound_always = True

soft_reconfiguration_inbound_set        Set soft-reconfiguration inbound attribute::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.soft_reconfiguration_inbound_set = True

soo                                     Site-of-origin extcommunity::

                                            - Type: str()
                                            - Valid values:
                                                - ASN2:NN
                                                - ASN4:NN
                                                - IPV4:NN
                                            - Examples:
                                                task.soo = '65000:40'
                                                task.soo = '1055423144:40`
                                                task.soo = '10.167.1.4:40`

suppress_inactive                       Advertise only active routes to peer::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.suppress_inactive = True

unsuppress_map                          Route-map to selectively unsuppress
                                        suppressed routes::

                                            - Type: str()
                                            - Example:
                                                task.unsuppress_map = 'US_RM'

weight                                  Set default weight for routes from this
                                        neighbor in this address-family::

                                            - Type: int()
                                            - Valid values:
                                                - range 0-65535
                                            - Example:
                                                task.weight = 1200

neighbor_address                        IP address/[prefixlen] of this neighbor::

                                            - Type: str()
                                            - Valid values:
                                                - ipv4 address without prefixlen
                                                - ipv4 address with prefixlen
                                                - ipv6 address without prefixlen
                                                - ipv6 address with prefixlen
                                            - Examples:
                                                task.neighbor_address = '1.2.3.4'
                                                task.neighbor_address = '1.2.3.0/24'
                                                task.neighbor_address = '2001:aaaa::1'
                                                task.neighbor_address = '2001:aaaa::0/126'


task_name                               Name of the task. Ansible will display this
                                        when the playbook is run::

                                            - Type: str()
                                            - Examples:
                                                - task.task_name = 'my task'

vrf                                     Name of VRF in which bgp neighbor resides::

                                            - Type: str()
                                            - Examples:
                                                - task.vrf = 'MY_VRF'

====================================    =========================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosBgpNeighborAddressFamily(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp_neighbor_address_family'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.address_family_list = list()
        self.bgp_neighbors_list = list()
        self.bgp_neighbors_list_vrf = list()
        self.vrf_list = list()

        # The set of ansible module properties that should be written
        # when the user calls instance.update().
        self.ansible_module_set = set()
        self.ansible_module_set.add('state')
        self.ansible_module_set.add('running_config')

        # Used in init_address_family() to clear all address
        # family properties
        self.address_family_set = set()
        self.address_family_set.add('advertise_map_exist_map')
        self.address_family_set.add('advertise_map_non_exist_map')
        self.address_family_set.add('advertise_map_route_map')
        self.address_family_set.add('advertisement_interval')
        self.address_family_set.add('afi')
        self.address_family_set.add('allowas_in_max_occurences')
        self.address_family_set.add('allowas_in_set')
        self.address_family_set.add('as_override')
        self.address_family_set.add('capability_additional_paths_receive')
        self.address_family_set.add('capability_additional_paths_send')
        self.address_family_set.add('default_originate_route_map')
        self.address_family_set.add('default_originate_set')
        self.address_family_set.add('disable_peer_as_check')
        self.address_family_set.add('filter_list_inbound')
        self.address_family_set.add('filter_list_outbound')
        self.address_family_set.add('inherit_sequence')
        self.address_family_set.add('inherit_template')
        self.address_family_set.add('maximum_prefix_generate_warning_threshold')
        self.address_family_set.add('maximum_prefix_max_prefix_limit')
        self.address_family_set.add('maximum_prefix_restart_interval')
        self.address_family_set.add('maximum_prefix_warning_only')
        self.address_family_set.add('next_hop_self_all_routes')
        self.address_family_set.add('next_hop_self_set')
        self.address_family_set.add('next_hop_third_party')
        self.address_family_set.add('prefix_list_inbound')
        self.address_family_set.add('prefix_list_outbound')
        self.address_family_set.add('rewrite_evpn_rt_asn')
        self.address_family_set.add('route_map_inbound')
        self.address_family_set.add('route_map_outbound')
        self.address_family_set.add('route_reflector_client')
        self.address_family_set.add('safi')
        self.address_family_set.add('send_community_both')
        self.address_family_set.add('send_community_extended')
        self.address_family_set.add('send_community_set')
        self.address_family_set.add('send_community_standard')
        self.address_family_set.add('soft_reconfiguration_inbound_always')
        self.address_family_set.add('soft_reconfiguration_inbound_set')
        self.address_family_set.add('soo')
        self.address_family_set.add('suppress_inactive')
        self.address_family_set.add('unsuppress_map')
        self.address_family_set.add('weight')

        # The set of atomic -- not members of a dict() -- 
        # properties.  Written when the user calls
        # instance.add_address_family().
        self.address_family_atomic_properties = set()
        self.address_family_atomic_properties.add('advertisement_interval')
        self.address_family_atomic_properties.add('afi')
        self.address_family_atomic_properties.add('as_override')
        self.address_family_atomic_properties.add('disable_peer_as_check')
        self.address_family_atomic_properties.add('next_hop_third_party')
        self.address_family_atomic_properties.add('rewrite_evpn_rt_asn')
        self.address_family_atomic_properties.add('route_reflector_client')
        self.address_family_atomic_properties.add('safi')
        self.address_family_atomic_properties.add('soo')
        self.address_family_atomic_properties.add('suppress_inactive')
        self.address_family_atomic_properties.add('unsuppress_map')
        self.address_family_atomic_properties.add('weight')

        # The set of atomic -- not members of a dict() -- 
        # bgp neighbor properties.
        # Written when the user calls instance.add_bgp_neighbor().
        # These will be written to the top-level of self.bgp_neighbor_dict
        # before it is appended to self.bgp_neighbors_list
        self.bgp_neighbor_atomic_properties = set()
        self.bgp_neighbor_atomic_properties.add('neighbor_address')

        # Used in init_bgp_neighbor()
        self.bgp_neighbor_set = set()
        self.bgp_neighbor_set.add('neighbor_address')

        # used to populate self.properties_set
        self.config_set = set()
        self.config_set.add('as_number')

        # The set of atomic -- not members of a dict() --
        # properties that should be written when 
        # the caller calls instance.update()
        self.config_atomic = set()
        self.config_atomic.add('as_number')

        # The set of atomic -- not members of a dict() -- 
        # vrf properties.
        # Written when the user calls instance.add_vrf().
        # These will be written to the top-level of self.config dict, 
        # after disambiguation, which is then appended to vrfs list()
        self.vrf_atomic_properties = set()
        self.vrf_atomic_properties.add('vrf')

        # Used in init_properties_vrf()
        self.vrf_set = set()
        self.vrf_set.add('vrf')

        # propery_map is used to convert the disambiguated property
        # names that users access, to the (potentially) ambiguous 
        # property names that nxos_bgp_neighbor_address_family uses.
        self.property_map = dict()
        self.property_map['as_number'] = 'as_number'
        self.property_map['advertise_map_exist_map'] = 'exist_map'
        self.property_map['advertise_map_non_exist_map'] = 'non_exist_map'
        self.property_map['advertise_map_route_map'] = 'route_map'
        self.property_map['advertisement_interval'] = 'advertisement_interval'
        self.property_map['afi'] = 'afi'
        self.property_map['allowas_in_max_occurences'] = 'max_occurences'
        self.property_map['allowas_in_set'] = 'set'
        self.property_map['as_override'] = 'as_override'
        self.property_map['capability_additional_paths_receive'] = 'receive'
        self.property_map['capability_additional_paths_send'] = 'send'
        self.property_map['default_originate_route_map'] = 'route_map'
        self.property_map['default_originate_set'] = 'set'
        self.property_map['disable_peer_as_check'] = 'disable_peer_as_check'
        self.property_map['filter_list_inbound'] = 'inbound'
        self.property_map['filter_list_outbound'] = 'outbound'
        self.property_map['inherit_sequence'] = 'sequence'
        self.property_map['inherit_template'] = 'template'
        self.property_map['maximum_prefix_generate_warning_threshold'] = 'generate_warning_threshold'
        self.property_map['maximum_prefix_max_prefix_limit'] = 'max_prefix_limit'
        self.property_map['maximum_prefix_restart_interval'] = 'restart_interval'
        self.property_map['maximum_prefix_warning_only'] = 'warning_only'
        self.property_map['neighbor_address'] = 'neighbor_address'
        self.property_map['next_hop_self_all_routes'] = 'all_routes'
        self.property_map['next_hop_self_set'] = 'set'
        self.property_map['next_hop_third_party'] = 'next_hop_third_party'
        self.property_map['prefix_list_inbound'] = 'inbound'
        self.property_map['prefix_list_outbound'] = 'outbound'
        self.property_map['rewrite_evpn_rt_asn'] = 'rewrite_evpn_rt_asn'
        self.property_map['route_map_inbound'] = 'inbound'
        self.property_map['route_map_outbound'] = 'outbound'
        self.property_map['route_reflector_client'] = 'route_reflector_client'
        self.property_map['safi'] = 'safi'
        self.property_map['send_community_both'] = 'both'
        self.property_map['send_community_extended'] = 'extended'
        self.property_map['send_community_set'] = 'set'
        self.property_map['send_community_standard'] = 'standard'
        self.property_map['soft_reconfiguration_inbound_always'] = 'always'
        self.property_map['soft_reconfiguration_inbound_set'] = 'set'
        self.property_map['soo'] = 'soo'
        self.property_map['suppress_inactive'] = 'suppress_inactive'
        self.property_map['unsuppress_map'] = 'unsuppress_map'
        self.property_map['weight'] = 'weight'
        self.property_map['vrf'] = 'vrf'

        self.valid_afi = set()
        self.valid_afi.add('ipv4')
        self.valid_afi.add('ipv6')
        self.valid_afi.add('l2vpn')
        self.valid_afi.add('link-state')
        self.valid_afi.add('vpnv4')
        self.valid_afi.add('vpnv6')

        self.valid_capability_additional_paths_receive = set()
        self.valid_capability_additional_paths_receive.add('disable')
        self.valid_capability_additional_paths_receive.add('enable')

        self.valid_capability_additional_paths_send = set()
        self.valid_capability_additional_paths_send.add('disable')
        self.valid_capability_additional_paths_send.add('enable')

        self.valid_safi = set()
        self.valid_safi.add('evpn')
        self.valid_safi.add('multicast')
        self.valid_safi.add('mvpn')
        self.valid_safi.add('unicast')

        self.valid_state = set()
        self.valid_state.add('deleted')
        self.valid_state.add('gathered')
        self.valid_state.add('merged')
        self.valid_state.add('overridden')
        self.valid_state.add('parsed')
        self.valid_state.add('rendered')
        self.valid_state.add('replaced')

        # properties_set is the full set of disambiguated property
        # names found in nxos_bgp_neighbor_address_family module.  This includes all
        # global, neighbor, vrf, and ansible properties.
        self.properties_set = set()
        self.properties_set.update(self.ansible_module_set)
        self.properties_set.update(self.config_set)
        self.properties_set.update(self.address_family_set)
        self.properties_set.update(self.bgp_neighbor_set)
        self.properties_set.update(self.vrf_set)

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.advertisement_interval_min = 1
        self.advertisement_interval_max = 1

        self.allowas_in_max_occurences_min = 1
        self.allowas_in_max_occurences_max = 10

        self.maximum_prefix_generate_warning_threshold_min = 1
        self.maximum_prefix_generate_warning_threshold_max = 100

        self.maximum_prefix_max_prefix_limit_min = 1
        self.maximum_prefix_max_prefix_limit_max = 4294967295

        self.maximum_prefix_restart_interval_min = 1
        self.maximum_prefix_restart_interval_max = 65535

        self.weight_min = 1
        self.weight_max = 65535

        # Keyed on feature, value is a pointer to the verification
        # method for the feature
        self.verification_dispatch_table = dict()
        self.verification_dispatch_table['maximum_prefix'] = self.verify_maximum_prefix

        self.address_family_property_groups = set()
        self.address_family_property_groups.add('advertise_map')
        self.address_family_property_groups.add('allowas_in')
        self.address_family_property_groups.add('default_originate')
        self.address_family_property_groups.add('filter_list')
        self.address_family_property_groups.add('inherit')
        self.address_family_property_groups.add('maximum_prefix')
        self.address_family_property_groups.add('next_hop_self')
        self.address_family_property_groups.add('prefix_list')
        self.address_family_property_groups.add('route_map')
        self.address_family_property_groups.add('send_community')
        self.address_family_property_groups.add('soft_reconfiguration_inbound')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        self.address_family = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def init_address_family(self):
        self.address_family = dict()
        for p in self.address_family_set:
            self.properties[p] = None

    def init_bgp_neighbor(self):
        self.address_family_list = list()
        for p in self.bgp_neighbor_set:
            self.properties[p] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.as_number == None:
            self.task_log.error('exiting. call instance.as_number before calling instance.update()')
            exit(1)

    def update_config_atomic(self):
        '''
        Update all atomic (not member of a dictionary) properties at
        the top-level of self.config
        '''
        for p in self.config_atomic:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                self.config[mapped_p] = self.properties[p]

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        self.config = dict()

        self.update_config_atomic()
        if len(self.bgp_neighbors_list) != 0:
            self.config['neighbors'] = deepcopy(self.bgp_neighbors_list)
        if len(self.vrf_list) != 0:
            self.config['vrfs'] = deepcopy(self.vrf_list)
        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['config'] = deepcopy(self.config)
        self.ansible_task[self.ansible_module]['state'] = self.state

    def update_address_family_atomic(self):
        '''
        Update all atomic (not member of a dictionary) address-family
        properties
        '''
        for p in self.address_family_atomic_properties:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                self.address_family_dict[mapped_p] = self.properties[p]

    def update_address_family_capability(self):
        d = dict()
        additional_paths = dict()
        for p in self.address_family_set:
            if not p.startswith('capability_'):
                continue
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                additional_paths[mapped_p] = self.properties[p]
        if len(additional_paths) != 0:
            d['additional_paths'] = deepcopy(additional_paths)
        if len(d) != 0:
            self.address_family_dict['capability'] = deepcopy(d)

    def verify_maximum_prefix(self):
        if self.maximum_prefix_max_prefix_limit == None:
            if self.maximum_prefix_generate_warning_threshold != None:
                self.task_log.error('exiting. maximum_prefix_max_prefix_limit must be set if maximum_prefix_generate_warning_threshold is set.')
                exit(1)
            if self.maximum_prefix_restart_interval != None:
                self.task_log.error('exiting. maximum_prefix_max_prefix_limit must be set if maximum_prefix_restart_interval is set.')
                exit(1)
            if self.maximum_prefix_warning_only != None:
                self.task_log.error('exiting. maximum_prefix_max_prefix_limit must be set if maximum_prefix_warning_only is set.')
            exit(1)

    def update_property_group(self, item):
        '''
        update address family properties whose structure is
        a single-level dictionary
        '''
        d = dict()
        for p in self.address_family_set:
            if not p.startswith(item):
                continue
            if item in self.verification_dispatch_table:
                self.verification_dispatch_table[item]()
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        if len(d) != 0:
            self.address_family_dict[item] = deepcopy(d)

    def verify_address_family(self):
        if self.afi == None:
            self.task_log.error('exiting. afi is a mandatory property but is not set.')
            exit(1)
        if self.safi == None:
            self.task_log.error('exiting. safi is a mandatory property but is not set.')
            exit(1)
    def add_address_family(self):
        '''
        Add an address-family to self.address_family_list

        Example: Add ipv4 unicast and evpn l2vpn address-families
        to a bgp neighbor

        instance.afi = 'ipv4'
        instance.safi = 'unicast'
        instance.next_hop_self = True
        instance.add_address_family()

        instance.afi = 'l2vpn'
        instance.safi = 'evpn'
        instance.add_address_family()

        instance.neighbor_address = '10.254.1.1'
        instance.as_number = 65001
        instance.add_bgp_neighbor()

        '''
        self.verify_address_family()
        self.address_family_dict = dict()
        self.update_address_family_atomic()
        self.update_address_family_capability()
        for pg in self.address_family_property_groups:
            self.update_property_group(pg)
        if len(self.address_family_dict) == 0:
            self.task_log.error('exiting. One or more address-family properties must be set before calling add_address_family()')
            exit(1)
        self.address_family_list.append(deepcopy(self.address_family_dict))
        self.init_address_family()

    def verify_bgp_neighbor(self):
        if self.properties['neighbor_address'] == None:
            self.task_log.error('exiting. Set neighbor_address before calling instance.add_bgp_neighbor()')
            exit(1)
        if len(self.address_family_list) == 0:
            self.task_log.error('exiting. call instance.add_address_family() at least once before calling instance.add_bgp_neighbor()')
            exit(1)

    def add_bgp_neighbor(self):
        '''
        Add a BGP neighbor to self.bgp_neighbors_list

        Example:

        instance.neighbor_address = '1.1.1.1'
        instance.add_bgp_neighbor()
        '''
        self.verify_bgp_neighbor()
        d = dict()
        d['neighbor_address'] = self.neighbor_address
        d['address_family'] = deepcopy(self.address_family_list)
        self.bgp_neighbors_list.append(deepcopy(d))
        self.init_bgp_neighbor()

    def add_vrf_bgp_neighbor(self):
        '''
        Add a BGP neighbor to self.bgp_neighbors_list_vrf

        Example:

        instance.afi = 'ipv4'
        instance.safi = 'unicast'
        instance.add_address_family()
        instance.neighbor_address = '1.1.1.1'
        instance.add_vrf_bgp_neighbor()
        instance.vrf = 'FOO'
        instance.add_vrf()
        '''
        self.verify_bgp_neighbor()
        d = dict()
        d['neighbor_address'] = self.neighbor_address
        d['address_family'] = deepcopy(self.address_family_list)
        self.bgp_neighbors_list_vrf.append(deepcopy(d))
        self.init_bgp_neighbor()

    def init_properties_vrf(self):
        for p in self.vrf_set:
            self.properties[p] = None
    def final_verification_vrf(self):
        if self.vrf == None:
            self.task_log.error('exiting. instance.vrf must be set before calling instance.add_vrf()')
            exit(1)
        if len(self.bgp_neighbors_list_vrf) == 0:
            self.task_log.error('exiting. call instance.add_vrf_bgp_neighbor() at least once before calling instance.add_vrf()')
            exit(1)
    def add_vrf(self):
        '''
        add all configured properties to self.vrf_list
        '''
        self.final_verification_vrf()
        d = dict()
        d['vrf'] = self.vrf
        d['neighbors'] = deepcopy(self.bgp_neighbors_list_vrf)
        self.bgp_neighbors_list_vrf = list()
        self.vrf_list.append(deepcopy(d))
        self.init_properties_vrf()

    def verify_advertisement_interval(self, x, parameter='advertisement_interval'):
        source_class = self.class_name
        range_min = self.advertisement_interval_min
        range_max = self.advertisement_interval_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_afi(self, x, parameter='afi'):
        verify_set = self.valid_afi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_afi'
        expectation = ','.join(sorted([str(x) for x in verify_set]))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_allowas_in_max_occurences(self, x, parameter='allowas_in_max_occurences'):
        source_class = self.class_name
        range_min = self.allowas_in_max_occurences_min
        range_max = self.allowas_in_max_occurences_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_capability_additional_paths_receive(self, x, parameter='capability_additional_paths_receive'):
        verify_set = self.valid_capability_additional_paths_receive
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_capability_additional_paths_receive'
        expectation = ','.join(sorted([str(x) for x in verify_set]))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_capability_additional_paths_send(self, x, parameter='capability_additional_paths_send'):
        verify_set = self.valid_capability_additional_paths_send
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_capability_additional_paths_send'
        expectation = ','.join(sorted([str(x) for x in verify_set]))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_inherit_sequence(self, x, parameter):
        if self.isdigits(x):
            return
        source_class = self.class_name
        source_method = 'verify_inherit_sequence'
        expectation = 'int()'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_maximum_prefix_generate_warning_threshold(self, x, parameter='maximum_prefix_generate_warning_threshold'):
        source_class = self.class_name
        range_min = self.maximum_prefix_generate_warning_threshold_min
        range_max = self.maximum_prefix_generate_warning_threshold_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_maximum_prefix_max_prefix_limit(self, x, parameter='maximum_prefix_max_prefix_limit'):
        source_class = self.class_name
        range_min = self.maximum_prefix_max_prefix_limit_min
        range_max = self.maximum_prefix_max_prefix_limit_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_maximum_prefix_restart_interval(self, x, parameter='maximum_prefix_restart_interval'):
        source_class = self.class_name
        range_min = self.maximum_prefix_restart_interval_min
        range_max = self.maximum_prefix_restart_interval_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    def verify_neighbor_address(self, x, parameter='neighbor_address'):
        if self.is_ipv4_address(x):
            return
        if self.is_ipv6_address(x):
            return
        if self.is_ipv4_address_with_prefix(x):
            return
        if self.is_ipv6_address_with_prefix(x):
            return
        source_class = self.class_name
        source_method = 'verify_neighbor_address'
        expectation = '[ipv4/ipv6 address with or without prefixlen]'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_safi(self, x, parameter='safi'):
        verify_set = self.valid_safi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_safi'
        expectation = ','.join(sorted([str(x) for x in verify_set]))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_state(self, x, parameter='state'):
        verify_set = self.valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_weight(self, x, parameter='weight'):
        source_class = self.class_name
        range_min = self.weight_min
        range_max = self.weight_max
        self.verify_integer_range(x, range_min, range_max, self.class_name, parameter)

    @property
    def advertise_map_exist_map(self):
        return self.properties['advertise_map_exist_map']
    @advertise_map_exist_map.setter
    def advertise_map_exist_map(self, x):
        parameter = 'advertise_map_exist_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def advertise_map_non_exist_map(self):
        return self.properties['advertise_map_non_exist_map']
    @advertise_map_non_exist_map.setter
    def advertise_map_non_exist_map(self, x):
        parameter = 'advertise_map_non_exist_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def advertise_map_route_map(self):
        return self.properties['advertise_map_route_map']
    @advertise_map_route_map.setter
    def advertise_map_route_map(self, x):
        parameter = 'advertise_map_route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def advertisement_interval(self):
        return self.properties['advertisement_interval']
    @advertisement_interval.setter
    def advertisement_interval(self, x):
        parameter = 'advertisement_interval'
        if self.set_none(x, parameter):
            return
        self.verify_advertisement_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.verify_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def allowas_in_max_occurences(self):
        return self.properties['allowas_in_max_occurences']
    @allowas_in_max_occurences.setter
    def allowas_in_max_occurences(self, x):
        parameter = 'allowas_in_max_occurences'
        if self.set_none(x, parameter):
            return
        self.verify_allowas_in_max_occurences(x, parameter)
        self.properties[parameter] = x

    @property
    def allowas_in_set(self):
        return self.properties['allowas_in_set']
    @allowas_in_set.setter
    def allowas_in_set(self, x):
        parameter = 'allowas_in_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
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
    def as_number(self):
        return self.properties['as_number']
    @as_number.setter
    def as_number(self, x):
        parameter = 'as_number'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def capability_additional_paths_receive(self):
        return self.properties['capability_additional_paths_receive']
    @capability_additional_paths_receive.setter
    def capability_additional_paths_receive(self, x):
        parameter = 'capability_additional_paths_receive'
        if self.set_none(x, parameter):
            return
        self.verify_capability_additional_paths_receive(x, parameter)
        self.properties[parameter] = x

    @property
    def capability_additional_paths_send(self):
        return self.properties['capability_additional_paths_send']
    @capability_additional_paths_send.setter
    def capability_additional_paths_send(self, x):
        parameter = 'capability_additional_paths_send'
        if self.set_none(x, parameter):
            return
        self.verify_capability_additional_paths_send(x, parameter)
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
    def default_originate_set(self):
        return self.properties['default_originate_set']
    @default_originate_set.setter
    def default_originate_set(self, x):
        parameter = 'default_originate_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
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
    def filter_list_inbound(self):
        return self.properties['filter_list_inbound']
    @filter_list_inbound.setter
    def filter_list_inbound(self, x):
        parameter = 'filter_list_inbound'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def filter_list_outbound(self):
        return self.properties['filter_list_outbound']
    @filter_list_outbound.setter
    def filter_list_outbound(self, x):
        parameter = 'filter_list_outbound'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def inherit_sequence(self):
        return self.properties['inherit_sequence']
    @inherit_sequence.setter
    def inherit_sequence(self, x):
        parameter = 'inherit_sequence'
        if self.set_none(x, parameter):
            return
        self.verify_inherit_sequence(x, parameter)
        self.properties[parameter] = x

    @property
    def inherit_template(self):
        return self.properties['inherit_template']
    @inherit_template.setter
    def inherit_template(self, x):
        parameter = 'inherit_template'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def maximum_prefix_generate_warning_threshold(self):
        return self.properties['maximum_prefix_generate_warning_threshold']
    @maximum_prefix_generate_warning_threshold.setter
    def maximum_prefix_generate_warning_threshold(self, x):
        parameter = 'maximum_prefix_generate_warning_threshold'
        if self.set_none(x, parameter):
            return
        self.verify_maximum_prefix_generate_warning_threshold(x, parameter)
        self.properties[parameter] = x

    @property
    def maximum_prefix_max_prefix_limit(self):
        return self.properties['maximum_prefix_max_prefix_limit']
    @maximum_prefix_max_prefix_limit.setter
    def maximum_prefix_max_prefix_limit(self, x):
        parameter = 'maximum_prefix_max_prefix_limit'
        if self.set_none(x, parameter):
            return
        self.verify_maximum_prefix_max_prefix_limit(x, parameter)
        self.properties[parameter] = x

    @property
    def maximum_prefix_restart_interval(self):
        return self.properties['maximum_prefix_restart_interval']
    @maximum_prefix_restart_interval.setter
    def maximum_prefix_restart_interval(self, x):
        parameter = 'maximum_prefix_restart_interval'
        if self.set_none(x, parameter):
            return
        self.verify_maximum_prefix_restart_interval(x, parameter)
        self.properties[parameter] = x

    @property
    def maximum_prefix_warning_only(self):
        return self.properties['maximum_prefix_warning_only']
    @maximum_prefix_warning_only.setter
    def maximum_prefix_warning_only(self, x):
        parameter = 'maximum_prefix_warning_only'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor_address(self):
        return self.properties['neighbor_address']
    @neighbor_address.setter
    def neighbor_address(self, x):
        parameter = 'neighbor_address'
        if self.set_none(x, parameter):
            return
        self.verify_neighbor_address(x, parameter)
        self.properties[parameter] = x

    @property
    def next_hop_self_all_routes(self):
        return self.properties['next_hop_self_all_routes']
    @next_hop_self_all_routes.setter
    def next_hop_self_all_routes(self, x):
        parameter = 'next_hop_self_all_routes'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def next_hop_self_set(self):
        return self.properties['next_hop_self_set']
    @next_hop_self_set.setter
    def next_hop_self_set(self, x):
        parameter = 'next_hop_self_set'
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
    def prefix_list_inbound(self):
        return self.properties['prefix_list_inbound']
    @prefix_list_inbound.setter
    def prefix_list_inbound(self, x):
        parameter = 'prefix_list_inbound'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def prefix_list_outbound(self):
        return self.properties['prefix_list_outbound']
    @prefix_list_outbound.setter
    def prefix_list_outbound(self, x):
        parameter = 'prefix_list_outbound'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def rewrite_evpn_rt_asn(self):
        return self.properties['rewrite_evpn_rt_asn']
    @rewrite_evpn_rt_asn.setter
    def rewrite_evpn_rt_asn(self, x):
        parameter = 'rewrite_evpn_rt_asn'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def route_map_inbound(self):
        return self.properties['route_map_inbound']
    @route_map_inbound.setter
    def route_map_inbound(self, x):
        parameter = 'route_map_inbound'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def route_map_outbound(self):
        return self.properties['route_map_outbound']
    @route_map_outbound.setter
    def route_map_outbound(self, x):
        parameter = 'route_map_outbound'
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
        self.verify_safi(x, parameter)
        self.properties[parameter] = x

    @property
    def send_community_both(self):
        return self.properties['send_community_both']
    @send_community_both.setter
    def send_community_both(self, x):
        parameter = 'send_community_both'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def send_community_extended(self):
        return self.properties['send_community_extended']
    @send_community_extended.setter
    def send_community_extended(self, x):
        parameter = 'send_community_extended'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def send_community_set(self):
        return self.properties['send_community_set']
    @send_community_set.setter
    def send_community_set(self, x):
        parameter = 'send_community_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def send_community_standard(self):
        return self.properties['send_community_standard']
    @send_community_standard.setter
    def send_community_standard(self, x):
        parameter = 'send_community_standard'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def soft_reconfiguration_inbound_always(self):
        return self.properties['soft_reconfiguration_inbound_always']
    @soft_reconfiguration_inbound_always.setter
    def soft_reconfiguration_inbound_always(self, x):
        parameter = 'soft_reconfiguration_inbound_always'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def soft_reconfiguration_inbound_set(self):
        return self.properties['soft_reconfiguration_inbound_set']
    @soft_reconfiguration_inbound_set.setter
    def soft_reconfiguration_inbound_set(self, x):
        parameter = 'soft_reconfiguration_inbound_set'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def soo(self):
        return self.properties['soo']
    @soo.setter
    def soo(self, x):
        parameter = 'soo'
        if self.set_none(x, parameter):
            return
        self.verify_bgp_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_state(x, parameter)
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
        self.verify_weight(x, parameter)
        self.properties[parameter] = x
