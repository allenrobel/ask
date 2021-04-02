#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_ntp_auth.py
our_version = 103

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

def add_task_name(task):
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    for key in sorted(task.scriptkit_properties):
        task.append_to_task_name(key)

def add_task(pb):
    task = NxosNtpAuth(log)
    task.auth_type = 'text'
    task.authentication = 'on'
    task.key_id = 12345
    task.md5string = 'foobarbizbang'
    task.state = 'present'
    task.trusted_key = True
    add_task_name(task)
    task.commit()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
