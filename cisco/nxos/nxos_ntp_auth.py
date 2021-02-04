# NxosNtpAuth() - cisco/nxos/nxos_ntp_auth.py
our_version = 100
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_ntp_auth.py

Description:

NxosNtpAuth() generates Ansible Playbook tasks conformant with nxos_ntp_auth
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_ntp_auth.py

Properties:

    Valid values for all abool() types are: no, yes
    Valid range for all type int() is: 0-65535

    auth_type               str()   Whether the given md5string is in cleartext or has been encrypted.
                                    If in cleartext, the device will encrypt it before storing it.
                                    Valid values: text, encrypt
    authentication          str()   Turns NTP authentication on or off
                                    Valid values: on, off
    key_id                  str()   Authentication key identifier (numeric)
                                    Valid values: digits
    md5string               str()   MD5 String
    state                   str()   The state of the configuration after module completion
                                    Valid values: absent, present
    trusted_key             str()   Whether the given key is required to be supplied by a time source for the device to synchronize to the time source.
                                    Valid values: false, true
'''
class NxosNtpAuth(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_ntp_auth'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()

        self.properties_set = set()
        self.properties_set.add('auth_type')
        self.properties_set.add('authentication')
        self.properties_set.add('key_id')
        self.properties_set.add('md5string')
        self.properties_set.add('state')
        self.properties_set.add('trusted_key')

        self.nxos_ntp_auth_valid_auth_type = set()
        self.nxos_ntp_auth_valid_auth_type.add('text')
        self.nxos_ntp_auth_valid_auth_type.add('encrypt')

        self.nxos_ntp_auth_valid_authentication = set()
        self.nxos_ntp_auth_valid_authentication.add('on')
        self.nxos_ntp_auth_valid_authentication.add('off')

        self.nxos_ntp_auth_valid_state = set()
        self.nxos_ntp_auth_valid_state.add('absent')
        self.nxos_ntp_auth_valid_state.add('present')

        self.nxos_ntp_auth_valid_trusted_key = set()
        self.nxos_ntp_auth_valid_trusted_key.add('false')
        self.nxos_ntp_auth_valid_trusted_key.add('true')

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

    def update(self):
        '''
        call final_verification()
        populate and append dict() to self.ansible_task[self.ansible_module]['config']

        '''
        self.final_verification()

        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_ntp_auth_auth_type(self, x, parameter='auth_type'):
        verify_set = self.nxos_ntp_auth_valid_auth_type
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ntp_auth_auth_type'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ntp_auth_authentication(self, x, parameter='authentication'):
        verify_set = self.nxos_ntp_auth_valid_authentication
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ntp_auth_authentication'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ntp_auth_state(self, x, parameter='state'):
        verify_set = self.nxos_ntp_auth_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ntp_auth_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ntp_auth_trusted_key(self, x, parameter='trusted_key'):
        verify_set = self.nxos_ntp_auth_valid_trusted_key
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ntp_auth_trusted_key'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def auth_type(self):
        return self.properties['auth_type']
    @auth_type.setter
    def auth_type(self, x):
        parameter = 'auth_type'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ntp_auth_auth_type(x, parameter)
        self.properties[parameter] = x

    @property
    def authentication(self):
        return self.properties['authentication']
    @authentication.setter
    def authentication(self, x):
        parameter = 'authentication'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ntp_auth_authentication(x, parameter)
        self.properties[parameter] = x

    @property
    def key_id(self):
        return self.properties['key_id']
    @key_id.setter
    def key_id(self, x):
        parameter = 'key_id'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def md5string(self):
        return self.properties['md5string']
    @md5string.setter
    def md5string(self, x):
        parameter = 'md5string'
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
        self.verify_nxos_ntp_auth_state(x, parameter)
        self.properties[parameter] = x

    @property
    def trusted_key(self):
        return self.properties['trusted_key']
    @trusted_key.setter
    def trusted_key(self, x):
        parameter = 'trusted_key'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ntp_auth_trusted_key(x, parameter)
        self.properties[parameter] = x
