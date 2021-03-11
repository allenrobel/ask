#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp import NxosBgp

ansible_module = 'nxos_bgp'
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
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    for key in sorted(task.scriptkit_properties):
        task.append_to_task_name(key)

def add_task_bgp_general(pb):
    task = NxosBgp(log)
    task.asn = '65000.0'
    task.router_id = '10.239.0.0'
    task.state = 'present'
    task.vrf = 'default'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_bgp_timer(pb):
    task = NxosBgp(log)
    task.asn = '65000.0'
    # max values
    # task.timer_bgp_keepalive = 3599
    # task.timer_bgp_hold = 3600
    # min values
    # task.timer_bgp_keepalive = 1
    # task.timer_bgp_hold = 3
    # default keyword
    task.timer_bgp_keepalive = 'default'
    task.timer_bgp_hold = 'default'
    task.state = 'present'
    add_task_name(task)
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
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_bgp_timer(pb)
add_task_bgp_general(pb)
add_task_bgp_event_history(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
