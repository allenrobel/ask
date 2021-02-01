#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_evpn_vni.py
our_version = 101

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_evpn_global import NxosEvpnGlobal
from ask.cisco.nxos.nxos_evpn_vni import NxosEvpnVni

ansible_module = 'nxos_evpn_vni'
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

def add_task_evpn_global(pb):
    ansible_module = 'nxos_evpn_global'
    task = NxosEvpnGlobal(log)
    task.nv_overlay_evpn = 'yes'
    task.task_name = '{} {}'.format(ansible_module, ansible_host)
    task.update()
    pb.add_task(task)

def add_item_to_name(item, item_value, name):
    value = ''
    if item_value != None:
        value = '{}, {} {}'.format(name, item, item_value)
    else:
        value = name
    return value

def add_task_name_nxos_evpn_vni(task):
    task_name = '{} {}'.format(ansible_module, ansible_host)
    task_name = add_item_to_name('route_distinguisher', task.route_distinguisher, task_name)
    task_name = add_item_to_name('route_target_both', task.route_target_both, task_name)
    task_name = add_item_to_name('route_target_import', task.route_target_import, task_name)
    task_name = add_item_to_name('route_target_export', task.route_target_export, task_name)
    task_name = add_item_to_name('state', task.state, task_name)
    task.task_name = task_name

def add_task_evpn_vni_rd_digits_format(pb):
    task = NxosEvpnVni(log)
    task.vni = 10301
    task.route_distinguisher = '10301:301'
    task.route_target_import = 'auto'
    task.route_target_export = 'auto'
    task.state = 'present'
    add_task_name_nxos_evpn_vni(task)
    task.update()
    pb.add_task(task)
def add_task_evpn_vni_rd_ip_format(pb):
    task = NxosEvpnVni(log)
    task.vni = 10302
    task.route_distinguisher = '1.2.3.4:302'
    task.route_target_import = ['1.2.3.4:304', '56220:1']
    task.route_target_export = ['65122:13']
    task.state = 'present'
    add_task_name_nxos_evpn_vni(task)
    task.update()
    pb.add_task(task)

pb = playbook()
add_task_evpn_global(pb)
add_task_evpn_vni_rd_digits_format(pb)
add_task_evpn_vni_rd_ip_format(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
