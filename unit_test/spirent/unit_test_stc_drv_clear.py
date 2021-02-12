#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_drv_clear.py
our_version = 101
'''
****************************
unit_test_stc_drv_clear.py
****************************

Description
-----------
Generates Ansible playbook conformant with Spirent Ansible module: stc
This playbook clears Dynamic Result View (DRV) results on all ports.

Prerequisites
-------------

    1.  To run the playbook generated by this script,
        Spirent's Ansible libraries, and their prerequisites,
        must be installed.

        https://github.com/Spirent/stc-ansible

    2.  Playbooks created with the following ScriptKit classes
        (or equivilent playbooks) must be run prior to running
        the playbook created with this script.

======================  ====================  ===============================
Class                   File                  Example script
======================  ====================  ===============================
StcSession()            stc_session.py        unit_test_stc_session.py
StcPorts()              stc_ports.py          unit_test_stc_ports.py
StcPortControl()        stc_port_control.py   unit_test_stc_port_control.py
StcDevice()             stc_device.py         unit_test_stc_device.py
StcDrvCreate()          stc_drv_create.py     unit_test_stc_drv_create.py
======================  ====================  ===============================
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.spirent.stc_drv_clear import StcDrvClear

ansible_module = 'stc_drv_clear'
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = 'unit_test_{}'.format(ansible_module)
    pb.ansible_connection = 'paramiko'
    pb.ansible_password = None
    pb.ansible_network_os = None
    pb.ansible_host_key_checking = 'no'
    pb.ansible_ssh_pass = 'spirent'
    pb.ansible_ssh_common_args = '/bin/ssh'
    pb.ansible_paramiko_pty = 'no'
    pb.ansible_httpapi_validate_certs = None
    pb.ansible_httpapi_use_ssl = None
    pb.add_host('labserver-2001')
    return pb

def add_task_stc_drv_clear(pb):
    task = StcDrvClear(log)
    # If port_list is not specified, results on all ports are cleared
    #task.port_list = 'ref:/port'
    task.task_name = 'clear DRV'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_stc_drv_clear(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
