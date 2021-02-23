# NxosBgpNeighbor() - cisco/nxos/nxos_bgp_neighbor.py
our_version = 112
# Deprecation: Ansible module nxos_bgp_neighbor is DEPRECATED
# Deprecated on: 2021.01.27
# Removed after: 2023-01-27
# Alternative: nxos_bgp_global - cisco/nxos/nxos_bgp_global.py
#
import re
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosBgpNeighbor()
**************************************

.. contents::
   :local:
   :depth: 1

Deprecation
-----------

- Status: ``DEPRECATED``
- Alternative: `nxos_bgp_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_global_module.rst>`_
- 2021-01-27, deprecation date
- 2023-01-27, removal date (module may be removed after this date)

ScriptKit Synopsis
------------------
- NxosBgpNeighbor() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bgp_neighbor
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bgp_neighbor <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bgp_neighbor_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor.py>`_

TODO
----
20210223: if local_as is set, verify that asn and remote_as are different (i.e. eBGP with neighbor)

|

=============================   ==============================================
Property                        Description
=============================   ==============================================
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

bfd                             Enables/Disables BFD for the neighbor::

                                    - Type: str()
                                    - Valid values:
                                        - enable
                                        - disable
                                    - Example:
                                        task.bfd = 'enable'
                                    - NOTES:
                                        - 'feature bfd' must be enabled on the remote device

capability_negotiation          Negotiate capability with this neighbor::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.capability_negotiation = True

connected_check                 Check ``True`` or don't check ``False`` if this neighbor is
                                directy-connected when deciding to peer with it.  By default,
                                eBGP peers will not peer with a neighbor whose address is not
                                within the range of the peering interface unless ebgp-multihop
                                is configured.  Use ``connected_check`` to override this behavior
                                (e.g. when directly-connected routers are eBGP peering via
                                their Loopback interfaces)::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.connected_check = False

description                     Description of the neighbor::

                                    - Type: str()
                                    - Example:
                                        task.description = 'TOR peer'

dynamic_capability              Enable ``True`` or disable ``False`` dynamic capability::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.dynamic_capability = False

ebgp_multihop                   Specify multihop TTL for this eBGP neighbor. The value
                                represents the TTL to include in control-plane packets
                                sent to this eBGP neighbor.  Use this property when two
                                eBGP neighbors are separated by one or more transit routers
                                (since each transit router decrements the TTL).  Set the
                                value high enough that the TTL is not decremented to zero
                                before reaching the eBGP peer::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range: 2-255
                                        - str() Keyword: 'default' (disables ebgp multihop)
                                    - Examples:
                                        task.ebgp_multihop = 5
                                        task.ebgp_multihop = 'default'

local_as                        Specify the local-as number for the eBGP peer in
                                ``ASPLAIN`` or ``ASDOT`` notation.  Allows the router
                                to peer with the eBGP neighbor using an AS that differs
                                from that configured using the ``asn`` property::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-4294967295
                                        - <1-65535>.<0-65535>
                                        - str() Keyword: default (remove local_as config)
                                    - Examples:
                                        task.local_as = 64512
                                        task.local_as = 4200000000
                                        task.local_as = '2301.0'
                                        task.local_as = 'default'
                                    - NOTES:
                                        - Use only with eBGP peers
                                        - Cannot be used in quasi-eBGP scenarios, e.g.
                                            - Members of different confed sub-ASs

log_neighbor_changes            Specify whether or not to enable log messages
                                for neighbor up/down events::

                                    - Type: str()
                                    - Valid values:
                                        - enable
                                        - disable
                                        - inherit
                                            Remove log_neighbor_changes config
                                            from this neighbor config, and use
                                            the value, if one exists, from an
                                            applied peer-template.
                                    - Example:
                                        task.log_neighbor_changes = 'disable'

low_memory_exempt               Specify whether or not to shut down this neighbor
                                under memory pressure::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.low_memory_exempt = True

maximum_peers                   Maximum number of peers for this neighbor prefix::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range: 1-1000
                                        - str() Keyword: default (no peer limit)
                                    - Examples:
                                        - task.maximum_peers = 20
                                        - task.maximum_peers = 'default'
                                    NOTES:
                                        -   maximum_peers is accepted only 
                                            on neighbors with address/prefix

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

peer_type                       Specify the peer type for BGP session::

                                    - Type: str()
                                    - Valid values:
                                        - fabric_border_leaf
                                        - fabric_external
                                        - disable
                                    - Example:
                                        task.peer_type = 'fabric_external'

pwd                             Password for this BGP peer::

                                    - Type: str()
                                    - Example:
                                        task.pwd = 'hackersnotwelcome'

pwd_type                        Specify the encryption type the password will use::

                                    - Type: str()
                                    - Valid values:
                                        - 3des
                                        - cisco_type_7
                                        - default

remote_as                       The remote AS number for the BGP peer in
                                ``ASPLAIN`` or ``ASDOT`` notation::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range 1-4294967295
                                        - <1-65535>.<0-65535>
                                        - str() Keyword: default (remove remote_as config)
                                    - Examples:
                                        task.remote_as = 64512
                                        task.remote_as = 4200000000
                                        task.remote_as = '2301.0'
                                        task.remote_as = 'default'
                                    - NOTES:
                                        - private asn ranges
                                            - 64512 to 65534
                                            - 4200000000 to 4294967294

remove_private_as               Remove private AS number from outbound updates::

                                    - Type: str()
                                    - Valid values:
                                        - all         Remove all private AS numbers
                                        - disable     Do not remove private AS numbers
                                        - enable      Remove private AS numbers that appear
                                                      after the confederation portion of the
                                                      AS path
                                        - replace-as  Replace private AS numbers with our AS
                                    - Example:
                                        task.remove_private_as = 'all'

shutdown                        Administratively shutdown this neighbor::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.shutdown = False

state                           Determines whether the config should be present or
                                not on the device::

                                    - Type: str()
                                    - Valid values:
                                        - absent
                                        - present
                                    - Example:
                                        task.state = 'present'

suppress_4_byte_as              If ``neighbor`` is not capable of 4-byte AS,
                                capability negotiation with ``neighbor`` will
                                fail and the session will not come up.  Use
                                the ``suppress_4_byte_as`` property to suppress
                                sending 4-byte AS capability during initial capability
                                negotiation with ``neighbor``::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.suppress_4_byte_as = False

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Examples:
                                        - task.task_name = 'my task'

timers_holdtime                 Specify holdtime timer value::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range: 0-3600 seconds
                                        - str() Keyword: default
                                                - configure holdtime to 180 seconds

timers_keepalive                Specify keepalive timer value::

                                    - Type: int() or str()
                                    - Valid values:
                                        - int() range: 0-3600 seconds
                                        - str() Keyword: default
                                                - configure keepalive to 60 seconds

transport_passive_only          Allow passive connection establishment::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Example:
                                        task.transport_passive_only = False
                                    - NOTES:
                                        - Do not use for prefix-peering i.e.
                                          when the peer IP address includes
                                          a prefixlen e.g. 10.1.1.0/24

update_source                   Source interface of BGP session and updates::

                                    - Type: str()
                                    - Valid values:
                                        - Full interface name
                                    - Examples:
                                        task.update_source = 'Ethernet1/1'
                                        task.update_source = 'Loopback0'
                                        task.update_source = 'port-channel20'
                                        task.update_source = 'Vlan10'

=============================   ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosBgpNeighbor(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bgp_neighbor'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.task_log.warning('*******************************************************************************************')
        self.task_log.warning('NxosBgpNeighbor is DEPRECATED as its Ansible module nxos_bgp_neighbor is DEPRECATED.')
        self.task_log.warning('Use NxosBgpGlobal() (nxos_bgp_global) instead.')
        self.task_log.warning('*******************************************************************************************')
        self.init_properties()

        self.nxos_bgp_neighbor_valid_log_neighbor_changes = set()
        self.nxos_bgp_neighbor_valid_log_neighbor_changes.add('enable')
        self.nxos_bgp_neighbor_valid_log_neighbor_changes.add('disable')
        self.nxos_bgp_neighbor_valid_log_neighbor_changes.add('disable')

        self.nxos_bgp_neighbor_valid_peer_type = set()
        self.nxos_bgp_neighbor_valid_peer_type.add('fabric_border_leaf')
        self.nxos_bgp_neighbor_valid_peer_type.add('fabric_external')
        self.nxos_bgp_neighbor_valid_peer_type.add('disable')

        self.nxos_bgp_neighbor_valid_pwd_type = set()
        self.nxos_bgp_neighbor_valid_pwd_type.add('3des')
        self.nxos_bgp_neighbor_valid_pwd_type.add('cisco_type_7')
        self.nxos_bgp_neighbor_valid_pwd_type.add('default')

        self.nxos_bgp_neighbor_valid_remove_private_as = set()
        self.nxos_bgp_neighbor_valid_remove_private_as.add('enable')
        self.nxos_bgp_neighbor_valid_remove_private_as.add('disable')
        self.nxos_bgp_neighbor_valid_remove_private_as.add('all')
        self.nxos_bgp_neighbor_valid_remove_private_as.add('replace-as')

        self.nxos_bgp_neighbor_valid_state = set()
        self.nxos_bgp_neighbor_valid_state.add('absent')
        self.nxos_bgp_neighbor_valid_state.add('present')

        self.nxos_bgp_neighbor_maximum_peers_min = 1
        self.nxos_bgp_neighbor_maximum_peers_max = 1000

        self.properties_set = set()
        self.properties_set.add('asn')
        self.properties_set.add('bfd')
        self.properties_set.add('capability_negotiation')
        self.properties_set.add('connected_check')
        self.properties_set.add('description')
        self.properties_set.add('dynamic_capability')
        self.properties_set.add('ebgp_multihop')
        self.properties_set.add('local_as')
        self.properties_set.add('log_neighbor_changes')
        self.properties_set.add('low_memory_exempt')
        self.properties_set.add('maximum_peers')
        self.properties_set.add('neighbor')
        self.properties_set.add('peer_type')
        self.properties_set.add('pwd')
        self.properties_set.add('pwd_type')
        self.properties_set.add('remote_as')
        self.properties_set.add('remove_private_as')
        self.properties_set.add('shutdown')
        self.properties_set.add('state')
        self.properties_set.add('suppress_4_byte_as')
        self.properties_set.add('timers_holdtime')
        self.properties_set.add('timers_keepalive')
        self.properties_set.add('transport_passive_only')
        self.properties_set.add('update_source')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification_nxos_bgp_neighbor_maximum_peers(self):
        '''
        maximum_peers is valid only with prefix-peering
        '''
        if self.maximum_peers == None:
            return
        if self.is_ipv4_address_with_prefix(self.neighbor):
            return
        if self.is_ipv6_address_with_prefix(self.neighbor):
            return
        self.task_log.error('exiting. maximum_peers is used only when neighbor is a prefix-peer')
        self.task_log.error('maximum_peers: {}'.format(self.maximum_peers))
        self.task_log.error('neighbor: {}'.format(self.neighbor))
        self.task_log.error('Either specify neighbor as a prefix-peer e.g. 10.1.1.0/24, 2001:aaaa::/120, or unset maximum_peers')
        exit(1)

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.asn == None:
            self.task_log.error('exiting. call instance.asn before calling instance.update()')
            exit(1)
        if self.neighbor == None:
            self.task_log.error('exiting. call instance.neighbor before calling instance.update()')
            exit(1)
        self.final_verification_nxos_bgp_neighbor_maximum_peers()

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

    def verify_nxos_bgp_neighbor_asn(self, x, parameter=''):
        if self.is_bgp_asn(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_asn'
        expectation = 'digits, digits.digits'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_ebgp_multihop(self, x, parameter='ebgp_multihop'):
        if self.is_default(x):
            return
        if x in list(range(2,256)):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_ebgp_multihop'
        expectation = 'int() range 2-255, str() keyword: default'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_neighbor(self, x, parameter='neighbor'):
        if self.is_ipv4_address(x):
            return
        if self.is_ipv6_address(x):
            return
        if self.is_ipv4_network(x):
            return
        if self.is_ipv6_network(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_neighbor'
        expectation = 'ipv4 address, ipv6 address, ipv4 address with prefixlen, ipv6 address with prefixlen'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_local_as(self, x, parameter='local_as'):
        if self.is_default(x):
            return
        if self.is_bgp_asn(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_local_as'
        expectation = 'digits, digits.digits, keyword: default'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_maximum_peers(self, x, parameter='maximum_peers'):
        source_class = self.class_name
        range_min = self.nxos_bgp_neighbor_maximum_peers_min
        range_max = self.nxos_bgp_neighbor_maximum_peers_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_bgp_neighbor_peer_type(self, x, parameter='peer_type'):
        verify_set = self.nxos_bgp_neighbor_valid_peer_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_pwd_type(self, x, parameter='unspecified'):
        verify_set = self.nxos_bgp_neighbor_valid_pwd_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_pwd_type'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_remove_private_as(self, x, parameter=''):
        verify_set = self.nxos_bgp_neighbor_valid_remove_private_as
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_remove_private_as'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_state(self, x, parameter='state'):
        verify_set = self.nxos_bgp_neighbor_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bgp_neighbor_timers(self, x, parameter='timers'):
        '''
        verify timers_holdtime and timers_keepalive are between 0-3600 or == 'default'
        '''
        if self.is_default(x):
            return
        if x in list(range(0,3601)):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bgp_neighbor_timers'
        expectation = '[2-255, "default"]'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def asn(self):
        return self.properties['asn']
    @asn.setter
    def asn(self, x):
        parameter = 'asn'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def bfd(self):
        return self.properties['bfd']
    @bfd.setter
    def bfd(self, x):
        parameter = 'bfd'
        if self.set_none(x, parameter):
            return
        self.verify_enable_disable(x, parameter)
        self.properties[parameter] = x

    @property
    def capability_negotiation(self):
        return self.properties['capability_negotiation']
    @capability_negotiation.setter
    def capability_negotiation(self, x):
        parameter = 'capability_negotiation'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def connected_check(self):
        return self.properties['connected_check']
    @connected_check.setter
    def connected_check(self, x):
        parameter = 'connected_check'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

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
    def dynamic_capability(self):
        return self.properties['dynamic_capability']
    @dynamic_capability.setter
    def dynamic_capability(self, x):
        parameter = 'dynamic_capability'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def ebgp_multihop(self):
        return self.properties['ebgp_multihop']
    @ebgp_multihop.setter
    def ebgp_multihop(self, x):
        parameter = 'ebgp_multihop'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_ebgp_multihop(x, parameter)
        self.properties[parameter] = x

    @property
    def local_as(self):
        return self.properties['local_as']
    @local_as.setter
    def local_as(self, x):
        parameter = 'local_as'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_local_as(x, parameter)
        self.properties[parameter] = x

    @property
    def log_neighbor_changes(self):
        return self.properties['log_neighbor_changes']
    @log_neighbor_changes.setter
    def log_neighbor_changes(self, x):
        parameter = 'log_neighbor_changes'
        if self.set_none(x, parameter):
            return
        if x not in self.nxos_bgp_neighbor_valid_log_neighbor_changes:
            expectation = ','.join(self.nxos_bgp_neighbor_valid_log_neighbor_changes)
            self.fail(self.class_name, parameter, x, parameter, expectation)
        self.properties[parameter] = x

    @property
    def low_memory_exempt(self):
        return self.properties['low_memory_exempt']
    @low_memory_exempt.setter
    def low_memory_exempt(self, x):
        parameter = 'low_memory_exempt'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def maximum_peers(self):
        return self.properties['maximum_peers']
    @maximum_peers.setter
    def maximum_peers(self, x):
        parameter = 'maximum_peers'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_maximum_peers(x, parameter)
        self.properties[parameter] = x

    @property
    def neighbor(self):
        return self.properties['neighbor']
    @neighbor.setter
    def neighbor(self, x):
        parameter = 'neighbor'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_neighbor(x)
        self.properties[parameter] = x

    @property
    def peer_type(self):
        return self.properties['peer_type']
    @peer_type.setter
    def peer_type(self, x):
        parameter = 'peer_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_peer_type(x, parameter)
        self.properties[parameter] = x

    @property
    def pwd(self):
        return self.properties['pwd']
    @pwd.setter
    def pwd(self, x):
        parameter = 'pwd'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def pwd_type(self):
        return self.properties['pwd_type']
    @pwd_type.setter
    def pwd_type(self, x):
        '''
        '''
        parameter = 'pwd_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_pwd_type(x)
        self.properties[parameter] = x

    @property
    def remote_as(self):
        return self.properties['remote_as']
    @remote_as.setter
    def remote_as(self, x):
        '''
        '''
        parameter = 'remote_as'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_asn(x, parameter)
        self.properties[parameter] = x

    @property
    def remove_private_as(self):
        return self.properties['remove_private_as']
    @remove_private_as.setter
    def remove_private_as(self, x):
        '''
        '''
        parameter = 'remove_private_as'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_remove_private_as(x, parameter)
        self.properties[parameter] = x

    @property
    def shutdown(self):
        return self.properties['shutdown']
    @shutdown.setter
    def shutdown(self, x):
        '''
        '''
        parameter = 'shutdown'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties['shutdown'] = x

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
        self.verify_nxos_bgp_neighbor_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suppress_4_byte_as(self):
        return self.properties['suppress_4_byte_as']
    @suppress_4_byte_as.setter
    def suppress_4_byte_as(self, x):
        '''
        '''
        parameter = 'suppress_4_byte_as'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_holdtime(self):
        return self.properties['timers_holdtime']
    @timers_holdtime.setter
    def timers_holdtime(self, x):
        '''
        '''
        parameter = 'timers_holdtime'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_timers(x, parameter)
        self.properties[parameter] = x

    @property
    def timers_keepalive(self):
        return self.properties['timers_keepalive']
    @timers_keepalive.setter
    def timers_keepalive(self, x):
        '''
        '''
        parameter = 'timers_keepalive'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bgp_neighbor_timers(x, parameter)
        self.properties[parameter] = x

    @property
    def transport_passive_only(self):
        return self.properties['transport_passive_only']
    @transport_passive_only.setter
    def transport_passive_only(self, x):
        '''
        '''
        parameter = 'transport_passive_only'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def update_source(self):
        return self.properties['update_source']
    @update_source.setter
    def update_source(self, x):
        '''
        '''
        parameter = 'update_source'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter)
        self.properties[parameter] = x
