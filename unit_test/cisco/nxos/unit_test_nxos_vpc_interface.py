#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vpc_interface.py
our_version = 107

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vpc_interface import NxosVpcInterface

ansible_module = 'nxos_vpc_interface'
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
    task.append_to_task_name(ansible_host)
    for key in sorted(task.properties_set):
        task.append_to_task_name(key)

def add_task_vpc_peer_link(pb):
    task = NxosVpcInterface(log)
    task.peer_link = True
    task.portchannel = 1
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)
def add_task_vpc_port_channel(pb):
    task = NxosVpcInterface(log)
    task.portchannel = 10
    task.vpc = 10
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_vpc_peer_link(pb)
add_task_vpc_port_channel(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
