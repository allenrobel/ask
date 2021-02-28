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
                        device config parser::

                            - Type: list()
                            - Valid values: list() containing configuration CLIs
                            - Example:
                                config = list()
                                config.append('interface Ethernet1/1')
                                config.append('  no shutdown')
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
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
