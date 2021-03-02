#!/usr/bin/env python3
# unit_test/nxos/cisco/unit_test_nxos_lag_interfaces.py
our_version = 104
'''
Name: unit_test_ans_task_nxos_lag_interfaces.py

Description:
    Example script and half-hearted unit test for:
        NxosLagInterfaces()   - cisco/nxos/nxos_lag_interfaces.py
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_lag_interfaces import NxosLagInterfaces
from ask.ansible.register_save import RegisterSave

ansible_module = 'nxos_lag_interfaces'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.profile_nxos()
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_task_state_merged(pb):
    task = NxosLagInterfaces(log)
    task.task_name = 'my_lag_task'

    task.name = 'port-channel10'
    task.member = 'Ethernet1/49'
    task.force = True
    task.mode = 'on'
    task.add_member()
    task.member = 'Ethernet1/50'
    task.mode = 'on'
    task.add_member()
    task.add_lag()

    task.name = 'port-channel20'
    task.member = 'Ethernet1/4'
    task.force = True
    task.mode = 'on'
    task.add_member()
    task.member = 'Ethernet1/5'
    task.mode = 'on'
    task.add_member()
    task.add_lag()

    task.state = 'merged'
    task.update()
    pb.add_task(task)

def add_task_state_parsed(pb):
    task = NxosLagInterfaces(log)
    task.running_config = '/tmp/parsed.cfg'
    task.state = 'parsed'
    task.register = 'parsed'
    task.task_name = 'test state parsed'
    task.update()
    pb.add_task(task)

    task = RegisterSave(log)
    task.filename = '/tmp/parsed_output.txt'
    task.var = 'parsed'
    task.task_name = 'save register'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_state_merged(pb)
#add_task_state_parsed(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
