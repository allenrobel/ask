#!/usr/bin/env python3
# unit_test/cisco/nxos/nxos_interface.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_interface import NxosInterface

ansible_module = 'nxos_interface'
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

def fabric_forwarding_anycast_gateway(pb):
    task = NxosInterface(log)
    task.name = 'Ethernet1/3'
    task.admin_state = 'up'
    task.mtu = 9216
    task.fabric_forwarding_anycast_gateway = True
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def layer2(pb):
    task = NxosInterface(log)
    task.name = 'Ethernet1/1'
    task.admin_state = 'up'
    task.mtu = 9216
    task.mode = 'layer2'
    task.ip_forward = 'disable'
    task.speed = 40000
    task.state = 'present'
    task.neighbor_host = 'test_hostname1'
    task.neighbor_port = 'Ethernet1/2'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def layer3(pb):
    task = NxosInterface(log)
    task.name = 'Ethernet1/2'
    task.admin_state = 'up'
    task.mtu = 9216
    task.speed = 'auto'
    task.mode = 'layer3'
    task.ip_forward = 'enable'
    task.state = 'present'
    task.neighbor_host = 'test_hostname2'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

pb = playbook()
fabric_forwarding_anycast_gateway(pb)
layer2(pb)
layer3(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))

