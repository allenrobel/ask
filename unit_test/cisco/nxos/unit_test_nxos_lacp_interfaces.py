#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_lacp_interfaces.py
our_version = 103
'''
Name: unit_test_nxos_lacp_interfaces.py

Description

Unit test for:
    NxosLacpInterfaces()   - cisco/nxos/nxos_lacp_interfaces.py
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_lacp_interfaces import NxosLacpInterfaces

ansible_module = 'nxos_lacp_interfaces'
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

def add_task(pb):
    task = NxosLacpInterfaces(log)
    task.task_name = 'my_lacp_task'
    task.state = 'merged'

    task.name = 'port-channel10'
    task.max = 32
    task.min = 8
    task.graceful = 'yes'
    task.vpc = 'yes'
    task.suspend_individual = 'yes'
    task.mode = 'delay'
    task.state = 'merged'
    task.update()

    task.name = 'Ethernet1/49'
    task.rate = 'fast'
    task.port_priority = 200
    task.state = 'merged'
    task.update()

    task.name = 'Ethernet1/50'
    task.rate = 'fast'
    task.port_priority = 100
    task.state = 'merged'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
