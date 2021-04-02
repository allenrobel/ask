# NxosNtpAuth() - cisco/nxos/nxos_ntp_auth.py
our_version = 102
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosNtpAuth()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosNtpAuth() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_ntp_auth
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_ntp_auth <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_ntp_auth_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_ntp_auth.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_ntp_auth.py>`_


|

====================    ==============================================
Property                Description
====================    ==============================================
auth_type               Whether the given md5string is in cleartext
                        or has been encrypted.  If in cleartext, the
                        device will encrypt it before storing it::

                            - Type: str()
                            - Valid values:
                                - encrypt
                                - text
                            - Example:
                                task.auth_type = 'encrypt'

authentication          Turns NTP authentication on or off::

                            - Type: str()
                            - Valid values:
                                - off
                                - on
                            - Example:
                                task.authentication = 'on'

key_id                  Authentication key identifier (numeric)::

                            - Type: int()
                            - Example:
                                task.key_id = 2

md5string               MD5 String::

                            - Type: str()
                            - Example:
                                task.md5string = 'e1rgdr6w'

trusted_key             Whether the given key is required to be
                        supplied by a time source for the device
                        to synchronize to the time source::

                            - Type: bool()
                            - Valid values:
                                - False
                                - True
                            - Example:
                                task.trusted_key = False

state                   The state of the configuration after
                        module completion::

                            - Type: str()
                            - Valid values:
                                - absent
                                - present
                            - Example:
                                task.state = 'present'
                            - Required

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'ntp auth config'
                                        
====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

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

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_ntp_auth_valid_auth_type = set()
        self.nxos_ntp_auth_valid_auth_type.add('text')
        self.nxos_ntp_auth_valid_auth_type.add('encrypt')

        self.nxos_ntp_auth_valid_authentication = set()
        self.nxos_ntp_auth_valid_authentication.add('on')
        self.nxos_ntp_auth_valid_authentication.add('off')

        self.nxos_ntp_auth_valid_state = set()
        self.nxos_ntp_auth_valid_state.add('absent')
        self.nxos_ntp_auth_valid_state.add('present')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name']    = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
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
        self.verify_digits(x, parameter)
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
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x
