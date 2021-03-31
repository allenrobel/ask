#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_config.py
our_version = 108

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_config import NxosConfig

ansible_module = 'nxos_config'
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

def save_when(pb):
    task = NxosConfig(log)
    cfg = list()
    cfg.append('ntp server {} use-vrf management'.format('10.1.2.3'))
    cfg.append('ntp source-interface mgmt0')
    task.lines = cfg
    task.save_when = 'modified'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def diff_against_startup(pb):
    task = NxosConfig(log)
    task.diff_against = 'startup'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def match(pb):
    task = NxosConfig(log)
    cfg = list()
    cfg.append('10 permit ip 192.0.2.1/32 any log')
    cfg.append('20 permit ip 192.0.2.2/32 any log')
    cfg.append('30 permit ip 192.0.2.3/32 any log')
    cfg.append('40 permit ip 192.0.2.4/32 any log')
    cfg.append('50 permit ip 192.0.2.5/32 any log')
    parents = list()
    parents.append('ip access-list test')
    before = list()
    before.append('no ip access-list test')

    task.lines = cfg
    task.parents = parents
    task.before = before
    task.match = 'exact'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def replace_block(pb):
    task = NxosConfig(log)
    cfg = list()
    cfg.append('10 permit ip 192.0.2.1/32 any log')
    cfg.append('20 permit ip 192.0.2.2/32 any log')
    cfg.append('30 permit ip 192.0.2.3/32 any log')
    cfg.append('40 permit ip 192.0.2.4/32 any log')
    parents = list()
    parents.append('ip access-list test')
    before = list()
    before.append('no ip access-list test')

    task.lines = cfg
    task.parents = parents
    task.before = before
    task.replace = 'block'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def replace_config(pb):
    task = NxosConfig(log)
    task.replace_src = 'bootflash:/config.txt'
    task.replace = 'config'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def parents(pb):
    task = NxosConfig(log)
    cfg = list()
    cfg.append('shutdown')
    parents = list()
    parents.append('router bgp 64518')
    parents.append('neighbor 10.0.1.2')
    task.lines = cfg
    task.parents = parents

    add_task_name(task)
    task.commit()
    pb.add_task(task)

pb = playbook()

#save_when(pb)
diff_against_startup(pb)
#match(pb)
#replace_block(pb)
#replace_config(pb)
#parents(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
