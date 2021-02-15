#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_pim_interface.py
our_version = 103

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_pim_interface import NxosPimInterface

ansible_module = 'nxos_pim_interface'
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

def add_task_pim_interface_base(pb):
    task = NxosPimInterface(log)
    task.bfd = 'enable'
    task.border = 'no'
    task.dr_prio = 4
    task.hello_interval = 3
    task.interface = 'Ethernet1/49'
    task.sparse = 'yes'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_interface_jp_policy(pb):
    task = NxosPimInterface(log)
    task.jp_policy_in = 'JP_IN'
    task.jp_type_in = 'routemap'
    task.jp_policy_out = 'JP_OUT'
    task.jp_type_out = 'prefix'
    task.interface = 'Ethernet1/49'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_pim_interface_neighbor_policy(pb):
    task = NxosPimInterface(log)
    task.neighbor_policy = 'PIM_NBR_POLICY'
    task.neighbor_type = 'routemap'
    task.interface = 'Ethernet1/49'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_pim_interface_base(pb)
add_task_pim_interface_jp_policy(pb)
add_task_pim_interface_neighbor_policy(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
