**************************************
NxosStaticRoutes()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosStaticRoutes() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_static_routes
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_static_routes <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_static_routes_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_static_routes.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_static_routes.py>`_

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

                                - Type: str(
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
