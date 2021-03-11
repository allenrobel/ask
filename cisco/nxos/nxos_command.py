# NxosCommand() - cisco/nxos/nxos_command.py
our_version = 105

from copy import deepcopy
from ask.common.task import Task

'''
***************
NxosCommand()
***************

.. contents::
   :local:
   :depth: 1

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

'''

class NxosCommand(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_command'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()

        self.properties_set = set()
        self.properties_set.add('answer')
        self.properties_set.add('command')
        self.properties_set.add('commands')
        self.properties_set.add('interval')
        self.properties_set.add('match')
        self.properties_set.add('output')
        self.properties_set.add('prompt')
        self.properties_set.add('retries')
        self.properties_set.add('register')
        self.properties_set.add('wait_for')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_command_valid_output = set()
        self.nxos_command_valid_output.add('text')
        self.nxos_command_valid_output.add('json')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.commands == None and self.command == None:
            self.task_log.error('exiting. instance.commands or instance.command must be set before calling instance.update()')
            exit(1)
        if self.commands != None and self.command != None:
            self.task_log.error('exiting. instance.commands and instance.command cannot both be set')
            exit(1)
        if self.command == None and self.output != None:
            self.task_log.error('exiting. instance.command must be set if instance.output ({}) is set'.format(self.output))
            exit(1)
        if self.command != None and self.output == None:
            self.output = 'text'
        if self.register == None:
            self.task_log.error('exiting. instance.register must be set before calling instance.update()')
            exit(1)
        if self.interval == None:
            self.interval = 1
        if self.match == None:
            self.match = 'all'
        if self.retries == None:
            self.retries = 10

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        d = dict()
        if self.commands != None:
            c = dict()
            d['commands'] = list()
            for command in self.commands:
                c['command'] = command
                c['output'] = self.output
                d['commands'].append(deepcopy(c))
        if self.command != None:
            c = dict()
            c['command'] = self.command
            c['output'] = self.output
            if self.prompt != None:
                c['prompt'] = self.prompt
            if self.answer != None:
                c['answer'] = self.answer
            d['commands'] = list()
            d['commands'].append(deepcopy(c))
        if self.interval != None:
            d['interval'] = self.interval
        if self.match != None:
            d['match'] = self.match
        if self.retries != None:
            d['retries'] = self.retries
        if self.wait_for != None:
            d['wait_for'] = self.wait_for
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.register != None:
            self.ansible_task['register'] = self.register
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_command_output(self, x, parameter='output'):
        verify_set = self.nxos_command_valid_output
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_command_output'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def answer(self):
        return self.properties['answer']
    @answer.setter
    def answer(self, x):
        parameter = 'answer'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def command(self):
        return self.properties['command']
    @command.setter
    def command(self, x):
        parameter = 'command'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def commands(self):
        return self.properties['commands']
    @commands.setter
    def commands(self, x):
        parameter = 'commands'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def interval(self):
        return self.properties['interval']
    @interval.setter
    def interval(self, x):
        parameter = 'interval'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = x

    @property
    def match(self):
        return self.properties['match']
    @match.setter
    def match(self, x):
        parameter = 'match'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def output(self):
        return self.properties['output']
    @output.setter
    def output(self, x):
        parameter = 'output'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_command_output(x, parameter)
        self.properties[parameter] = x

    @property
    def prompt(self):
        return self.properties['prompt']
    @prompt.setter
    def prompt(self, x):
        parameter = 'prompt'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def register(self):
        return self.properties['register']
    @register.setter
    def register(self, x):
        parameter = 'register'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def retries(self):
        return self.properties['retries']
    @retries.setter
    def retries(self, x):
        parameter = 'retries'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = x

    @property
    def wait_for(self):
        return self.properties['wait_for']
    @wait_for.setter
    def wait_for(self, x):
        parameter = 'wait_for'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
