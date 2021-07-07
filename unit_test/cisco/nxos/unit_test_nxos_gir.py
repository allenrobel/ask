#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_gir.py
# Status = BETA
our_version = 100
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_gir import NxosGir

def playbook():
    pb = Playbook(log)
    pb.profile_nxos()
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def example(pb):
    task = NxosGir(log)
    task.system_mode_maintenance = True
    task.system_mode_maintenance_timeout = 5
    task.state = 'present'
    task.task_name = 'gir isolate state {}'.format(task.state)
    task.commit()
    pb.add_task(task)

def test_invalid_range(pb):
    description = 'system_mode_maintenance_timeout invalid range'
    task = NxosGir(log)
    task.system_mode_maintenance = True
    try:
        task.system_mode_maintenance_timeout = 1
    except:
        log.info('PASS {}'.format(description))
        return
    log.error('FAIL {}'.format(description))

def test_mutual_exclusion_1(pb):
    description = 'mutex system_mode_maintenance & system_mode_maintenance_dont_generate_profile'
    task = NxosGir(log)
    task.state = 'present'
    task.system_mode_maintenance = True
    task.system_mode_maintenance_dont_generate_profile = True
    task.task_name = 'test_mutual_exclusion_1'
    try:
        task.commit()
    except:
        log.info('PASS {}'.format(description))
        return
    log.error('FAIL {}'.format(description))
def test_mutual_exclusion_2(pb):
    description = 'mutex system_mode_maintenance & system_mode_maintenance_shutdown'
    task = NxosGir(log)
    task.state = 'present'
    task.system_mode_maintenance = True
    task.system_mode_maintenance_shutdown = True
    task.task_name = 'test_mutual_exclusion_2'
    try:
        task.commit()
    except:
        log.info('PASS {}'.format(description))
        return
    log.error('FAIL {}'.format(description))
def test_mutual_exclusion_3(pb):
    description = 'mutex system_mode_maintenance_shutdown & system_mode_maintenance_dont_generate_profile'
    task = NxosGir(log)
    task.state = 'present'
    task.system_mode_maintenance_shutdown = True
    task.system_mode_maintenance_dont_generate_profile = True
    task.task_name = 'test_mutual_exclusion_1'
    try:
        task.commit()
    except:
        log.info('PASS {}'.format(description))
        return
    log.error('FAIL {}'.format(description))


ansible_module = 'nxos_gir'
ansible_host = 'dc-101' # must be in ansible inventory
log_level_console = 'INFO'
log_level_file = 'DEBUG'
log = Log('unit_test_{}'.format(ansible_module), log_level_console, log_level_file)

pb = playbook()

example(pb)
# test_invalid_range(pb)
# test_mutual_exclusion_1(pb)
# test_mutual_exclusion_2(pb)
# test_mutual_exclusion_3(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
