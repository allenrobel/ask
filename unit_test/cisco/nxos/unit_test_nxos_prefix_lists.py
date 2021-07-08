#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_prefix_lists.py
our_version = 100

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_prefix_lists import NxosPrefixLists

ansible_module = 'nxos_prefix_lists'
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

def example(pb):
    task = NxosPrefixLists(log)
    task.action = 'permit'
    task.eq = 30
    task.prefix = '10.0.1.0/24'
    task.sequence = 10
    task.add_prefix_list_entry()

    task.action = 'deny'
    task.ge = 24
    task.prefix = '10.1.0.0/16'
    task.sequence = 20
    task.add_prefix_list_entry()

    task.name = 'EXAMPLE_PREFIX_LIST_IPV4'
    task.description = 'An example prefix list'
    task.add_prefix_list()
    task.afi = 'ipv4'
    task.add_afi()
    task.state = 'merged'
    task.commit()
    pb.add_task(task)

pb = playbook()

example(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
