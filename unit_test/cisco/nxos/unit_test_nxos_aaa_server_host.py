#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_aaa_server_host.py
our_version = 103

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_aaa_server_host import NxosAaaServerHost

ansible_module = 'nxos_aaa_server_host'
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

def nxos_aaa_server_host(pb):
    task = NxosAaaServerHost(log)
    task.address = '172.29.167.250'
    task.encrypt_type = 0
    task.host_timeout = 10
    task.key = 'foobar'
    task.server_type = 'tacacs'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

nxos_aaa_server_host(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
