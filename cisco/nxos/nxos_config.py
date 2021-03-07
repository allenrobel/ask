# NxosConfig() - cisco/nxos/nxos_config.py
our_version = 114
from copy import deepcopy
import re
from ask.common.task import Task

'''
**************************************
NxosConfig()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosConfig() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_config
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_config <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_config_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_config.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_config.py>`_


|

====================    ==============================================
Property                Description
====================    ==============================================
dir_path                dir_path specifies the path ending with
                        directory name in which the file specified
                        with ``backup`` will be stored. If the directory
                        does not exist it will be created and the filename
                        is either the value of ``filename`` or default
                        filename as described in ``filename``. If the path
                        value is not given, a backup directory will be
                        created in the current working directory and
                        backup configuration will be copied in filename 
                        within backup directory::

                            - Type: str()
                            - Example:
                                task.dir_path = '/tmp'

filename                The filename to be used to store the configuraion
                        specified with ``backup``. If the filename is not
                        given it will be generated based on the hostname,
                        current time and date in the following format: 
                        <hostname>_config.<current-date>@<current-time>::

                            - Type: str()
                            - Example:
                                task.filename = 'backup_config'

after                   The ordered set of commands to append to the end
                        of the command stack if a change needs to be made.
                        Just like with ``before` this allows the playbook
                        designer to append a set of commands to be
                        executed after the command set::

                            - Type: list()
                            - Example:
                                after = list()
                                after.append('clear counters')
                                task.after = after

backup                  Create a full backup of the current running-config
                        from the remote device before any changes are made.
                        If the ``backup_options`` value is not set, the 
                        backup file is written to the backup folder in the
                        playbook root directory or role root directory,
                        if playbook is part of an ansible role. If the
                        directory does not exist, it is created::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.backup = True


before                  The ordered set of commands to push on to the
                        command stack if a change needs to be made. This
                        allows the playbook designer the opportunity to
                        perform configuration commands prior to pushing
                        any changes without affecting how the set of
                        commands are matched against the system::

                            - Type: list()
                            - Example:
                                before = list()
                                before.append('interface Ethernet1/1')
                                before.append('no shutdown')
                                task.before = before

defaults                Influences how the running-config is collected
                        from the device. When the value is set to True,
                        the command used to collect the running-config
                        is appended with the all keyword. When the value
                        is set to False, the command is issued without
                        the all keyword::

                            - Type: bool()
                            - Valid values: False, True
                            - Example:
                                task.defaults = False

diff_against            When using the ansible-playbook ``--diff`` command
                        line argument, the module can generate diffs against
                        different sources::

                            - Type: str()
                            - Valid values:
                                - intended
                                    return the diff of the running-config
                                    against the configuration provided
                                    in the intended_config argument
                                - running
                                    return the before and after diff of the
                                    running-config with respect to any changes
                                    made to the device configuration
                                - startup
                                    return the diff of the running-config
                                    against the startup-config

diff_ignore_lines       Specify one or more lines that should be ignored during
                        the diff. This is used for lines in the configuration
                        that are automatically updated by the system. This
                        argument takes a list of regular expressions or exact
                        line matches::

                            - Type: list()
                            - Example:
                                ignore = list()
                                ignore.append('^version.*$')
                                task.diff_ignore_lines = ignore

intended_config         Specifies the master configuration that the node should
                        conform to and is used to check the final running-config
                        against. This argument will not modify any settings on
                        the remote device and is strictly used to check the
                        compliance of the current device's configuration
                        against. When specifying this argument, the task
                        should also modify the ``diff_against`` value and
                        set it to ``intended``. The configuration lines for this
                        value should be similar to how it will appear if present
                        in the running-configuration of the device including the
                        indentation to ensure correct diff::

                            - Type: str()
                            - Example:
                                task.intended_config = '/tmp/intended.cfg'

lines                   The ordered set of commands that should be configured in
                        the section. The commands must be the exact same commands
                        as found in the device running-config to ensure idempotency
                        and correct diff. Be sure to note the configuration command
                        syntax as some commands are automatically modified by the
                        device config parser.

                        ScriptKit note: Please note the indentation in the examples
                        below.  ScriptKit requires consistent indentation since it
                        uses this to construct the YAML that nxos_config expects::

                            - Type: list()
                            - Valid values: list() containing configuration CLIs
                            - Examples:
                                config = list()
                                config.append('interface Ethernet1/1')
                                config.append('  no shutdown')
                                task.lines = config

                                config = list()
                                config.append('router bgp 65418')
                                config.append('  address-family ipv4 unicast')
                                config.append('    redistribute direct route-map TOR-EXPORT')
                                config.append('    maximum-paths ibgp 16'
                                config.append('  address-family ipv6 unicast')
                                config.append('    redistribute direct route-map TOR-EXPORT')
                                config.append('    maximum-paths ibgp 16'
                                task.lines = config

match                   Instructs the module on the way to perform the matching
                        of the set of commands against the current device config::

                            - Type: str()
                            - Value values:
                                - exact
                                    command lines must be an equal match
                                - line
                                    commands are matched line by line
                                - none
                                    no comparison is made between source configuration
                                    and running configuration
                                - strict
                                    command lines are matched with respect to position

parents                 An ordered list that identifies the section or hierarcical
                        position the commands should be checked against::

                            - Type: list()
                            - Example:
                                parents = list()
                                parents.append('router bgp 64518')
                                parents.append('address-family ipv4 unicast')
                                task.parents = parents

replace                 Instructs the module on the way to perform the
                        configuration on the device::

                            - Type: str()
                            - Valid values:
                                - block
                                    entire command block is pushed to the device in 
                                    configuration mode
                                - config
                                    NX-OS version must support ``config replace``.
                                    Push the whole config to the device
                                - line
                                    modified lines are pushed to the device in
                                    configuration mode

replace_src             Path to file containing configuration that will replace the entire
                        current configuration on the device.  Mutually exclusive with the
                        ``lines`` and ``src`` arguments.  Device must be running a version
                        of NX-OS that supports ``config replace``.  Use the nxos_file_copy
                        module to copy the configuration file to the remote device and
                        then use the path (typically including bootflash:/) as the value
                        for ``replace_src``. The configuration lines in the file should be
                        similar to how it will appear if present in the running-config
                        of the device including the indentation to ensure idempotency
                        and correct diff::

                            - Type: str()
                            - Example:
                                task.replace_src = 'bootflash:/replace.cfg'


running_config          The module, by default, will connect to the remote device and
                        retrieve the current running-config to use as a base for comparing
                        against the contents of source. There are times when it is not
                        desirable to have the task get the current running-config for
                        every task in a playbook. The running_config argument allows the
                        implementer to pass in the configuration to use as the base
                        config for comparison. The configuration lines for this option
                        should be similar to how it will appear if present in the
                        running-config of the device including the indentation to ensure
                        idempotency and correct diff.::

                            - Type: str()
                            - Example:
                                task.running_config = '/tmp/running.cfg'

save_when               When changes are made to the device running-config, the changes
                        are not copied to non-volatile storage by default. Using this
                        argument will change this behavior:: 

                            - Type: str()
                            - Valid values:
                                - always
                                    Always issue copy running-config startup-config
                                - changed
                                    Issue copy running-config startup-config if the
                                    task made a change
                                - modified
                                    Issue copy running-config startup-config if the
                                    modified config differs from the startup-config
                                - never
                                    Never issue copy running-config startup-config

src                     Path to the configuration file to load into the remote device.
                        Mutually exclusive with ``lines``, ``parents``, and
                        ``replace_src`` arguments::

                            - Type: str()
                            - Example:
                                task.src = '/tmp/config.txt'

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'enable lacp'
                                        
====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosConfig(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_config'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()

        self.properties_set = set()
        self.properties_set.add('after')
        self.properties_set.add('backup')
        self.properties_set.add('before')
        self.properties_set.add('defaults')
        self.properties_set.add('diff_against')
        self.properties_set.add('diff_ignore_lines')
        self.properties_set.add('intended_config')
        self.properties_set.add('lines')
        self.properties_set.add('match')
        self.properties_set.add('parents')
        self.properties_set.add('replace')
        self.properties_set.add('replace_src')
        self.properties_set.add('running_config')
        self.properties_set.add('save_when')
        self.properties_set.add('src')

        self.nxos_config_verify_diff_against = set()
        self.nxos_config_verify_diff_against.add('intended')
        self.nxos_config_verify_diff_against.add('running')
        self.nxos_config_verify_diff_against.add('startup')

        self.nxos_config_verify_match = set()
        self.nxos_config_verify_match.add('exact')
        self.nxos_config_verify_match.add('line')
        self.nxos_config_verify_match.add('none')
        self.nxos_config_verify_match.add('strict')

        self.nxos_config_verify_replace = set()
        self.nxos_config_verify_replace.add('block')
        self.nxos_config_verify_replace.add('config')
        self.nxos_config_verify_replace.add('line')

        self.nxos_config_verify_save_when = set()
        self.nxos_config_verify_save_when.add('always')
        self.nxos_config_verify_save_when.add('changed')
        self.nxos_config_verify_save_when.add('modified')
        self.nxos_config_verify_save_when.add('never')

        self.backup_options_set = set()
        self.backup_options_set.add('dir_path')
        self.backup_options_set.add('filename')

        # the following are used in converting an NXOS config snippet
        # into a format that is expected by the Ansible nxos_config module
        self.last = dict() # see self.push_line() and self.get_stanza()
        for level in list(range(0,31)): # support up to 32 levels of indentation
            self.last[level] = None
        self.re_blank_line = re.compile('^\s*$')
        self.re_leading_spaces = re.compile('^(\s*).*')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.replace_src != None and self.src != None:
            self.task_log.error('exiting. replace_src is mutually-exclusive with src.  Unset one or the other.')
            exit(1)
        if self.replace_src != None and self.lines != None:
            self.task_log.error('exiting. replace_src is mutually-exclusive with lines.  Unset one or the other.')
            exit(1)
        if self.src != None and self.lines != None:
            self.task_log.error('exiting. src is mutually-exclusive with lines.  Unset one or the other.')
            exit(1)
        if self.src != None and self.parents != None:
            self.task_log.error('exiting. src is mutually-exclusive with parents.  Unset one or the other.')
            exit(1)

    def are_all_backup_options_set(self):
        result = True
        for p in self.backup_options_set:
            if self.properties[p] == None:
                result = False
        return result

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        if self.are_all_backup_options_set == True:
            d['backup_options'] = dict()
            for p in self.backup_options_set:
                d['backup_options'][p] = self.properties[p]
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    #---------------------------------------------------------------
    # BEGIN
    # Methods to convert a properly-indented NXOS config into
    # a set of lines that can be consumed by Ansible nxos_config
    #---------------------------------------------------------------
    def indentation_level(self,line):
        '''
        returns int() - the indentation level of line, expressed as the
        number of spaces preceeding line. 

        Example:

        line                 indentation level
        -------------------  -----------------
        router bgp 65000     0
          router-id 1.1.1.1  2
        '''
        m = self.re_leading_spaces.search(line)
        return len(m.group(1))

    def push_line(self, line):
        level = self.indentation_level(line)
        for item in self.last:
            if item == level:
                self.last[item] = line.strip()
            if item > level:
                self.last[item] = None

    def get_stanza(self):
        lines = list()
        for item in sorted(self.last):
            if self.last[item] != None:
                lines.append(self.last[item])
        if len(lines) != 0:
            config = ' ; '.join(lines)
            return config

    @staticmethod
    def is_comment(line):
        if '#' in line:
            return True
        return False
    def is_empty_line(self,line):
        if self.re_blank_line.search(line.strip()):
            return True
        return False

    def gen_lines(self, lines):
        '''
        where lines is a list of nxos config commands, properly
        indented as they would appear in a running or startup config

        Called from lines() property setter
        '''
        config = list()
        for line in lines:
            if self.is_comment(line):
                continue
            if self.is_empty_line(line):
                continue
            self.push_line(line)
            config.append(self.get_stanza())
        return config

    #---------------------------------------------------------------
    # END
    # Methods to convert a properly-indented NXOS config into
    # a set of lines that can be consumed by Ansible nxos_config
    #---------------------------------------------------------------

    def verify_nxos_config_diff_against(self, x, parameter='diff_against'):
        verify_set = self.nxos_config_verify_diff_against
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_config_diff_against'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_config_match(self, x, parameter='match'):
        verify_set = self.nxos_config_verify_match
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_config_match'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_config_replace(self, x, parameter='replace'):
        verify_set = self.nxos_config_verify_replace
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_config_replace'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_config_save_when(self, x, parameter='save_when'):
        verify_set = self.nxos_config_verify_save_when
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_config_save_when'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def dir_path(self):
        return self.properties['dir_path']
    @dir_path.setter
    def dir_path(self, x):
        parameter = 'dir_path'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def filename(self):
        return self.properties['filename']
    @filename.setter
    def filename(self, x):
        parameter = 'filename'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def after(self):
        return self.properties['after']
    @after.setter
    def after(self, x):
        parameter = 'after'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def backup(self):
        return self.properties['backup']
    @backup.setter
    def backup(self, x):
        parameter = 'backup'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x)
        self.properties[parameter] = x

    @property
    def before(self):
        return self.properties['before']
    @before.setter
    def before(self, x):
        parameter = 'before'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def defaults(self):
        return self.properties['defaults']
    @defaults.setter
    def defaults(self, x):
        parameter = 'defaults'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x)
        self.properties[parameter] = x

    @property
    def diff_against(self):
        return self.properties['diff_against']
    @diff_against.setter
    def diff_against(self, x):
        parameter = 'diff_against'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_config_diff_against(x, parameter)
        self.properties[parameter] = x

    @property
    def diff_ignore_lines(self):
        return self.properties['diff_ignore_lines']
    @diff_ignore_lines.setter
    def diff_ignore_lines(self, x):
        parameter = 'diff_ignore_lines'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def intended_config(self):
        return self.properties['intended_config']
    @intended_config.setter
    def intended_config(self, x):
        parameter = 'intended_config'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def lines(self):
        return self.properties['lines']
    @lines.setter
    def lines(self, x):
        parameter = 'lines'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = self.gen_lines(x)

    @property
    def match(self):
        return self.properties['match']
    @match.setter
    def match(self, x):
        parameter = 'match'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_config_match(x, parameter)
        self.properties[parameter] = x

    @property
    def parents(self):
        return self.properties['parents']
    @parents.setter
    def parents(self, x):
        parameter = 'parents'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def replace(self):
        return self.properties['replace']
    @replace.setter
    def replace(self, x):
        parameter = 'replace'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_config_replace(x, parameter)
        self.properties[parameter] = x

    @property
    def replace_src(self):
        return self.properties['replace_src']
    @replace_src.setter
    def replace_src(self, x):
        parameter = 'replace_src'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def running_config(self):
        return self.properties['running_config']
    @running_config.setter
    def running_config(self, x):
        parameter = 'running_config'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def save_when(self):
        return self.properties['save_when']
    @save_when.setter
    def save_when(self, x):
        parameter = 'save_when'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_config_save_when(x, parameter)
        self.properties[parameter] = x

    @property
    def src(self):
        return self.properties['src']
    @src.setter
    def src(self, x):
        parameter = 'src'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
