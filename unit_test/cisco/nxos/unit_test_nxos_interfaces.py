#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_interfaces.py
our_version = 103

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_interfaces import NxosInterfaces

ansible_module = 'nxos_interfaces'
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
    task.append_to_task_name('v.{}'.format(our_version))
    task.append_to_task_name(ansible_host)
    for key in sorted(task.properties_set):
        task.append_to_task_name(key)

def add_ethernet(pb):
    task = NxosInterfaces(log)
    task.name = 'Ethernet1/10'
    task.mtu = 9216
    task.mode = 'layer2'
    task.speed = 100000
    task.duplex = 'auto'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_svi(pb):
    task = NxosInterfaces(log)
    task.name = 'Vlan222'
    task.mtu = 1500
    task.fabric_forwarding_anycast_gateway = True
    task.mode = 'layer3'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_ethernet(pb)
add_svi(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
