#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_device_config.py
our_version = 102
'''
******************************
unit_test_stc_device_config.py
******************************

Description
-----------
Generates Ansible playbook conformant with Spirent Ansible module: stc
This playbook configures a Spirent ipv4 emulated device and a Spirent
ipv6 emulated device.

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
======================  ====================  ===============================
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.spirent.stc_device_config import StcDeviceConfigIpv4,StcDeviceConfigIpv6

ansible_module = 'stc_device_config'
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.profile_spirent()
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = 'unit_test_{}'.format(ansible_module)
    pb.add_host('labserver-2001')
    return pb

def add_task_stc_device_config_ipv4(pb):
    task = StcDeviceConfigIpv4(log)
    task.count = 1
    task.address = '10.1.1.2'
    task.prefixlen = 25
    task.gateway = '10.1.1.1'
    task.device_name = 'ipv4_device'
    task.task_name = 'ipv4 device config'
    task.update()
    pb.add_task(task)

def add_task_stc_device_config_ipv6(pb):
    task = StcDeviceConfigIpv6(log)
    task.count = 1
    task.address = '2001:a::2'
    task.prefixlen = 120
    task.gateway = '2001:a::1'
    task.device_name = 'ipv6_device'
    task.task_name = 'ipv6 device config'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_stc_device_config_ipv4(pb)
add_task_stc_device_config_ipv6(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
