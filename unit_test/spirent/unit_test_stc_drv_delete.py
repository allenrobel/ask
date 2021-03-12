#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_drv_delete.py
our_version = 102
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
ansible_host = 'labserver-2001'
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.profile_spirent()
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = 'unit_test_{}'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_task_name(task):
    task.append_to_task_name('{} v{}, {}'.format(ansible_module, our_version, ansible_host))
    for key in sorted(task.scriptkit_properties):
        task.append_to_task_name(key)

def add_task_stc_drv_delete_default(pb):
    task = StcDrvDelete(log)
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_stc_drv_delete_custom(pb):
    task = StcDrvDelete(log)
    task.drv_name = "myDRV"
    task.reset_existing = True
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_stc_drv_delete_default(pb)
add_task_stc_drv_delete_custom(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
