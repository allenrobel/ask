#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vxlan_vtep.py
our_version = 108
'''
Name
----
unit_test_nxos_vxlan_vtep.py

Description
-----------
Example script and half-hearted unit test for Ansible module::

    nxos_vxlan_vtep

'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vxlan_vtep import NxosVxlanVtep

ansible_module = 'nxos_vxlan_vtep'
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

def add_task(pb):
    task = NxosVxlanVtep(log)
    task.description = 'testing nve1'
    task.global_ingress_replication_bgp = 'yes'
    task.global_mcast_group_L2 = 'default'
    task.global_mcast_group_L3 = '225.1.2.3'
    task.host_reachability = 'no'
    task.interface = 'nve1'
    task.multisite_border_gateway_interface = 'Loopback1'
    task.shutdown = 'no'
    task.source_interface = 'Loopback0'
    task.source_interface_hold_down_time = 380
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
