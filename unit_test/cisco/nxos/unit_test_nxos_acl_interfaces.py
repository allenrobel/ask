#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_acl_interfaces.py
our_version = 108

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_acl_interfaces import NxosAclInterfaces

ansible_module = 'nxos_acl_interfaces'
ansible_host = 'dc-101' # must be in ansible inventory
log_level_console = 'INFO'
log_level_file = 'DEBUG'
log = Log('unit_test_{}'.format(ansible_module), log_level_console, log_level_file)

def playbook():
    pb = Playbook(log)
    pb.profile_nxos()
    pb.ansible_password = 'mypassword'
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

def add_task_name(task):
    '''
    add_task_name() can be used to add all currently-set properties
    and their values to the task name.  If a user-accessible property
    key is passed to task.append_to_task_name(), the key AND its
    value are appended to the task name.  All ScriptKit libraries
    include the property task.scriptkit_properties, which is a
    python set() containing all user-accessible property keys
    supported by the library.

    We are not using add_task_name() in this script, but leave
    it here as an example should you want to leverage it.
    '''
    task.append_to_task_name('v{}, {}'.format(our_version, ansible_host))
    for key in sorted(task.scriptkit_properties):
        task.append_to_task_name(key)

def ipv4_access_group(task):
    task.acl_name = 'IPv4_ACL_IN'
    task.append_to_task_name(task.acl_name)
    task.acl_port = False
    task.acl_direction = 'in'
    task.add_acl()
    task.acl_name = 'IPv4_ACL_OUT'
    task.append_to_task_name(task.acl_name)
    task.acl_port = False
    task.acl_direction = 'out'
    task.add_acl()
    task.afi = 'ipv4'
    task.add_access_group()

def ipv6_access_group(task):
    task.acl_name = 'IPv6_ACL_IN'
    task.append_to_task_name(task.acl_name)
    task.acl_port = False
    task.acl_direction = 'in'
    task.add_acl()
    task.acl_name = 'IPv6_ACL_OUT'
    task.append_to_task_name(task.acl_name)
    task.acl_port = False
    task.acl_direction = 'out'
    task.add_acl()
    task.afi = 'ipv6'
    task.add_access_group()

def config_acl_interfaces(task):
    for port in [3,4]:
        ipv4_access_group(task)
        ipv6_access_group(task)
        task.name = 'Ethernet1/{}'.format(port)
        task.append_to_task_name(task.name)
        task.add_interface()

task = NxosAclInterfaces(log)
config_acl_interfaces(task)
task.state = 'merged'
task.commit()

pb = playbook()
pb.add_task(task)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
