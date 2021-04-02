#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_logging.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_logging import NxosLogging

ansible_module = 'nxos_logging'
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

def add_task_logging_event_link_enable(pb):
    task = NxosLogging(log)
    task.event = 'link-enable'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_facility_link_status(pb):
    task = NxosLogging(log)
    task.facility = 'ethpm'
    task.facility_link_status = 'link-up-notif'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_facility_bgp(pb):
    task = NxosLogging(log)
    task.facility = 'bgp'
    task.facility_level = 2
    task.remove_server = '1.2.3.4'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_facility_ospf(pb):
    task = NxosLogging(log)
    task.facility = 'ospf'
    task.facility_level = 3
    task.remove_server = '1.2.3.4'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_logfile(pb):
    task = NxosLogging(log)
    task.dest = 'logfile'
    task.dest_level = 1
    task.file_size = 4194300
    task.name = 'mylog'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_server_ipv4(pb):
    task = NxosLogging(log)
    task.dest = 'server'
    task.dest_level = 0
    task.remote_server = '1.2.3.4'
    task.use_vrf = 'management'
    task.facility = 'local0'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_server_ipv6(pb):
    task = NxosLogging(log)
    task.dest = 'server'
    task.dest_level = 1
    task.remote_server = '2001:a:b:c:d::e'
    task.use_vrf = 'management'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_server_domain_name(pb):
    task = NxosLogging(log)
    task.dest = 'server'
    task.dest_level = 2
    task.remote_server = 'foo.bar.com'
    task.use_vrf = 'management'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_monitor(pb):
    task = NxosLogging(log)
    task.dest = 'monitor'
    task.dest_level = 0
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_timestamp(pb):
    task = NxosLogging(log)
    task.timestamp = '0'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_interface(pb):
    task = NxosLogging(log)
    task.interface = 'mgmt0'
    task.use_vrf = 'management'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_interface_message(pb):
    task = NxosLogging(log)
    task.interface_message = 'add-interface-description'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_timestamp(pb):
    task = NxosLogging(log)
    task.timestamp = 'microseconds'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_logging_purge(pb):
    task = NxosLogging(log)
    task.purge = False
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

pb = playbook()

add_task_logging_event_link_enable(pb)
add_task_logging_facility_link_status(pb)
add_task_logging_facility_bgp(pb)
add_task_logging_facility_ospf(pb)
add_task_logging_logfile(pb)
add_task_logging_monitor(pb)
add_task_logging_server_ipv4(pb)
add_task_logging_server_ipv6(pb)
add_task_logging_server_domain_name(pb)
add_task_logging_interface(pb)
add_task_logging_interface_message(pb)
add_task_logging_timestamp(pb)
add_task_logging_purge(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
