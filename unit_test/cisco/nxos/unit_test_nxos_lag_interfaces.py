#!/usr/bin/env python3
# unit_test/nxos/cisco/unit_test_nxos_lag_interfaces.py
our_version = 102
'''
Name: unit_test_ans_task_nxos_lag_interfaces.py

Description:
    Example script and half-hearted unit test for:
        NxosLagInterfaces()   - cisco/nxos/nxos_lag_interfaces.py
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_lag_interfaces import NxosLagInterfaces

ansible_module = 'nxos_lag_interfaces'
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

def add_task(pb):
    task = NxosLagInterfaces(log)
    task.task_name = 'my_lag_task'

    task.name = 'port-channel10'
    task.member = 'Ethernet1/49'
    # task.force = 'yes'
    # task.mode = 'on'
    task.add_member()
    task.member = 'Ethernet1/50'
    # task.mode = 'on'
    task.add_member()
    task.add_lag()

    task.name = 'port-channel20'
    task.member = 'Ethernet1/4'
    # task.force = 'yes'
    # task.mode = 'on'
    task.add_member()
    task.member = 'Ethernet1/5'
    # task.mode = 'on'
    task.add_member()
    task.add_lag()

    task.state = 'merged'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
