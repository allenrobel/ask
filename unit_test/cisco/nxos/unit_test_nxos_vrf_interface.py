#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vrf_interface.py
our_version = 102

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vrf_interface import NxosVrfInterface

ansible_module = 'nxos_vrf_interface'
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
    task.append_to_task_name('v.{}'.format(our_version))
    task.append_to_task_name(ansible_host)
    for key in sorted(task.properties_set):
        task.append_to_task_name(key)

def mk_vrf_interface(interfaces, vrf, pb):
    if type(interfaces) == type(str()):
        interfaces = [interfaces]
    for interface in interfaces:
        task = NxosVrfInterface(log)
        task.interface = interface
        task.vrf = vrf
        task.state = 'present'
        add_task_name(task)
        task.update()
        pb.add_task(task)

pb = playbook()

for interface in ['Ethernet1/{}'.format(x) for x in range(11,14)]:
    mk_vrf_interface(interface, 'v200', pb)
for interface in ['Vlan{}'.format(x) for x in range(11,14)]:
    mk_vrf_interface(interface, 'v201', pb)
for interface in ['port-channel{}'.format(x) for x in range(17,20)]:
    mk_vrf_interface(interface, 'v301', pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
