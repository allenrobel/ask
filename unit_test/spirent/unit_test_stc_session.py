#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_session.py
our_version = 101
'''
****************************
unit_test_stc_session.py
****************************

Description
-----------
Generates Ansible playbook conformant with Spirent Ansible module: stc

This playbook creates a session to a Spirent LabServer.

Prerequisites
-------------

    1.  To run the playbook generated by this script,
        Spirent's Ansible libraries, and their prerequisites,
        must be installed.

        https://github.com/Spirent/stc-ansible

'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.spirent.stc_session import StcSession

ansible_module = 'stc_session'
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.profile_spirent()
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = 'unit_test_{}'.format(ansible_module)
    pb.add_host('labserver-2001')
    return pb

def add_task_stc_session_create(pb):
    task = StcSession(log)
    #task.command = 'create' # optional. create is the default
    task.name = 'east_west'
    task.user = 'Administrator'
    task.password = 'spirent'
    task.task_name = 'create STC session'
    task.update()
    pb.add_task(task)

def add_task_stc_session_delete(pb):
    '''
    delete is currently not supported.  When support
    is added, this is what it will look like.
    '''
    task = StcSession(log)
    task.command = 'delete'
    task.name = 'east_west'
    task.user = 'Administrator'
    task.task_name = 'delete STC session'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_stc_session_create(pb)
#add_task_stc_session_delete(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
