#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor.py
our_version = 102
 
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp_neighbor import NxosBgpNeighbor

ansible_module = 'nxos_bgp_neighbor'
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

def add_item_to_name(item, item_value, name):
    value = ''
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
    else:
        value = name
    return value

def add_task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('asn', task.asn, task_name)
    task_name = add_item_to_name('neighbor', task.neighbor, task_name)
    task_name = add_item_to_name('remote_as', task.remote_as, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('vrf', task.vrf, task_name)
    task.task_name = task_name

def add_task(pb):
    task = NxosBgpNeighbor(log)
    task.asn = '12000.0'
    task.neighbor = '10.1.1.1'
    task.remote_as = '6201.0'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
