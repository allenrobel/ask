#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_system.py
our_version = 107
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_system import NxosSystem

ansible_module = 'nxos_system'
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

def hostname(pb):
    task = NxosSystem(log)
    task.hostname = 'dc-101'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def domain_lookup(pb):
    task = NxosSystem(log)
    task.domain_lookup = True
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def domain_name(pb):
    task = NxosSystem(log)
    task.domain_name = 'dc-101.foo.com'
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def domain_search(pb):
    task = NxosSystem(log)
    task.domain_search = ['foo.com', 'bar.com']
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def name_servers_list(pb):
    task = NxosSystem(log)
    task.name_servers = ['1.2.3.4', '5.6.7.8']
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def name_servers_dict(pb):
    task = NxosSystem(log)
    task.name_servers = [
                            {'server': '1.2.3.4', 'vrf': 'management'},
                            {'server': '5.6.7.8', 'vrf': 'my_vrf'}
                        ]
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

def system_mtu(pb):
    task = NxosSystem(log)
    task.system_mtu = 9216
    task.state = 'present'
    add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
system_mtu(pb)
hostname(pb)
domain_name(pb)
name_servers_list(pb)
name_servers_dict(pb)
domain_lookup(pb)
domain_search(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
