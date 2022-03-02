# Playbook() - common/playbook.py
our_version = 118
from copy import deepcopy
from os import path # write_playbook()
import yaml
'''
***********************************
Playbook()
***********************************

.. contents::
   :local:
   :depth: 1

Version
-------
118

ScriptKit Synopsis
------------------
- Playbook() generates an Ansible Playbook

ScriptKit Example
-----------------
- `unit_test/common/unit_test_playbook.py <https://github.com/allenrobel/ask/blob/main/unit_test/common/unit_test_playbook.py>`_

TODO
----
- This documentation is not yet complete.  ETA: 2021-06-26

|

========================    ============================================
Method                      Description
========================    ============================================
add_environment()           Add a key,value to the playbook environment.::

                                - Type: function()
                                - Example:
                                    pb = Playbook(log)
                                    pb.add_environment('no_proxy', '*')
                                    pb.add_environment('my_key', 'my_value')

add_host()                  Add an ansible host to the current playbook
                            hosts key.  This must match a host in the
                            ansible inventory.::

                                - Type: function()
                                - Example:
                                    pb = Playbook(log)
                                    pb.add_host('spine-101')

add_task()                  Add a task to the current playbook.::

                                - Type: function()
                                - Example:
                                    # Add two tasks to a playbook
                                    pb = Playbook(log)
                                    task = NxosBfdGlobal(log)
                                    task.task_name = 'my bfd task'
                                    task.bfd_interval = 150
                                    task.bfd_min_rx = 150
                                    task.bfd_multiplier = 4
                                    task.commit()
                                    pb.add_task(task)

                                    task = Pause(log)
                                    task.seconds = 10
                                    task.task_name = 'pause 10 seconds'
                                    task.commit()
                                    pb.add_task(task)

                                    pb.append_playbook()
                                    pb.write_playbook()

add_vars()                  Add a key,value to the playbook's vars dict()::

                                - Type: function()
                                - Example:
                                    pb = Playbook(log)
                                    pb.add_vars('my_var1', 'my_var_value1')
                                    pb.add_vars('my_var2', 'my_var_value2')

append_playbook()           Append the current set of tasks as a playbook.
                            Ansible playbook files can contain several 
                            playbooks (in which case, they are called
                            streams).  Hence, append_playbook() can be
                            called multiple times.::

                                - Type: function()
                                - Example:
                                    # Add two playbooks, each with one
                                    # task, to an Ansible Stream.
                                    pb = Playbook(log)
                                    task = NxosBfdGlobal(log)
                                    task.task_name = 'my bfd task'
                                    task.bfd_interval = 150
                                    task.bfd_min_rx = 150
                                    task.bfd_multiplier = 4
                                    task.commit()
                                    pb.add_task(task)
                                    pb.append_playbook()

                                    task = Pause(log)
                                    task.seconds = 10
                                    task.task_name = 'pause 10 seconds'
                                    task.commit()
                                    pb.add_task(task)
                                    pb.append_playbook()

                                    pb.write_playbook()

profile_local()             Set various variables appropriately for
                            a playbook that runs on a local host.
                            Specifically, the following vars are set
                            to None::

                                ansible_connection
                                ansible_host_key_checking
                                ansible_ssh_pass
                                ansible_ssh_common_args
                                ansible_paramiko_pty
                                ansible_password
                                ansible_network_os
                                ansible_httpapi_validate_certs
                                ansible_httpapi_use_ssl::

                            Note, each of the above is
                            also a property, so you can call
                            ``profile_local()`` and then set individual
                            vars as needed, as shown below.::

                                - Type: function()
                                - Example:
                                    pb = Playbook(log)
                                    pb.profile_local()
                                    pb.ansible_password = 'mysecret'

profile_nxos()              Set various variables appropriately for a
                            playbook running against an NX-OS target.
                            Specifically, the following variables are
                            set::

                                ansible_connection = 'httpapi'
                                ansible_command_timeout = 90
                                ansible_host_key_checking = 'no'
                                ansible_httpapi_validate_certs = False
                                ansible_httpapi_use_ssl = True
                                ansible_network_os = 'nxos'
                                ansible_user = 'admin'
                                ansible_paramiko_pty = None
                                ansible_ssh_pass = None
                                ansible_ssh_common_args = None
                                ansible_paramiko_pty = None::

                            Note, each of the above is also a
                            property, so you can call ``profile_nxos()``
                            and then set individual vars to different
                            values as needed, as shown below::

                                - Type: function()
                                - Example:
                                    pb = Playbook(log)
                                    pb.profile_nxos()
                                    pb.ansible_command_timeout = 180
                                    pb.ansible_httpapi_validate_certs = True

write_playbook()            Write the playbook file to disk.::

                                - Type: function()
                                - Example:
                                    pb = Playbook(log)
                                    task = NxosBfdGlobal(log)
                                    task.task_name = 'my bfd task'
                                    task.bfd_interval = 150
                                    task.bfd_min_rx = 150
                                    task.bfd_multiplier = 4
                                    task.commit()
                                    pb.add_task(task)
                                    pb.append_playbook()
                                    pb.write_playbook()

========================    ============================================

|

============================    ==============================================
Property                        Description
============================    ==============================================
file                            Filename to which playbook contents are written.
                                If set to the string 'STDOUT', write to standard
                                output instead of to a file.

                                    - Type: str()
                                    - Examples:
                                        pb.file = '/tmp/playbook.yaml'
                                        pb.file = 'STDOUT'

gather_facts                    Set the Ansible gather_facts key::

                                    - Type: bool()
                                    - Example:
                                        pb = Playbook(log)
                                        pb.gather_facts = False

hosts                           A getter property that returns a python list()
                                of hosts that have been added using
                                ``add_hosts()``::

                                    - Type: getter
                                    - Examples:
                                        pb = Playbook(log)
                                        pb.add_host('host-1')
                                        pb.add_host('host-2')                                        
                                        current_hosts = pb.hosts
                                        # current_hosts contains: ['host-1', 'host-2']

                                        pb = Playbook(log)
                                        current_hosts = pb.hosts
                                        # current_hosts contains an empty list: []

name                            The playbook's name::

                                    - Type: str()
                                    - Example:
                                        pb.name = 'my playbook'

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

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
        self._environment = dict() # see add_environment(), append_playbook()
        # Added for Spirent
        # ansible_host_key_checking:no
        # ansible_ssh_pass:spirent
        # ansible_ssh_common_args:/bin/ssh 
        # ansible_paramiko_pty:no
        self.playbook['vars'] = dict()
        self.playbook['vars']['ansible_command_timeout'] = 90
        self.playbook['vars']['ansible_connection'] = 'httpapi'   # httpapi, network_cli, local, paramiko, ssh
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
        self.ansible_user = 'admin'
        self.ansible_password = None
        self.ansible_network_os = None
        self.ansible_httpapi_validate_certs = None
        self.ansible_httpapi_use_ssl = None

    def profile_local(self):
        self.ansible_connection = None
        self.ansible_host_key_checking = None
        self.ansible_ssh_pass = None
        self.ansible_ssh_common_args = None
        self.ansible_paramiko_pty = None
        self.ansible_password = None
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
        '''
        conveniemce property.  User can also use the following instead:
        pb.add_environment('no_proxy', 'value')
        '''
        if 'no_proxy' in self._environment:
            return self._environment['no_proxy']
        self.log.error('exiting. Set instance.no_proxy before attempting to use it')
        exit(1)
    @no_proxy.setter
    def no_proxy(self, x):
        self._environment['no_proxy'] = x

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

    def add_environment(self, key, value):
        '''
        Add a key,value pair to the environment dict()

        instance.add_environment('no_proxy', '*')
        '''
        self._environment[key] = value

    def add_vars(self, key, value):
        '''
        Add a key,value pair to the vars dict()

        instance.add_vars('my_var', 'my_var_value')
        '''
        self.playbook['vars'][key] = value

    def write_playbook(self):
        '''
        write the playbook.yaml file
        If the file already exists, exit with error.
        '''
        if self.file == None:
            self.log.error('exiting. call pb.file = <filename> before calling pb.write_playbook()')
            exit(1)
        if len(self.stream) == 0:
            self.log.error('exiting. nothing to write.')
            exit(1)
        if self.file == 'STDOUT':
            import sys
            print('{}'.format(yaml.dump(self.stream)))
        else:
            import os
            if path.exists(self.file):
                self.log.error('exiting. refusing to overwrite playbook file {}. delete it first.'.format(self.file))
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
        if len(self._environment) != 0:
            self.playbook['environment'] = deepcopy(self._environment)
        self.stream.append(deepcopy(self.playbook))
        self.init_playbook()
