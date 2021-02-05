#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_ospf_interfaces.py
our_version = 103
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
    pb.ansible_connection = 'httpapi' # httpapi, network_cli
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_ipv4_process_1(task):
    task.process_area_id = 0
    task.process_secondaries = 'no'
    task.process_multi_areas = [11, 21]
    task.process_id = 1
    task.add_process()
def add_ipv4_process_2(task):
    task.process_area_id = 0
    task.process_secondaries = 'yes'
    task.process_multi_areas = [12, 22]
    task.process_id = 2
    task.add_process()

def add_ipv4_authentication(task):
    task.authentication_enable = 'yes'
    task.authentication_key_chain = 'foobar'
    task.authentication_message_digest = 'no'
    task.authentication_null_auth = 'yes'

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
    task.process_secondaries = 'yes'
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
    task.mtu_ignore = 'no'
    task.network = 'point-to-point'
    task.passive_interface = 'no'
    #task.priority = 10

def add_ospf_interface(pb):
    task = NxosOspfInterfaces(log)
    task.task_name = '{} {}'.format(ansible_host, ansible_module)
    add_general_parameters(task)
    add_timers(task)
    add_afi_ipv4(task)
    task.add_address_family()

    add_afi_ipv6(task)
    task.add_address_family()

    #task.instance = 1
    task.name = 'Ethernet1/7'
    task.state = 'merged'
    task.update()
    pb.add_task(task)

def task_nxos_ospf_interfaces_shutdown(pb):
        task = NxosOspfInterfaces(log)
        task.name = 'Ethernet1/8'
        task.afi = 'ipv4'
        task.shutdown = 'yes'
        # We call task.task_name prior to task.add_address_family() since 
        # task.add_address_family() calls init_address_family() which initializes
        # afi to None.
        task.task_name = '{} {} shutdown ospf afi {} on interface {}'.format(
            ansible_host,
            ansible_module,
            task.afi,
            task.name)
        task.add_address_family()
        task.state = 'merged'
        task.update()
        pb.add_task(task)

pb = playbook()
add_ospf_interface(pb)
task_nxos_ospf_interfaces_shutdown(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
