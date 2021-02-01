# NxosAaaServer() - cisco/nxos/nxos_aaa_server.py
our_version = 103
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_aaa_server.py
Description:

NxosAaaServer() generates Ansible Playbook tasks conformant with Ansible module: nxos_aaa_server

This task can then be fed to Playbook().add_task()

Properties:

    deadtime        - Duration, in minutes, after which a non-reachable AAA server is skipped
                        Type: str()
                        Range: 1-1440
                        Device default: 0
    directed_request    - Enables direct authentication requests to AAA server
                            Type: str()
                            Valid values: enabled, disabled, default
                            Default: disabled
    encrypt_type        - The state of encryption applied to the entered global key Type-6 encryption is not supported
                            Type: str()
                            Valid values: 0, 7
                                0 - clear text
                                7 - encrypted
    global_key          - Global AAA shared secret or keyword 'default'.
                            Type: str()
    server_timeout      - Global AAA server timeout period, in seconds, or keyword 'default
                            Type: str()
                            Range: 1-60
                            Device default: 5
    server_type         - The server type is either radius or tacacs
                            Type: str()
                            Valid values: radius, tacacs
    state               - State of the resource
                            Type: str()
                            Valid values: present, default
                            Default: present

Usage example:
    See cisco/nxos/unit_test_nxos_aaa_server.py
'''

class NxosAaaServer(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_aaa_server'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.nxos_aaa_server_deadtime_min = 1
        self.nxos_aaa_server_deadtime_max = 1440

        self.nxos_aaa_server_server_timeout_min = 1
        self.nxos_aaa_server_server_timeout_max = 60

        self.nxos_aaa_server_valid_directed_request = set()
        self.nxos_aaa_server_valid_directed_request.add('enabled')
        self.nxos_aaa_server_valid_directed_request.add('disabled')
        self.nxos_aaa_server_valid_directed_request.add('default')

        self.nxos_aaa_server_valid_encrypt_type = set()
        self.nxos_aaa_server_valid_encrypt_type.add('0')
        self.nxos_aaa_server_valid_encrypt_type.add('7')
        self.nxos_aaa_server_valid_encrypt_type.add(0)
        self.nxos_aaa_server_valid_encrypt_type.add(7)

        self.nxos_aaa_server_valid_server_type = set()
        self.nxos_aaa_server_valid_server_type.add('radius')
        self.nxos_aaa_server_valid_server_type.add('tacacs')

        self.nxos_aaa_server_valid_state = set()
        self.nxos_aaa_server_valid_state.add('present')
        self.nxos_aaa_server_valid_state.add('default')

        self.properties_set = set()
        self.properties_set.add('deadtime')
        self.properties_set.add('directed_request')
        self.properties_set.add('encrypt_type')
        self.properties_set.add('global_key')
        self.properties_set.add('server_timeout')
        self.properties_set.add('server_type')
        self.properties_set.add('state')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.server_type == None:
            self.task_log.error('exiting. Set instance.server_type before calling instance.update()')
            exit(1)
        if self.task_name == None:
            self.task_name = 'nxos_aaa_server: server_type {}'.format(self.server_type)

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

    def verify_nxos_aaa_server_deadtime(self, x, parameter='deadtime'):
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_deadtime'
        range_min = self.nxos_aaa_server_deadtime_min
        range_max = self.nxos_aaa_server_deadtime_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_aaa_server_directed_request(self, x, parameter='directed_request'):
        verify_set = self.nxos_aaa_server_valid_directed_request
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_directed_request'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_aaa_server_encrypt_type(self, x, parameter='encrypt_type'):
        verify_set = self.nxos_aaa_server_valid_encrypt_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_encrypt_type'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_aaa_server_state(self, x, parameter='state'):
        verify_set = self.nxos_aaa_server_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_aaa_server_server_timeout(self, x, parameter='server_timeout'):
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_server_timeout'
        range_min = self.nxos_aaa_server_server_timeout_min
        range_max = self.nxos_aaa_server_server_timeout_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_aaa_server_server_type(self, x, parameter='server_type'):
        verify_set = self.nxos_aaa_server_valid_server_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_aaa_server_server_type'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def deadtime(self):
        return self.properties['deadtime']
    @deadtime.setter
    def deadtime(self, x):
        parameter = 'deadtime'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_deadtime(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def directed_request(self):
        return self.properties['directed_request']
    @directed_request.setter
    def directed_request(self, x):
        parameter = 'directed_request'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_directed_request(x, parameter)
        self.properties[parameter] = x

    @property
    def encrypt_type(self):
        return self.properties['encrypt_type']
    @encrypt_type.setter
    def encrypt_type(self, x):
        parameter = 'encrypt_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_encrypt_type(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def global_key(self):
        return self.properties['global_key']
    @global_key.setter
    def global_key(self, x):
        parameter = 'global_key'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def server_timeout(self):
        return self.properties['server_timeout']
    @server_timeout.setter
    def server_timeout(self, x):
        parameter = 'server_timeout'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_server_timeout(x, parameter)
        self.properties[parameter] = str(x)

    @property
    def server_type(self):
        return self.properties['server_type']
    @server_type.setter
    def server_type(self, x):
        parameter = 'server_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_server_type(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_aaa_server_state(x, parameter)
        self.properties[parameter] = x

