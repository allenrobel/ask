#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_hsrp_interfaces.py
our_version = 101

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_hsrp_interfaces import NxosHsrpInterfaces

ansible_module = 'nxos_hsrp_interfaces'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.ansible_connection = 'httpapi' # httpapi, network_cli
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def hsrp_interface_bfd_enable_task(pb):
    task = NxosHsrpInterfaces(log)
    task.name = 'Ethernet1/10'
    task.bfd = 'enable'
    task.state = 'merged'
    task.task_name = '{}: name {} bfd {} state {}'.format(
        ansible_module,
        task.name,
        task.bfd,
        task.state)
    task.update()
    pb.add_task(task)

def hsrp_interface_bfd_disable_task(pb):
    task = NxosHsrpInterfaces(log)
    task.name = 'Ethernet1/11'
    task.bfd = 'disable'
    task.state = 'merged'
    task.task_name = '{}: name {} bfd {} state {}'.format(
        ansible_module,
        task.name,
        task.bfd,
        task.state)
    task.update()
    pb.add_task(task)

pb = playbook()

hsrp_interface_bfd_enable_task(pb)
hsrp_interface_bfd_disable_task(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
