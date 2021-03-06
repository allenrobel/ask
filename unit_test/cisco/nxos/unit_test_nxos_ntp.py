#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_ntp.py
our_version = 108

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

def add_task_name(task):
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    for key in sorted(task.properties_set):
        task.append_to_task_name(key)

def add_task(pb):
    task = NxosNtp(log)
    task.key_id = 10
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
