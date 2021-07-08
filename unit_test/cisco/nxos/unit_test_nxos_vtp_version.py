#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vtp_version.py
our_version = 100

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vtp_version import NxosVtpVersion


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

def example(pb):
    task = NxosVtpVersion(log)
    task.version = 2
    add_task_name(task)
    task.commit()
    pb.add_task(task)

ansible_module = 'nxos_vtp_version'
ansible_host = 'dc-101' # must be in ansible inventory
log_level_console = 'INFO'
log_level_file = 'DEBUG'
log = Log('unit_test_{}'.format(ansible_module), log_level_console, log_level_file)

pb = playbook()
example(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote playbook {}'.format(pb.file))
