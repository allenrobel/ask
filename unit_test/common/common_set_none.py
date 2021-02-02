#!/usr/bin/env python3
# common/unit_test/common_set_none.py
our_version = 100
from ask.common.playbook import Playbook
from ask.cisco.nxos.nxos_aaa_server import NxosAaaServer
from ask.common.log import Log
log = Log('test_common_set_none', 'INFO', 'DEBUG')

def nxos_aaa_server(pb):
    task = NxosAaaServer(log)
    task.directed_request = 'enabled'
    log.info('BEFORE: task.directed request {}'.format(task.directed_request))
    task.directed_request = None # verifies that Common().set_none() is working
    log.info('AFTER: task.directed request {}'.format(task.directed_request))
    if task.directed_request != None:
        log.error('FAIL: task.directed_request = None')
        exit(1)
    task.server_type = 'tacacs'
    task.state = 'present'
    task.update()
    pb.add_task(task)

pb = Playbook(log)
pb.file = '/tmp/unit_test_common_set_none.yaml'
pb.add_host('dc-101')  # host in Ansible inventory

nxos_aaa_server(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
