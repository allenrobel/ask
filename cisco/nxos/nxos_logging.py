# NxosLogging() - cisco/nxos/nxos_logging.py
our_version = 102
from copy import deepcopy
from ask.common.task import Task
'''
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

'''
class NxosLogging(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_logging'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()

        self.properties_set = set()
        self.properties_set.add('dest')
        self.properties_set.add('dest_level')
        self.properties_set.add('event')
        self.properties_set.add('facility')
        self.properties_set.add('facility_level')
        self.properties_set.add('facility_link_status')
        self.properties_set.add('file_size')
        self.properties_set.add('interface')
        self.properties_set.add('interface_message')
        self.properties_set.add('name')
        self.properties_set.add('purge')
        self.properties_set.add('remote_server')
        self.properties_set.add('state')
        self.properties_set.add('timestamp')
        self.properties_set.add('use_vrf')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_logging_valid_dest = set()
        self.nxos_logging_valid_dest.add('console')
        self.nxos_logging_valid_dest.add('logfile')
        self.nxos_logging_valid_dest.add('module')
        self.nxos_logging_valid_dest.add('monitor')
        self.nxos_logging_valid_dest.add('server')

        self.nxos_logging_valid_event = set()
        self.nxos_logging_valid_event.add('link-enable')
        self.nxos_logging_valid_event.add('link-default')
        self.nxos_logging_valid_event.add('trunk-enable')
        self.nxos_logging_valid_event.add('trunk-default')

        self.nxos_logging_valid_facility_link_status = set()
        self.nxos_logging_valid_facility_link_status.add('link-down-notif')
        self.nxos_logging_valid_facility_link_status.add('link-down-error')
        self.nxos_logging_valid_facility_link_status.add('link-up-notif')
        self.nxos_logging_valid_facility_link_status.add('link-up-error')

        self.nxos_logging_valid_interface_message = set()
        self.nxos_logging_valid_interface_message.add('add-interface-description')

        self.nxos_logging_valid_state = set()
        self.nxos_logging_valid_state.add('absent')
        self.nxos_logging_valid_state.add('present')

        self.nxos_logging_valid_timestamp = set()
        self.nxos_logging_valid_timestamp.add('microseconds')
        self.nxos_logging_valid_timestamp.add('milliseconds')
        self.nxos_logging_valid_timestamp.add('seconds')

        self.nxos_logging_file_size_min = 4096
        self.nxos_logging_file_size_max = 4194304

        self.nxos_logging_level_min = 0
        self.nxos_logging_level_max = 7

        self.nxos_logging_facility_level_min = 0
        self.nxos_logging_facility_level_max = 7

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name']    = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.dest == 'server' and self.remote_server == None:
            self.task_log.error('exiting. instance.dest == server, but instance.remote_server is not set')
            exit(1)
        if self.dest != 'server' and self.remote_server != None:
            self.task_log.error('exiting. instance.dest != server, but instance.remote_server is set')
            exit(1)
        if self.dest == 'logfile' and self.name == None:
            self.task_log.error('exiting. instance.dest == logfile, but instance.name is not set')
            exit(1)
        if self.dest != 'logfile' and self.name != None:
            self.task_log.error('exiting. instance.dest != logfile, but instance.name is set')
            exit(1)
        if self.file_size != None and self.name == None:
            self.task_log.error('exiting. instance.file_size is set, but instance.name is not set')
            exit(1)
        if self.facility != None and self.facility_level == None and self.facility_link_status == None and self.remote_server == None:
            self.task_log.error('exiting. instance.facility is set, but one of instance.facility_level or instance.facility_link_status or instance.remote_server is not set')
            exit(1)
        if self.facility_level != None and (self.facility == None and self.facility_link_status == None and self.remote_server == None):
            self.task_log.error('exiting. instance.facility_level is set, but one of instance.facility or instance.facility_link_status or instance.remote_server is not set')
            exit(1)

    def commit(self):
        self.update()
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
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_logging_dest(self, x, parameter='dest'):
        verify_set = self.nxos_logging_valid_dest
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_logging_dest'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_logging_event(self, x, parameter='event'):
        verify_set = self.nxos_logging_valid_event
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_logging_event'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_logging_facility_link_status(self, x, parameter='facility_link_status'):
        verify_set = self.nxos_logging_valid_facility_link_status
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_logging_facility_link_status'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_logging_file_size(self, x):
        source_class = self.class_name
        source_method='verify_nxos_logging_file_size'
        range_min = self.nxos_logging_file_size_min
        range_max = self.nxos_logging_file_size_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_logging_interface(self, x, parameter='logging_interface'):
        if self.is_ethernet_interface(x):
            return
        if self.is_loopback_interface(x):
            return
        if self.is_management_interface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_logging_interface'
        expectation = 'Full name of an IP interface e.g. Ethernet1/1, port-channel4, Vlan32, Loopback3'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_logging_interface_message(self, x, parameter='interface_message'):
        verify_set = self.nxos_logging_valid_interface_message
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_logging_interface_message'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_logging_state(self, x, parameter='state'):
        verify_set = self.nxos_logging_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_logging_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_logging_timestamp(self, x, parameter='timestamp'):
        verify_set = self.nxos_logging_valid_timestamp
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_logging_timestamp'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_logging_level(self, x):
        range_min = self.nxos_logging_level_min
        range_max = self.nxos_logging_level_max
        source_class = self.class_name
        source_method='verify_nxos_logging_level'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_logging_facility_level(self, x):
        range_min = self.nxos_logging_facility_level_min
        range_max = self.nxos_logging_facility_level_max
        source_class = self.class_name
        source_method='verify_nxos_logging_facility_level'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    @property
    def dest(self):
        return self.properties['dest']
    @dest.setter
    def dest(self, x):
        parameter = 'dest'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_dest(x, parameter)
        self.properties[parameter] = x

    @property
    def dest_level(self):
        return self.properties['dest_level']
    @dest_level.setter
    def dest_level(self, x):
        parameter = 'dest_level'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_level(x)
        self.properties[parameter] = x

    @property
    def event(self):
        return self.properties['event']
    @event.setter
    def event(self, x):
        parameter = 'event'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_event(x, parameter)
        self.properties[parameter] = x

    @property
    def facility(self):
        return self.properties['facility']
    @facility.setter
    def facility(self, x):
        parameter = 'facility'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def facility_level(self):
        return self.properties['facility_level']
    @facility_level.setter
    def facility_level(self, x):
        parameter = 'facility_level'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_facility_level(x)
        self.properties[parameter] = x

    @property
    def facility_link_status(self):
        return self.properties['facility_link_status']
    @facility_link_status.setter
    def facility_link_status(self, x):
        parameter = 'facility_link_status'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_facility_link_status(x, parameter)
        self.properties[parameter] = x

    @property
    def file_size(self):
        return self.properties['file_size']
    @file_size.setter
    def file_size(self, x):
        parameter = 'file_size'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_file_size(x)
        self.properties[parameter] = x

    @property
    def interface(self):
        return self.properties['interface']
    @interface.setter
    def interface(self, x):
        parameter = 'interface'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def interface_message(self):
        return self.properties['interface_message']
    @interface_message.setter
    def interface_message(self, x):
        parameter = 'interface_message'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_interface_message(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def purge(self):
        return self.properties['purge']
    @purge.setter
    def purge(self, x):
        parameter = 'purge'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def remote_server(self):
        return self.properties['remote_server']
    @remote_server.setter
    def remote_server(self, x):
        parameter = 'remote_server'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_state(x, parameter)
        self.properties[parameter] = x

    @property
    def timestamp(self):
        return self.properties['timestamp']
    @timestamp.setter
    def timestamp(self, x):
        parameter = 'timestamp'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_logging_timestamp(x, parameter)
        self.properties[parameter] = x

    @property
    def use_vrf(self):
        return self.properties['use_vrf']
    @use_vrf.setter
    def use_vrf(self, x):
        parameter = 'use_vrf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

