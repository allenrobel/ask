#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_hsrp_interfaces.py
our_version = 103

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
    task.append_to_task_name('v.{}'.format(our_version))
    task.append_to_task_name(ansible_host)
    task.append_to_task_name('state {}'.format(task.state))
    for key in sorted(task.properties_set):
        task.append_to_task_name(key)

def hsrp_interface_bfd_enable_task(pb):
    task = NxosHsrpInterfaces(log)
    task.name = 'Ethernet1/10'
    task.bfd = 'enable'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def hsrp_interface_bfd_disable_task(pb):
    task = NxosHsrpInterfaces(log)
    task.name = 'Ethernet1/11'
    task.bfd = 'disable'
    task.state = 'merged'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

hsrp_interface_bfd_enable_task(pb)
hsrp_interface_bfd_disable_task(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
