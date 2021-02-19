#!/usr/bin/env python3
# unit_test/spirent/unit_test_stc_streamblock.py
our_version = 102
'''
Name: stc_streamblock.py

Description: unit-test for StcStreamblock()
'''
from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.spirent.stc_streamblock import StcStreamblock

ansible_module = 'stc_streamblock'
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.profile_spirent()
    pb.file = '/tmp/{}.yaml'.format(ansible_module)
    pb.name = 'unit_test_{}'.format(ansible_module)
    pb.add_host('labserver-2001')
    return pb

def add_streamblock_under_port(pb):
    task = StcStreamblock(log)
    task.name = '5111_TO_6111'

    task.tx_name = "host_5111"
    task.tx_protocol = 'ipv4'
    task.tx_selector = "EQUAL"
    task.tx_type = 'device'

    task.rx_name = 'host_6111'
    task.rx_protocol = 'ipv4'
    task.rx_selector = "EQUAL"
    task.rx_type = 'device'

    task.port_name = 'port_5111'

    task.stream_only_generation = True
    task.load = 10000
    task.load_unit = 'FRAMES_PER_SECOND'
    task.traffic_pattern = 'PAIR'

    task.task_name = 'StreamBlock under port'
    task.update()
    pb.add_task(task)

def add_streamblock_under_project(pb):
    task = StcStreamblock(log)
    task.name = 'MANY_PORTS_TO_5111'

    task.tx_name = 'host_61'
    task.tx_protocol = 'ipv4'
    task.tx_selector = "STARTS_WITH"
    task.tx_type = 'device'

    task.rx_name = "host_5111"
    task.rx_protocol = 'ipv4'
    task.rx_selector = "EQUAL"
    task.rx_type = 'device'

    task.stream_only_generation = False
    task.load = 5000
    task.load_unit = 'FRAMES_PER_SECOND'
    task.traffic_pattern = 'BACKBONE'

    task.task_name = 'StreamBlock under project'
    task.update()
    pb.add_task(task)

def delete_streamblock(pb):
    '''
    This currently does not work
    '''
    task = StcStreamblock(log)
    task.action = 'delete'
    task.name = 'WE_301_302'
    task.update()
    pb.add_task(task)

pb = playbook()
add_streamblock_under_port(pb)
add_streamblock_under_project(pb)
# delete_streamblock(pb)
pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
