#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_l2_interface.py
our_version = 103

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_l2_interface import NxosL2Interface

ansible_module = 'nxos_l2_interface'
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
    task_name = add_item_to_name('name', task.name, task_name)
    task_name = add_item_to_name('access_vlan', task.access_vlan, task_name)
    task_name = add_item_to_name('mode', task.mode, task_name)
    task_name = add_item_to_name('trunk_allowed_vlans', task.trunk_allowed_vlans, task_name)
    task_name = add_item_to_name('trunk_vlans', task.trunk_vlans, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task.task_name = task_name

def add_task_access_interface(pb):
    task = NxosL2Interface(log)
    task.name = 'Ethernet1/50'
    task.mode = 'access'
    task.access_vlan = 10
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_trunk_interface(pb):
    task = NxosL2Interface(log)
    task.name = 'Ethernet1/49'
    task.mode = 'trunk'
    task.trunk_allowed_vlans = '2,10-20'
    task.trunk_vlans = '3,30-31'
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_access_interface(pb)
add_task_trunk_interface(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
