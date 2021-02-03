#!/usr/bin/env python3
# python/lib3/ut/unit_test_ans_task_nxos_lldp_global.py
our_version = 100

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_lldp_global import NxosLldpGlobal

ansible_module = 'nxos_lldp_global'
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

def add_item_to_name(item, item_value, name):
    #value = ''
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
        return value
    return name

def add_task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('dcbxp', task.dcbxp, task_name)
    task_name = add_item_to_name('holdtime', task.holdtime, task_name)
    task_name = add_item_to_name('management_address_v4', task.management_address_v4, task_name)
    task_name = add_item_to_name('management_address_v6', task.management_address_v6, task_name)
    task_name = add_item_to_name('port_description', task.port_description, task_name)
    task_name = add_item_to_name('port_id', task.port_id, task_name)
    task_name = add_item_to_name('port_vlan', task.port_vlan, task_name)
    task_name = add_item_to_name('power_management', task.power_management, task_name)
    task_name = add_item_to_name('reinit', task.reinit, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('system_capabilities', task.system_capabilities, task_name)
    task_name = add_item_to_name('system_description', task.system_description, task_name)
    task_name = add_item_to_name('system_name', task.system_name, task_name)
    task_name = add_item_to_name('timer', task.timer, task_name)
    task.task_name = task_name

def add_task_global(pb):
    task = NxosLldpGlobal(log)
    task.holdtime = 2
    task.port_id = 1    # 0 - Advertise interfaces with long-form names
                        # 1 - Advertise interfaces with short-form names
    task.reinit = 3
    task.timer = 4
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_tlv_select(pb):
    task = NxosLldpGlobal(log)
    task.dcbxp = 'no'
    task.power_management = 'no'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_tlv_select_management_address(pb):
    task = NxosLldpGlobal(log)
    task.management_address_v4 = 'no'
    task.management_address_v6 = 'no'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_tlv_select_port(pb):
    task = NxosLldpGlobal(log)
    task.port_description = 'no'
    task.port_vlan = 'no'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_tlv_select_system(pb):
    task = NxosLldpGlobal(log)
    task.system_capabilities = 'no'
    task.system_description = 'no'
    task.system_name = 'no'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

add_task_global(pb)
add_task_tlv_select(pb)
add_task_tlv_select_management_address(pb)
add_task_tlv_select_port(pb)
add_task_tlv_select_system(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
