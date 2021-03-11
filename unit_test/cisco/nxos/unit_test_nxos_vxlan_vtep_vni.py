#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vxlan_vtep_vni.py
our_version = 107
'''
Name
----
unit_test_nxos_vxlan_vtep_vni.py

Description
-----------

Example script and half-hearted unit test for Ansible
module: nxos_vxlan_vtep_vni
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vxlan_vtep_vni import NxosVxlanVtepVni

ansible_module = 'nxos_vxlan_vtep_vni'
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
    task = NxosVxlanVtepVni(log)
    task.ingress_replication = 'static'
    task.multisite_ingress_replication = 'enable'
    task.interface = 'nve1'
    task.multicast_group = '225.1.1.1'
    task.peer_list = ['10.1.1.1', '10.1.1.2', '10.1.1.3']
    task.state = 'present'
    task.vni = 11932
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
