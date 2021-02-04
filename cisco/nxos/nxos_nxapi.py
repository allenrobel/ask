# NxosNxapi() - cisco/nxos/nxos_nxapi.py
our_version = 101
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_nxapi.py

Description:

NxosNxapi() generates Ansible Playbook tasks conformant with nxos_nxapi
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_nxapi.py

NOTES:

    1. sandbox not currently support on N9K as of NXOS version 9.3(6)

Properties:

    Valid values for all bool() types are: no, yes

    http                bool()  Controls the operating state of the HTTP protocol as one of
                                the underlying transports for NXAPI.
                                By default, NXAPI will enable the HTTP transport when the feature is first configured.
                                Default: yes
    http_port           int()   Configure the port on which the HTTP server will listen for requests
                                Valid values: range 1-65535
                                Default: 80
    https               bool()  Controls the operating state of the HTTPS protocol as one of
                                the underlying transports for NXAPI.
                                By default, NXAPI will disable the HTTP transport when the feature is first configured.
                                Default: no
    https_port          int()   Configure the port on which the HTTPS server will listen for requests
                                Valid values: range 1-65535
                                Default: 443
    sandbox             bool()  The NXAPI feature provides a web base UI for developers for entering commands.
                                This feature is initially disabled when the NXAPI feature is configured for the first time.
                                Default: no
    ssl_strong_ciphers  bool()  Controls the use of whether strong or weak ciphers are configured.
                                Default: no
    state               str()   The state of the configuration after module completion
                                Valid values: absent, present
    tlsv1_0             bool()  Controls whether NXAPI will use Transport Layer Security version 1.0
                                Default: yes
    tlsv1_1             bool()  Controls whether NXAPI will use Transport Layer Security version 1.1
                                Default: no
    tlsv1_2             bool()  Controls whether NXAPI will use Transport Layer Security version 1.2
                                Default: no
'''
class NxosNxapi(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_nxapi'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('http')
        self.properties_set.add('http_port')
        self.properties_set.add('https')
        self.properties_set.add('https_port')
        self.properties_set.add('sandbox')
        self.properties_set.add('ssl_strong_ciphers')
        self.properties_set.add('state')
        self.properties_set.add('tlsv1_0')
        self.properties_set.add('tlsv1_1')
        self.properties_set.add('tlsv1_2')

        self.nxos_nxapi_valid_state = set()
        self.nxos_nxapi_valid_state.add('absent')
        self.nxos_nxapi_valid_state.add('present')

        self.http_port_min = 1
        self.http_port_max = 65535

        self.https_port_min = 1
        self.https_port_max = 65535

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
        populate ansible_task dict()
        '''
        self.final_verification()

        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_nxapi_state(self, x, parameter='state'):
        verify_set = self.nxos_nxapi_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_nxapi_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_nxapi_http_port(self, x):
        source_class = self.class_name
        source_method = 'verify_nxos_nxapi_http_port'
        self.verify_integer_range(x, self.http_port_min, self.http_port_max, self.class_name, source_method)
    def verify_nxos_nxapi_https_port(self, x):
        source_class = self.class_name
        source_method = 'verify_nxos_nxapi_https_port'
        self.verify_integer_range(x, self.https_port_min, self.https_port_max, self.class_name, source_method)

    @property
    def http(self):
        return self.properties['http']
    @http.setter
    def http(self, x):
        parameter = 'http'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def http_port(self):
        return self.properties['http_port']
    @http_port.setter
    def http_port(self, x):
        parameter = 'http_port'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_nxapi_http_port(x)
        self.properties[parameter] = x

    @property
    def https(self):
        return self.properties['https']
    @https.setter
    def https(self, x):
        parameter = 'https'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def https_port(self):
        return self.properties['https_port']
    @https_port.setter
    def https_port(self, x):
        parameter = 'https_port'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_nxapi_https_port(x)
        self.properties[parameter] = x

    @property
    def sandbox(self):
        return self.properties['sandbox']
    @sandbox.setter
    def sandbox(self, x):
        parameter = 'sandbox'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def ssl_strong_ciphers(self):
        return self.properties['ssl_strong_ciphers']
    @ssl_strong_ciphers.setter
    def ssl_strong_ciphers(self, x):
        parameter = 'ssl_strong_ciphers'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_nxapi_state(x, parameter)
        self.properties[parameter] = x

    @property
    def tlsv1_0(self):
        return self.properties['tlsv1_0']
    @tlsv1_0.setter
    def tlsv1_0(self, x):
        parameter = 'tlsv1_0'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def tlsv1_1(self):
        return self.properties['tlsv1_1']
    @tlsv1_1.setter
    def tlsv1_1(self, x):
        parameter = 'tlsv1_1'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def tlsv1_2(self):
        return self.properties['tlsv1_2']
    @tlsv1_2.setter
    def tlsv1_2(self, x):
        parameter = 'tlsv1_2'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

