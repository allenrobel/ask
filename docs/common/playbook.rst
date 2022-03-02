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
                                If set to the string "STDOUT", write to standard
                                output instead of to a file::

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

