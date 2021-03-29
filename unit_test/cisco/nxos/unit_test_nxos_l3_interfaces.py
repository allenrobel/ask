#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_l3_interfaces.py
our_version = 107

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_l3_interfaces import NxosL3Interfaces
from ask.ansible.register_save import RegisterSave

ansible_module = 'nxos_l3_interfaces'
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

def dual_stack_interface(task):
    task.name = 'Ethernet1/32'
    task.ipv4_address = '10.1.1.1/24'
    task.ipv4_tag = 10
    task.add_ipv4()
    task.ipv4_address = '10.2.1.1/24'
    task.ipv4_tag = 20
    #task.ipv4_secondary = False # negative test
    task.ipv4_secondary = True
    task.add_ipv4()
    task.ipv6_address = '2001:aaaa::1/64'
    task.ipv6_tag = 10
    task.add_ipv6()
    task.ipv6_address = '2001:bbbb::1/64'
    task.ipv6_tag = 20
    task.add_ipv6()
    task.append_to_task_name('{} dual-stack'.format(task.name))
    task.add_interface()

def ipv4_interface(pb):
    task.name = 'Ethernet1/33'
    task.ipv4_address = '10.1.2.1/24'
    task.redirects = False
    task.unreachables = False
    task.add_ipv4()
    task.append_to_task_name('{} ipv4'.format(task.name))
    task.add_interface()

def ipv6_interface(pb):
    task.name = 'Ethernet1/34'
    task.ipv6_address = '2001:cccc::1/64'
    task.ipv6_tag = 30
    task.add_ipv6()
    task.append_to_task_name('{} ipv6'.format(task.name))
    task.add_interface()

def add_task_deleted(pb):
    task = NxosL3Interfaces(log)
    task.append_to_task_name('clear L3 interface config')
    for port in [32,33,34]:
        task.name = 'Ethernet1/{}'.format(port)
        task.append_to_task_name(task.name)
        task.add_interface()
    task.state = 'deleted'
    task.update()
    pb.add_task(task)

def add_task_parsed(pb):
    task = NxosL3Interfaces(log)
    task.running_config = '/tmp/parsed.cfg'
    task.state = 'parsed'
    task.register = 'parsed'
    add_task_name(task)
    task.update()
    pb.add_task(task)

    task = RegisterSave(log)
    task.filename = '/tmp/parsed_output.txt'
    task.var = 'parsed'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_deleted(pb)

task = NxosL3Interfaces(log)
task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
dual_stack_interface(task)
ipv4_interface(task)
ipv6_interface(task)
task.state = 'merged'
task.update()
pb.add_task(task)

#add_task_parsed(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
