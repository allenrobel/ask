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
                                    - Valid values: False, True

destination_host                Destination host IP address::

                                    - Type: str()
                                    - Valid values: ipv4 or ipv6 address
                                    - Examples:
                                        task.destination_address = '1.1.1.2'
                                        task.destination_address = '2011:a::2'

destination_port_eq             Match on a specific destination port number::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.destination_port_eq = 80
                                        task.destination_port_eq = 8088

destination_port_gt             Match destination port numbers greater than provided value::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.destination_port_gt = 80
                                        task.destination_port_gt = 8088

destination_port_lt             Match destination port numbers less than provided value::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.destination_port_lt = 80
                                        task.destination_port_lt = 8088

destination_port_neq            Match destination port numbers not equal to provided value::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.destination_port_neq = 80
                                        task.destination_port_neq = 8088


destination_port_range_end      Match destination port numbers within a range, where
                                value is the end of the range::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.destination_port_range_end = 8088

destination_port_range_start    Match destination port numbers within a range, where
                                value is the start of the range::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.destination_port_range_start = 8000

destination_prefix              Destination network prefix.
                                Destination prefixes of 32 (ipv4) and 128 (ipv6) 
                                should be specified using the property: destination_host::

                                    - Type: int()
                                    - Valid values: int()
                                        - range ipv4: 0-31
                                        - range ipv6: 0-127
                                    - See also: destination_host
                                    - Examples:
                                        task.destination_prefix = 24
                                        task.destination_prefix = 120

destination_wildcard_bits       Destination wildcard bits::

                                    - Type: str()
                                    - Valid values: A wildcard mask
                                    - Examples:
                                        task.destination_wildcard_bits = '255.255.0.0'
                                        task.destination_wildcard_bits = '255:255::255:0' 

dscp                               Match packets with given DSCP value::

                                    - Type: str()
                                    - Valid values:
                                        - int() range: 1-64

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

fragments                       Check non-initial fragments::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Required

grant                           Action to be applied on the rule::

                                    - Type: str()
                                    - Valid values: deny, permit

log                             Log matches against this entry::

                                    - Type: bool()
                                    - Valid values: False, True
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

protocol                        Protocol to match::

                                    - Type: str()
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

remark                          ACL comment::

                                    - Type: str()

sequence                        ACE sequence number::

                                    - Type: int() range: 1-4294967295

source_address                  Source network address::

                                    - Type: str()
                                    - Valid values: ipv4 or ipv6 network
                                    - Examples:
                                        task.source_address = '1.1.1.0/24'
                                        task.source_address = '2011:a::0/120'

source_any                      Any source address::

                                    - Type: bool()
                                    - Valid values: False, True

source_host                     Source host IP address::

                                    - Type: str()
                                    - Valid values: ipv4 or ipv6 address
                                    - Examples:
                                        task.source_address = '1.1.1.2'
                                        task.source_address = '2011:a::2'

source_port_eq                  Match on a specific source port number::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.source_port_eq = 80
                                        task.source_port_eq = 8088

source_port_gt                  Match source port numbers greater than provided value::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.source_port_gt = 80
                                        task.source_port_gt = 8088

source_port_lt                  Match source port numbers less than provided value::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.source_port_lt = 80
                                        task.source_port_lt = 8088

source_port_neq                 Match source port numbers not equal to provided value::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.source_port_neq = 80
                                        task.source_port_neq = 8088


source_port_range_end           Match source port numbers within a range, where
                                value is the end of the range::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.source_port_range_end = 8088

source_port_range_start         Match source port numbers within a range, where
                                value is the start of the range::

                                    - Type: int()
                                    - Valid values: int() range: 0-65535
                                    - Examples:
                                        task.source_port_range_start = 8000

source_prefix                   Source network prefix.
                                Source prefixes of 32 (ipv4) and 128 (ipv6) 
                                should be specified using the property: source_host::

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
                                    - Valid values: A wildcard mask
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
                                    - Required
============================    ==============================================

|
|

================================    ==============================================
Property (icmp)                     Description
================================    ==============================================
icmp_administratively_prohibited
                                    - Type: bool()
                                    - Valid values: False, True

icmp_alternate_address
                                    - Type: bool()
                                    - Valid values: False, True

icmp_conversion_error
                                    - Type: bool()
                                    - Valid values: False, True
icmp_dod_net_prohibited
                                    - Type: bool()
                                    - Valid values: False, True
icmp_echo_request
                                    - Type: bool()
                                    - Valid values: False, True
icmp_echo
                                    - Type: bool()
                                    - Valid values: False, True
icmp_echo_reply
                                    - Type: bool()
                                    - Valid values: False, True
icmp_general_parameter_problem
                                    - Type: bool()
                                    - Valid values: False, True
icmp_host_isolated
                                    - Type: bool()
                                    - Valid values: False, True
icmp_host_precedence_unreachable
                                    - Type: bool()
                                    - Valid values: False, True
icmp_host_redirect
                                    - Type: bool()
                                    - Valid values: False, True
icmp_host_tos_redirect
                                    - Type: bool()
                                    - Valid values: False, True
icmp_host_tos_unreachable
                                    - Type: bool()
                                    - Valid values: False, True
icmp_host_unknown
                                    - Type: bool()
                                    - Valid values: False, True
icmp_host_unreachable
                                    - Type: bool()
                                    - Valid values: False, True
icmp_information_reply
                                    - Type: bool()
                                    - Valid values: False, True
icmp_information_request
                                    - Type: bool()
                                    - Valid values: False, True
icmp_mask_reply
                                    - Type: bool()
                                    - Valid values: False, True
icmp_mask_request
                                    - Type: bool()
                                    - Valid values: False, True
icmp_message_code
                                    - Type: bool()
                                    - Valid values: False, True
icmp_message_type
                                    - Type: bool()
                                    - Valid values: False, True
icmp_mobile_redirect
                                    - Type: bool()
                                    - Valid values: False, True
icmp_net_redirect
                                    - Type: bool()
                                    - Valid values: False, True
icmp_net_tos_redirect
                                    - Type: bool()
                                    - Valid values: False, True
icmp_net_tos_unreachable
                                    - Type: bool()
                                    - Valid values: False, True
icmp_net_unreachable
                                    - Type: bool()
                                    - Valid values: False, True
icmp_network_unknown
                                    - Type: bool()
                                    - Valid values: False, True
icmp_no_room_for_option
                                    - Type: bool()
                                    - Valid values: False, True
icmp_option_missing
                                    - Type: bool()
                                    - Valid values: False, True
icmp_packet_too_big
                                    - Type: bool()
                                    - Valid values: False, True
icmp_parameter_problem
                                    - Type: bool()
                                    - Valid values: False, True
icmp_port_unreachable
                                    - Type: bool()
                                    - Valid values: False, True
icmp_precedence_unreachable
                                    - Type: bool()
                                    - Valid values: False, True
icmp_protocol_unreachable
                                    - Type: bool()
                                    - Valid values: False, True
icmp_reassembly_timeout
                                    - Type: bool()
                                    - Valid values: False, True
icmp_redirect
                                    - Type: bool()
                                    - Valid values: False, True
icmp_router_advertisement
                                    - Type: bool()
                                    - Valid values: False, True
icmp_router_solicitation
                                    - Type: bool()
                                    - Valid values: False, True
icmp_source_quench
                                    - Type: bool()
                                    - Valid values: False, True
icmp_source_route_failed
                                    - Type: bool()
                                    - Valid values: False, True
icmp_time_exceeded
                                    - Type: bool()
                                    - Valid values: False, True
icmp_timestamp_reply
                                    - Type: bool()
                                    - Valid values: False, True
icmp_timestamp_request
                                    - Type: bool()
                                    - Valid values: False, True
icmp_traceroute
                                    - Type: bool()
                                    - Valid values: False, True
icmp_ttl_exceeded
                                    - Type: bool()
                                    - Valid values: False, True
icmp_unreachable
                                    - Type: bool()
                                    - Valid values: False, True
================================    ==============================================

|
|

============================    ==============================================
Property (igmp)                 Description
============================    ==============================================
igmp_dvmrp
                                    - Type: bool()
                                    - Valid values: False, True
igmp_host_query
                                    - Type: bool()
                                    - Valid values: False, True
igmp_host_report
                                    - Type: bool()
                                    - Valid values: False, True

============================    ==============================================

|
|

============================    ==============================================
Property (tcp)                  Description
============================    ==============================================
tcp_ack
                                    - Type: bool()
                                    - Valid values: False, True

tcp_established
                                    - Type: bool()
                                    - Valid values: False, True

tcp_fin
                                    - Type: bool()
                                    - Valid values: False, True

tcp_psh
                                    - Type: bool()
                                    - Valid values: False, True

tcp_rst
                                    - Type: bool()
                                    - Valid values: False, True

tcp_syn
                                    - Type: bool()
                                    - Valid values: False, True

tcp_urg
                                    - Type: bool()
                                    - Valid values: False, True

============================    ==============================================

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
