#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_static_routes.py
our_version = 101
'''
========================================
unit_test_ans_task_nxos_static_routes.py
========================================

Description
-----------
Unit test for ScriptKit library for Ansible module: nxos_static_routes
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_static_routes import NxosStaticRoutes

ansible_module = 'nxos_static_routes'
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
    task_name = add_item_to_name('afi', task.afi, task_name)
    task_name = add_item_to_name('admin_distance', task.admin_distance, task_name)
    task_name = add_item_to_name('dest', task.dest, task_name)
    task_name = add_item_to_name('dest_vrf', task.dest_vrf, task_name)
    task_name = add_item_to_name('forward_router_address', task.forward_router_address, task_name)
    task_name = add_item_to_name('interface', task.interface, task_name)
    task_name = add_item_to_name('route_name', task.route_name, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('tag', task.tag, task_name)
    task_name = add_item_to_name('track', task.track, task_name)
    task.task_name = task_name

def add_ipv4_next_hops_vrf(pb):
    task = NxosStaticRoutes(log)
    task.afi = 'ipv4'
    task.admin_distance = 10
    task.dest = '1.1.0.0/24'
    task.dest_vrf = 'vrf1'
    task.forward_router_address = '15.1.1.1'
    task.interface = 'Ethernet1/15'
    task.route_name = 'ipv4_route_1'
    task.tag = 15
    task.vrf = 'vrf2'
    task.add_next_hop()

    task.admin_distance = 10
    task.dest_vrf = 'vrf1'
    task.forward_router_address = '16.1.1.1'
    task.interface = 'Ethernet1/16'
    task.route_name = 'ipv4_route_2'
    task.tag = 16
    task.vrf = 'vrf2'
    task_name(task)
    task.add_next_hop()
    task.state = 'merged'

    task.update()
    pb.add_task(task)

def add_ipv4_next_hops_no_vrf(task):
    task.afi = 'ipv4'
    task.dest = '1.1.0.0/24'
    task.forward_router_address = '15.1.1.1'
    task.interface = 'Ethernet1/17'
    task.add_next_hop()

    task.forward_router_address = '16.1.1.1'
    task.interface = 'Ethernet1/18'
    task.add_next_hop()

def add_ipv6_next_hops_no_vrf(task):
    task.afi = 'ipv6'
    task.dest = '2001:10:20:30::/64'

    task.forward_router_address = '2000:15:15::15'
    task.interface = 'Ethernet1/19'
    task_name(task)
    task.add_next_hop()

    task.forward_router_address = '2000:16:16::16'
    task.interface = 'Ethernet1/20'
    task.add_next_hop()

def add_next_hops_no_vrf(pb):
    task = NxosStaticRoutes(log)
    add_ipv4_next_hops_no_vrf(task)
    add_ipv6_next_hops_no_vrf(task)
    task_name(task)
    task.state = 'merged'
    task.update()
    pb.add_task(task)

pb = playbook()
add_ipv4_next_hops_vrf(pb)
add_next_hops_no_vrf(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
