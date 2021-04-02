#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vlans.py
our_version = 104

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

def add_task_name(task):
    '''
    add_task_name() can be used to add all currently-set properties
    and their values to the task name.  If a user-accessible property
    key is passed to task.append_to_task_name(), the key AND its
    value are appended to the task name.  All ScriptKit libraries
    include the property task.scriptkit_properties, which is a
    python set() containing all user-accessible property keys
    supported by the library.

    We are not using add_task_name() in this script, but leave
    it here as an example should you want to leverage it.
    '''
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    for key in sorted(task.scriptkit_properties):
        task.append_to_task_name(key)

def add_task(pb):
    task = NxosVlans(log)
    task.append_to_task_name('Enable vlans')
    vlans = [10, 20]
    vnis = [10010, 10020]

    for vlan_id,mapped_vni in zip(vlans, vnis):
        task.enabled = True
        task.mapped_vni = mapped_vni
        task.vlan_state = 'active'
        task.vlan_id = vlan_id
        task.append_to_task_name(task.vlan_id)
        task.add_vlan()
    task.state = 'merged'
    task.commit()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
