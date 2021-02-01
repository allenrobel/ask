#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_aaa_server_host.py
our_version = 101

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_aaa_server_host import NxosAaaServerHost

ansible_module = 'nxos_aaa_server_host'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def nxos_aaa_server_host(pb):
    task = NxosAaaServerHost(log)
    task.address = '172.29.167.250'
    task.encrypt_type = 0
    task.host_timeout = 10
    task.key = 'foobar'
    task.server_type = 'tacacs'
    task.state = 'present'
    task.task_name = '{} (v{}): address {}, encrypt_type {}, host_timeout {}, key {}, server_type {}, state {}, hosts {}'.format(
        ansible_module,
        our_version,
        task.address,
        task.encrypt_type,
        task.host_timeout,
        task.key,
        task.server_type,
        task.state,
        ','.join(pb.hosts))
    task.update()
    pb.add_task(task)

pb = playbook()

nxos_aaa_server_host(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
