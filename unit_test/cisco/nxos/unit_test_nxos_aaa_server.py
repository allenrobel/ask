#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_aaa_server.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_aaa_server import NxosAaaServer

ansible_module = 'nxos_aaa_server'
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

def nxos_aaa_server(pb):
    task = NxosAaaServer(log)
    task.deadtime = 10
    task.directed_request = 'enabled'
    task.directed_request = None
    task.encrypt_type = 0
    task.global_key = 'foobar'
    task.server_timeout = 40
    task.server_type = 'tacacs'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

pb = playbook()

nxos_aaa_server(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
