#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_feature.py
our_version = 102

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_feature import NxosFeature

ansible_module = 'nxos_feature'
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

def enable_feature(pb, feature):
    task = NxosFeature(log)
    task.feature = feature         # string: feature name (type feature ? in config-mode on nxos switch for a list)
    task.state = 'enabled'         # string: enabled, disabled
    task.task_name = '{}: feature {} state {}'.format(ansible_module, task.feature, task.state)
    task.update()
    pb.add_task(task)
def disable_feature(pb, feature):
    task = NxosFeature(log)
    task.feature = feature         # string: feature name (type feature ? in config-mode on nxos switch for a list)
    task.state = 'disabled'        # string: enabled, disabled
    task.task_name = '{}: feature {} state {}'.format(ansible_module, task.feature, task.state)
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

