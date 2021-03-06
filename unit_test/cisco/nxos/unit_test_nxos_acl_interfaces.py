#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_acl_interfaces.py
our_version = 105

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_acl_interfaces import NxosAclInterfaces

ansible_module = 'nxos_acl_interfaces'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.profile_nxos()
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_task_name(task):
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    for key in sorted(task.scriptkit_properties):
        task.append_to_task_name(key)

def ipv4_interface_acl(pb):
    task = NxosAclInterfaces(log)
    task.name = 'Ethernet1/36'
    task.acl_name = 'IPv4_ACL'
    task.afi = 'ipv4'
    task.acl_port = False
    task.acl_direction = 'in'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def ipv6_interface_acl(pb):
    task = NxosAclInterfaces(log)
    task.name = 'Ethernet1/36'
    task.acl_name = 'IPv6_ACL'
    task.afi = 'ipv6'
    task.acl_port = False
    task.acl_direction = 'in'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

ipv4_interface_acl(pb)
ipv6_interface_acl(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
