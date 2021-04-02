#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_ospf_interfaces.py
our_version = 106
'''
----
Name
- unit_test_ans_task_nxos_ospf_interfaces.py

Description
-----------
- Example script and half-hearted unit test for Ansible module: nxos_ospf_interfaces
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_ospf_interfaces import NxosOspfInterfaces

ansible_module = 'nxos_ospf_interfaces'
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

def add_ipv4_process_1(task):
    task.process_area_id = 0
    task.process_secondaries = False
    task.process_multi_areas = [11, 21]
    task.process_id = 1
    task.add_process()
def add_ipv4_process_2(task):
    task.process_area_id = 0
    task.process_secondaries = True
    task.process_multi_areas = [12, 22]
    task.process_id = 2
    task.add_process()

def add_ipv4_authentication(task):
    task.authentication_enable = True
    task.authentication_key_chain = 'foobar'
    task.authentication_message_digest = False
    task.authentication_null_auth = True

def add_ipv4_authentication_key(task):
    task.authentication_key_encryption = 0
    task.authentication_key = 'foobar'

def add_afi_ipv4(task):
    task.afi = 'ipv4'
    add_ipv4_authentication(task)
    add_ipv4_authentication_key(task)
    task.cost = 10
    add_ipv4_process_1(task)
    add_ipv4_process_2(task)

def add_ipv6_message_digest(task):
    task.message_digest_encryption = 7
    task.message_digest_key = 'foobar'
    task.message_digest_key_id = 8

def add_ipv6_process_6(task):
    task.process_area_id = 0
    task.process_secondaries = True
    task.process_id = 6
    task.add_process()

def add_afi_ipv6(task):
    task.afi = 'ipv6'
    add_ipv6_message_digest(task)
    task.cost = 20
    add_ipv6_process_6(task)

def add_timers(task):
    task.dead_interval = 9
    task.hello_interval = 3
    task.retransmit_interval = 3
    task.transmit_delay = 3

def add_general_parameters(task):
    task.mtu_ignore = False
    task.network = 'point-to-point'
    task.passive_interface = False
    #task.priority = 10

def configure_ospf(pb):
    task = NxosOspfInterfaces(log)
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    task.append_to_task_name('Configure OSPF interface:')
    for port in range(1,6):
        task.name = 'Ethernet1/{}'.format(port)
        add_general_parameters(task)
        add_timers(task)
        add_afi_ipv4(task)
        task.add_address_family()
        add_afi_ipv6(task)
        task.add_address_family()
        #task.instance = 1
        task.append_to_task_name(task.name)
        task.add_interface()
    task.state = 'merged'
    task.commit()
    pb.add_task(task)

def shutdown_ospf_process(pb):
    task = NxosOspfInterfaces(log)
    task.append_to_task_name('OSPF shutdown: ')
    for port in range(6,11):
        task.name = 'Ethernet1/{}'.format(port)
        task.afi = 'ipv4'
        task.shutdown = True
        task.add_address_family()
        task.append_to_task_name(task.name)
        task.add_interface()
    task.state = 'merged'
    task.commit()
    pb.add_task(task)

pb = playbook()
configure_ospf(pb)
shutdown_ospf_process(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
