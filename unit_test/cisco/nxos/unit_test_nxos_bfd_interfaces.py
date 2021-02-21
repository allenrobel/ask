#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bfd_interfaces.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bfd_interfaces import NxosBfdInterfaces

ansible_module = 'nxos_bfd_interfaces'
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

def delete_bfd_from_all_interfaces(pb):
    task = NxosBfdInterfaces(log)
    task.state = 'deleted'
    task.task_name = '{}: delete_bfd_from_all_interfaces'.format(ansible_module)
    task.update()
    pb.add_task(task)

def delete_bfd_from_some_interfaces(pb):
    task = NxosBfdInterfaces(log)
    for port in [1,2,3,4]:
        task.name = 'Ethernet1/{}'.format(port)
        task.add_interface()
    task.state = 'deleted'
    task.task_name = '{}: delete_bfd_from_some_interfaces'.format(ansible_module)
    task.update()
    pb.add_task(task)

def enable_bfd_on_some_interfaces(pb):
    task = NxosBfdInterfaces(log)
    for port in [5,6,7,8]:
        task.name = 'Ethernet1/{}'.format(port)
        task.bfd = 'enable'
        task.add_interface()
    task.state = 'merged'
    task.task_name = '{}: enable_bfd_on_some_interfaces'.format(ansible_module)
    task.update()
    pb.add_task(task)

def enable_bfd_echo_on_one_interface(pb):
    task = NxosBfdInterfaces(log)
    task.name = 'port-channel101'
    task.echo = 'enable'
    task.add_interface()
    task.state = 'merged'
    task.task_name = '{}: enable_bfd_echo_on_one_interface'.format(ansible_module)
    task.update()
    pb.add_task(task)

pb = playbook()
delete_bfd_from_all_interfaces(pb)
delete_bfd_from_some_interfaces(pb)
enable_bfd_on_some_interfaces(pb)
enable_bfd_echo_on_one_interface(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
