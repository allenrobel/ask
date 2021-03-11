#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor_af.py
our_version = 106

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp_neighbor_af import NxosBgpNeighborAf

ansible_module = 'nxos_bgp_neighbor_af'
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

def add_task_nxos_bgp_neighbor_af_ipv4(pb):
    task = NxosBgpNeighborAf(log)
    task.additional_paths_receive = 'inherit'
    task.afi = 'ipv4'
    task.asn = '2301.0'
    task.neighbor = '10.1.1.1'
    task.safi = 'unicast'
    task.state = 'present'
    task.vrf = 'default'
    add_task_name(task)
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
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_nxos_bgp_neighbor_af_ipv4(pb)
add_task_nxos_bgp_neighbor_af_ipv6(pb)
pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
