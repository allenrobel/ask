#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_evpn_vni.py
our_version = 104

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_evpn_global import NxosEvpnGlobal
from ask.cisco.nxos.nxos_evpn_vni import NxosEvpnVni

ansible_module = 'nxos_evpn_vni'
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
    for key in sorted(task.properties_set):
        task.append_to_task_name(key)

def add_task_evpn_global(pb):
    ansible_module = 'nxos_evpn_global'
    task = NxosEvpnGlobal(log)
    task.nv_overlay_evpn = True
    add_task_name(task)
    task.commit()
    pb.add_task(task)

def add_task_evpn_vni_rd_digits_format(pb):
    task = NxosEvpnVni(log)
    task.vni = 10301
    task.route_distinguisher = '10301:301'
    task.route_target_import = 'auto'
    task.route_target_export = 'auto'
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)
def add_task_evpn_vni_rd_ip_format(pb):
    task = NxosEvpnVni(log)
    task.vni = 10302
    task.route_distinguisher = '1.2.3.4:302'
    task.route_target_import = ['1.2.3.4:304', '56220:1']
    task.route_target_export = ['65122:13']
    task.state = 'present'
    add_task_name(task)
    task.commit()
    pb.add_task(task)

pb = playbook()
add_task_evpn_global(pb)
add_task_evpn_vni_rd_digits_format(pb)
add_task_evpn_vni_rd_ip_format(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
