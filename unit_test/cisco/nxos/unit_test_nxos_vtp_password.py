#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vtp_password.py
our_version = 100

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vtp_password import NxosVtpPassword

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

def task_vtp_password_add(pb):
    task = NxosVtpPassword(log)
    task.vtp_password = 'my_vtp_password'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def task_vtp_password_remove(pb):
    task = NxosVtpPassword(log)
    task.state = 'absent'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

ansible_module = 'nxos_vtp_password'
ansible_host = 'dc-101' # must be in ansible inventory
log_level_console = 'INFO'
log_level_file = 'DEBUG'
log = Log('unit_test_{}'.format(ansible_module), log_level_console, log_level_file)

pb = playbook()
task_vtp_password_add(pb)
#task_vtp_password_remove(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote playbook {}'.format(pb.file))
