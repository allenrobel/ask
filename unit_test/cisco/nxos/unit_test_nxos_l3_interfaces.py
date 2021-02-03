#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_l3_interfaces.py
our_version = 103

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_l3_interfaces import NxosL3Interfaces

ansible_module = 'nxos_l3_interfaces'
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
    if item == 'ipv4':
        value = '{}, {}x {}'.format(name, len(item_value), item)
        return value
    if item == 'ipv6':
        value = '{}, {}x {}'.format(name, len(item_value), item)
        return value
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
        return value
    return name

def add_task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('dot1q', task.dot1q, task_name)
    task_name = add_item_to_name('evpn_multisite_tracking', task.evpn_multisite_tracking, task_name)
    task_name = add_item_to_name('name', task.name, task_name)
    task_name = add_item_to_name('ipv4', task.ipv4, task_name)
    task_name = add_item_to_name('ipv6', task.ipv6, task_name)
    task_name = add_item_to_name('redirects', task.redirects, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('unreachables', task.unreachables, task_name)
    task.task_name = task_name

def dual_stack_interface(pb):
    task = NxosL3Interfaces(log)
    task.name = 'Ethernet1/49'
    task.ipv4_address = '10.1.1.1/24'
    #task.ipv4_secondary = 'no'
    task.ipv4_tag = 10
    task.add_ipv4()
    task.ipv4_address = '10.2.1.1/24'
    task.ipv4_tag = 20
    #task.ipv4_secondary = 'no'
    task.ipv4_secondary = 'yes'
    task.add_ipv4()
    task.ipv6_address = '2001:aaaa::1/64'
    task.ipv6_tag = 10
    task.add_ipv6()
    task.ipv6_address = '2001:bbbb::1/64'
    task.ipv6_tag = 20
    task.add_ipv6()
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def ipv4_interface(pb):
    task = NxosL3Interfaces(log)
    task.name = 'Ethernet1/50'
    task.ipv4_address = '10.1.2.1/24'
    task.add_ipv4()
    task.redirects = 'no'
    task.unreachables = 'no'
    task.state = 'replaced'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def ipv6_interface(pb):
    task = NxosL3Interfaces(log)
    task.name = 'Ethernet1/51'
    task.ipv6_address = '2001:cccc::1/64'
    task.ipv6_tag = 30
    task.add_ipv6()
    task.state = 'replaced'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

dual_stack_interface(pb)
ipv4_interface(pb)
ipv6_interface(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
