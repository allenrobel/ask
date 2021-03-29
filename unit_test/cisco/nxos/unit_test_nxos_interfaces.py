#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_interfaces.py
our_version = 105

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_interfaces import NxosInterfaces

ansible_module = 'nxos_interfaces'
ansible_host = 'dc-101' # must be in ansible inventory
log_level_console = 'INFO'
log_level_file = 'DEBUG'
log = Log('unit_test_{}'.format(ansible_module), log_level_console, log_level_file)

def playbook():
    pb = Playbook(log)
    pb.profile_nxos()
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = '{} 5 ethernet and 5 SVI interfaces'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_ethernet_interfaces(task):
    for port in range(1,6):
        task.name = 'Ethernet1/{}'.format(port)
        task.description = '{} Vlan{} hosts'.format(task.name, port + 220)
        task.mtu = 9216
        task.mode = 'layer2'
        task.speed = 100000
        task.duplex = 'auto'
        task.append_to_task_name(task.name)
        task.add_interface()

def add_svi_interfaces(task):
    for vlan in range(221,226):
        task.name = 'Vlan{}'.format(vlan)
        task.mtu = 1500
        task.fabric_forwarding_anycast_gateway = True
        task.mode = 'layer3'
        task.append_to_task_name(task.name)
        task.add_interface()

pb = playbook()
task = NxosInterfaces(log)
task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
add_ethernet_interfaces(task)
add_svi_interfaces(task)
task.state = 'merged'
task.update()
pb.add_task(task)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
