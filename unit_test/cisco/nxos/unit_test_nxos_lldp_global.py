#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_ans_task_nxos_lldp_global.py
our_version = 103

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_lldp_global import NxosLldpGlobal
from ask.ansible.register_save import RegisterSave

ansible_module = 'nxos_lldp_global'
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

def add_task_global(pb):
    task = NxosLldpGlobal(log)
    task.holdtime = 2
    task.port_id = 1
    task.reinit = 3
    task.timer = 4
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_tlv_select(pb):
    task = NxosLldpGlobal(log)
    task.dcbxp = False
    task.power_management = False
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_tlv_select_management_address(pb):
    task = NxosLldpGlobal(log)
    task.management_address_v4 = False
    task.management_address_v6 = False
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_tlv_select_port(pb):
    task = NxosLldpGlobal(log)
    task.port_description = False
    task.port_vlan = False
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_tlv_select_system(pb):
    task = NxosLldpGlobal(log)
    task.system_capabilities = False
    task.system_description = False
    task.system_name = False
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def add_task_state_parsed(pb):
    task = NxosLldpGlobal(log)
    task.running_config = '/tmp/parsed.cfg'
    task.state = 'parsed'
    task.register = 'parsed'
    task.task_name = 'test state parsed'
    add_task_name(task)
    task.update()
    pb.add_task(task)

    task = RegisterSave(log)
    task.filename = '/tmp/parsed_output.txt'
    task.var = 'parsed'
    task.task_name = 'save register'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

add_task_global(pb)
add_task_tlv_select(pb)
add_task_tlv_select_management_address(pb)
add_task_tlv_select_port(pb)
add_task_tlv_select_system(pb)
add_task_state_parsed(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
