#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_acls.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_acls import NxosAcls

ansible_module = 'nxos_acls'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.ansible_connection = 'httpapi' # httpapi, network_cli
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_ipv4_ace_10(task):
    task.afi = 'ipv4'
    task.grant = 'permit'
    task.protocol = 'ip'
    task.sequence = 10
    task.destination_address = '1.2.2.2'
    task.destination_wildcard_bits = '0.0.255.255'
    task.source_address = '1.1.1.1'
    task.source_wildcard_bits = '0.0.0.255'
    task.add_ace()
def add_ipv4_ace_20(task):
    task.afi = 'ipv4'
    task.grant = 'deny'
    task.sequence = 20
    task.protocol = 'ip'
    task.destination_address = '2.2.2.2'
    task.destination_wildcard_bits = '0.0.255.255'
    task.source_address = '2.1.1.1'
    task.source_wildcard_bits = '0.0.0.255'
    task.add_ace()
def add_ipv4_ace_30(task):
    task.afi = 'ipv4'
    task.grant = 'deny'
    task.sequence = 30
    task.protocol = 'igmp'
    task.igmp_host_query = 'yes'
    task.destination_address = '2.2.2.2'
    task.destination_wildcard_bits = '0.0.255.255'
    task.source_address = '2.1.1.1'
    task.source_wildcard_bits = '0.0.0.255'
    task.add_ace()
def add_ipv4_ace_40(task):
    task.afi = 'ipv4'
    task.grant = 'deny'
    task.sequence = 40
    task.protocol = 'igmp'
    task.igmp_host_report = 'yes'
    task.destination_address = '2.2.2.2'
    task.destination_wildcard_bits = '0.0.255.255'
    task.source_address = '2.1.1.1'
    task.source_wildcard_bits = '0.0.0.255'
    task.add_ace()
def add_ipv4_ace_50(task):
    task.afi = 'ipv4'
    task.grant = 'deny'
    task.sequence = 50
    task.protocol = 'icmp'
    task.icmp_echo = 'yes'
    task.destination_address = '2.2.2.2'
    task.destination_wildcard_bits = '0.0.255.255'
    task.source_address = '2.1.1.1'
    task.source_wildcard_bits = '0.0.0.255'
    task.add_ace()

def add_ipv6_ace_10(task):
    task.afi = 'ipv6'
    task.grant = 'permit'
    task.sequence = 10
    task.protocol = 'ipv6'
    task.destination_prefix = '2001:2:2:2::/64'
    task.source_prefix = '2001:1:1:1::/64'
    task.add_ace()
def add_ipv6_ace_20(task):
    task.afi = 'ipv6'
    task.grant = 'deny'
    task.sequence = 20
    task.protocol = 'ipv6'
    task.destination_prefix = '2002:2:2:2::/64'
    task.source_prefix = '2002:1:1:1::/64'
    task.add_ace()
def add_ipv6_ace_30(task):
    task.afi = 'ipv6'
    task.grant = 'deny'
    task.sequence = 30
    task.protocol = 'icmp'
    task.icmp_echo_reply = 'yes'
    task.destination_prefix = '2002:2:2:2::/64'
    task.source_prefix = '2002:1:1:1::/64'
    task.add_ace()
def add_ipv6_ace_40(task):
    task.afi = 'ipv6'
    task.grant = 'deny'
    task.sequence = 40
    task.protocol = 'icmp'
    task.icmp_echo_request = 'yes'
    task.destination_prefix = '2002:2:2:2::/64'
    task.source_prefix = '2002:1:1:1::/64'
    task.add_ace()

pb = playbook()
task = NxosAcls(log)

add_ipv4_ace_10(task)
add_ipv4_ace_20(task)
add_ipv4_ace_30(task)
add_ipv4_ace_40(task)
add_ipv4_ace_50(task)
task.name = 'IPv4_ACL'
task.add_acl()

add_ipv6_ace_10(task)
add_ipv6_ace_20(task)
add_ipv6_ace_30(task)
add_ipv6_ace_40(task)
task.name = 'IPv6_ACL'
task.add_acl()

task.state = 'merged'
task.update()
pb.add_task(task)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
