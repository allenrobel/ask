#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_lacp_interfaces.py
our_version = 105
'''
Name: unit_test_nxos_lacp_interfaces.py

Description

Unit test for:
    NxosLacpInterfaces()   - cisco/nxos/nxos_lacp_interfaces.py
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_lacp_interfaces import NxosLacpInterfaces
from ask.ansible.register_save import RegisterSave

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

def add_task_name(task):
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    for key in sorted(task.scriptkit_properties):
        task.append_to_task_name(key)

def add_task_single_lacp_interface(pb):
    task = NxosLacpInterfaces(log)

    task.name = 'port-channel10'
    task.max = 32
    task.min = 8
    task.graceful = True
    task.vpc = True
    task.suspend_individual = True
    task.mode = 'delay'
    add_task_name(task)
    task.add_interface()
    task.state = 'replaced'
    task.update()
    pb.add_task(task)

def add_task_multiple_lacp_interfaces(pb):
    task = NxosLacpInterfaces(log)

    task.name = 'port-channel10'
    task.max = 32
    task.min = 8
    task.graceful = True
    task.vpc = True
    task.suspend_individual = True
    task.mode = 'delay'
    add_task_name(task)
    task.add_interface()

    task.name = 'Ethernet1/49'
    task.rate = 'fast'
    task.port_priority = 200
    add_task_name(task)
    task.add_interface()

    task.name = 'Ethernet1/50'
    task.rate = 'fast'
    task.port_priority = 100
    add_task_name(task)
    task.add_interface()

    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_parsed(pb):
    task = NxosLacpInterfaces(log)
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

add_task_single_lacp_interface(pb)
add_task_multiple_lacp_interfaces(pb)
add_task_parsed(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
