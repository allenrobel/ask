#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vrf.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vrf import NxosVrf

ansible_module = 'nxos_vrf'
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
    task = NxosVrf(log)
    task.admin_state = 'up'
    task.description = 'single vrf demo'
    #task.interfaces = 'default'
    task.interfaces = ['Ethernet1/1', 'Vlan11']
    task.name = 'vrf_1'
    task.rd = '10.1.1.1:111'
    task.state = 'present'
    task.vni = 20001
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_aggregate_task(pb):
    task = NxosVrf(log)

    task.admin_state = 'up'
    task.description = 'aggregate demo vrf_2'
    task.interfaces = ['Ethernet1/2', 'Vlan12']
    task.name = 'vrf_2'
    task.rd = '60002:200'
    task.state = 'present'
    task.vni = 20002
    task.add_vrf()

    task.admin_state = 'down'
    task.delay = 20
    task.description = 'aggregate demo vrf_3'
    task.interfaces = ['Ethernet1/3', 'Vlan13']
    task.name = 'vrf_3'
    task.rd = '60003:300'
    task.state = 'present'
    task.vni = 20003
    task.add_vrf()

    task.purge = True
    task.task_name = 'aggregate vrfs'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
add_aggregate_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
