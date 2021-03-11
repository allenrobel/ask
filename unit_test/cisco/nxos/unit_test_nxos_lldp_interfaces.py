#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_lldp_interfaces.py
our_version = 105

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_lldp_interfaces import NxosLldpInterfaces
from ask.ansible.register_save import RegisterSave

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

def add_task_name(task):
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    for key in sorted(task.scriptkit_properties):
        task.append_to_task_name(key)


# def add_task_name(task):
#     task.append_to_task_name('v.{}'.format(our_version))
#     task.append_to_task_name(ansible_host)
#     if task.running_config != None:
#         task.append_to_task_name('running_config {}'.format(task.running_config))
#     for key in sorted(task.properties_set):
#         task.append_to_task_name(key)

def task_tlv_set_0_member(pb):
    task = NxosLldpInterfaces(log)
    task.name = 'Ethernet1/10'
    task.receive = True
    task.transmit = True
    task.state = 'merged'
    add_task_name(task)
    task.add_interface()
    task.update()
    pb.add_task(task)

def task_tlv_set_1_member(pb):
    task = NxosLldpInterfaces(log)
    task.name = 'Ethernet1/1'
    task.receive = False
    task.transmit = True
    task.tlv_set_management_address = '1.1.1.1'
    task.state = 'merged'
    add_task_name(task)
    task.add_interface()
    task.update()
    pb.add_task(task)

def task_tlv_set_2_member(pb):
    task = NxosLldpInterfaces(log)
    task.name = 'Ethernet1/2'
    task.receive = True
    task.transmit = True
    task.tlv_set_management_address = '2.1.1.1'
    task.tlv_set_vlan = 2
    task.state = 'merged'
    add_task_name(task)
    task.add_interface()
    task.update()
    pb.add_task(task)

def add_task_state_parsed(pb):
    task = NxosLldpInterfaces(log)
    task.running_config = '/tmp/parsed.cfg'
    task.state = 'parsed'
    task.register = 'parsed'
    task.task_name = 'test state parsed'
    task.update()
    pb.add_task(task)

    task = RegisterSave(log)
    task.filename = '/tmp/parsed_output.txt'
    task.var = 'parsed'
    task.task_name = 'save register'
    task.update()
    pb.add_task(task)

pb = playbook()

task_tlv_set_0_member(pb)
task_tlv_set_1_member(pb)
task_tlv_set_2_member(pb)
add_task_state_parsed(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
