#!/usr/bin/env python3
# unit_test/cisco/nxos/nxos_interface.py
our_version = 102

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_interface import NxosInterface

ansible_module = 'nxos_interface'
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

def layer2(pb):
    task = NxosInterface(log)
    task.name = 'Ethernet1/1'
    task.admin_state = 'up'
    task.mtu = 9216
    task.mode = 'layer2'
    task.ip_forward = 'disable'
    task.state = 'present'
    task.neighbor_host = 'test_hostname1'
    task.neighbor_port = 'Ethernet1/2'
    task.task_name = '{}: name {}, mode {}, admin_state {}, mtu {}, ip_forward {}, state {}'.format(
        ansible_module,
        task.name,
        task.mode,
        task.admin_state,
        task.mtu,
        task.ip_forward,
        task.state)
    task.update()
    pb.add_task(task)

def layer3(pb):
    task = NxosInterface(log)
    task.name = 'Ethernet1/2'
    task.admin_state = 'up'
    task.mtu = 9216
    task.mode = 'layer3'
    task.ip_forward = 'enable'
    task.state = 'present'
    task.neighbor_host = 'test_hostname2'
    task.task_name = '{}: name {}, mode {}, admin_state {}, mtu {}, ip_forward {}, state {}'.format(
        ansible_module,
        task.name,
        task.mode,
        task.admin_state,
        task.mtu,
        task.ip_forward,
        task.state)
    task.update()
    pb.add_task(task)

pb = playbook()
layer2(pb)
layer3(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))

