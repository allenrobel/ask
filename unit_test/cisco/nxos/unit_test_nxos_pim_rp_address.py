#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_pim_rp_address.py
our_version = 100

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_pim_rp_address import NxosPimRpAddress

ansible_module = 'nxos_pim_rp_address'
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
    task_name = add_item_to_name('bidir', task.bidir, task_name)
    task_name = add_item_to_name('group_list', task.group_list, task_name)
    task_name = add_item_to_name('prefix_list', task.prefix_list, task_name)
    task_name = add_item_to_name('route_map', task.route_map, task_name)
    task_name = add_item_to_name('rp_address', task.rp_address, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task.task_name = task_name

def add_task_pim_rp_address_group_list(pb):
    task = NxosPimRpAddress(log)
    task.bidir = 'no'
    task.group_list = '224.1.2.0/24'
    task.rp_address = '2.2.2.2'
    task.state = 'present'
    task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_rp_address_prefix_list(pb):
    task = NxosPimRpAddress(log)
    task.bidir = 'no'
    task.prefix_list = 'PIM_RP_PREFIX_LIST'
    task.rp_address = '3.3.3.3'
    task.state = 'present'
    task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_rp_address_route_map(pb):
    task = NxosPimRpAddress(log)
    task.bidir = 'no'
    task.route_map = 'PIM_RP_ROUTE_MAP'
    task.rp_address = '4.4.4.4'
    task.state = 'present'
    task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_rp_address_bidir(pb):
    task = NxosPimRpAddress(log)
    task.bidir = 'yes'
    task.group_list = '225.5.0.0/16'
    task.rp_address = '5.5.5.5'
    task.state = 'present'
    task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_pim_rp_address_group_list(pb)
add_task_pim_rp_address_prefix_list(pb)
add_task_pim_rp_address_route_map(pb)
add_task_pim_rp_address_bidir(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
