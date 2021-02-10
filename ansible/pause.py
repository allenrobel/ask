# Pause() - python/lib3/ask_task_pause.py
our_version = 103
from copy import deepcopy
from ask.common.task import Task
'''
==================
Pause() - pause.py
==================

Description
-----------
Pause() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Example usage
-------------

unit_test/ansible/pause.py

Properties
----------

========================    ===========
Property                    Description
========================    ===========
seconds                     Number of seconds to pause::

                                - Type: int()
                                - Valid values: int()
                                - Required
'''

class Pause(Task):
    def __init__(self, task_log):
        ansible_module = 'pause'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self._classname = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('seconds')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.seconds == None:
            self.task_log.error('exiting. call instance.seconds before calling instance.update()')
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

    def verify_ansible_pause_seconds(self, x, parameter='seconds'):
        if self.is_digits(x):
            return
        source_class = self._classname
        source_method = 'verify_ansible_pause_seconds'
        expectation = 'int()'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def seconds(self):
        return self.properties['seconds']
    @seconds.setter
    def seconds(self, x):
        parameter = 'seconds'
        if self.set_none(x, parameter):
            return
        self.verify_ansible_pause_seconds(x, parameter)
        self.properties[parameter] = x
