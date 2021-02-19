#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_drv_save.py
our_version = 100
'''
Name: unit_test_stc_drv_save.py

Description:

Generates Ansible playbook conformant with Spirent Ansible module: stc
This playbook creates Spirent device

Prerequisites:

A playbook created with stc_session_gen.py must be run prior to running the playbook created with this script
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.spirent.stc_drv_save import StcDrvSave

ansible_module = 'stc_drv_save'
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.profile_spirent()
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = 'unit_test_{}'.format(ansible_module)
    pb.add_host('labserver-2001')
    return pb

def add_task_stc_drv_save(pb):
    task = StcDrvSave(log)
    #task.drv_name = "Dropped Frames DRV" # if not using default, change drv_name to match drv_create
    task.task_name = 'save DRV'
    task.register = 'RxResults'
    task.filename = '/tmp/drv_save.json'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_stc_drv_save(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
