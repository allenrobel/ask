#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_af.py
our_version = 102

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp_af import NxosBgpAf

ansible_module = 'nxos_bgp_af'
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

def add_item_to_name(item, item_value, name):
    value = ''
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
    else:
        value = name
    return value

def add_task_name_ipv4(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('afi', task.afi, task_name)
    task_name = add_item_to_name('asn', task.asn, task_name)
    task_name = add_item_to_name('maximum_paths', task.maximum_paths, task_name)
    task_name = add_item_to_name('maximum_paths_ibgp', task.maximum_paths_ibgp, task_name)
    task_name = add_item_to_name('safi', task.safi, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('vrf', task.vrf, task_name)
    task.task_name = task_name

def ipv4(pb):
    ipv4_networks = list()
    ipv4_networks.append(['10.239.0.0/32', 'ORIGINATE_TOR_LOOPBACK'])
    ipv4_networks.append(['15.224.0.0/25', 'ORIGINATE_TOR_SUBNETS'])
    ipv4_networks.append(['15.224.0.128/25', 'ORIGINATE_TOR_SUBNETS'])

    task = NxosBgpAf(log)
    task.afi = 'ipv4'
    task.asn = '65100.0'
    task.maximum_paths = 8
    task.maximum_paths_ibgp = 8
    task.networks = ipv4_networks
    task.safi = 'unicast'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name_ipv4(task)
    task.update()
    pb.add_task(task)

def add_task_name_ipv6(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('afi', task.afi, task_name)
    task_name = add_item_to_name('asn', task.asn, task_name)
    task_name = add_item_to_name('maximum_paths', task.maximum_paths, task_name)
    task_name = add_item_to_name('maximum_paths_ibgp', task.maximum_paths_ibgp, task_name)
    task_name = add_item_to_name('safi', task.safi, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task_name = add_item_to_name('vrf', task.vrf, task_name)
    task.task_name = task_name

def ipv6(pb):
    ipv6_networks = list()
    ipv6_networks.append(['2001:aaaa::0/128', 'ORIGINATE_TOR_LOOPBACK'])
    ipv6_networks.append(['2001:aaaa:bbbb::/64', 'ORIGINATE_TOR_SUBNETS'])
    ipv6_networks.append(['2001:aaaa:cccc::/64', 'ORIGINATE_TOR_SUBNETS'])

    task = NxosBgpAf(log)
    task.afi = 'ipv6'
    task.asn = '65101.0'
    task.maximum_paths = 16
    task.maximum_paths_ibgp = 16
    task.networks = ipv6_networks
    task.safi = 'unicast'
    task.state = 'present'
    task.vrf = 'default'
    task.task_name = add_task_name_ipv6(task)
    task.update()
    pb.add_task(task)

pb = playbook()

ipv4(pb)
ipv6(pb)

pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
