#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bfd_interfaces.py
our_version = 103

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bfd_interfaces import NxosBfdInterfaces

ansible_module = 'nxos_bfd_interfaces'
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

def add_task_nxos_bfd_interfaces(pb):
    task = NxosBfdInterfaces(log)
    task.name = 'Ethernet1/35'
    task.bfd = 'enable'
    task.echo = 'disable'
    task.state = 'merged'
    task.task_name = '{}: name {} bfd {} echo {} state {}'.format(
        ansible_module,
        task.name,
        task.bfd,
        task.echo,
        task.state)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_nxos_bfd_interfaces(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
