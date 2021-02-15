#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_l3_interface.py
our_version = 105
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_l3_interface import NxosL3Interface

ansible_module = 'nxos_l3_interface'
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

def add_item_to_name(item, item_value, name):
    value = ''
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
    else:
        value = name
    return value

def add_task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('name', task.name, task_name)
    task_name = add_item_to_name('ipv4', task.ipv4, task_name)
    task_name = add_item_to_name('ipv6', task.ipv6, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task.task_name = task_name

def add_task_interface_dual_stack(pb):
    task = NxosL3Interface(log)
    task.name = 'Ethernet1/1'
    task.ipv4 = '10.1.1.1/24'
    task.ipv6 = '2001:aaaa::1/64'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_interface_ipv4(pb):
    task = NxosL3Interface(log)
    task.name = 'Ethernet1/2'
    task.ipv4 = '10.2.1.1/24'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_interface_ipv6(pb):
    task = NxosL3Interface(log)
    task.name = 'Ethernet1/3'
    task.ipv6 = '2003:cccc::3/64'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_interface_dual_stack(pb)
add_task_interface_ipv4(pb)
add_task_interface_ipv6(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
