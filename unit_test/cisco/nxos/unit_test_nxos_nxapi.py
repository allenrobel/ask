#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_nxapi.py
our_version = 100

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_nxapi import NxosNxapi

ansible_module = 'nxos_nxapi'
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
    task_name = add_item_to_name('http', task.http, task_name)
    task_name = add_item_to_name('http_port', task.http_port, task_name)
    task_name = add_item_to_name('https', task.https, task_name)
    task_name = add_item_to_name('https_port', task.https_port, task_name)
    task_name = add_item_to_name('sandbox', task.sandbox, task_name)
    task_name = add_item_to_name('ssl_strong_ciphers', task.ssl_strong_ciphers, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('tlsv1_0', task.tlsv1_0, task_name)
    task_name = add_item_to_name('tlsv1_1', task.tlsv1_1, task_name)
    task_name = add_item_to_name('tlsv1_2', task.tlsv1_2, task_name)
    task.task_name = task_name

def add_task(pb):
    task = NxosNxapi(log)
    task.http = 'yes'
    task.http_port = 80
    task.https = 'yes'
    task.https_port = 443
    #task.sandbox = 'yes'          # Not supported on N9K as of 9.3(6)
    task.ssl_strong_ciphers = 'no'
    task.state = 'present'
    task.tlsv1_0 = 'yes'
    task.tlsv1_1 = 'yes'
    task.tlsv1_2 = 'yes'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))