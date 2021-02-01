#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_igmp_snooping.py
our_version = 103

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_igmp_snooping import NxosIgmpSnooping

ansible_module = 'nxos_igmp_snooping'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.ansible_connection = 'httpapi' # httpapi, network_cli
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_item_to_name(item, item_value, name):
    value = ''
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
    else:
        value = name
    return value
def add_task_name(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('group_timeout', task.group_timeout, task_name)
    task_name = add_item_to_name('link_local_grp_supp', task.link_local_grp_supp, task_name)
    task_name = add_item_to_name('report_supp', task.report_supp, task_name)
    task_name = add_item_to_name('snooping', task.snooping, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('v3_report_supp', task.v3_report_supp, task_name)
    task.task_name = task_name
def add_task(pb):
    task = NxosIgmpSnooping(log)
    task.group_timeout = 'default'
    task.link_local_grp_supp = 'yes'
    task.report_supp = 'yes'
    task.snooping = 'yes'
    task.state = 'present'
    task.v3_report_supp = 'yes'
    add_task_name(task)
    task.update()
    pb.add_task(task)
def add_task_disable_snooping(pb):
    task = NxosIgmpSnooping(log)
    task.snooping = 'no'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)
def add_task_link_local_grp_supp(pb):
    task = NxosIgmpSnooping(log)
    task.link_local_grp_supp = 'yes'
    task.report_supp = 'yes'
    task.snooping = 'yes'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)
def add_task_report_supp(pb):
    task = NxosIgmpSnooping(log)
    task.report_supp = 'no'
    task.snooping = 'yes'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)
def add_task_enable_snooping_non_defaults(pb):
    task = NxosIgmpSnooping(log)
    task.group_timeout = '4444'
    task.link_local_grp_supp = 'no'
    task.report_supp = 'no'
    task.snooping = 'yes'
    task.state = 'present'
    task.v3_report_supp = 'yes'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
add_task_link_local_grp_supp(pb)
add_task_report_supp(pb)
add_task_disable_snooping(pb)
add_task_enable_snooping_non_defaults(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
