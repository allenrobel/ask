#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_hsrp_interfaces.py
our_version = 105

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_hsrp_interfaces import NxosHsrpInterfaces

ansible_module = 'nxos_hsrp_interfaces'
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

def hsrp_interface_bfd_enable_task(pb):
    task = NxosHsrpInterfaces(log)
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    task.append_to_task_name('HSRP BFD enable:')
    for port in range(1,6):
        task.name = 'Ethernet1/{}'.format(port)
        task.bfd = 'enable'
        task.append_to_task_name(task.name)
        task.add_interface()
    task.state = 'merged'
    task.commit()
    pb.add_task(task)

def hsrp_interface_bfd_disable_task(pb):
    task = NxosHsrpInterfaces(log)
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    task.append_to_task_name('HSRP BFD disable:')
    for port in range(6,11):
        task.name = 'Ethernet1/{}'.format(port)
        task.bfd = 'disable'
        task.append_to_task_name(task.name)
        task.add_interface()
    task.state = 'merged'
    task.commit()
    pb.add_task(task)

pb = playbook()

hsrp_interface_bfd_enable_task(pb)
hsrp_interface_bfd_disable_task(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
