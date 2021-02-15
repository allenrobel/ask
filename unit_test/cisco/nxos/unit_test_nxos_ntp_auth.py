#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_ntp_auth.py
our_version = 101

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_ntp_auth import NxosNtpAuth

ansible_module = 'nxos_ntp_auth'
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

def task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('auth_type', task.auth_type, task_name)
    task_name = add_item_to_name('authentication', task.authentication, task_name)
    task_name = add_item_to_name('key_id', task.key_id, task_name)
    task_name = add_item_to_name('md5string', task.md5string, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('trusted_key', task.trusted_key, task_name)
    task.task_name = task_name

def add_task(pb):
    task = NxosNtpAuth(log)
    task.auth_type = 'text'
    task.authentication = 'on'
    task.key_id = 12345
    task.md5string = 'foobarbizbang'
    task.state = 'present'
    task.trusted_key = 'true'
    task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
