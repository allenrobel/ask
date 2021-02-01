#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_ans_task_nxos_command.py
our_version = 101

from ask.ansible.register_save import RegisterSave
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_command import NxosCommand

ansible_module = 'nxos_command'
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

def save_result(pb, filename):
    task = RegisterSave(log)
    task.var = 'output.stdout[0]'
    task.filename = filename # full path to file e.g. /tmp/my_result.json
    task.task_name = 'save {} to {}'.format(task.var, task.filename)
    task.update()
    pb.add_task(task)

def show(pb, command):
    commands = list()
    commands.append(command)
    task = NxosCommand(log)
    task.task_name = '{}: {}'.format(ansible_module, ','.join(commands))
    task.commands = commands
    task.register = 'output'
    task.update()
    pb.add_task(task)

def show_json(pb, command):
    task = NxosCommand(log)
    task.task_name = '{}: output json, {}'.format(ansible_module, command)
    task.command = command
    task.output = 'json'
    task.register = 'output'
    task.update()
    pb.add_task(task)

pb = playbook()

show(pb, 'show clock')
save_result(pb, '/tmp/show_clock.txt')
show(pb, 'show ip bgp summary')
save_result(pb, '/tmp/show_ip_bgp_summary.txt')
show_json(pb, 'show bgp process')
save_result(pb, '/tmp/show_bgp_process.json')

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
