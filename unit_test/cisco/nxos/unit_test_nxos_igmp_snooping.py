#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_igmp_snooping.py
our_version = 106

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_igmp_snooping import NxosIgmpSnooping

ansible_module = 'nxos_igmp_snooping'
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

def add_task(pb):
    task = NxosIgmpSnooping(log)
    task.group_timeout = 'default'
    task.link_local_grp_supp = True
    task.report_supp = True
    task.snooping = True
    task.state = 'present'
    task.v3_report_supp = True
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_disable_snooping(pb):
    task = NxosIgmpSnooping(log)
    task.snooping = False
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_link_local_grp_supp(pb):
    task = NxosIgmpSnooping(log)
    task.link_local_grp_supp = True
    task.report_supp = True
    task.snooping = True
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_report_supp(pb):
    task = NxosIgmpSnooping(log)
    task.report_supp = False
    task.snooping = True
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_enable_snooping_non_defaults(pb):
    task = NxosIgmpSnooping(log)
    task.group_timeout = '4444'
    task.link_local_grp_supp = False
    task.report_supp = False
    task.snooping = True
    task.state = 'present'
    task.v3_report_supp = True
    add_task_name(task)
    task.commit()
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
