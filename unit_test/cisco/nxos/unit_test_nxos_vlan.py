#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vlan.py
our_version = 106

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vlan import NxosVlan

ansible_module = 'nxos_vlan'
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

def add_task(pb):
    task = NxosVlan(log)
    task.admin_state = 'up'
    task.delay = 20
    task.interfaces = ['Ethernet1/7', 'Ethernet1/8']
    task.name = "my_vlan_2001"
    task.mapped_vni = 20001
    task.state = 'present'
    task.vlan_id = 2001
    task.vlan_state = 'active'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_aggregate_task(pb):
    task = NxosVlan(log)

    task.admin_state = 'up'
    task.delay = 20
    task.interfaces = ['Ethernet1/9', 'Ethernet1/10']
    task.name = "my_vlan_2002"
    task.mapped_vni = 20002
    task.state = 'present'
    task.vlan_id = 2002
    task.vlan_state = 'active'
    task.add_vlan()

    task.admin_state = 'down'
    task.delay = 20
    task.interfaces = ['Ethernet1/11', 'Ethernet1/12']
    task.name = "my_vlan_2003"
    task.mapped_vni = 20003
    task.state = 'present'
    task.vlan_id = 2003
    task.vlan_state = 'active'
    task.add_vlan()

    task.task_name = 'aggregate vlans'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
add_aggregate_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
