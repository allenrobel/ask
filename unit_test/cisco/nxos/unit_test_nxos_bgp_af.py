#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_bgp_af.py
our_version = 106

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_bgp_af import NxosBgpAf

ansible_module = 'nxos_bgp_af'
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

def additional_paths_install(pb, asn, afi, safi, vrf):
    task = NxosBgpAf(log)
    task.asn = asn
    task.afi = afi
    task.safi = safi
    task.vrf = vrf
    task.additional_paths_install = True
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def dampening_default(pb, asn, afi, safi, vrf):
    task = NxosBgpAf(log)
    task.asn = asn
    task.afi = afi
    task.safi = safi
    task.vrf = vrf
    task.dampen_igp_metric = 'default'
    task.dampening_half_time = 'default'
    task.dampening_max_suppress_time = 'default'
    task.dampening_reuse_time = 'default'
    task.dampening_suppress_time = 'default'
    # uncomment to test verification mutual-exclusivity
    # task.dampening_state = True
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def dampening_non_default(pb, asn, afi, safi, vrf):
    task = NxosBgpAf(log)
    task.asn = asn
    task.afi = afi
    task.safi = safi
    task.vrf = vrf
    task.dampen_igp_metric = 100
    task.dampening_half_time = 10
    task.dampening_suppress_time = 25
    task.dampening_max_suppress_time = 30
    task.dampening_reuse_time = 20
    # uncomment to test verification mutual-exclusivity
    # task.dampening_state = True
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def networks(pb, asn, afi, safi, vrf):
    networks_list = list()
    if afi == 'ipv6':
        #pass
        networks_list.append(['2001:aaaa::0/128', 'ORIGINATE_TOR_LOOPBACK'])
        networks_list.append(['2001:aaaa:bbbb::/64', 'ORIGINATE_TOR_SUBNETS'])
        networks_list.append(['2001:aaaa:cccc::/64', 'ORIGINATE_TOR_SUBNETS'])
    elif afi == 'ipv4':
        #pass
        networks_list.append(['10.239.0.0/32', 'ORIGINATE_TOR_LOOPBACK'])
        networks_list.append(['15.224.0.0/25', 'ORIGINATE_TOR_SUBNETS'])
        networks_list.append(['15.224.0.128/25', 'ORIGINATE_TOR_SUBNETS'])
    else:
        log.error('exiting. unknown afi {}'.format(afi))
        exit(1)

    task = NxosBgpAf(log)
    task.asn = asn
    task.afi = afi
    task.safi = safi
    task.networks = networks_list
    task.vrf = vrf
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def maximum_paths(pb, asn, afi, safi, vrf):
    task = NxosBgpAf(log)
    task.asn = asn
    task.afi = afi
    task.safi = safi
    task.vrf = vrf
    task.maximum_paths = 16
    task.maximum_paths_ibgp = 16
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

def retain_route_target(pb, asn, afi, safi, vrf):
    task = NxosBgpAf(log)
    task.asn = asn
    task.afi = afi
    task.safi = safi
    task.vrf = vrf
    task.retain_route_target = 'all'
    task.state = 'present'
    task.task_name = add_task_name(task)
    task.update()
    pb.add_task(task)

pb = playbook()

asn = '2301.0'
afi = 'ipv4'
safi = 'unicast'
vrf = 'default'
additional_paths_install(pb, asn, afi, safi, vrf)
networks(pb, asn, afi, safi, vrf)
maximum_paths(pb, asn, afi, safi, vrf)
dampening_default(pb, asn, afi, safi, vrf)
dampening_non_default(pb, asn, afi, safi, vrf)
retain_route_target(pb, asn, afi, safi, vrf)
afi = 'ipv6'
additional_paths_install(pb, asn, afi, safi, vrf)
networks(pb, asn, afi, safi, vrf)
maximum_paths(pb, asn, afi, safi, vrf)
dampening_default(pb, asn, afi, safi, vrf)
dampening_non_default(pb, asn, afi, safi, vrf)
retain_route_target(pb, asn, afi, safi, vrf)

pb.append_playbook()
pb.write_playbook()
print('wrote {}'.format(pb.file))
