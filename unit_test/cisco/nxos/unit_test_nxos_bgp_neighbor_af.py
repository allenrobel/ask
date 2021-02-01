#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_af.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp_neighbor_af import NxosBgpNeighborAf

ansible_module = 'nxos_bgp_neighbor_af'
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
    task_name = add_item_to_name('additional_paths_receive', task.additional_paths_receive, task_name)
    task_name = add_item_to_name('afi', task.afi, task_name)
    task_name = add_item_to_name('asn', task.asn, task_name)
    task_name = add_item_to_name('neighbor', task.neighbor, task_name)
    task_name = add_item_to_name('safi', task.safi, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('vrf', task.vrf, task_name)
    task.task_name = task_name

def add_task_nxos_bgp_neighbor_af_ipv4(pb):
    task = NxosBgpNeighborAf(log)
    task.additional_paths_receive = 'inherit'
    task.afi = 'ipv4'
    task.asn = '2301.0'
    task.neighbor = '10.1.1.1'
    task.safi = 'unicast'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_nxos_bgp_neighbor_af_ipv6(pb):
    task = NxosBgpNeighborAf(log)
    task.afi = 'ipv6'
    task.asn = '2301.0'
    task.neighbor = '2001:1000:14a5::1'
    task.safi = 'unicast'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_nxos_bgp_neighbor_af_ipv4(pb)
add_task_nxos_bgp_neighbor_af_ipv6(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
