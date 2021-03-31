#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_evpn_global.py
our_version = 106

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_evpn_global import NxosEvpnGlobal

ansible_module = 'nxos_evpn_global'
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

def test_positive():
    task = NxosEvpnGlobal(log)
    task.nv_overlay_evpn = True
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def test_negative():
    task = NxosEvpnGlobal(log)
    task.task_name = '{}: test_negative'.format(ansible_module)
    try:
        log.info('START ignore these errors')
        task.commit()
        pb.add_task(task)
    except:
        log.info('END ignore these errors')
        pass

pb = playbook()
test_positive()
test_negative()
pb.append_playbook()
pb.write_playbook()
print('wrote playbook {}'.format(pb.file))
