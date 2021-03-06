**************************************
NxosLogging()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosLogging() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_logging
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_logging <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_logging_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_logging.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_logging.py>`_


|

========================    ==============================================
Property                    Description
========================    ==============================================
dest                        Destination of the logs::

                                - Type: str()
                                - Valid values:
                                    - console
                                    - logfile
                                    - module
                                    - monitor
                                    - server
                                - Example
                                    task.dest = 'monitor'

dest_level                  Set logging severity level::

                                - Type: int()
                                - Valid values: range: 0-7
                                - Example
                                    task.dest_level = 3

event                       Link/trunk enable/default interface
                            configuration logging::

                                - Type: str()
                                - Valid values:
                                    - link-enable
                                    - link-default
                                    - trunk-enable
                                    - trunk-default
                                - Example:
                                    task.event = 'link-enable'

facility                    Facility name for logging::

                                - Type: str()
                                - Valid values: See NX-OS documentation for list of facilities
                                - Example:
                                    task.facility = 'ospf'

facility_level              Set logging severity levels for facility
                            based log messages::

                                - Type: int()
                                - Valid values: range: 0-7
                                - Example
                                    task.facility_level = 5

facility_link_status        Set logging facility ethpm link status.
                            Not idempotent with version 6.0 images::

                                - Type: str()
                                - Valid values:
                                    - link-down-notif
                                    - link-down-error
                                    - link-up-notif
                                    - link-up-error
                                - Example:
                                    task.facility_link_status = 'link-down-error'

file_size                   Set logfile size::

                                - Type: int()
                                - Valid values: range: 4096-4194304
                                - Example
                                    task.file_size = 500000

interface                   Source interface when sending logging messages::

                                - Type: str()
                                - Valid values: An IP interface
                                - Examples
                                    task.interface = 'Ethernet1/1'
                                    task.interface = 'mgmt0'

interface_message           Add interface description to interface
                            syslogs. Does not work with version 6.0
                            images using nxapi as a transport::

                                - Type: str()
                                - Valid values: add-interface-description
                                - Example:
                                    task.interface_message = 'add-interface-description'

name                        If value of ``dest`` is logfile ``name`` refers to
                            a file name::

                                - Type: str()
                                - Example:
                                    task.name = 'logfile.txt'

purge                       Remove any switch logging configuration that does
                            not match what has been configured.  Not supported
                            for ansible_connection local.  All nxos_logging
                            tasks must use the same ansible_connection type::

                                - Type: bool()
                                - Valid values: False, True
                                - Example:
                                    task.purge = True

remote_server               Hostname or IP Address for remote logging (when
                            ``dest`` is 'server')::

                                - Type: str()
                                - Valid values:
                                    - ipv4 address e.g. A.B.C.D
                                    - ipv6 address e.g. A:B::C:D
                                    - hostname e.g. myhost.mydomain.org
                                - Examples:
                                    task.remote_server = '10.1.1.1'
                                    task.remote_server = '2001::1'
                                    task.remote_server = 'syslog.foo.com'

state                       Desired state after task completion::

                                - Type: str()
                                - Valid values:
                                    - absent
                                    - present
                                - Example:
                                    task.state = 'present'
                                - Required

timestamp                   Set logging timestamp format::

                                - Type: str()
                                - Valid values:
                                    - microseconds
                                    - milliseconds
                                    - seconds
                                - Example:
                                    task.timestamp = 'seconds'

use_vrf                     VRF to be used when sending logging
                            messages to logging servers i.e.
                            ``when`` dest is 'server'::

                                - Type: str()
                                - Example:
                                    task.interface = 'mgmt0'
                                    task.use_vrf = 'management'

task_name                   Name of the task. Ansible will display this
                            when the playbook is run::

                                - Type: str()
                                - Example:
                                    - task.task_name = 'enable lacp'
                                        
========================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
