#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_gir_profile_management.py
# Status = BETA
our_version = 100
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_gir_profile_management import NxosGirProfileManagement

log_level_console = 'INFO'
log_level_file = 'DEBUG'
log = Log('my_log', log_level_console, log_level_file)

pb = Playbook(log)
pb.profile_nxos()
pb.ansible_password = 'mypassword'
pb.name = 'nxos_gir_profile_management example'
pb.add_host('dc-101')
pb.file = '/tmp/nxos_gir_profile_management.yaml'

commands = list()
commands.append('router ospf 1')
commands.append('isolate')
task = NxosGirProfileManagement(log)
task.commands = commands
task.mode = 'maintenance'
task.state = 'present'
task.task_name = 'gir mode {} state {}'.format(task.mode, task.state)
task.commit()

pb.add_task(task)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
