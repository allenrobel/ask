# NxosAcls() - cisco/nxos/nxos_acls.py
our_version = 113
from copy import deepcopy
import re
from ask.common.task import Task
'''
******************************************
NxosAcls()
******************************************

Version
-------
111

ScriptKit Synopsis
------------------
NxosAcls() generates Ansible task instances conformant with cisco.nxos.nxos_acls.
These task instances can then be passed to Playbook().add_task()

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_acls.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_acls.py>`_

Caveats
-------

- See TODO

TODO
----

- 20210627: Add handling for port_protocol range start/end
- 20210627: Improve handling for port_protocol
- 20200104: Add verification for address properties
- 20200104: Add verification for wildcard_bits properties

Ansible Module Documentation
----------------------------
- `nxos_acls <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_acls_module.rst>`_

|

========================    ==============================================
Method                      Description
========================    ==============================================
add_ace()                   Add an access control entry (ACE) to a list() of
                            ipv4 or ipv6 ACEs.  ``afi`` determines which list()
                            the ACE is added to.::

                                - Type: function()
                                - Example:
                                    See add_acl()

add_acl()                   Add all currently-set access control entries (ACEs)
                            to an access control list (ACL)::

                                - Type: function()
                                - Example:
                                    pb = Playbook(log)
                                    pb.profile_nxos()
                                    pb.ansible_password = 'mypassword'
                                    pb.file = '/tmp/nxos_acls.yaml'
                                    pb.name = 'nxos_acls play'
                                    pb.add_host('dc-101')
                                    task = NxosAcls(log)
                                    task.remark = 'example ipv4 acl'
                                    task.sequence = 5
                                    task.add_ace()
                                    task.afi = 'ipv4'
                                    task.grant = 'permit'
                                    task.protocol = 'ip'
                                    task.sequence = 10
                                    task.dscp = 'af31'
                                    task.destination_address = '1.2.2.2'
                                    task.destination_wildcard_bits = '0.0.255.255'
                                    task.source_address = '1.1.1.1'
                                    task.source_wildcard_bits = '0.0.0.255'
                                    task.add_ace()
                                    task.name = 'IPv4_ACL'
                                    task.add_acl()
                                    task.state = 'merged'
                                    task.commit()
                                    pb.add_task(task)
                                    pb.append_playbook()
                                    pb.write_playbook()

commit()                    Perform final verification and commit the 
                            current task::
                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See add_acl()
                                    See ScriptKit Example above for full script

========================    ==============================================

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
                                    - NOTES:
                                        1. Valid only for ipv4 afi
                                        2. Use icmp_echo_request for ipv6 afi

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


Authors
~~~~~~~

- Allen Robel (@PacketCalc)
'''
class NxosAcls(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_acls'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()

        self.properties_ace = set()
        self.properties_ace.add('dscp')
        self.properties_ace.add('fragments')
        self.properties_ace.add('grant')
        self.properties_ace.add('log')
        self.properties_ace.add('precedence')
        self.properties_ace.add('protocol')
        self.properties_ace.add('remark')
        self.properties_ace.add('sequence')

        self.properties_acl = set()
        self.properties_acl.add('name')

        self.properties_destination = set()
        self.properties_destination.add('destination_address')
        self.properties_destination.add('destination_any')
        self.properties_destination.add('destination_host')
        self.properties_destination.add('destination_port_eq')
        self.properties_destination.add('destination_port_gt')
        self.properties_destination.add('destination_port_lt')
        self.properties_destination.add('destination_port_neq')
        self.properties_destination.add('destination_port_range_end')
        self.properties_destination.add('destination_port_range_start')
        self.properties_destination.add('destination_prefix')
        self.properties_destination.add('destination_wildcard_bits')

        self.properties_icmp = set()
        self.properties_icmp.add('icmp_administratively_prohibited')
        self.properties_icmp.add('icmp_alternate_address')
        self.properties_icmp.add('icmp_conversion_error')
        self.properties_icmp.add('icmp_dod_net_prohibited')
        self.properties_icmp.add('icmp_echo_request')
        self.properties_icmp.add('icmp_echo')
        self.properties_icmp.add('icmp_echo_reply')
        self.properties_icmp.add('icmp_general_parameter_problem')
        self.properties_icmp.add('icmp_host_isolated')
        self.properties_icmp.add('icmp_host_precedence_unreachable')
        self.properties_icmp.add('icmp_host_redirect')
        self.properties_icmp.add('icmp_host_tos_redirect')
        self.properties_icmp.add('icmp_host_tos_unreachable')
        self.properties_icmp.add('icmp_host_unknown')
        self.properties_icmp.add('icmp_host_unreachable')
        self.properties_icmp.add('icmp_information_reply')
        self.properties_icmp.add('icmp_information_request')
        self.properties_icmp.add('icmp_mask_reply')
        self.properties_icmp.add('icmp_mask_request')
        self.properties_icmp.add('icmp_message_code')
        self.properties_icmp.add('icmp_message_type')
        self.properties_icmp.add('icmp_mobile_redirect')
        self.properties_icmp.add('icmp_net_redirect')
        self.properties_icmp.add('icmp_net_tos_redirect')
        self.properties_icmp.add('icmp_net_tos_unreachable')
        self.properties_icmp.add('icmp_net_unreachable')
        self.properties_icmp.add('icmp_network_unknown')
        self.properties_icmp.add('icmp_no_room_for_option')
        self.properties_icmp.add('icmp_option_missing')
        self.properties_icmp.add('icmp_packet_too_big')
        self.properties_icmp.add('icmp_parameter_problem')
        self.properties_icmp.add('icmp_port_unreachable')
        self.properties_icmp.add('icmp_precedence_unreachable')
        self.properties_icmp.add('icmp_protocol_unreachable')
        self.properties_icmp.add('icmp_reassembly_timeout')
        self.properties_icmp.add('icmp_redirect')
        self.properties_icmp.add('icmp_router_advertisement')
        self.properties_icmp.add('icmp_router_solicitation')
        self.properties_icmp.add('icmp_source_quench')
        self.properties_icmp.add('icmp_source_route_failed')
        self.properties_icmp.add('icmp_time_exceeded')
        self.properties_icmp.add('icmp_timestamp_reply')
        self.properties_icmp.add('icmp_timestamp_request')
        self.properties_icmp.add('icmp_traceroute')
        self.properties_icmp.add('icmp_ttl_exceeded')
        self.properties_icmp.add('icmp_unreachable')

        self.properties_igmp = set()
        self.properties_igmp.add('igmp_dvmrp')
        self.properties_igmp.add('igmp_host_query')
        self.properties_igmp.add('igmp_host_report')

        self.properties_source = set()
        self.properties_source.add('source_address')
        self.properties_source.add('source_any')
        self.properties_source.add('source_host')
        self.properties_source.add('source_port_eq')
        self.properties_source.add('source_port_gt')
        self.properties_source.add('source_port_lt')
        self.properties_source.add('source_port_neq')
        self.properties_source.add('source_port_range_end')
        self.properties_source.add('source_port_range_start')
        self.properties_source.add('source_prefix')
        self.properties_source.add('source_wildcard_bits')

        self.properties_tcp = set()
        self.properties_tcp.add('tcp_ack')
        self.properties_tcp.add('tcp_established')
        self.properties_tcp.add('tcp_fin')
        self.properties_tcp.add('tcp_psh')
        self.properties_tcp.add('tcp_rst')
        self.properties_tcp.add('tcp_syn')
        self.properties_tcp.add('tcp_urg')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_ace)
        self.scriptkit_properties.update(self.properties_acl)
        self.scriptkit_properties.update(self.properties_destination)
        self.scriptkit_properties.update(self.properties_icmp)
        self.scriptkit_properties.update(self.properties_igmp)
        self.scriptkit_properties.update(self.properties_source)
        self.scriptkit_properties.update(self.properties_tcp)

        # property_map is used to map between de-ambiguated property names
        # and the ambiguous Ansible property names used in the Ansible playbook
        # For example, the property names for destination address and source address
        # are ambiguous (they are both 'address').  We disambiguate these by providing
        # properties for destination_address, and source_address.  Later, we use property_map
        # to apply the correct property values when populating the playbook.
        #     destination_address -> address
        #     source_address      -> address
        self.property_map = dict()
        self.property_map['destination_address'] = 'address'
        self.property_map['destination_any'] = 'any'
        self.property_map['destination_host'] = 'host'
        self.property_map['destination_port_eq'] = 'eq'
        self.property_map['destination_port_gt'] = 'gt'
        self.property_map['destination_port_lt'] = 'lt'
        self.property_map['destination_port_neq'] = 'neq'
        self.property_map['destination_port_range_end'] = 'end'
        self.property_map['destination_port_range_start'] = 'start'
        self.property_map['destination_prefix'] = 'prefix'
        self.property_map['destination_wildcard_bits'] = 'wildcard_bits'

        self.property_map['source_address'] = 'address'
        self.property_map['source_any'] = 'any'
        self.property_map['source_host'] = 'host'
        self.property_map['source_port_eq'] = 'eq'
        self.property_map['source_port_gt'] = 'gt'
        self.property_map['source_port_lt'] = 'lt'
        self.property_map['source_port_neq'] = 'neq'
        self.property_map['source_port_range_end'] = 'end'
        self.property_map['source_port_range_start'] = 'start'
        self.property_map['source_prefix'] = 'prefix'
        self.property_map['source_wildcard_bits'] = 'wildcard_bits'

        for p in self.properties_icmp:
            self.property_map[p] = re.sub('icmp_', '', p)
        for p in self.properties_igmp:
            self.property_map[p] = re.sub('igmp_', '', p)
        for p in self.properties_tcp:
            self.property_map[p] = re.sub('tcp_', '', p)

        self.nxos_acls_valid_afi = set()
        self.nxos_acls_valid_afi.add('ipv4')
        self.nxos_acls_valid_afi.add('ipv6')

        self.nxos_acls_valid_dscp = set()
        for x in range(0,64):
            self.nxos_acls_valid_dscp.add(str(x))
        for x in range(1,5):
            for y in range(1,4):
                self.nxos_acls_valid_dscp.add('af{}{}'.format(x,y))
        for x in range(1,8):
            self.nxos_acls_valid_dscp.add('cs{}'.format(x))
        self.nxos_acls_valid_dscp.add('default')
        self.nxos_acls_valid_dscp.add('ef')

        self.nxos_acls_valid_grant = set()
        self.nxos_acls_valid_grant.add('permit')
        self.nxos_acls_valid_grant.add('deny')

        self.nxos_acls_valid_precedence = set()
        for x in range(0,8):
            self.nxos_acls_valid_precedence.add(str(x))
        self.nxos_acls_valid_precedence.add('critical')
        self.nxos_acls_valid_precedence.add('flash')
        self.nxos_acls_valid_precedence.add('flash-override')
        self.nxos_acls_valid_precedence.add('immediate')
        self.nxos_acls_valid_precedence.add('internet')
        self.nxos_acls_valid_precedence.add('network')
        self.nxos_acls_valid_precedence.add('priority')
        self.nxos_acls_valid_precedence.add('routine')

        self.nxos_acls_valid_protocol = set()
        for x in range(0,256):
            self.nxos_acls_valid_protocol.add(str(x))
        self.nxos_acls_valid_protocol.add('ahp')
        self.nxos_acls_valid_protocol.add('eigrp')
        self.nxos_acls_valid_protocol.add('esp')
        self.nxos_acls_valid_protocol.add('gre')
        self.nxos_acls_valid_protocol.add('icmp')
        self.nxos_acls_valid_protocol.add('igmp')
        self.nxos_acls_valid_protocol.add('ip')
        self.nxos_acls_valid_protocol.add('nos')
        self.nxos_acls_valid_protocol.add('ospf')
        self.nxos_acls_valid_protocol.add('pcp')
        self.nxos_acls_valid_protocol.add('pim')
        self.nxos_acls_valid_protocol.add('tcp')
        self.nxos_acls_valid_protocol.add('udf')
        self.nxos_acls_valid_protocol.add('udp')

        self.nxos_acls_valid_state = set()
        self.nxos_acls_valid_state.add('merged')
        self.nxos_acls_valid_state.add('replaced')
        self.nxos_acls_valid_state.add('overridden')
        self.nxos_acls_valid_state.add('deleted')
        self.nxos_acls_valid_state.add('gathered')
        self.nxos_acls_valid_state.add('rendered')
        self.nxos_acls_valid_state.add('parsed')

        self.port_min = 1
        self.port_max = 65535

        self.init_properties()

    def get_mapped_property(self, x):
        '''
        return either a mapped property, if one exists, or x
        '''
        if x in self.property_map:
            return self.property_map[x]
        return x

    def init_properties_destination(self):
        '''
        Valid range for all type int() is: 0-65535

        destination_address             str()   Destination network address
                                                Valid values: ipv4/ipv6 address
        destination_any                 bool()  Any destination address
        destination_host                str()   Host IP address
                                                Valid values: ipv4/ipv6 address
        destination_port_eq             int()   Match packets with a given port number
        destination_port_gt             int()   Match packets with a greater port number
        destination_port_lt             int()   Match packets with a lower port number
        destination_port_neq            int()   Match packets without a given port number
        destination_port_range_end      int()   End of the port range
        destination_port_range_start    int()   Start of the port range
        destination_prefix              int()   Destination network prefix e.g. 30, 126
                                                Valid values: ipv4 range 0-31, ipv6 range 0-127
                                                for 32 (ipv4), 128 (ipv6), use host keyword instead
                                                e.g. host 10.1.1.1
        destination_wildcard_bits       str()   Dotted notation mask specifying wildcard e.g. 0.0.255.255
        '''
        for p in self.properties_destination:
            self.properties[p] = None


    def init_properties_icmp(self):
        '''
        All icmp properties are Ansible boolean with valid values: no, yes
        '''
        for p in self.properties_icmp:
            self.properties[p] = None

    def init_properties_igmp(self):
        '''
        All igmp properties are Ansible boolean with valid values: no, yes
        '''
        for p in self.properties_igmp:
            self.properties[p] = None

    def init_properties_tcp(self):
        '''
        All tcp properties are Ansible boolean with valid values: no, yes
        '''
        for p in self.properties_tcp:
            self.properties[p] = None

    def init_properties_protocol_options(self):
        self.init_properties_icmp()
        self.init_properties_igmp()
        self.init_properties_tcp()

    def init_properties_source(self):
        '''
        Valid range for all type int() is: 0-65535

        source_address          str()   Source network address
                                        Valid values: ipv4/ipv6 address
        source_any              bool()  Any destination address
        source_host             str()   Host IP address
                                        Valid values: ipv4/ipv6 address
        source_port_eq          int()   Match packets with a given port number
        source_port_gt          int()   Match packets with a greater port number
        source_port_lt          int()   Match packets with a lower port number
        source_port_neq         int()   Match packets without a given port number
        source_port_range_end   int()   end of the port range
        source_port_range_start int()   start of the port range
        source_prefix           int()   Destination network prefix e.g. 30, 126
                                        Valid values: ipv4 range 0-31, ipv6 range 0-127
                                        for 32 (ipv4), 128 (ipv6), use host keyword instead
                                        e.g. host 10.1.1.1
        source_wildcard_bits    str()   Dotted notation mask specifying wildcard e.g. 0.0.255.255
        '''
        for _property in self.properties_source:
            self.properties[_property] = None

    def init_properties_ace(self):
        '''
        dscp        str()   Match packets with given DSCP value
                            Valid values: see self.nxos_acls_valid_dscp
        fragments   bool()  Check non-initial fragments
        grant       str()   Action to be applied on the rule
                            Valid values: deny, permit
        log         bool()  Log matches against this entry
        precedence  str()   Match packets with given precedence value
                            Valid values: see self.nxos_acls_valid_precedence
        protocol    str()   Specify the protocol
                            Valid values: see self.nxos_acls_valid_protocol
        remark      str()   ACL comment
        sequence    int()   ACE sequence number

        '''
        self.init_properties_destination()
        self.init_properties_protocol_options()
        self.init_properties_source()
        for p in self.properties_ace:
            self.properties[p] = None

    def init_properties_acl(self):
        '''
        name    str()   Name of the ACL
                        Required
        '''
        self.init_properties_ace()
        self.properties['afi']      = None  # str() see self.__init__().nxos_acls_valid_state
        self.aces = list()
        for p in self.properties_acl:
            self.properties[p] = None

    def init_properties(self):
        self.properties = dict()
        self.acls_ipv4 = list()
        self.acls_ipv6 = list()
        self.init_properties_acl()
        self.properties['task_name']    = None
        self.properties['state']        = None  # str() see self.__init__().nxos_acls_valid_state

    def ace_set_for_remark(self):
        '''
        We skip sequence and remark since ace_set_for_remark() is used in
        verify_ace_remark() to verify if mutually-exclusive properties are
        set.  Specifically, if remark is set, then no other properties 
        should be set, except sequence.
        '''
        s = set()
        for p in self.properties_ace:
            if p == 'remark':
                continue
            if p == 'sequence':
                continue
            if self.properties[p] != None:
                s.add(p)
        return s
    def ace_set(self):
        '''
        '''
        s = set()
        for p in self.properties_ace:
            if self.properties[p] != None:
                s.add(p)
        return s
    def destination_set(self):
        s = set()
        for p in self.properties_destination:
            if self.properties[p] != None:
                s.add(p)
        return s
    def icmp_set(self):
        s = set()
        for p in self.properties_icmp:
            if self.properties[p] != None:
                s.add(p)
        return s
    def igmp_set(self):
        s = set()
        for p in self.properties_igmp:
            if self.properties[p] != None:
                s.add(p)
        return s
    def source_set(self):
        s = set()
        for p in self.properties_source:
            if self.properties[p] != None:
                s.add(p)
        return s
    def tcp_set(self):
        s = set()
        for p in self.properties_tcp:
            if self.properties[p] != None:
                s.add(p)
        return s

    def verify_ace_destination_any(self):
        s = set()
        for p in ['destination_host', 'destination_prefix', 'destination_address', 'destination_wildcard_bits']:
            if self.properties[p] != None:
                s.add(p)
        if self.destination_any != None and len(s) != 0:
            self.task_log.error('exiting. The following should not be set if instance.destination_any is set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
    def verify_ace_destination_address(self):
        s = set()
        for p in ['destination_host', 'destination_prefix']:
            if self.properties[p] != None:
                s.add(p)
        if self.destination_address != None and len(s) != 0:
            self.task_log.error('exiting. The following should not be set if instance.destination_address is set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
        if self.destination_address != None and self.destination_wildcard_bits == None:
            self.task_log.error('exiting. if instance.destination_address is set instance.destination_wildcard_bits must also be set.')
            exit(1)
    def verify_ace_destination_prefix(self):
        s = set()
        for p in ['destination_any', 'destination_host', 'destination_wildcard_bits']:
            if self.properties[p] != None:
                s.add(p)
        if self.destination_prefix != None and len(s) != 0:
            self.task_log.error('exiting. The following should not be set if instance.destination_prefix is set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
    def verify_ace_destination_port_range(self):
        s = set()
        for p in ['destination_port_range_end', 'destination_port_range_start']:
            if self.properties[p] != None:
                s.add(p)
        if len(s) == 2:
            if self.properties['destination_port_range_start'] > self.properties['destination_port_range_end']:
                self.task_log.error('exiting. range_start must be less than range_end.')
                for p in s:
                    self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
                exit(1)
        if len(s) in [0,2]:
            return s
        self.task_log.error('exiting. Both destination_port_range_start and destination_port_range_end must be set or unset.')
        for p in s:
            self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
        exit(1)
    def verify_ace_destination_port(self, s_pr):
        s = set()
        for p in ['destination_port_eq', 'destination_port_gt', 'destination_port_lt', 'destination_port_neq']:
            if self.properties[p] != None:
                s.add(p)
        if len(s) > 1:
            self.task_log.error('exiting. Only one destination_port property can be set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
        if len(s) != 0 and len(s_pr) != 0:
            self.task_log.error('exiting. Only one destination_port property can be set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            for p in ['destination_port_range_end', 'destination_port_range_start']:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)

    def verify_ace_source_any(self):
        s = set()
        for p in ['source_host', 'source_prefix', 'source_address', 'source_wildcard_bits']:
            if self.properties[p] != None:
                s.add(p)
        if self.source_any != None and len(s) != 0:
            self.task_log.error('exiting. The following should not be set if instance.source_any is set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
    def verify_ace_source_address(self):
        s = set()
        for p in ['source_host', 'source_prefix']:
            if self.properties[p] != None:
                s.add(p)
        if self.source_address != None and len(s) != 0:
            self.task_log.error('exiting. The following should not be set if instance.source_address is set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
        if self.source_address != None and self.source_wildcard_bits == None:
            self.task_log.error('exiting. if instance.source_address is set instance.source_wildcard_bits must also be set.')
            exit(1)
    def verify_ace_source_prefix(self):
        s = set()
        for p in ['source_any', 'source_host', 'source_wildcard_bits']:
            if self.properties[p] != None:
                s.add(p)
        if self.source_prefix != None and len(s) != 0:
            self.task_log.error('exiting. The following should not be set if instance.source_prefix is set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
    def verify_ace_source_port_range(self):
        s = set()
        for p in ['source_port_range_end', 'source_port_range_start']:
            if self.properties[p] != None:
                s.add(p)
        if len(s) == 2:
            if self.properties['source_port_range_start'] > self.properties['source_port_range_end']:
                self.task_log.error('exiting. range_start must be less than range_end.')
                for p in s:
                    self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
                exit(1)
        if len(s) in [0,2]:
            return s
        self.task_log.error('exiting. Both source_port_range_start and source_port_range_end must be set or unset.')
        for p in s:
            self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
        exit(1)
    def verify_ace_source_port(self, s_pr):
        s = set()
        for p in ['source_port_eq', 'source_port_gt', 'source_port_lt', 'source_port_neq']:
            if self.properties[p] != None:
                s.add(p)
        if len(s) > 1:
            self.task_log.error('exiting. Only one source_port property can be set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
        if len(s) != 0 and len(s_pr) != 0:
            self.task_log.error('exiting. Only one source_port property can be set.')
            for p in s:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            for p in ['source_port_range_end', 'source_port_range_start']:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)

    def verify_ace_afi(self):
        if self.afi == None:
            self.task_log.error('exiting. instance.afi must be set prior to calling instance.add_ace()')
            exit(1)
    def verify_ace_destination(self):
        self.verify_ace_destination_any()
        self.verify_ace_destination_address()
        self.verify_ace_destination_prefix()
        s_pr = self.verify_ace_destination_port_range()
        self.verify_ace_destination_port(s_pr)
    def verify_ace_source(self):
        self.verify_ace_source_any()
        self.verify_ace_source_address()
        self.verify_ace_source_prefix()
        s_pr = self.verify_ace_source_port_range()
        self.verify_ace_source_port(s_pr)
    def verify_ace_grant(self):
        if self.remark != None:
            return
        if self.grant == None:
            self.task_log.error('exiting. instance.grant must be set if instance.remark is not set.')
            exit(1)
    def verify_ace_remark(self):
        if self.remark == None:
            return
        if self.sequence == None:
            self.task_log.error('exiting. instance.sequence must be set if instance.remark is set.')
            exit(1)
        verify_set = set()
        verify_set.update(self.ace_set_for_remark())
        verify_set.update(self.destination_set())
        verify_set.update(self.icmp_set())
        verify_set.update(self.igmp_set())
        verify_set.update(self.source_set())
        verify_set.update(self.tcp_set())
        if len(verify_set) != 0:
            self.task_log.error('exiting. The following should not be set if instance.remark is set.')
            for p in verify_set:
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
    def verify_ace_sequence(self):
        if self.sequence == None:
            self.task_log.error('exiting. instance.sequence must be set before calling instance.add_ace()')
            exit(1)

    def verify_ace_protocol_options(self):
        '''
        Exit with error if mutually-exclusive options for icmp, igmp, tcp are set

        If self.protocol is not set appropriately, set it for the user and print a warning.
        '''
        if len(self.igmp_set()) > 1:
            self.task_log.error('exiting. igmp options are mututually-exclusive. Only one should be set, per ACE.')
            self.task_log.error('Got igmp options: {}'.format(sorted(self.igmp_set())))
            exit(1)

        verified = True
        all_protocol_options = set()
        all_protocol_options.update(self.icmp_set())
        all_protocol_options.update(self.igmp_set())
        all_protocol_options.update(self.tcp_set())
        if len(self.icmp_set()) != 0 and len(self.icmp_set()) != len(all_protocol_options):
            verified = False
        if len(self.igmp_set()) != 0 and len(self.igmp_set()) != len(all_protocol_options):
            verified = False
        if len(self.tcp_set()) != 0 and len(self.tcp_set()) != len(all_protocol_options):
            verified = False
        if verified == False:
            self.task_log.error('exiting. options for only one of icmp, igmp, tcp should be set.')
            self.task_log.error('The following options were set:')
            for p in sorted(all_protocol_options):
                self.task_log.error('   property {}: {}'.format(p, self.properties[p]))
            exit(1)
        if len(self.icmp_set()) != 0 and self.protocol != 'icmp':
            self.task_log.warning('setting instance.protocol = icmp due to icmp options are set')
            self.protocol = 'icmp'
        if len(self.igmp_set()) != 0 and self.protocol != 'igmp':
            self.task_log.warning('setting instance.protocol = igmp due to igmp options are set')
            self.protocol = 'igmp'
        if len(self.tcp_set()) != 0 and self.protocol != 'tcp':
            self.task_log.warning('setting instance.protocol = tcp due to tcp options are set')
            self.protocol = 'tcp'

    def verify_ace_icmp_echo(self):
        if self.afi == 'ipv6' and self.icmp_echo != None:
            self.task_log.error('exiting. icmp_echo is not valid when afi is set to ipv6.  Use icmp_echo_request instead.')
            exit(1)

    def verify_ace(self):
        if self.protocol == None:
            self.task_log.error('exiting. instance.protocol must be set before calling intance.add_ace()')
            exit(1)
        self.verify_ace_afi()
        self.verify_ace_remark()
        self.verify_ace_grant()
        self.verify_ace_destination()
        self.verify_ace_protocol_options()
        self.verify_ace_sequence()
        self.verify_ace_source()
        self.verify_ace_icmp_echo()

    def add_ace(self):
        d = dict()
        if self.remark != None:
            self.verify_ace_remark()
            d['remark'] = self.remark
            d['sequence'] = self.sequence
            self.aces.append(deepcopy(d))
            self.init_properties_ace()
            return

        self.verify_ace()
        destination = dict()
        source = dict()
        icmp = dict()
        igmp = dict()
        tcp = dict()
        protocol_options = dict()
        for p in self.properties_source:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                if mapped_p in ['eq', 'neq', 'gt', 'lt']:
                    source['port_protocol'] = dict()
                    source['port_protocol'][mapped_p] = self.properties[p]
                elif mapped_p in ['start', 'end']:
                    try:
                        source['port_protocol']['range'][mapped_p] = self.properties[p]
                    except:
                        source['port_protocol'] = dict()
                        source['port_protocol']['range'] = dict()
                        source['port_protocol']['range'][mapped_p] = self.properties[p]
                else:
                    source[mapped_p] = self.properties[p]
        for p in self.properties_destination:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                if mapped_p in ['eq', 'neq', 'gt', 'lt']:
                    destination['port_protocol'] = dict()
                    destination['port_protocol'][mapped_p] = self.properties[p]
                elif mapped_p in ['start', 'end']:
                    try:
                        destination['port_protocol']['range'][mapped_p] = self.properties[p]
                    except:
                        destination['port_protocol'] = dict()
                        destination['port_protocol']['range'] = dict()
                        destination['port_protocol']['range'][mapped_p] = self.properties[p]
                else:
                    destination[mapped_p] = self.properties[p]
        for p in self.properties_icmp:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                icmp[mapped_p] = self.properties[p]
        for p in self.properties_igmp:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                igmp[mapped_p] = self.properties[p]
        for p in self.properties_tcp:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                tcp[mapped_p] = self.properties[p]
        for p in self.properties_ace:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                d[mapped_p] = self.properties[p]
        if len(source) == 0:
            self.task_log.error('exiting. No source information was set')
            exit(1)
        if len(destination) == 0:
            self.task_log.error('exiting. No destination information was set')
            exit(1)
        if len(icmp) != 0:
            d['protocol_options'] = dict()
            d['protocol_options']['icmp'] = icmp
        if len(igmp) != 0:
            d['protocol_options'] = dict()
            d['protocol_options']['igmp'] = igmp
        if len(tcp) != 0:
            d['protocol_options'] = dict()
            d['protocol_options']['tcp'] = tcp
        d['destination'] = destination
        d['source'] = source

        self.aces.append(deepcopy(d))
        self.init_properties_ace()

    def verify_acl(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.add_acl()')
            exit(1)
        if self.afi == None:
            self.task_log.error('exiting. call instance.afi before calling instance.add_acl()')
            exit(1)

    def add_acl(self):
        self.verify_acl()
        d = dict()
        d['name'] = self.name
        if len(self.aces) != 0:
            d['aces'] = self.aces.copy()
        if self.afi == 'ipv4':
            self.acls_ipv4.append(deepcopy(d))
        if self.afi == 'ipv6':
            self.acls_ipv6.append(deepcopy(d))
        self.init_properties_acl()

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        populate and append dict() to self.ansible_task[self.ansible_module]['config']

        '''
        self.final_verification()

        config = list()
        if len(self.acls_ipv4) != 0:
            d = dict()
            d['afi'] = 'ipv4'
            d['acls'] = self.acls_ipv4.copy()
            config.append(deepcopy(d))
        if len(self.acls_ipv6) != 0:
            d = dict()
            d['afi'] = 'ipv6'
            d['acls'] = self.acls_ipv6.copy()
            config.append(deepcopy(d))
        self.ansible_task[self.ansible_module]['config'] = config.copy()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['state'] = self.state

    def verify_nxos_acls_afi(self, x, parameter='afi'):
        verify_set = self.nxos_acls_valid_afi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_acls_afi'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_acls_dscp(self, x, parameter='dscp'):
        verify_set = self.nxos_acls_valid_dscp
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_acls_dscp'
        expectation = ','.join(sorted([str(x) for x in verify_set]))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_acls_prefix(self, x, parameter='prefix'):
        source_class = self.class_name
        source_method = 'verify_nxos_acls_prefix'
        expectation = 'ipv4 or ipv6 prefix <= 31 (ipv4) and <= 127 (ipv6) e.g. 1.1.1.0/30, 2001::0/126'
        if self.is_ipv4_network(x):
            return
        if self.is_ipv6_network(x):
            return
        self.fail(source_class, source_method, x, parameter, expectation)            

    def verify_nxos_acls_state(self, x, parameter='state'):
        verify_set = self.nxos_acls_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_acls_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)



    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_acls_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def destination_address(self):
        return self.properties['destination_address']
    @destination_address.setter
    def destination_address(self, x):
        parameter = 'destination_address'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def destination_any(self):
        return self.properties['destination_any']
    @destination_any.setter
    def destination_any(self, x):
        parameter = 'destination_any'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def destination_host(self):
        return self.properties['destination_host']
    @destination_host.setter
    def destination_host(self, x):
        parameter = 'destination_host'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def destination_port_eq(self):
        return self.properties['destination_port_eq']
    @destination_port_eq.setter
    def destination_port_eq(self, x):
        parameter = 'destination_port_eq'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def destination_port_gt(self):
        return self.properties['destination_port_gt']
    @destination_port_gt.setter
    def destination_port_gt(self, x):
        parameter = 'destination_port_gt'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def destination_port_lt(self):
        return self.properties['destination_port_lt']
    @destination_port_lt.setter
    def destination_port_lt(self, x):
        parameter = 'destination_port_lt'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def destination_port_neq(self):
        return self.properties['destination_port_neq']
    @destination_port_neq.setter
    def destination_port_neq(self, x):
        parameter = 'destination_port_neq'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def destination_port_range_end(self):
        return self.properties['destination_port_range_end']
    @destination_port_range_end.setter
    def destination_port_range_end(self, x):
        parameter = 'destination_port_range_end'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def destination_port_range_start(self):
        return self.properties['destination_port_range_start']
    @destination_port_range_start.setter
    def destination_port_range_start(self, x):
        parameter = 'destination_port_range_start'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def destination_prefix(self):
        return self.properties['destination_prefix']
    @destination_prefix.setter
    def destination_prefix(self, x):
        parameter = 'destination_prefix'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_acls_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def destination_wildcard_bits(self):
        return self.properties['destination_wildcard_bits']
    @destination_wildcard_bits.setter
    def destination_wildcard_bits(self, x):
        parameter = 'destination_wildcard_bits'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def dscp(self):
        return self.properties['dscp']
    @dscp.setter
    def dscp(self, x):
        parameter = 'dscp'
        if self.set_none(x, parameter):
            return
        x = str(x)
        self.verify_nxos_acls_dscp(x, parameter)
        self.properties[parameter] = x

    @property
    def fragments(self):
        return self.properties['fragments']
    @fragments.setter
    def fragments(self, x):
        parameter = 'fragments'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def grant(self):
        return self.properties['grant']
    @grant.setter
    def grant(self, x):
        parameter = 'grant'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def icmp_administratively_prohibited(self):
        return self.properties['icmp_administratively_prohibited']
    @icmp_administratively_prohibited.setter
    def icmp_administratively_prohibited(self, x):
        parameter = 'icmp_administratively_prohibited'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_alternate_address(self):
        return self.properties['icmp_alternate_address']
    @icmp_alternate_address.setter
    def icmp_alternate_address(self, x):
        parameter = 'icmp_alternate_address'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_conversion_error(self):
        return self.properties['icmp_conversion_error']
    @icmp_conversion_error.setter
    def icmp_conversion_error(self, x):
        parameter = 'icmp_conversion_error'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_dod_net_prohibited(self):
        return self.properties['icmp_dod_net_prohibited']
    @icmp_dod_net_prohibited.setter
    def icmp_dod_net_prohibited(self, x):
        parameter = 'icmp_dod_net_prohibited'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_echo_request(self):
        return self.properties['icmp_echo_request']
    @icmp_echo_request.setter
    def icmp_echo_request(self, x):
        parameter = 'icmp_echo_request'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_echo(self):
        return self.properties['icmp_echo']
    @icmp_echo.setter
    def icmp_echo(self, x):
        parameter = 'icmp_echo'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_echo_reply(self):
        return self.properties['icmp_echo_reply']
    @icmp_echo_reply.setter
    def icmp_echo_reply(self, x):
        parameter = 'icmp_echo_reply'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_general_parameter_problem(self):
        return self.properties['icmp_general_parameter_problem']
    @icmp_general_parameter_problem.setter
    def icmp_general_parameter_problem(self, x):
        parameter = 'icmp_general_parameter_problem'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_host_isolated(self):
        return self.properties['icmp_host_isolated']
    @icmp_host_isolated.setter
    def icmp_host_isolated(self, x):
        parameter = 'icmp_host_isolated'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_host_precedence_unreachable(self):
        return self.properties['icmp_host_precedence_unreachable']
    @icmp_host_precedence_unreachable.setter
    def icmp_host_precedence_unreachable(self, x):
        parameter = 'icmp_host_precedence_unreachable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_host_redirect(self):
        return self.properties['icmp_host_redirect']
    @icmp_host_redirect.setter
    def icmp_host_redirect(self, x):
        parameter = 'icmp_host_redirect'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_host_tos_redirect(self):
        return self.properties['icmp_host_tos_redirect']
    @icmp_host_tos_redirect.setter
    def icmp_host_tos_redirect(self, x):
        parameter = 'icmp_host_tos_redirect'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_host_tos_unreachable(self):
        return self.properties['icmp_host_tos_unreachable']
    @icmp_host_tos_unreachable.setter
    def icmp_host_tos_unreachable(self, x):
        parameter = 'icmp_host_tos_unreachable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_host_unknown(self):
        return self.properties['icmp_host_unknown']
    @icmp_host_unknown.setter
    def icmp_host_unknown(self, x):
        parameter = 'icmp_host_unknown'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_host_unreachable(self):
        return self.properties['icmp_host_unreachable']
    @icmp_host_unreachable.setter
    def icmp_host_unreachable(self, x):
        parameter = 'icmp_host_unreachable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_information_reply(self):
        return self.properties['icmp_information_reply']
    @icmp_information_reply.setter
    def icmp_information_reply(self, x):
        parameter = 'icmp_information_reply'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_information_request(self):
        return self.properties['icmp_information_request']
    @icmp_information_request.setter
    def icmp_information_request(self, x):
        parameter = 'icmp_information_request'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_mask_reply(self):
        return self.properties['icmp_mask_reply']
    @icmp_mask_reply.setter
    def icmp_mask_reply(self, x):
        parameter = 'icmp_mask_reply'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_mask_request(self):
        return self.properties['icmp_mask_request']
    @icmp_mask_request.setter
    def icmp_mask_request(self, x):
        parameter = 'icmp_mask_request'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_message_code(self):
        return self.properties['icmp_message_code']
    @icmp_message_code.setter
    def icmp_message_code(self, x):
        parameter = 'icmp_message_code'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_message_type(self):
        return self.properties['icmp_message_type']
    @icmp_message_type.setter
    def icmp_message_type(self, x):
        parameter = 'icmp_message_type'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_mobile_redirect(self):
        return self.properties['icmp_mobile_redirect']
    @icmp_mobile_redirect.setter
    def icmp_mobile_redirect(self, x):
        parameter = 'icmp_mobile_redirect'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_net_redirect(self):
        return self.properties['icmp_net_redirect']
    @icmp_net_redirect.setter
    def icmp_net_redirect(self, x):
        parameter = 'icmp_net_redirect'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_net_tos_redirect(self):
        return self.properties['icmp_net_tos_redirect']
    @icmp_net_tos_redirect.setter
    def icmp_net_tos_redirect(self, x):
        parameter = 'icmp_net_tos_redirect'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_net_tos_unreachable(self):
        return self.properties['icmp_net_tos_unreachable']
    @icmp_net_tos_unreachable.setter
    def icmp_net_tos_unreachable(self, x):
        parameter = 'icmp_net_tos_unreachable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_net_unreachable(self):
        return self.properties['icmp_net_unreachable']
    @icmp_net_unreachable.setter
    def icmp_net_unreachable(self, x):
        parameter = 'icmp_net_unreachable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_network_unknown(self):
        return self.properties['icmp_network_unknown']
    @icmp_network_unknown.setter
    def icmp_network_unknown(self, x):
        parameter = 'icmp_network_unknown'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_no_room_for_option(self):
        return self.properties['icmp_no_room_for_option']
    @icmp_no_room_for_option.setter
    def icmp_no_room_for_option(self, x):
        parameter = 'icmp_no_room_for_option'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_option_missing(self):
        return self.properties['icmp_option_missing']
    @icmp_option_missing.setter
    def icmp_option_missing(self, x):
        parameter = 'icmp_option_missing'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_packet_too_big(self):
        return self.properties['icmp_packet_too_big']
    @icmp_packet_too_big.setter
    def icmp_packet_too_big(self, x):
        parameter = 'icmp_packet_too_big'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_parameter_problem(self):
        return self.properties['icmp_parameter_problem']
    @icmp_parameter_problem.setter
    def icmp_parameter_problem(self, x):
        parameter = 'icmp_parameter_problem'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_port_unreachable(self):
        return self.properties['icmp_port_unreachable']
    @icmp_port_unreachable.setter
    def icmp_port_unreachable(self, x):
        parameter = 'icmp_port_unreachable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_precedence_unreachable(self):
        return self.properties['icmp_precedence_unreachable']
    @icmp_precedence_unreachable.setter
    def icmp_precedence_unreachable(self, x):
        parameter = 'icmp_precedence_unreachable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_protocol_unreachable(self):
        return self.properties['icmp_protocol_unreachable']
    @icmp_protocol_unreachable.setter
    def icmp_protocol_unreachable(self, x):
        parameter = 'icmp_protocol_unreachable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_reassembly_timeout(self):
        return self.properties['icmp_reassembly_timeout']
    @icmp_reassembly_timeout.setter
    def icmp_reassembly_timeout(self, x):
        parameter = 'icmp_reassembly_timeout'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_redirect(self):
        return self.properties['icmp_redirect']
    @icmp_redirect.setter
    def icmp_redirect(self, x):
        parameter = 'icmp_redirect'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_router_advertisement(self):
        return self.properties['icmp_router_advertisement']
    @icmp_router_advertisement.setter
    def icmp_router_advertisement(self, x):
        parameter = 'icmp_router_advertisement'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_router_solicitation(self):
        return self.properties['icmp_router_solicitation']
    @icmp_router_solicitation.setter
    def icmp_router_solicitation(self, x):
        parameter = 'icmp_router_solicitation'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_source_quench(self):
        return self.properties['icmp_source_quench']
    @icmp_source_quench.setter
    def icmp_source_quench(self, x):
        parameter = 'icmp_source_quench'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_source_route_failed(self):
        return self.properties['icmp_source_route_failed']
    @icmp_source_route_failed.setter
    def icmp_source_route_failed(self, x):
        parameter = 'icmp_source_route_failed'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_time_exceeded(self):
        return self.properties['icmp_time_exceeded']
    @icmp_time_exceeded.setter
    def icmp_time_exceeded(self, x):
        parameter = 'icmp_time_exceeded'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_timestamp_reply(self):
        return self.properties['icmp_timestamp_reply']
    @icmp_timestamp_reply.setter
    def icmp_timestamp_reply(self, x):
        parameter = 'icmp_timestamp_reply'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_timestamp_request(self):
        return self.properties['icmp_timestamp_request']
    @icmp_timestamp_request.setter
    def icmp_timestamp_request(self, x):
        parameter = 'icmp_timestamp_request'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_traceroute(self):
        return self.properties['icmp_traceroute']
    @icmp_traceroute.setter
    def icmp_traceroute(self, x):
        parameter = 'icmp_traceroute'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_ttl_exceeded(self):
        return self.properties['icmp_ttl_exceeded']
    @icmp_ttl_exceeded.setter
    def icmp_ttl_exceeded(self, x):
        parameter = 'icmp_ttl_exceeded'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def icmp_unreachable(self):
        return self.properties['icmp_unreachable']
    @icmp_unreachable.setter
    def icmp_unreachable(self, x):
        parameter = 'icmp_unreachable'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def igmp_dvmrp(self):
        return self.properties['igmp_dvmrp']
    @igmp_dvmrp.setter
    def igmp_dvmrp(self, x):
        parameter = 'igmp_dvmrp'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def igmp_host_query(self):
        return self.properties['igmp_host_query']
    @igmp_host_query.setter
    def igmp_host_query(self, x):
        parameter = 'igmp_host_query'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def igmp_host_report(self):
        return self.properties['igmp_host_report']
    @igmp_host_report.setter
    def igmp_host_report(self, x):
        parameter = 'igmp_host_report'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def log(self):
        return self.properties['log']
    @log.setter
    def log(self, x):
        parameter = 'log'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def precedence(self):
        return self.properties['precedence']
    @precedence.setter
    def precedence(self, x):
        parameter = 'precedence'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def protocol(self):
        return self.properties['protocol']
    @protocol.setter
    def protocol(self, x):
        parameter = 'protocol'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def remark(self):
        return self.properties['remark']
    @remark.setter
    def remark(self, x):
        parameter = 'remark'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def sequence(self):
        return self.properties['sequence']
    @sequence.setter
    def sequence(self, x):
        parameter = 'sequence'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def source_address(self):
        return self.properties['source_address']
    @source_address.setter
    def source_address(self, x):
        parameter = 'source_address'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def source_any(self):
        return self.properties['source_any']
    @source_any.setter
    def source_any(self, x):
        parameter = 'source_any'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def source_host(self):
        return self.properties['source_host']
    @source_host.setter
    def source_host(self, x):
        parameter = 'source_host'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def source_port_eq(self):
        return self.properties['source_port_eq']
    @source_port_eq.setter
    def source_port_eq(self, x):
        parameter = 'source_port_eq'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def source_port_gt(self):
        return self.properties['source_port_gt']
    @source_port_gt.setter
    def source_port_gt(self, x):
        parameter = 'source_port_gt'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def source_port_lt(self):
        return self.properties['source_port_lt']
    @source_port_lt.setter
    def source_port_lt(self, x):
        parameter = 'source_port_lt'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def source_port_neq(self):
        return self.properties['source_port_neq']
    @source_port_neq.setter
    def source_port_neq(self, x):
        parameter = 'source_port_neq'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def source_port_range_end(self):
        return self.properties['source_port_range_end']
    @source_port_range_end.setter
    def source_port_range_end(self, x):
        parameter = 'source_port_range_end'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def source_port_range_start(self):
        return self.properties['source_port_range_start']
    @source_port_range_start.setter
    def source_port_range_start(self, x):
        parameter = 'source_port_range_start'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def source_prefix(self):
        return self.properties['source_prefix']
    @source_prefix.setter
    def source_prefix(self, x):
        parameter = 'source_prefix'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_acls_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def source_wildcard_bits(self):
        return self.properties['source_wildcard_bits']
    @source_wildcard_bits.setter
    def source_wildcard_bits(self, x):
        parameter = 'source_wildcard_bits'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def tcp_ack(self):
        return self.properties['tcp_ack']
    @tcp_ack.setter
    def tcp_ack(self, x):
        parameter = 'tcp_ack'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def tcp_established(self):
        return self.properties['tcp_established']
    @tcp_established.setter
    def tcp_established(self, x):
        parameter = 'tcp_established'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def tcp_fin(self):
        return self.properties['tcp_fin']
    @tcp_fin.setter
    def tcp_fin(self, x):
        parameter = 'tcp_fin'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def tcp_psh(self):
        return self.properties['tcp_psh']
    @tcp_psh.setter
    def tcp_psh(self, x):
        parameter = 'tcp_psh'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def tcp_rst(self):
        return self.properties['tcp_rst']
    @tcp_rst.setter
    def tcp_rst(self, x):
        parameter = 'tcp_rst'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def tcp_syn(self):
        return self.properties['tcp_syn']
    @tcp_syn.setter
    def tcp_syn(self, x):
        parameter = 'tcp_syn'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def tcp_urg(self):
        return self.properties['tcp_urg']
    @tcp_urg.setter
    def tcp_urg(self, x):
        parameter = 'tcp_urg'
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
        self.verify_nxos_acls_state(x, parameter)
        self.properties[parameter] = x
