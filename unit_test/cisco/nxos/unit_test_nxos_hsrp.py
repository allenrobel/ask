#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_hsrp.py
our_version = 102

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_hsrp import NxosHsrp

ansible_module = 'nxos_hsrp'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.ansible_connection = 'httpapi' # httpapi, network_cli
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def hsrp(pb):
    task = NxosHsrp(log)
    task.group = 2
    task.interface = 'Vlan101'
    task.state = 'present'
    task.task_name = '{}: group {} interface {} state {}'.format(ansible_module, task.group, task.interface, task.state)
    task.update()
    pb.add_task(task)

pb = playbook()

hsrp(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))

