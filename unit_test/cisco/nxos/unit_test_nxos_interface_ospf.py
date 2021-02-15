#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_interface_ospf.py
our_version = 105

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_interface_ospf import NxosInterfaceOspf

ansible_module = 'nxos_interface_ospf'
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
    task_name = add_item_to_name('area', task.area, task_name)
    task_name = add_item_to_name('interface', task.interface, task_name)
    task_name = add_item_to_name('network', task.network, task_name)
    task_name = add_item_to_name('ospf', task.ospf, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task.task_name = task_name

def add_task(pb):
    task = NxosInterfaceOspf(log)
    task.area = '100'
    task.interface = 'Ethernet1/1'
    task.network = 'point-to-point'
    task.ospf = '1'
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
