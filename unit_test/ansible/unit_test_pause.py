#!/usr/bin/env python3
# unit_test/ansible/unit_test_pause.py
our_version = 100
'''
Name: unit_test_pause.py

Description:

Generates Ansible playbook conformant with Ansible module: pause

Prerequisites:
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_evpn_global import NxosEvpnGlobal

ansible_module = 'pause'
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

def pause_10():
    task = AnsTaskPause(log)
    task.seconds = 10
    task.task_name = 'pause_10_seconds'
    task.update()
    return task
def pause_20():
    task = AnsTaskPause(log)
    task.seconds = 20
    task.task_name = 'pause_20_seconds'
    task.update()
    return task

def pause_playbook_vars(pb):
    pb.ansible_connection = None
    pb.ansible_password = None
    pb.ansible_network_os = None
    pb.ansible_host_key_checking = None
    pb.ansible_ssh_pass = None
    pb.ansible_ssh_common_args = None
    pb.ansible_paramiko_pty = None
    pb.ansible_httpapi_validate_certs = None
    pb.ansible_httpapi_use_ssl = None

pb = playbook()
pb.add_task(pause_10())
pb.add_task(pause_20())
pb.append_playbook()
pause_playbook_vars(pb)
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
