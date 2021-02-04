# NxosNtpOptions() - cisco/nxos/nxos_ntp_options.py
our_version = 100
import re
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_ntp_options.py

Description:

NxosNtpOptions() generates Ansible Playbook tasks conformant with nxos_ntp_options
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_ntp_options.py

Properties:

    Valid values for all abool() types are: no, yes

    logging                 abool() Sets whether NTP logging is enabled on the device
    master                  abool() Sets whether the device is an authoritative NTP server
    state                   str()   The state of the configuration after module completion
                                    Valid values: absent, present
    stratum                 str()   If master=yes, an optional stratum can be supplied
                                    Valid values: range 1-15
                                    Default: 8
'''
class NxosNtpOptions(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_ntp_options'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()

        self.properties_set = set()
        self.properties_set.add('logging')
        self.properties_set.add('master')
        self.properties_set.add('state')
        self.properties_set.add('stratum')

        self.nxos_ntp_options_valid_state = set()
        self.nxos_ntp_options_valid_state.add('absent')
        self.nxos_ntp_options_valid_state.add('present')

        self.stratum_min = 1
        self.stratum_max = 15

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
        if self.stratum != None and self.master != 'yes':
            self.task_log.error('exiting. If instance.stratum is set, instance.master must be set to yes')
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
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_ntp_options_state(self, x, parameter='state'):
        verify_set = self.nxos_ntp_options_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ntp_options_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_ntp_options_stratum(self, x):
        source_class = self.class_name
        source_method = 'verify_nxos_ntp_options_stratum'
        self.verify_integer_range(x, self.stratum_min, self.stratum_max, source_class, source_method)

    @property
    def logging(self):
        return self.properties['logging']
    @logging.setter
    def logging(self, x):
        parameter = 'logging'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def master(self):
        return self.properties['master']
    @master.setter
    def master(self, x):
        parameter = 'master'
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
        self.verify_nxos_ntp_options_state(x, parameter)
        self.properties[parameter] = x

    @property
    def stratum(self):
        return self.properties['stratum']
    @stratum.setter
    def stratum(self, x):
        parameter = 'stratum'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ntp_options_stratum(x)
        self.properties[parameter] = x
