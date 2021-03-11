******************************************
NxosAcls()
******************************************

ScriptKit Synopsis
------------------
NxosAcls() generates Ansible task instances conformant with cisco.nxos.nxos_acls.
These task instances can then be passed to Playbook().add_task()

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_acls.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_acls.py>`_

Caveats
-------
- dscp int() values are currently broken in the cisco.nxos.nxos_acls module.  The following issue has been filed:
   `#253 nxos_acls : dscp: 31 results in KeyError on Nexus9000 <https://github.com/ansible-collections/cisco.nxos/issues/253>`_

Ansible Module Documentation
----------------------------
- `nxos_acls <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_acls_module.rst>`_

|

============================    ==============================================
Property (aces)                 Description
============================    ==============================================
destination_address             Destination network address::

                                    - Type: str()
                                    - Valid values: ipv4 or ipv6 network
                                    - Examples:
                                        task.destination_address = '1.1.1.0/24'
                                        task.destination_address = '2011:a::0/120'

destination_any                 Any destination address::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.destination_any = False

destination_host                Destination host IP address::

                                    - Type: str()
                                    - Valid values:
                                        - ipv4 address
                                        - ipv6 address
                                    - Examples:
                                        task.destination_address = '1.1.1.2'
                                        task.destination_address = '2011:a::2'

destination_port_eq             Match on a specific destination port number::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.destination_port_eq = 80
                                        task.destination_port_eq = 8088

destination_port_gt             Match destination port numbers greater than provided value::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.destination_port_gt = 80
                                        task.destination_port_gt = 8088

destination_port_lt             Match destination port numbers less than provided value::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.destination_port_lt = 80
                                        task.destination_port_lt = 8088

destination_port_neq            Match destination port numbers not equal to provided value::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.destination_port_neq = 80
                                        task.destination_port_neq = 8088


destination_port_range_end      Match destination port numbers within a range, where
                                value is the end of the range::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Example:
                                        task.destination_port_range_end = 8088

destination_port_range_start    Match destination port numbers within a range, where
                                value is the start of the range::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Example:
                                        task.destination_port_range_start = 8000

destination_prefix              Destination network prefix.
                                Destination prefixes of 32 (ipv4) and 128 (ipv6) 
                                should be specified using the property: destination_host::

                                    - Type: int()
                                    - Valid values:
                                        - range ipv4: 0-31
                                        - range ipv6: 0-127
                                    - See also: destination_host
                                    - Examples:
                                        task.destination_prefix = 24
                                        task.destination_prefix = 120

destination_wildcard_bits       Destination wildcard bits::

                                    - Type: str()
                                    - Valid values:
                                        - A wildcard mask
                                    - Examples:
                                        task.destination_wildcard_bits = '255.255.0.0'
                                        task.destination_wildcard_bits = '255:255::255:0' 

dscp                               Match packets with given DSCP value::

                                    - Type: str()
                                    - Valid values:
                                        - range: 1-64

                                        - af11 (001010)
                                        - af12 (001100)
                                        - af13 (001110)
                                        - af21 (010010)
                                        - af22 (010100)
                                        - af23 (010110)
                                        - af31 (011010)
                                        - af32 (011100)
                                        - af33 (011110)
                                        - af41 (100010)
                                        - af42 (100100)
                                        - af43 (100110)

                                        - cs1 (001000) (precedence 1)
                                        - cs2 (010000) (precedence 2)
                                        - cs3 (011000) (precedence 3)
                                        - cs4 (100000) (precedence 4)
                                        - cs5 (101000) (precedence 5)
                                        - cs6 (110000) (precedence 6)
                                        - cs7 (111000) (precedence 7)

                                        - default
                                        - ef
                                    - Examples:
                                        task.dscp = 61
                                        task.dscp = 'cs5'
                                        task.dscp = 'af11'
                                        task.dscp = 'default'
                                        task.dscp = 'ef'

fragments                       Check non-initial fragments::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.fragments = False
                                    - Required

grant                           Action to be applied on the rule::

                                    - Type: str()
                                    - Valid values:
                                        - deny
                                        - permit
                                    - Example:
                                        task.fragments = 'deny'

log                             Log matches against this entry::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.log = False
                                    - Required

precedence                      Precedence to match::

                                    - Type: str()
                                    - Valid values:
                                        - critical
                                        - flash
                                        - flash-override
                                        - immediate
                                        - internet
                                        - network
                                        - priority
                                        - routine
                                    - Example:
                                        task.precedence = 'priority'

protocol                        Protocol to match::

                                    - Type: str() or int()
                                    - Valid values:
                                        - int() range: 1-256                                        
                                        - ahp
                                        - eigrp
                                        - esp
                                        - gre
                                        - icmp
                                        - igmp
                                        - ip
                                        - nos
                                        - ospf
                                        - pcp
                                        - pim
                                        - tcp
                                        - udf
                                        - udp
                                    - Examples:
                                        task.protocol = 80
                                        task.protocol = 'icmp'

remark                          ACL comment::

                                    - Type: str()
                                    - Example:
                                        task.remark = 'deny transit'

sequence                        ACE sequence number::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-4294967295
                                    - Example:
                                        task.sequence = 10

source_address                  Source network address::

                                    - Type: str()
                                    - Valid values:
                                        - ipv4 network
                                        - ipv6 network
                                    - Examples:
                                        task.source_address = '1.1.1.0/24'
                                        task.source_address = '2011:a::0/120'

source_any                      Any source address::

                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.source_any = True

source_host                     Source host IP address::

                                    - Type: str()
                                    - Valid values:
                                        - ipv4 address
                                        - ipv6 address
                                    - Examples:
                                        task.source_host = '1.1.1.2'
                                        task.source_host = '2011:a::2'

source_port_eq                  Match on a specific source port number::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.source_port_eq = 80
                                        task.source_port_eq = 8088

source_port_gt                  Match source port numbers greater than provided value::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.source_port_gt = 80
                                        task.source_port_gt = 8088

source_port_lt                  Match source port numbers less than provided value::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.source_port_lt = 80
                                        task.source_port_lt = 8088

source_port_neq                 Match source port numbers not equal to provided value::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.source_port_neq = 80
                                        task.source_port_neq = 8088


source_port_range_end           Match source port numbers within a range, where
                                value is the end of the range::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.source_port_range_end = 8088

source_port_range_start         Match source port numbers within a range, where
                                value is the start of the range::

                                    - Type: int()
                                    - Valid values:
                                        - range: 0-65535
                                    - Examples:
                                        task.source_port_range_start = 8000

source_prefix                   Source network prefix.
                                Source prefixes of 32 (ipv4) and 128 (ipv6) 
                                should be specified using the property
                                ``source_host``::

                                    - Type: int()
                                    - Valid values: int()
                                        - range ipv4: 0-31
                                        - range ipv6: 0-127
                                    - See also: source_host
                                    - Examples:
                                        task.source_prefix = 24
                                        task.source_prefix = 120

source_wildcard_bits            Source wildcard bits::

                                    - Type: str()
                                    - Valid values:
                                        - A wildcard mask
                                    - Examples:
                                        task.source_wildcard_bits = '255.255.0.0'
                                        task.source_wildcard_bits = '255:255::255:0' 

============================    ==============================================

|
|

============================    ==============================================
Property (acl)                  Description
============================    ==============================================
name                            Name of the ACL::

                                    - Type: str()
                                    - Example:
                                        task.name = 'deny ipv6'
                                    - Required
============================    ==============================================

|
|

================================    ==============================================
Property (icmp)                     Description
================================    ==============================================
icmp_administratively_prohibited
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_administratively_prohibited = False

icmp_alternate_address
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_alternate_address = False

icmp_conversion_error
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_conversion_error = False

icmp_dod_net_prohibited
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_dod_net_prohibited = False

icmp_echo_request
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_echo_request = False

icmp_echo
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_echo = False

icmp_echo_reply
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_echo_reply = False

icmp_general_parameter_problem
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_general_parameter_problem = False

icmp_host_isolated
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_host_isolated = False

icmp_host_precedence_unreachable
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_host_precedence_unreachable = False

icmp_host_redirect
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_host_redirect = False

icmp_host_tos_redirect
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_host_tos_redirect = False

icmp_host_tos_unreachable
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_host_tos_unreachable = False

icmp_host_unknown
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_host_unknown = False

icmp_host_unreachable
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_host_unreachable = False

icmp_information_reply
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_information_reply = False

icmp_information_request
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_information_request = False

icmp_mask_reply
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_mask_reply = False

icmp_mask_request
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_mask_request = False

icmp_message_code
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_message_code = False

icmp_message_type
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_message_type = False

icmp_mobile_redirect
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_mobile_redirect = False

icmp_net_redirect
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_net_redirect = False

icmp_net_tos_redirect
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_net_tos_redirect = False

icmp_net_tos_unreachable
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_net_tos_unreachable = False

icmp_net_unreachable
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_net_unreachable = False

icmp_network_unknown
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_network_unknown = False

icmp_no_room_for_option
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_no_room_for_option = False

icmp_option_missing
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_option_missing = False

icmp_packet_too_big
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_packet_too_big = False

icmp_parameter_problem
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_parameter_problem = False

icmp_port_unreachable
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_port_unreachable = False

icmp_precedence_unreachable
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_precedence_unreachable = False

icmp_protocol_unreachable
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_protocol_unreachable = False

icmp_reassembly_timeout
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_reassembly_timeout = False

icmp_redirect
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_redirect = False

icmp_router_advertisement
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_router_advertisement = False

icmp_router_solicitation
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_router_solicitation = False

icmp_source_quench
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_source_quench = False

icmp_source_route_failed
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_source_route_failed = False

icmp_time_exceeded
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_time_exceeded = False

icmp_timestamp_reply
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_timestamp_reply = False

icmp_timestamp_request
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_timestamp_request = False

icmp_traceroute
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_traceroute = False

icmp_ttl_exceeded
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_ttl_exceeded = False

icmp_unreachable
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.icmp_unreachable = False

================================    ==============================================

|
|

============================    ==============================================
Property (igmp)                 Description
============================    ==============================================
igmp_dvmrp
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.igmp_dvmrp = False

igmp_host_query
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.igmp_host_query = False

igmp_host_report
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.igmp_host_report = False

============================    ==============================================

|
|

============================    ==============================================
Property (tcp)                  Description
============================    ==============================================
tcp_ack
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.tcp_ack = False

tcp_established
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.tcp_established = False

tcp_fin
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.tcp_fin = False

tcp_psh
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.tcp_psh = False

tcp_rst
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.tcp_rst = False

tcp_syn
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.tcp_syn = False

tcp_urg
                                    - Type: bool()
                                    - Valid values:
                                        - False
                                        - True
                                    - Example:
                                        task.tcp_urg = False

============================    ==============================================


TODO
----

- 20200104: Add verification for address properties
- 20200104: Add verification for wildcard_bits properties
- 20200107: icmp_echo for afi = 'ipv6' is currently broken in the 
  Ansible module.  Make any modifications to this library
  once a fix is available in the module.

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
