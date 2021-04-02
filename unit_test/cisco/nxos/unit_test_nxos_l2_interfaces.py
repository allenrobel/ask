#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_l2_interfaces.py
our_version = 105

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

def add_access_interfaces(task):
    for port in range(1,6):
        task.name = 'Ethernet1/{}'.format(port)
        task.mode = 'access'
        task.vlan = port + 220
        task.append_to_task_name('[{} : {}]'.format(task.name, task.vlan))
        task.add_interface()

def add_trunk_interfaces(task):
    allowed_vlan_base = 100
    for port in range(10,16):
        task.name = 'Ethernet1/{}'.format(port)
        task.mode = 'trunk'
        task.native_vlan = 10
        allowed_vlans = [str(x) for x in range(allowed_vlan_base, allowed_vlan_base+4)]
        task.allowed_vlans = ','.join(allowed_vlans)
        task.append_to_task_name('[{} : {}]'.format(task.name, task.allowed_vlans))
        task.add_interface()
        allowed_vlan_base += 4

def add_task_deleted(pb):
    task = NxosL2Interfaces(log)
    task.name = 'Vlan10'
    task.add_interface()
    task.state = 'deleted'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def add_task_parsed(pb):
    task = NxosL2Interfaces(log)
    task.running_config = '/tmp/parsed.cfg'
    task.state = 'parsed'
    task.register = 'parsed'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

    task = RegisterSave(log)
    task.filename = '/tmp/parsed_output.txt'
    task.var = 'parsed'
    task.commit()
    pb.add_task(task)


pb = playbook()
task = NxosL2Interfaces(log)
add_access_interfaces(task)
add_trunk_interfaces(task)
task.state = 'merged'
task.commit()
pb.add_task(task)
add_task_deleted(pb)
add_task_parsed(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
