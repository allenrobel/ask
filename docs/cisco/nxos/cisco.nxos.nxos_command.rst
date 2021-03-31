***************
NxosCommand()
***************

.. contents::
   :local:
   :depth: 1

Version
-------
106

ScriptKit Synopsis
------------------
- NxosCommand() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_command
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_command <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_command_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_command.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_command.py>`_


|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task::
                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See also: ScriptKit Example above 

                                    #!/usr/bin/env python3
                                    # Save the output of show version as json
                                    from ask.ansible.register_save import RegisterSave
                                    from ask.common.playbook import Playbook
                                    from ask.common.log import Log
                                    from ask.cisco.nxos.nxos_command import NxosCommand

                                    log_level_console = 'INFO'
                                    log_level_file = 'DEBUG'
                                    log = Log('my_log', log_level_console, log_level_file)

                                    pb = Playbook(log)
                                    pb.profile_nxos()
                                    pb.ansible_password = 'mypassword'
                                    pb.name = 'Example nxos_command'
                                    pb.add_host('dc-101')
                                    pb.file = '/tmp/nxos_command.yaml'

                                    task = NxosCommand(log)
                                    task.command = 'show version'
                                    task.output = 'json'
                                    task.register = 'output'
                                    task.task_name = 'collect output'
                                    task.commit()
                                    pb.add_task(task)

                                    task = RegisterSave(log)
                                    task.var = 'output.stdout[0]'
                                    task.filename = '/tmp/show_version.json'
                                    task.task_name = 'save output'
                                    task.commit()
                                    pb.add_task(task)

                                    pb.append_playbook()
                                    pb.write_playbook()
                                    log.info('wrote {}'.format(pb.file))

                                - Resulting tasks:

                                    hosts: dc-101
                                    name: Example nxos_command
                                    tasks:
                                    -   cisco.nxos.nxos_command:
                                            commands:
                                            -   command: show version
                                                output: json
                                            interval: 1
                                            match: all
                                            retries: 10
                                        name: collect output
                                        register: output
                                    -   local_action: copy content="{{ output.stdout[0] }}" dest="/tmp/show_version.json"
                                        name: save output
                                        vars:
                                            ansible_connection: local

========================    ============================================

|

============================    ==============================================
Property                        Description
============================    ==============================================
answer                          When ``command`` is expected to present a prompt,
                                (see ``prompt``), ``answer`` is how nxos_command
                                should reply to ``prompt``.  ScriptKit ignores
                                both ``answer`` and ``prompt`` if ``commands``
                                is used.  It processes ``answer`` and  ``prompt``
                                only if ``command`` is used::

                                    - Type: str()
                                    - Example:
                                        task.command = 'guestshell destroy'
                                        task.prompt = '[n]'
                                        task.answer = 'y'

commands                        python list() of commands to issue on the
                                remote device::

                                    - Type: list()
                                    - Valid values: list() of str()
                                    - Example:
                                        cmds = list()
                                        cmds.append('show clock')
                                        cmds.append('show version')
                                        task.commands = cmds

command                         An NXOS command to issue on the remote device.
                                If set, commands must NOT be set::

                                    - Type: str()
                                    - Example:
                                        task.command = 'show version'

interval                        Configures the interval in seconds to wait
                                between retries of the command. If the command
                                does not pass the specified conditional, the
                                interval indicates how to long to wait before 
                                trying the command again::

                                    - Type: int()
                                    - Default: 1
                                    - Example:
                                        task.interval = 20

match                           Used in conjunction with ``wait_for`` to specify
                                the match policy::

                                    - Type: str()
                                    - Valid values:
                                        - all: all conditionals in wait_for must be satisfied
                                        - any: only one value in wait_for must be satisfied
                                    - Default: all
                                    - Example:
                                        task.match = 'any'

output                          Desired output format for ``command`` or ``commands``::

                                    - Type: str()
                                    - Valid values:
                                        - json
                                        - text
                                    - Example:
                                        task.output = 'json'

prompt                          When ``command`` is expected to present a prompt,
                                use ``prompt`` to tell Ansible what string to expect.
                                ScriptKit ignores both ``answer`` and ``prompt`` if
                                ``commands`` is used.  It processes ``answer`` and 
                                ``prompt`` only if ``command`` is used::

                                    - Type: str()
                                    - Example:
                                        task.command = 'guestshell destroy'
                                        task.prompt = '[n]'
                                        task.answer = 'y'

retries                         Specifies the number of times a command 
                                should be tried before it is considered failed.
                                The command is run on the target device every
                                retry and evaluated against the wait_for 
                                conditionals::

                                    - Type: int()
                                    - Default: 10
                                    - Example:
                                        task.retries = 3

register                        Variable in which to save the command output::

                                    - Type: str()
                                    - Example:
                                        task.register = 'result'

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Example:
                                        task.task_name = 'issue show version'

wait_for                        Specifies what to evaluate from the output of the
                                command and what conditionals to apply. This argument
                                will cause the task to wait for a particular conditional
                                to be true before moving forward. If the conditional is not
                                true by the configured retries, the task fails::

                                    - Type: python list()
                                    - Valid values: list() of str()
                                    - Example:
                                        waitfor = list()
                                        waitfor.append('result[0] contains "NXOS:"')
                                        waitfor.append('result[1] contains "Ethernet1/1"')
                                        task.wait_for = waitfor

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

