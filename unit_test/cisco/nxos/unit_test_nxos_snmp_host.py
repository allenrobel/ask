#!/usr/bin/env python3
our_version = 105
# unit_test/cisco/nxos/unit_test_nxos_snmp_host.py

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_snmp_host import NxosSnmpHost

ansible_module = 'nxos_snmp_host'
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

def add_task(pb):
    task = NxosSnmpHost(log)
    task.community = 'public'
    task.snmp_host = '172.29.167.250'
    task.snmp_type = 'trap'
    task.src_intf = 'mgmt0'
    task.version = 'v2c'
    task.vrf = 'management'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
