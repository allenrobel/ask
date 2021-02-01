# NxosBanner() - cisco/nxos/nxos_banner.py
our_version = 103
# standard library
from copy import deepcopy
# scriptkit library
from ask.common.task import Task
'''
Name: nxos_banner.py

Description:

NxosBanner() generates Ansible Playbook tasks conformant with nxos_banner
which can be fed to Playbook().add_task()

Properties:

    banner      - Specifies which banner that should be configured on the remote device
                    Valid values: exec, motd
                    Required
    text        - The banner text that should be present in the remote device running configuration.
                    This argument accepts a multiline string, with no empty lines. 
                    Requires state=present
    state       - The state the configuration should be left in
                    Valid values: See self.nxos_banner_valid_state
    task_name   - Name of the task. Ansible will display this when executing the playbook

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_banner.py

'''

class NxosBanner(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_banner'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()

        self.nxos_banner_valid_banner = set()
        self.nxos_banner_valid_banner.add('exec')
        self.nxos_banner_valid_banner.add('motd')

        self.nxos_banner_valid_state = set()
        self.nxos_banner_valid_state.add('present')
        self.nxos_banner_valid_state.add('absent')

        self.properties_set = set()
        self.properties_set.add('banner')
        self.properties_set.add('text')
        self.properties_set.add('state')
        self.properties_set.add('banner')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.banner == None:
            self.task_log.error('exiting. call instance.banner before calling instance.update()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.state == 'absent' and self.text != None:
            self.task_log.error('exiting. instance.text must not be set if instance.state == absent.')
            exit(1)
        if self.state == 'present' and self.text == None:
            self.task_log.error('exiting. instance.text must be set if instance.state == present.')
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate and append dict() to self.ansible_task[self.ansible_module]['config']
        '''
        self.final_verification()

        d = dict()
        d['banner'] = self.banner
        d['state'] = self.state
        if self.text != None:
            d['text'] = self.text
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def nxos_banner_verify_banner(self, x, parameter='afi'):
        verify_set = self.nxos_banner_valid_banner
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_banner_verify_banner'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_banner_verify_state(self, x, parameter='state'):
        verify_set = self.nxos_banner_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_banner_verify_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def banner(self):
        return self.properties['banner']
    @banner.setter
    def banner(self, x):
        parameter = 'banner'
        if self.set_none(x, parameter):
            return
        self.nxos_banner_verify_banner(x, parameter)
        self.properties[parameter] = x

    @property
    def text(self):
        return self.properties['text']
    @text.setter
    def text(self, x):
        parameter = 'text'
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
        self.nxos_banner_verify_state(x, parameter)
        self.properties[parameter] = x
