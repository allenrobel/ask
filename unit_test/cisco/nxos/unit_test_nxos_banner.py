#!/usr/bin/env python3
# unit_test/cisco/nxos/unit_test_nxos_banner.py
our_version = 101

from ask.common.playbook import Playbook
from ask.common.log import Log
from ask.cisco.nxos.nxos_banner import NxosBanner

ansible_module = 'nxos_banner'
ansible_host = 'dc-101' # must be in ansible inventory
log = Log('unit_test_{}'.format(ansible_module), 'INFO', 'DEBUG')

def playbook():
    pb = Playbook(log)
    pb.file = '/tmp/playbook_{}.yaml'.format(ansible_module)
    pb.name = '{} task'.format(ansible_module)
    pb.add_host(ansible_host)
    return pb

# You cannot use '@' in exec_banner since that is the delimiter
# string and you cannot change the delimiter string with nxos_banner
# So, for example, jdoe@foo.com will not work.
exec_banner = '''
Device: {}'
Location: Rack Lab 155, Row C'
Contact: John Doe (jdoe), 555-111-2222'
Project: Customer PoC
'''.format(ansible_host)

motd_banner = "This device is going down for maintenance on April Fool's Day"

def banner_exec(pb):
    task = NxosBanner(log)
    task.banner = 'exec'
    task.text = exec_banner
    task.state = 'present'
    task.task_name = '{} v{}: banner {}, state {}'.format(
        ansible_module,
        our_version,
        task.banner,
        task.state)
    task.update()
    pb.add_task(task)

def banner_motd(pb):
    task = NxosBanner(log)
    task.banner = 'motd'
    task.text = motd_banner
    task.state = 'present'
    task.task_name = '{} v{}: banner {}, state {}'.format(
        ansible_module,
        our_version,
        task.banner,
        task.state)
    task.update()
    pb.add_task(task)

pb = playbook()

banner_exec(pb)
banner_motd(pb)

pb.append_playbook()
pb.write_playbook()
log.info('wrote playbook {}'.format(pb.file))
