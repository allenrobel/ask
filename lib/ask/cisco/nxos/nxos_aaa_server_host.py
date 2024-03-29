# NxosAaaServerHost() - cisco/nxos/nxos_aaa_server_host.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
******************************************
NxosAaaServerHost() 
******************************************

Version
-------
107

ScriptKit Synopsis
------------------
NxosAaaServerHost() generates Ansible task instances conformant with cisco.nxos.nxos_aaa_server_host.
These task instances can then be passed to Playbook().add_task()

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_aaa_server_host.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_aaa_server_host.py>`_

Ansible Module Documentation
----------------------------
- `nxos_aaa_server_host <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_aaa_server_host_module.rst>`_

|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task::
                                - Type: function()
                                - Alias: update()
                                - Example:
                                    # see ScriptKit Example above for
                                    # full script
                                    pb = Playbook(log)
                                    task = NxosAaaServerHost(log)
                                    task.address = '172.29.167.250'
                                    task.encrypt_type = 0
                                    task.host_timeout = 10
                                    task.key = 'foobar'
                                    task.server_type = 'tacacs'
                                    task.state = 'present'
                                    task.commit()
                                    pb.add_task(task)

========================    ============================================

|

============================    ==============================================
Property                        Description
============================    ==============================================
acct_port                       Alternate UDP port for RADIUS accounting::

                                    - Type: int() or str()
                                    - Valid values:
                                        - range: UDP port-range
                                        - keyword: default
                                    - Examples:
                                        task.acct_port = 8030
                                        task.acct_port = 'default'

address                         Address or name of the radius or tacacs host::

                                    - Type: str()
                                    - Valid values:
                                        - ip address
                                        - hostname
                                    - Examples:
                                        task.address = '10.1.1.2'
                                        task.address = 'aaa.foo.com'
                                    - Required

auth_port                       Alternate UDP port for RADIUS authentication::

                                    - Type: int() or str()
                                    - Valid values:
                                        - range: UDP port-range
                                        - keyword: default
                                    - Examples:
                                        task.auth_port = 8031
                                        task.auth_port = 'default'

encrypt_type                    The state of encryption applied to the entered global key.
                                Type-6 encryption is not supported::

                                    - Type: str()
                                    - Valid values:
                                        0 - clear text
                                        7 - encrypted
                                    - Example:
                                        task.encrypt_type = 7

host_timeout                    Timeout period for the specified host::

                                    - Type: int() or str()
                                    - Units: seconds
                                    - Valid values:
                                        - range: 1-60
                                        - keyword: default
                                    - Examples:
                                        task.host_timeout = 30
                                        task.host_timeout = 'default'

key                             Shared secret for the specified host::

                                    - Type: str()
                                    - Valid values:
                                        - a shared secret key
                                        - keyword: default
                                    - Examples:
                                        task.key = 'a1fe45004f'
                                        task.key = 'default'

server_type                     The authentication protocol used by the server::

                                    - Type: str()
                                    - Valid values:
                                        - radius
                                        - tacacs
                                    - Example:
                                        task.server_type = 'tacacs'

state                           State of the resource after playbook execution::

                                    - Type: str()
                                    - Valid values:
                                        - present
                                        - default
                                    - Default: present
                                    - Example:
                                        task.state = 'default'

tacacs_port                     Alternate TCP port TACACS Server::

                                    - Type: str()
                                    - Valid values:
                                        - range: TCP port-range
                                        - keyword: default
                                    - Examples:
                                        task.tacacs_port = 8045
                                        task.tacacs_port = 'default'

============================    ==============================================

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosAaaServerHost(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_aaa_server_host'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.nxos_aaa_server_host_acct_port_min = 1
        self.nxos_aaa_server_host_acct_port_max = 65535

        self.nxos_aaa_server_host_auth_port_min = 1
        self.nxos_aaa_server_host_auth_port_max = 65535

        self.nxos_aaa_server_host_host_timeout_min = 1
        self.nxos_aaa_server_host_host_timeout_max = 60

        self.nxos_aaa_server_host_tacacs_port_min = 1
        self.nxos_aaa_server_host_tacacs_port_max = 65535

        self.nxos_aaa_server_host_valid_encrypt_type = set()
        self.nxos_aaa_server_host_valid_encrypt_type.add('0')
        self.nxos_aaa_server_host_valid_encrypt_type.add('7')
        self.nxos_aaa_server_host_valid_encrypt_type.add(0)
        self.nxos_aaa_server_host_valid_encrypt_type.add(7)

        self.nxos_aaa_server_host_valid_server_type = set()
        self.nxos_aaa_server_host_valid_server_type.add('radius')
        self.nxos_aaa_server_host_valid_server_type.add('tacacs')

        self.nxos_aaa_server_host_valid_state = set()
        self.nxos_aaa_server_host_valid_state.add('present')
        self.nxos_aaa_server_host_valid_state.add('default')

        self.properties_set = set()
        self.properties_set.add('acct_port')
        self.properties_set.add('address')
        self.properties_set.add('auth_port')
        self.properties_set.add('encrypt_type')
        self.properties_set.add('host_timeout')
        self.properties_set.add('key')
        self.properties_set.add('server_type')
        self.properties_set.add('state')
        self.properties_set.add('tacacs_port')
        self.init_properties()

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.address == None:
            self.task_log.error('exiting. Set instance.address before calling instance.commit()')
            exit(1)
        if self.server_type == None:
            self.task_log.error('exiting. Set instance.server_type before calling instance.commit()')
            exit(1)
        if self.task_name == None:
            self.task_name = 'nxos_aaa_server_host: address {}, server_type {}'.format(self.address, self.server_type)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        call init_properties()
        '''
        self.final_verification()

        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)
        self.init_properties()

    def verify_nxos_aaa_server_host_acct_port(self, x, parameter='acct_port'):
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_host_acct_port'
        range_min = self.nxos_aaa_server_host_acct_port_min
        range_max = self.nxos_aaa_server_host_acct_port_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_aaa_server_host_address(self, x, parameter='address'):
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_host_address'
        if self.is_ipv4_unicast_address(x):
            return
        if self.is_ipv6_address(x):
            return
        expectation = 'ipv4 address or ipv6 address. e.g. 1.1.1.1, 2001::1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_aaa_server_host_auth_port(self, x, parameter='auth_port'):
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_host_auth_port'
        range_min = self.nxos_aaa_server_host_auth_port_min
        range_max = self.nxos_aaa_server_host_auth_port_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_aaa_server_host_encrypt_type(self, x, parameter='encrypt_type'):
        verify_set = self.nxos_aaa_server_host_valid_encrypt_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_host_encrypt_type'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_aaa_server_host_host_timeout(self, x, parameter='host_timeout'):
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_host_host_timeout'
        range_min = self.nxos_aaa_server_host_host_timeout_min
        range_max = self.nxos_aaa_server_host_host_timeout_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_aaa_server_host_state(self, x, parameter='state'):
        verify_set = self.nxos_aaa_server_host_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_host_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)


    def verify_nxos_aaa_server_host_server_type(self, x, parameter='server_type'):
        verify_set = self.nxos_aaa_server_host_valid_server_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_host_server_type'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_aaa_server_host_tacacs_port(self, x, parameter='tacacs_port'):
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_host_tacacs_port'
        range_min = self.nxos_aaa_server_host_tacacs_port_min
        range_max = self.nxos_aaa_server_host_tacacs_port_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    @property
    def acct_port(self):
        return self.properties['acct_port']
    @acct_port.setter
    def acct_port(self, x):
        parameter = 'acct_port'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_host_acct_port(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def address(self):
        return self.properties['address']
    @address.setter
    def address(self, x):
        parameter = 'address'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_host_address(x, parameter)
        self.properties[parameter] = x

    @property
    def auth_port(self):
        return self.properties['auth_port']
    @auth_port.setter
    def auth_port(self, x):
        parameter = 'auth_port'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_host_auth_port(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def encrypt_type(self):
        return self.properties['encrypt_type']
    @encrypt_type.setter
    def encrypt_type(self, x):
        parameter = 'encrypt_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_host_encrypt_type(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def host_timeout(self):
        return self.properties['host_timeout']
    @host_timeout.setter
    def host_timeout(self, x):
        parameter = 'host_timeout'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_host_host_timeout(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def key(self):
        return self.properties['key']
    @key.setter
    def key(self, x):
        parameter = 'key'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def server_type(self):
        return self.properties['server_type']
    @server_type.setter
    def server_type(self, x):
        parameter = 'server_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_host_server_type(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_host_state(x, parameter)
        self.properties[parameter] = x

    @property
    def tacacs_port(self):
        return self.properties['tacacs_port']
    @tacacs_port.setter
    def tacacs_port(self, x):
        parameter = 'tacacs_port'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_host_tacacs_port(x, parameter)
        self.properties[parameter] = str(x)
