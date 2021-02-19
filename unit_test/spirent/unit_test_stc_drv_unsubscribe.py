#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_drv_unsubscribe.py
our_version = 101
'''
*********************************
unit_test_stc_drv_unsubscribe.py
*********************************

Description
-----------
Generates Ansible playbook conformant with Spirent Ansible module: stc

This script generates an Ansible task which unsubscribes from a named
Spirent Dynamic Result View (DRV).

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
StcDrvSubscribe()       stc_drv_subscribe.py  unit_test_stc_drv_subscribe.py
======================  ====================  ===============================

'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.spirent.stc_drv_unsubscribe import StcDrvUnsubscribe

ansible_module = 'stc_drv_unsubscribe'
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.profile_spirent()
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = 'unit_test_{}'.format(ansible_module)
    pb.add_host('labserver-2001')
    return pb

def add_task_stc_drv_unsubscribe_default(pb):
    task = StcDrvUnsubscribe(log)
    task.task_name = 'unsubscribe DRV default'
    task.update()
    pb.add_task(task)

def add_task_stc_drv_unsubscribe_custom(pb):
    task = StcDrvUnsubscribe(log)
    task.drv_name = 'My DRV'
    task.reset_existing = True
    task.task_name = 'unsubscribe DRV custom'
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_stc_drv_unsubscribe_default(pb)
add_task_stc_drv_unsubscribe_custom(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote {}'.format(pb.file))
