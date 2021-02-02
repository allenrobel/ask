#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp.py
our_version = 102

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp import NxosBgp

ansible_module = 'nxos_bgp'
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
    task_name = add_item_to_name('asn', task.asn, task_name)
    task_name = add_item_to_name('event_history_cli', task.event_history_cli, task_name)
    task_name = add_item_to_name('event_history_detail', task.event_history_detail, task_name)
    task_name = add_item_to_name('event_history_events', task.event_history_events, task_name)
    task_name = add_item_to_name('event_history_periodic', task.event_history_periodic, task_name)
    task_name = add_item_to_name('router_id', task.router_id, task_name)
    task_name = add_item_to_name('event_history_cli', task.event_history_cli, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('vrf', task.vrf, task_name)
    task.task_name = task_name

def add_task_bgp_general(pb):
    task = NxosBgp(log)
    task.asn = '65000.0'
    task.router_id = '10.239.0.0'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_bgp_event_history(pb):
    task = NxosBgp(log)
    task.asn = '65000.0'
    task.event_history_cli = 'size_small'
    task.event_history_detail = 'size_medium'
    task.event_history_events = 'size_large'
    task.event_history_periodic = 'size_disable'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_bgp_general(pb)
add_task_bgp_event_history(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
