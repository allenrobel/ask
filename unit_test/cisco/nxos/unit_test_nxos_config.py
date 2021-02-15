#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_config.py
our_version = 105

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

def ntp():
    task = NxosConfig(log)
    task.task_name = '{} {} ntp'.format(ansible_host, ansible_module)
    cfg = list()
    cfg.append('ntp server {} use-vrf management'.format('172.29.167.1'))
    cfg.append('ntp source-interface mgmt0')
    task.lines = cfg
    task.update()
    return task

def hostname():
    task = NxosConfig(log)
    task.task_name = '{} {} hostname'.format(ansible_host, ansible_module)
    cfg = list()
    cfg.append('hostname {}'.format(ansible_host))
    task.lines = cfg
    task.update()
    return task

def bgp():
    task = NxosConfig(log)
    task.task_name = '{} {} bgp_router'.format(ansible_host, ansible_module)
    cfg = list()
    cfg.append('router bgp 17234')
    cfg.append('  address-family ipv4 unicast')
    cfg.append('    send-community')
    cfg.append('  address-family ipv6 unicast')
    cfg.append('    send-community')
    cfg.append('  neighbor 1.1.1.1')
    cfg.append('    inherit peer foo')
    task.lines = cfg
    task.update()
    return task

def tcam():
    task = NxosConfig(log)
    task.task_name = '{} {} tcam'.format(ansible_host, ansible_module)
    cfg = list()
    cfg.append('hardware access-list tcam region ipv6-ifacl 0')
    cfg.append('hardware access-list tcam region mac-ifacl 0')
    cfg.append('hardware access-list tcam region ipv6-racl 0')
    cfg.append('hardware access-list tcam region e-racl 4096')
    task.lines = cfg
    task.update()
    return task

def vrf_context_management():
    task = NxosConfig(log)
    task.task_name = '{} {} vrf context management'.format(ansible_host, ansible_module)
    cfg = list()
    cfg.append('vrf context management')
    cfg.append('ip name-server {}'.format('172.29.167.250'))
    cfg.append('ip route 0.0.0.0/0 {}'.format('172.29.167.1'))
    cfg.append('ipv6 route ::/0 2001:420:283:2000:3:11:160:1')
    task.lines = cfg
    task.update()
    return task

pb = playbook()

pb.add_task(hostname())
pb.add_task(ntp())
pb.add_task(vrf_context_management())
pb.add_task(tcam())
pb.add_task(bgp())

pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
