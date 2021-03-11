#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_hsrp.py
our_version = 105

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_hsrp import NxosHsrp

ansible_module = 'nxos_hsrp'
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

def hsrp_priority_default(pb):
    task = NxosHsrp(log)
    task.group = 2
    task.priority = 'default'
    task.interface = 'Vlan101'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def hsrp_version_1_group(pb):
    task = NxosHsrp(log)
    task.group = 255
    #task.group = 256 # negative test
    task.version = 1
    task.priority = 255
    task.interface = 'Vlan102'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def hsrp_version_2_group(pb):
    task = NxosHsrp(log)
    task.group = 4095
    #task.group = 4096 # negative test
    task.version = 2
    task.priority = 255
    task.interface = 'Vlan103'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

hsrp_priority_default(pb)
hsrp_version_1_group(pb)
hsrp_version_2_group(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))

