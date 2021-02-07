#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vpc_interface.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vpc_interface import NxosVpcInterface

ansible_module = 'nxos_vpc_interface'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.ansible_connection = 'httpapi' # httpapi, network_cli
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_task_name(task):
    def add_item_to_name(item, item_value, name):
        value = ''
        if item_value != None:
            value = '{}, {} {}'.format(name, item, item_value)
        else:
            value = name
        return value
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('portchannel', task.portchannel, task_name)
    task_name = add_item_to_name('peer_link', task.peer_link, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('vpc', task.vpc, task_name)
    task.task_name = task_name

def add_task_vpc_peer_link(pb):
    task = NxosVpcInterface(log)
    task.peer_link = 'yes'
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
