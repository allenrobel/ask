#!/usr/bin/env python3
# unit_test/ansible/unit_test_pause.py
our_version = 101
'''
==================
unit_test_pause.py
==================

Description
-----------

Generates Ansible playbook conformant with Ansible module: pause
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.ansible.pause import Pause

ansible_module = 'pause'
ansible_host = 'localhost'
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.ansible_connection = 'local'
    pb.ansible_password = None
    pb.ansible_network_os = None
    pb.ansible_host_key_checking = None
    pb.ansible_ssh_pass = None
    pb.ansible_ssh_common_args = None
    pb.ansible_paramiko_pty = None
    pb.ansible_httpapi_validate_certs = None
    pb.ansible_httpapi_use_ssl = None
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{}'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def pause_10(pb):
    task = Pause(log)
    task.seconds = 10
    task.task_name = 'pause_{}_seconds'.format(task.seconds)
    task.update()
    pb.add_task(task)

def pause_20(pb):
    task = Pause(log)
    task.seconds = 20
    task.task_name = 'pause_{}_seconds'.format(task.seconds)
    task.update()
    pb.add_task(task)

pb = playbook()
pause_10(pb)
pause_20(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
