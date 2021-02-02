#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_l2_interfaces.py
our_version = 101

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_l2_interfaces import NxosL2Interfaces

ansible_module = 'nxos_l2_interfaces'
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

def add_item_to_name(item, item_value, name):
    value = ''
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
    else:
        value = name
    return value

def add_task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('allowed_vlans', task.allowed_vlans, task_name)
    task_name = add_item_to_name('mode', task.mode, task_name)
    task_name = add_item_to_name('name', task.name, task_name)
    task_name = add_item_to_name('native_vlan', task.native_vlan, task_name)
    task_name = add_item_to_name('vlan', task.vlan, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task.task_name = task_name

def add_task_trunk_interface(pb):
    task = NxosL2Interfaces(log)
    task.name = 'Ethernet1/10'
    task.mode = 'trunk'
    task.native_vlan = 10
    task.allowed_vlans = '11,12,13'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_access_interface(pb):
    task = NxosL2Interfaces(log)
    task.name = 'Ethernet1/11'
    task.mode = 'access'
    task.vlan = 11
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_access_interface(pb)
add_task_trunk_interface(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
