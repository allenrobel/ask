# NxosBanner() - cisco/nxos/nxos_banner.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosBanner()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
107

ScriptKit Synopsis
------------------
- NxosBanner() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_banner
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_banner <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_banner_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_banner.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_banner.py>`_


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
                                    task = NxosBanner(log)
                                    task.banner = 'motd'
                                    task.text = 'system going down in 1 hour'
                                    task.state = 'present'
                                    task.commit()
                                    pb.add_task(task)

========================    ============================================

|

============================    ==============================================
Property                        Description
============================    ==============================================
banner                          Specifies which banner to configure on the 
                                remote device::

                                    - Type: str()
                                    - Valid values:
                                        - exec
                                        - motd
                                    - Example:
                                        task.banner = 'motd'
                                    - Required

text                            The banner text that should be present in the
                                remote device running configuration. This 
                                argument accepts a multiline string, with no
                                empty lines::

                                    - Type: str()
                                    - Example:
                                        task.text = 'message of the day'
                                    - Requires:
                                        task.state = 'present'
                                    - Notes:
                                        1.  '@' cannot be used within text, since
                                            this is the delimiter character.

state                           Controls whether banner should be configured
                                on the remote device::

                                    - Type: str()
                                    - Valid values:
                                        - absent
                                        - present
                                    - Example:
                                        task.state = 'present'

task_name                       Name of the task. Ansible will display this
                                when the playbook is run::

                                    - Type: str()
                                    - Example:
                                        task.task_name = 'my task'

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosBanner(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_banner'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

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

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.banner == None:
            self.task_log.error('exiting. call instance.banner before calling instance.commit()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if self.state == 'absent' and self.text != None:
            self.task_log.error('exiting. instance.text must not be set if instance.state == absent.')
            exit(1)
        if self.state == 'present' and self.text == None:
            self.task_log.error('exiting. instance.text must be set if instance.state == present.')
            exit(1)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        update self.ansible_task
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
