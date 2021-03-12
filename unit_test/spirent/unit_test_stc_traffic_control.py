#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_traffic_control.py
our_version = 101
'''
Name: unit_test_stc_traffic_control.py

Description:

Generates Ansible playbook conformant with Spirent Ansible module: stc
This playbook creates Spirent device

Prerequisites:

A playbook created with stc_traffic_control_gen.py must be run prior to running the playbook created with this script
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.spirent.stc_traffic_control import StcTrafficControl

ansible_module = 'stc_traffic_control'
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
    for key in task.scriptkit_properties:
        task.append_to_task_name(key)

def add_task_traffic(pb, command):
    task = StcTrafficControl(log)
    task.command = command
    #task.generator_list = 'ref:/project' # If not set, the default is ref:/project (all generators)
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_traffic(pb, 'start')
add_task_traffic(pb, 'stop')
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
