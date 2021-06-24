#!/usr/bin/env python3
# unit_test/common/unit_test_pause.py
our_version = 101
from ask.common.playbook import Playbook
from ask.common.pause import Pause
from ask.common.log import Log

ansible_module = 'pause'
log_level_console = 'INFO'
log_level_file = 'DEBUG'
log = Log('unit_test_{}'.format(ansible_module), log_level_console, log_level_file)

def playbook():
    pb = Playbook(log)
    pb.profile_local()
    pb.file = '/tmp/pause.yaml'
    pb.name = 'pause playbook'
    # Playbook() requires a host.  You can use any host
    # in your inventory here since Pause() ignores it.
    pb.add_host('dc-101') # from Ansible inventory
    return pb

def pause_10(pb):
    task = Pause(log)
    task.seconds = 10
    task.task_name = 'Pause 10 seconds'
    task.commit()
    pb.add_task(task)
def pause_20(pb):
    task = Pause(log)
    task.seconds = 20
    task.task_name = 'Pause 20 seconds'
    task.commit()
    pb.add_task(task)

pb = playbook()
pause_10(pb)
pause_20(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
