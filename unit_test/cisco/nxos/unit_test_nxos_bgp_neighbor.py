#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_neighbor.py
our_version = 104
 
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp_neighbor import NxosBgpNeighbor

ansible_module = 'nxos_bgp_neighbor'
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

def ipv4_neighbor(pb):
    task = NxosBgpNeighbor(log)
    task.asn = '12000.0'
    task.neighbor = '10.1.1.1'
    task.remote_as = '6201.0'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.commit()
    pb.add_task(task)

def ipv4_neighbor_prefix_peer(pb):
    task = NxosBgpNeighbor(log)
    task.asn = '12000'
    task.neighbor = '10.1.1.0/24'
    #task.neighbor = '10.1.1.1' # negative test
    task.remote_as = '6201.0'
    task.maximum_peers = 20
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.commit()
    pb.add_task(task)

def ipv4_neighbor_and_local_as(pb):
    task = NxosBgpNeighbor(log)
    task.asn = '12000.0'
    task.local_as = '23100'
    task.neighbor = '10.1.1.1'
    task.remote_as = '6201.0'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.commit()
    pb.add_task(task)

def ipv4_neighbor_peer_type(pb):
    task = NxosBgpNeighbor(log)
    task.asn = '12000'
    task.neighbor = '10.1.1.1'
    task.remote_as = '6201.0'
    task.peer_type = 'disable'
    #task.peer_type = 'foo' # negative test
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.commit()
    pb.add_task(task)

def ipv6_neighbor(pb):
    task = NxosBgpNeighbor(log)
    task.asn = '12000.0'
    task.neighbor = '2001:aaaa::1'
    task.remote_as = '4700000001'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.commit()
    pb.add_task(task)

def ipv6_neighbor_prefix_peer(pb):
    task = NxosBgpNeighbor(log)
    task.asn = '12000.0'
    task.neighbor = '2001:aaaa::/120'
    #task.neighbor = '2001:aaaa::1' # negative test
    task.remote_as = '4700000001'
    task.maximum_peers = 1000
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name(task)
    task.commit()
    pb.add_task(task)

pb = playbook()
ipv4_neighbor(pb)
ipv4_neighbor_prefix_peer(pb)
ipv4_neighbor_and_local_as(pb)
ipv4_neighbor_peer_type(pb)
ipv6_neighbor(pb)
ipv6_neighbor_prefix_peer(pb)

pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
