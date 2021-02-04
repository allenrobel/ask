#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_ntp_options.py
our_version = 100

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_ntp_options import NxosNtpOptions

ansible_module = 'nxos_ntp_options'
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
    task_name = add_item_to_name('logging', task.logging, task_name)
    task_name = add_item_to_name('master', task.master, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('stratum', task.stratum, task_name)
    task.task_name = task_name

def add_task(pb):
    task = NxosNtpOptions(log)
    task.logging = 'yes'
    task.master = 'yes'
    task.state = 'present'
    task.stratum = 10
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
