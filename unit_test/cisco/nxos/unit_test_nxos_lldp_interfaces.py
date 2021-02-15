#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_lldp_interfaces.py
our_version = 102

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_lldp_interfaces import NxosLldpInterfaces

ansible_module = 'nxos_lldp_interfaces'
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

def add_item_to_name(item, item_value, name):
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
        return value
    return name

def add_task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('name', task.name, task_name)
    task_name = add_item_to_name('receive', task.receive, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('tlv_set_management_address', task.tlv_set_management_address, task_name)
    task_name = add_item_to_name('tlv_set_vlan', task.tlv_set_vlan, task_name)
    task_name = add_item_to_name('transmit', task.transmit, task_name)
    task.task_name = task_name

def task_tlv_set_0_member(pb):
    task = NxosLldpInterfaces(log)
    task.name = 'Ethernet1/10'
    task.receive = 'yes'
    task.transmit = 'yes'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def task_tlv_set_1_member(pb):
    task = NxosLldpInterfaces(log)
    task.name = 'Ethernet1/1'
    task.receive = 'no'
    task.transmit = 'yes'
    task.tlv_set_management_address = '1.1.1.1'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def task_tlv_set_2_member(pb):
    task = NxosLldpInterfaces(log)
    task.name = 'Ethernet1/2'
    task.receive = 'yes'
    task.transmit = 'yes'
    task.tlv_set_management_address = '2.1.1.1'
    task.tlv_set_vlan = 2
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

task_tlv_set_0_member(pb)
task_tlv_set_1_member(pb)
task_tlv_set_2_member(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
