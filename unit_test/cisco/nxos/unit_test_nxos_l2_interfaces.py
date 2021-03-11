#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_l2_interfaces.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_l2_interfaces import NxosL2Interfaces
from ask.ansible.register_save import RegisterSave

ansible_module = 'nxos_l2_interfaces'
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
    task = NxosL2Interfaces(log)
    task.name = 'Ethernet1/11'
    task.mode = 'access'
    task.vlan = 11
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_trunk_interface(pb):
    task = NxosL2Interfaces(log)
    task.name = 'Ethernet1/10'
    task.mode = 'trunk'
    task.native_vlan = 10
    task.allowed_vlans = '11,12,13'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_deleted(pb):
    task = NxosL2Interfaces(log)
    task.name = 'Vlan10'
    task.state = 'deleted'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_parsed(pb):
    task = NxosL2Interfaces(log)
    task.running_config = '/tmp/parsed.cfg'
    task.state = 'parsed'
    task.register = 'parsed'
    add_task_name(task)
    task.update()
    pb.add_task(task)

    task = RegisterSave(log)
    task.filename = '/tmp/parsed_output.txt'
    task.var = 'parsed'
    task.update()
    pb.add_task(task)


pb = playbook()
add_task_access_interface(pb)
add_task_trunk_interface(pb)
add_task_deleted(pb)
add_task_parsed(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
