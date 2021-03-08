#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vlans.py
our_version = 102

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vlans import NxosVlans

ansible_module = 'nxos_vlans'
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

def add_task(pb):
    task = NxosVlans(log)
    vlans = [10, 20]
    vnis = [10010, 10020]

    for vlan_id,mapped_vni in zip(vlans, vnis):
        task.enabled = True
        task.mapped_vni = mapped_vni
        task.vlan_state = 'active'
        task.vlan_id = vlan_id
        task.name = 'vlan_{}_vni_{}'.format(task.vlan_id, task.mapped_vni)
        task.add_vlan()
    task.state = 'deleted'
    task.task_name = '{}: vlans {}, vnis {} state {}'.format(ansible_module, vlans, vnis, task.state)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
