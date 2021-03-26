# NxosSystem() - cisco/nxos/nxos_system.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosSystem()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosSystem() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_system
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_system <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_system_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_system.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_system.py>`_

|

========================    =======================================
Property                    Description
========================    =======================================
domain_lookup               When enabled, the system will try to resolve hostnames.
                            When disabled, hostnames will not be resolved::

                                - Type: bool()
                                - Valid values:
                                    - False
                                    - True
                                - Example:
                                    task.domain_lookup = True

domain_name                 Configures the default domain name 
                            suffix to be used when referencing
                            this node by its FQDN::

                                - Type: str()
                                - Example:
                                    task.domain_name = 'bar.com'

domain_search               Configures a list of domain name
                            suffixes to search when performing
                            DNS name resolution::

                                - Type: list()
                                - Example:
                                    domains = list()
                                    domains.append('foo.com')
                                    domains.append('bar.com')
                                    task.domain_search = domains

hostname                    Configure the device hostname parameter::

                                - Type: str()
                                - Valid values:
                                    - domain name
                                    - keyword: default
                                Examples:
                                    task.hostname = 'default'
                                    task.hostname = 'spine01.bar.com'

name_servers                List of DNS name server IP addresses to use 
                            to perform name resolution lookups::

                                - Type:
                                    - list() of str()
                                    - list() of dict()
                                Examples:
                                    # Using list() option

                                    dns = list()
                                    dns.append('1.2.3.4')
                                    dns.append('5.6.7.8')
                                    task.name_servers = dns

                                    # Or, same result
                                    task.name_servers = ['1.2.3.4', '5.6.7.8']

                                    # Using list() of dict() option
                                    from copy import deepcopy
                                    name_servers = list()
                                    dns = dict()
                                    dns['server'] = '1.2.3.4'
                                    dns['vrf'] = 'mgmt'
                                    name_servers.append(deepcopy(dns))
                                    dns = dict()
                                    dns['server'] = '5.6.7.8'
                                    dns['vrf'] = 'backup'
                                    name_servers.append(deepcopy(dns))

                                    # Or, same result:
                                    task.name_servers = [ 
                                        {
                                            'server': '1.2.3.4',
                                            'vrf': 'mgmt'
                                        },
                                        {
                                            'server': '5.6.7.8',
                                            'vrf': 'backup'
                                        }
                                    ]

state                       Desired state after task has completed::

                                - Type: str()
                                - Valid values:
                                    - absent
                                    - present
                                - Example:
                                    task.state = 'present'
                                - Required

system_mtu                  System maximum transfer unit::

                                - Type: int()
                                - Valid values:
                                    - range: 1500-9216
                                    - keyword: default
                                - Examples:
                                    task.system_mtu = 9216
                                    task.system_mtu = 'default'

task_name                   Name of the task. Ansible will display
                            this when the playbook is run::

                                - Type: str()
                                - Example:
                                    - task.task_name = 'my task'

========================    =======================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosSystem(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_system'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.system_mtu_min = 1500
        self.system_mtu_max = 9216

        self.nxos_system_valid_state = set()
        self.nxos_system_valid_state.add('absent')
        self.nxos_system_valid_state.add('present')

        self.properties_set = set()
        self.properties_set.add('domain_lookup')
        self.properties_set.add('domain_name')
        self.properties_set.add('domain_search')
        self.properties_set.add('hostname')
        self.properties_set.add('name_servers')
        self.properties_set.add('system_mtu')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['state'] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)

        # Ensure at least one property is configured by the user or that state == absent
        for p in self.properties_set:
            if self.properties[p] != None:
                return
        if self.state == 'absent':
            return
        self.task_log.error('exiting. No properties have been set.') 
        self.task_log.error('Set at least one property, or set state = "absent"')
        exit(1)

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
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_system_state(self, x, parameter='state'):
        verify_set = self.nxos_system_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_system_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @staticmethod
    def is_list_of_str(x):
        if type(x) != type(list()):
            return False
        for item in x:
            if type(item) != type(str()):
                return False
        return True

    @staticmethod
    def is_list_of_dict(x):
        if type(x) != type(list()):
            return False
        for item in x:
            if type(item) != type(dict()):
                return False
        return True

    def verify_nxos_system_mtu(self, x, parameter='system_mtu'):
        source_method = 'verify_nxos_system_mtu'
        range_min = self.system_mtu_min
        range_max = self.system_mtu_max
        self.verify_integer_range(x, range_min, range_max, source_method, parameter)

    def verify_nxos_system_domain_search(self, x, parameter='domain_search'):
        if x == 'default':
            return
        if self.is_list_of_str(x) == True:
            return
        if self.is_list_of_dict(x) == True:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_system_domain_search'
        expectation = 'list() of str(), list() of dict(), or keyword: default.'
        self.fail(source_class, source_method, x, parameter, expectation)

    @staticmethod
    def verify_name_servers_dict(x):
        for d in x:
            try:
                server = d['server']
                vrf = d['vrf']
            except:
                self.task_log.error('exiting. Expected server and vrf keys in name_servers dict()')
                self.task_log.error('Got {}'.format(d))
                exit(1)
    def verify_nxos_system_name_servers(self, x, parameter='name_servers'):
        if x == 'default':
            return
        if self.is_list_of_str(x) == True:
            return
        if self.is_list_of_dict(x) == True:
            self.verify_name_servers_dict(x)
            return
        source_class = self.class_name
        source_method = 'verify_nxos_system_domain_search'
        expectation = 'list() of str(), list() of dict(), or keyword: default.'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def domain_lookup(self):
        return self.properties['domain_lookup']
    @domain_lookup.setter
    def domain_lookup(self, x):
        parameter = 'domain_lookup'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def domain_name(self):
        return self.properties['domain_name']
    @domain_name.setter
    def domain_name(self, x):
        parameter = 'domain_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def domain_search(self):
        return self.properties['domain_search']
    @domain_search.setter
    def domain_search(self, x):
        parameter = 'domain_search'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_system_domain_search(x, parameter)
        self.properties[parameter] = x

    @property
    def hostname(self):
        return self.properties['hostname']
    @hostname.setter
    def hostname(self, x):
        parameter = 'hostname'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def name_servers(self):
        return self.properties['name_servers']
    @name_servers.setter
    def name_servers(self, x):
        parameter = 'name_servers'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_system_name_servers(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_system_state(x, parameter)
        self.properties[parameter] = x

    @property
    def system_mtu(self):
        return self.properties['system_mtu']
    @system_mtu.setter
    def system_mtu(self, x):
        parameter = 'system_mtu'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_system_mtu(x, parameter)
        self.properties[parameter] = str(x)
