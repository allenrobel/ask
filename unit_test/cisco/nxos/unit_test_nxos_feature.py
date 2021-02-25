#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_feature.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_feature import NxosFeature

ansible_module = 'nxos_feature'
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
    task.append_to_task_name('v.{}'.format(our_version))
    task.append_to_task_name(ansible_host)
    for key in sorted(task.properties_set):
        task.append_to_task_name(key)

def enable_feature(pb, feature):
    task = NxosFeature(log)
    task.feature = feature
    task.state = 'enabled'
    add_task_name(task)
    task.update()
    pb.add_task(task)
def disable_feature(pb, feature):
    task = NxosFeature(log)
    task.feature = feature
    task.state = 'disabled'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

enable_feature(pb, 'bgp')
enable_feature(pb, 'nv overlay')
enable_feature(pb, 'vn-segment-vlan-based')
disable_feature(pb, 'vpc')

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))

