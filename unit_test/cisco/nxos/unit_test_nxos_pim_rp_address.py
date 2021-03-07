#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_pim_rp_address.py
our_version = 103

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_pim_rp_address import NxosPimRpAddress

ansible_module = 'nxos_pim_rp_address'
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

def add_task_pim_rp_address_group_list(pb):
    task = NxosPimRpAddress(log)
    task.bidir = False
    task.group_list = '225.1.2.0/24'
    task.rp_address = '2.2.2.2'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_rp_address_prefix_list(pb):
    task = NxosPimRpAddress(log)
    task.bidir = False
    task.prefix_list = 'PIM_RP_PREFIX_LIST'
    task.rp_address = '3.3.3.3'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_rp_address_route_map(pb):
    task = NxosPimRpAddress(log)
    task.bidir = False
    task.route_map = 'PIM_RP_ROUTE_MAP'
    task.rp_address = '4.4.4.4'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_rp_address_bidir(pb):
    task = NxosPimRpAddress(log)
    task.bidir = True
    task.group_list = '225.5.0.0/16'
    task.rp_address = '5.5.5.5'
    task.state = 'present'
    add_task_name(task)
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
