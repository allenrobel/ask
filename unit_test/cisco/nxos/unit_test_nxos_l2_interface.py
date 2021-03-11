#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_l2_interface.py
our_version = 105

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_l2_interface import NxosL2Interface

ansible_module = 'nxos_l2_interface'
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

def add_task_access_interface(pb):
    task = NxosL2Interface(log)
    task.name = 'Ethernet1/50'
    task.mode = 'access'
    task.access_vlan = 10
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_trunk_interface(pb):
    task = NxosL2Interface(log)
    task.name = 'Ethernet1/49'
    task.mode = 'trunk'
    task.trunk_allowed_vlans = '2,10-20'
    task.trunk_vlans = '3,30-31'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_access_interface(pb)
add_task_trunk_interface(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
