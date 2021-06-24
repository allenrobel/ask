#!/usr/bin/env python3
from ask.common.log import Log
from ask.common.playbook import Playbook
from ask.cisco.nxos.nxos_interfaces import NxosInterfaces
from ask.cisco.nxos.nxos_bfd_interfaces import NxosBfdInterfaces

def task_nxos_interfaces(pb):
    '''
    add a NxosInterfaces() task
    '''
    interface = 'Ethernet1/49'
    neighbor_interface = 'Ethernet1/1'
    neighbor_hostname = 'spine-201'

    task = NxosInterfaces(log)
    task.task_name = 'configure interface {}'.format(interface)
    task.name = interface
    task.mtu = 9216
    task.mode = 'layer3'
    task.admin_state = 'up'
    task.description = '"{} : {} : {}"'.format(
        interface,
        neighbor_interface,
        neighbor_hostname)
    task.add_interface()
    task.state = 'merged'
    task.commit()
    pb.add_task(task)

def task_nxos_bfd_interfaces(pb):
    task = NxosBfdInterfaces(log)
    task.name = 'Ethernet1/49'
    task.echo = 'enable'
    task.add_interface()
    task.state = 'merged'
    task.task_name = 'enable bfd echo on {}'.format(task.name)
    task.commit()
    pb.add_task(task)

log = Log('test_playbook', 'INFO', 'DEBUG')
pb = Playbook(log)
pb.profile_nxos() # commonly used NXOS settings
pb.ansible_connection = 'network_cli' # profile_nxos() sets this to httpapi
pb.ansible_password = 'mypassword'
pb.file = '/tmp/playbook.yaml'

# Creates a single playbook with two tasks
task_nxos_interfaces(pb)
task_nxos_bfd_interfaces(pb)
pb.add_host('t301')  # host in Ansible inventory
pb.add_environment('no_proxy', '*')
pb.append_playbook()
pb.write_playbook()

# Alternatively, you can create two playbooks, each with a 
# single task, and write them both to the same file (Ansible
# calls this a Stream)

# task_nxos_interfaces(pb)
# pb.add_environment('no_proxy', '*')
# pb.add_host('t301')  # host in Ansible inventory
# pb.append_playbook()

# task_nxos_bfd_interfaces(pb)
# pb.add_environment('no_proxy', '*')
# pb.add_host('t301')  # host in Ansible inventory
# pb.append_playbook()

pb.write_playbook()

