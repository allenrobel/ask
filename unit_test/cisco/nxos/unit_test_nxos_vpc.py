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
    def add_item_to_name(item, item_value, name):
        value = ''
        if item_value != None:
            value = '{}, {} {}'.format(name, item, item_value)
        else:
            value = name
        return value
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('auto_recovery', task.auto_recovery, task_name)
    task_name = add_item_to_name('auto_recovery_reload_delay', task.auto_recovery_reload_delay, task_name)
    task_name = add_item_to_name('delay_restore', task.delay_restore, task_name)
    task_name = add_item_to_name('delay_restore_interface_vlan', task.delay_restore_interface_vlan, task_name)
    task_name = add_item_to_name('delay_restore_orphan_port', task.delay_restore_orphan_port, task_name)
    task_name = add_item_to_name('domain', task.domain, task_name)
    task_name = add_item_to_name('peer_gw', task.peer_gw, task_name)
    task_name = add_item_to_name('pkl_dest', task.pkl_dest, task_name)
    task_name = add_item_to_name('pkl_src', task.pkl_src, task_name)
    task_name = add_item_to_name('pkl_vrf', task.pkl_vrf, task_name)
    task_name = add_item_to_name('role_priority', task.role_priority, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('system_priority', task.system_priority, task_name)
    task.task_name = task_name

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
