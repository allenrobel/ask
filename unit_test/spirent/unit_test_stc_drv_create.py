#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_drv_create.py
our_version = 101
'''
Name: unit_test_stc_drv_create.py

Description:

Generates Ansible playbook conformant with Spirent Ansible module: stc
This playbook creates Spirent device
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.spirent.stc_drv_create import StcDrvCreate

ansible_module = 'stc_drv_create'
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

def add_task_stc_drv_create_default(pb):
    task = StcDrvCreate(log)
    task.update()
    pb.add_task(task)

def add_task_stc_drv_create_custom(pb):
    task = StcDrvCreate(log)
    task.drv_name = "Dropped Frames DRV Custom Select Properties"
    task.task_name = 'create DRV with custom select_properties'
    task.select_properties = 'StreamBlock.DroppedFrameCount'
    task.select_properties = 'StreamBlock.DroppedFrameDuration'
    task.sort_by = "StreamBlock.DroppedFrameCount"
    #task.sort_by = 'StreamBlock.TxFrameCount' # negative test, sort_by not in select_properties
    #task.sort_by = 'StreamBlock.FooBar' # negative test, unknown select_property
    task.sort_direction = "DESCENDING"
    task.disable_auto_grouping = False
    task.reset_existing = True
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_stc_drv_create_default(pb)
add_task_stc_drv_create_custom(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
