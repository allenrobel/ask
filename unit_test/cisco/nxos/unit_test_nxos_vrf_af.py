#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_vrf_af.py
our_version = 100

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_vrf_af import NxosVrfAf

ansible_module = 'nxos_vrf_af'
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

def export_rt(task, rt):
    task.rt = rt
    task.rt_direction = 'export'
    task.rt_state = 'present'
    task.add_rt()
def import_rt(task, rt):
    task.rt = rt
    task.rt_direction = 'import'
    task.rt_state = 'present'
    task.add_rt()

def add_task(pb):
    task = NxosVrfAf(log)

    export_list = list()
    export_list.append('300:2000')

    import_list = list()
    import_list.append('300:2001')
    import_list.append('300:2002')

    for rt in export_list:
        export_rt(task, rt)

    for rt in import_list:
        import_rt(task, rt)

    task.afi = 'ipv4'
    task.route_target_both_auto_evpn = False
    task.state = 'present'
    task.vrf = 'MyVrf'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
