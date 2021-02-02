#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bfd_global.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bfd_global import NxosBfdGlobal

ansible_module = 'nxos_bfd_global'
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

def add_task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('echo_rx_interval', task.echo_rx_interval, task_name)
    task_name = add_item_to_name('slow_timer', task.slow_timer, task_name)
    task_name = add_item_to_name('bfd_interval', task.bfd_interval, task_name)
    task_name = add_item_to_name('bfd_min_rx', task.bfd_min_rx, task_name)
    task_name = add_item_to_name('bfd_multiplier', task.bfd_multiplier, task_name)
    task_name = add_item_to_name('ipv4_echo_rx_interval', task.ipv4_echo_rx_interval, task_name)
    task_name = add_item_to_name('ipv4_slow_timer', task.ipv4_slow_timer, task_name)
    task_name = add_item_to_name('bfd_fabricpath_interval', task.bfd_fabricpath_interval, task_name)
    task_name = add_item_to_name('bfd_fabricpath_min_rx', task.bfd_fabricpath_min_rx, task_name)
    task_name = add_item_to_name('bfd_fabricpath_multiplier', task.bfd_fabricpath_multiplier, task_name)
    task_name = add_item_to_name('bfd_ipv4_interval', task.bfd_ipv4_interval, task_name)
    task_name = add_item_to_name('bfd_ipv4_min_rx', task.bfd_ipv4_min_rx, task_name)
    task_name = add_item_to_name('bfd_ipv4_multiplier', task.bfd_ipv4_multiplier, task_name)
    task_name = add_item_to_name('bfd_ipv6_interval', task.bfd_ipv6_interval, task_name)
    task_name = add_item_to_name('bfd_ipv6_min_rx', task.bfd_ipv6_min_rx, task_name)
    task_name = add_item_to_name('bfd_ipv6_multiplier', task.bfd_ipv6_multiplier, task_name)
    task.task_name = task_name

def add_task_bfd_general(pb):
    task = NxosBfdGlobal(log)
    task.echo_rx_interval = 50
    task.slow_timer = 2000
    task.bfd_interval = 50
    task.bfd_min_rx = 50
    task.bfd_multiplier = 3
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_bfd_fabricpath(pb):
    task = NxosBfdGlobal(log)
    task.bfd_fabricpath_interval = 50
    task.bfd_fabricpath_min_rx = 50
    task.bfd_fabricpath_multiplier = 3
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_bfd_ipv4(pb):
    task = NxosBfdGlobal(log)
    task.ipv4_echo_rx_interval = 50
    task.ipv4_slow_timer = 2000
    task.bfd_ipv4_interval = 50
    task.bfd_ipv4_min_rx = 50
    task.bfd_ipv4_multiplier = 3
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_bfd_ipv6(pb):
    task = NxosBfdGlobal(log)
    task.bfd_ipv6_interval = 50
    task.bfd_ipv6_min_rx = 50
    task.bfd_ipv6_multiplier = 3
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_bfd_general(pb)
add_task_bfd_fabricpath(pb)
add_task_bfd_ipv4(pb)
add_task_bfd_ipv6(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote playbook {}'.format(pb.file))
