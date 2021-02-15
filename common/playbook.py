# Playbook() - common/playbook.py
our_version = 114
from copy import deepcopy
from os import path # write_playbook()
import yaml
'''
========================
Playbook() - playbook.py
========================

Description
-----------

Playbook() generates Ansible Playbooks

Synopsis
--------

The following writes a playbook file named playbook.yaml with 
a single task using nxos_interface module.

from ask.common.log import Log
from ask.common.playbook import Playbook
from ask.cisco.nxos.nxos_interfaces import NxosInterfaces

log = Log('test_playbook', 'INFO', 'DEBUG')

pb = Playbook(log)
pb.file = 'playbook.yaml'
pb.add_host('t301')  # host in Ansible inventory

interface = 'Ethernet1/49'
neighbor_interface = 'Ethernet1/1'
neighbor_hostname = 'oz-201v6'

task = NxosInterfaces()
task.task_name = 'configure interface {}'.format(interface)
task.interface = interface
task.mtu = 9216
task.mode = 'layer3'
task.admin_state = 'up'
task.description = '"{} : {} : {}"'.format(
    interface,
    neighbor_interface,
    neighbor_hostname)
task.neighbor_host = neighbor_hostname
task.neighbor_port = neighbor_interface
task.add_neighbor()

pb.add_task(task)
pb.write_playbook()
'''
class Playbook(object):
    def __init__(self, log):
        self.log = log
        self.lib_version = our_version
        self._classname = __class__.__name__

        self._file = None
        self.stream = list() # a list of self.playbook - see self.append_playbook()

        self.init_playbook()

    def init_playbook(self):
        self._hosts = list()
        self._sid = None
        self._ansible_module = None
        self.playbook = dict()
        self.playbook['name'] = 'ansible_playbook'
        self.playbook['gather_facts'] = False
        self.playbook['hosts'] = None
        self.playbook['environment'] = dict()
        self.playbook['environment']['no_proxy'] = "*"
        # Added for Spirent
        # ansible_host_key_checking:no
        # ansible_ssh_pass:spirent
        # ansible_ssh_common_args:/bin/ssh 
        # ansible_paramiko_pty:no
        self.playbook['vars'] = dict()
        self.playbook['vars']['ansible_command_timeout'] = 90
        self.playbook['vars']['ansible_connection'] = 'httpapi'   # httpapi, paramiko, ssh
        self.playbook['vars']['ansible_host_key_checking'] = 'no'
        self.playbook['vars']['ansible_httpapi_use_ssl'] = True
        self.playbook['vars']['ansible_httpapi_validate_certs'] = False
        self.playbook['vars']['ansible_network_os'] = 'nxos'
        self.playbook['vars']['ansible_password'] = 'password'
        self.playbook['vars']['ansible_paramiko_pty'] = 'no'
        self.playbook['vars']['ansible_python_interpreter'] = 'auto_silent'
        self.playbook['vars']['ansible_ssh_pass'] = None
        self.playbook['vars']['ansible_ssh_common_args'] = None
        self.playbook['vars']['ansible_user'] = 'admin'
        self.playbook['tasks'] = list()


    def profile_spirent(self):
        self.ansible_connection = 'paramiko'
        self.ansible_host_key_checking = 'no'
        self.ansible_ssh_pass = 'spirent'
        self.ansible_ssh_common_args = '/bin/ssh'
        self.ansible_paramiko_pty = 'no'
        self.ansible_password = None
        self.ansible_user = None
        self.ansible_network_os = None
        self.ansible_httpapi_validate_certs = None
        self.ansible_httpapi_use_ssl = None

    def profile_nxos(self):
        self.ansible_connection = 'httpapi'
        self.ansible_command_timeout = 90
        self.ansible_host_key_checking = 'no'
        self.ansible_httpapi_validate_certs = False
        self.ansible_httpapi_use_ssl = True
        self.ansible_network_os = 'nxos'
        self.ansible_user = 'admin'
        self.ansible_paramiko_pty = None
        self.ansible_ssh_pass = None
        self.ansible_ssh_common_args = None
        self.ansible_paramiko_pty = None

    @property
    def file(self):
        return self._file
    @file.setter
    def file(self, x):
        self._file = x

    @property
    def name(self):
        return self.playbook['name']
    @name.setter
    def name(self, x):
        self.playbook['name'] = x

    @property
    def ansible_command_timeout(self):
        return self.playbook['vars']['ansible_command_timeout']
    @ansible_command_timeout.setter
    def ansible_command_timeout(self, x):
        try:
            x = int(x)
        except:
            self.log.error('exiting. expected digits.  Got {}'.format(x))
            exit(1)
        self.playbook['vars']['ansible_command_timeout'] = x

    @property
    def ansible_connection(self):
        return self.playbook['vars']['ansible_connection']
    @ansible_connection.setter
    def ansible_connection(self, x):
        self.playbook['vars']['ansible_connection'] = x

    @property
    def ansible_host_key_checking(self):
        return self.playbook['vars']['ansible_host_key_checking']
    @ansible_host_key_checking.setter
    def ansible_host_key_checking(self, x):
        self.playbook['vars']['ansible_host_key_checking'] = x

    @property
    def ansible_httpapi_use_ssl(self):
        return self.playbook['vars']['ansible_httpapi_use_ssl']
    @ansible_httpapi_use_ssl.setter
    def ansible_httpapi_use_ssl(self, x):
        self.playbook['vars']['ansible_httpapi_use_ssl'] = x

    @property
    def ansible_httpapi_validate_certs(self):
        return self.playbook['vars']['ansible_httpapi_validate_certs']
    @ansible_httpapi_validate_certs.setter
    def ansible_httpapi_validate_certs(self, x):
        self.playbook['vars']['ansible_httpapi_validate_certs'] = x

    @property
    def ansible_network_os(self):
        return self.playbook['vars']['ansible_network_os']
    @ansible_network_os.setter
    def ansible_network_os(self, x):
        self.playbook['vars']['ansible_network_os'] = x

    @property
    def ansible_paramiko_pty(self):
        return self.playbook['vars']['ansible_paramiko_pty']
    @ansible_paramiko_pty.setter
    def ansible_paramiko_pty(self, x):
        '''
        no, yes
        default: no
        '''
        self.playbook['vars']['ansible_paramiko_pty'] = x

    @property
    def ansible_password(self):
        return self.playbook['vars']['ansible_password']
    @ansible_password.setter
    def ansible_password(self, x):
        self.playbook['vars']['ansible_password'] = x

    @property
    def ansible_ssh_pass(self):
        return self.playbook['vars']['ansible_ssh_pass']
    @ansible_ssh_pass.setter
    def ansible_ssh_pass(self, x):
        self.playbook['vars']['ansible_ssh_pass'] = x

    @property
    def ansible_ssh_common_args(self):
        return self.playbook['vars']['ansible_ssh_common_args']
    @ansible_ssh_common_args.setter
    def ansible_ssh_common_args(self, x):
        self.playbook['vars']['ansible_ssh_common_args'] = x

    @property
    def ansible_user(self):
        return self.playbook['vars']['ansible_user']
    @ansible_user.setter
    def ansible_user(self, x):
        self.playbook['vars']['ansible_user'] = x

    @property
    def ansible_python_interpreter(self):
        return self.playbook['vars']['ansible_python_interpreter']
    @ansible_python_interpreter.setter
    def ansible_python_interpreter(self, x):
        self.playbook['vars']['ansible_python_interpreter'] = x

    @property
    def no_proxy(self):
        return self.playbook['environment']['no_proxy']
    @no_proxy.setter
    def no_proxy(self, x):
        self.playbook['environment']['no_proxy'] = x

    @property
    def gather_facts(self):
        return self.playbook['gather_facts']
    @gather_facts.setter
    def gather_facts(self, x):
        self.playbook['gather_facts'] = x

    @property
    def hosts(self):
        return self._hosts

    def add_host(self, x):
        self._hosts.append(x)

    def add_task(self, x):
        '''
        x is an instance of a subclass of AskTask() e.g. NxosL3Interfaces()
        '''
        if x == None:
            return
        self.playbook['tasks'].append(deepcopy(x.ansible_task))

    @property
    def ansible_module(self):
        return self._ansible_module
    @ansible_module.setter
    def ansible_module(self, x):
        '''
        The name of an ansible module e.g. nxos_l3_interfaces
        '''
        self._ansible_module = x

    def write_playbook(self):
        '''
        write the playbook.yaml file
        If the file already exists, exit with error.
        '''
        if self.file == None:
            self.log.error('exiting. call pb.file = <filename> before calling pb.write_playbook()')
            exit(1)
        import os
        if path.exists(self.file):
            self.log.error('exiting. refusing to overwrite playbook file {}. delete it first.'.format(self.file))
            exit(1)
        if len(self.stream) == 0:
            self.log.error('exiting. nothing to write.')
            exit(1)
        with open(self.file, 'w') as fh:
            yaml.dump(self.stream, fh, indent=4, allow_unicode=True, explicit_end=True, explicit_start=True, default_flow_style=False) 

    def append_playbook(self):
        if len(self._hosts) == 0:
            self.log.error('exiting. call instance.add_host() before calling pb.append_playbook()')
            exit(1)
        if len(self.playbook['tasks']) == 0:
            self.log.error('exiting. call instance.add_task() before calling pb.append_playbook()')
            exit(1)
        new_vars = dict()
        for var in self.playbook['vars']:
            if self.playbook['vars'][var] != None:
                new_vars[var] = self.playbook['vars'][var]
        self.playbook['vars'] = new_vars
        self.playbook['hosts'] = ','.join(self._hosts)
        self.stream.append(deepcopy(self.playbook))
        self.init_playbook()
