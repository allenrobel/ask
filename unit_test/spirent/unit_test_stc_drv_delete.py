#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_drv_delete.py
our_version = 101
'''
****************************
unit_test_stc_drv_delete.py
****************************

Description
-----------

Generates Ansible playbook conformant with Spirent Ansible module: stc
This playbook deletes a Dynamic Result View (DRV)
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.spirent.stc_drv_delete import StcDrvDelete

ansible_module = 'stc_drv_delete'
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = 'unit_test_{}'.format(ansible_module)
    pb.ansible_connection = 'paramiko'
    pb.ansible_password = None
    pb.ansible_network_os = None
    pb.ansible_host_key_checking = 'no'
    pb.ansible_ssh_pass = 'spirent'
    pb.ansible_ssh_common_args = '/bin/ssh'
    pb.ansible_paramiko_pty = 'no'
    pb.ansible_httpapi_validate_certs = None
    pb.ansible_httpapi_use_ssl = None
    pb.add_host('labserver-2001')
    return pb

def add_task_stc_drv_delete_default(pb):
    task = StcDrvDelete(log)
    task.task_name = 'delete DRV default'
    task.update()
    pb.add_task(task)

def add_task_stc_drv_delete_custom(pb):
    task = StcDrvDelete(log)
    task.task_name = 'delete DRV custom'
    task.drv_name = "myDRV"
    task.reset_existing = True
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_stc_drv_delete_default(pb)
add_task_stc_drv_delete_custom(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
