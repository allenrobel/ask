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
