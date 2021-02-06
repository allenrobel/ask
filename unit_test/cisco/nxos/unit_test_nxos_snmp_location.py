#!/usr/bin/env python3
our_version = 101
# unit_test/cisco/nxos/unit_test_nxos_snmp_location.py

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_snmp_location import NxosSnmpLocation

ansible_module = 'nxos_snmp_location'
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

def add_task_name(task):
    def add_item_to_name(item, item_value, name):
        value = ''
        if item_value != None:
            value = '{}, {} {}'.format(name, item, item_value)
        else:
            value = name
        return value
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('location', task.location, task_name)
    task_name = add_item_to_name('state', task.state, task_name)

def add_task(pb):
    task = NxosSnmpLocation(log)
    task.location = 'DC_004:Pod_035:Rack_142'
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
