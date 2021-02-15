#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_ntp.py
our_version = 107

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_ntp import NxosNtp

ansible_module = 'nxos_ntp'
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
    task_name = add_item_to_name('key_id', task.key_id, task_name)
    task_name = add_item_to_name('peer', task.peer, task_name)
    task_name = add_item_to_name('prefer', task.prefer, task_name)
    task_name = add_item_to_name('server', task.server, task_name)
    task_name = add_item_to_name('source_addr', task.source_addr, task_name)
    task_name = add_item_to_name('source_int', task.source_int, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('vrf', task.vrf, task_name)
    task.task_name = task_name

def add_task(pb):
    task = NxosNtp(log)
    task.key_id = 'asf123sd'
    task.peer = '172.29.167.1'
    task.prefer = 'enabled'
    task.server = '172.29.167.1'
    task.source_addr = '172.29.167.24'
    task.source_int = 'mgmt0'
    task.state = 'present'
    task.vrf = 'default'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
