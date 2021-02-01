# NxosConfig() - cisco/nxos/nxos_config.py
our_version = 111

# standard library
from copy import deepcopy
import re
# scriptkit library
from ask.common.task import Task

'''
Name: nxos_config.py

Description:

NxosConfig() creates an Ansible Playbook task conformant with Ansible module nxos_config
An instance of NxosConfig() is then fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_config.py

Properties:

    dir_path        This option provides the path ending with directory name in which the backup
                    configuration file will be stored. If the directory does not exist it will be 
                    created and the filename is either the value of filename or default filename 
                    as described in filename options description. If the path value is not given
                    in that case a backup directory will be created in the current working directory
                    and backup configuration will be copied in filename within backup directory.
    filename        The filename to be used to store the backup configuration. If the filename 
                    is not given it will be generated based on the hostname, current time and date
                    in format defined by <hostname>_config.<current-date>@<current-time>

    after           Valid values: list()
    backup          This argument will cause the module to create a full backup of the current
                    running-config from the remote device before any changes are made. If the
                    backup_options value is not given, the backup file is written to the backup
                    folder in the playbook root directory or role root directory, if playbook is
                    part of an ansible role. If the directory does not exist, it is created.
                    Valid values: no, yes
    before          The ordered set of commands to push on to the command stack if a change needs
                    to be made. This allows the playbook designer the opportunity to perform
                    configuration commands prior to pushing any changes without affecting how
                    the set of commands are matched against the system.
                    Valid values: list()
    defaults        The defaults argument will influence how the running-config is collected from
                    the device. When the value is set to true, the command used to collect the
                    running-config is append with the all keyword. When the value is set to false,
                    the command is issued without the all keyword
                    Valid values: no, yes
    diff_against        When using the ansible-playbook --diff command line argument the module can generate
                        diffs against different sources.
                        Valid values: startup, intended, running
                            - startup - return the diff of the running-config against the startup-config.
                            - intended - return the diff of the running-config against the configuration provided
                                in the intended_config argument.
                            - running - return the before and after diff of the running-config with respect to
                                any changes made to the device configuration.
    diff_ignore_lines   config lines to ignore when diffing
                        Valid values: list() 
    intended_config     list of config lines that the device should conform to
                        Valid values: list() 
    lines               list of config CLI to apply to the device
                        Valid values: list() 
    match               Instructs the module on the way to perform the matching of the
                        set of commands against the current device config.
                        Valid values: line, strict, exact, none
                            line - commands are matched line by line.
                            strict - command lines are matched with respect to position.
                            exact - command lines must be an equal match
                            none - no comparison is made between source configuration and running configuration
    parents             ordered list that identifies the section or hierarcical position the commands should be checked against
                        Valid values: list()
    replace             Valid values: line, block, config
                            line - modified lines are pushed to the device in configuration mode
                            block - entire command block is pushed to the device in configuration mode
                            config - only on Nexus9000.  Uses replace config to push the whole config to the device
    replace_src         path to file containing config that will replace the current config on the device
    running_config      rather than use the device's running-config for comparison, use this set of commands instead
                        Valid values: list()
    save_when           Valid values; always, never, modified, changed
                            always - always issue copy running-config startup-config
                            never - never issue copy running-config startup-config
                            modified - only issue copy running-config startup-config if the modified config differs from the startup-config
                            changed - only issue copy running-config startup-config if the task made a change
    src                 path to the configuration file to load into the remote device.
                        Mutually exclusive with lines and parents arguments

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
        if self.lines == None and self.src == None:
            self.task_log.error('exiting. Either instance.lines or instance.src must be set before calling instance.update()')
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
        self.properties[parameter] = x

    @property
    def diff_against(self):
        return self.properties['diff_against']
    @diff_against.setter
    def diff_against(self, x):
        parameter = 'diff_against'
        if self.set_none(x, parameter):
            return
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
