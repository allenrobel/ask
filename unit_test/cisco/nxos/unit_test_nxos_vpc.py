#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vpc.py
our_version = 103
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vpc import NxosVpc

ansible_module = 'nxos_vpc'
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

def add_task_name(task):
    task.append_to_task_name(ansible_host)
    for key in sorted(task.properties_set):
        task.append_to_task_name(key)

def add_task(pb):
    task = NxosVpc(log)
    task.auto_recovery_reload_delay = 120
    task.domain = 1
    task.delay_restore = 200
    task.delay_restore_interface_vlan = 400
    task.peer_gw = 'yes'
    task.pkl_dest = '1.1.1.1'
    task.pkl_src = '1.1.1.0'
    task.pkl_vrf = 'VPC'
    task.role_priority = 65535
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
