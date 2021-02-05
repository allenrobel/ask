#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_pim_interface.py
our_version = 101

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_pim_interface import NxosPimInterface

ansible_module = 'nxos_pim_interface'
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

def add_item_to_name(item, item_value, name):
    value = ''
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
    else:
        value = name
    return value

def task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('bfd', task.bfd, task_name)
    task_name = add_item_to_name('border', task.border, task_name)
    task_name = add_item_to_name('dr_prio', task.dr_prio, task_name)
    task_name = add_item_to_name('hello_auth_key', task.hello_auth_key, task_name)
    task_name = add_item_to_name('hello_interval', task.hello_interval, task_name)
    task_name = add_item_to_name('interface', task.interface, task_name)
    task_name = add_item_to_name('jp_policy_in', task.jp_policy_in, task_name)
    task_name = add_item_to_name('jp_policy_out', task.jp_policy_out, task_name)
    task_name = add_item_to_name('jp_type_in', task.jp_type_in, task_name)
    task_name = add_item_to_name('jp_type_out', task.jp_type_out, task_name)
    task_name = add_item_to_name('neighbor_policy', task.neighbor_policy, task_name)
    task_name = add_item_to_name('neighbor_type', task.neighbor_type, task_name)
    task_name = add_item_to_name('sparse', task.sparse, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task.task_name = task_name

def add_task_pim_interface_base(pb):
    task = NxosPimInterface(log)
    task.bfd = 'enable'
    task.border = 'no'
    task.dr_prio = 4
    task.hello_interval = 3
    task.interface = 'Ethernet1/49'
    task.sparse = 'yes'
    task.state = 'present'
    task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_interface_jp_policy(pb):
    task = NxosPimInterface(log)
    task.jp_policy_in = 'JP_IN'
    task.jp_type_in = 'routemap'
    task.jp_policy_out = 'JP_OUT'
    task.jp_type_out = 'prefix'
    task.interface = 'Ethernet1/49'
    task.state = 'present'
    task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_interface_neighbor_policy(pb):
    task = NxosPimInterface(log)
    task.neighbor_policy = 'PIM_NBR_POLICY'
    task.neighbor_type = 'routemap'
    task.interface = 'Ethernet1/49'
    task.state = 'present'
    task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_pim_interface_base(pb)
add_task_pim_interface_jp_policy(pb)
add_task_pim_interface_neighbor_policy(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
