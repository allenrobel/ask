# Task() - common/task.py
our_version = 103
'''
==========================
Task() = common/task.pu
==========================

Description
-----------

Task() is the base class for Ansible Playbook Task classes

Example usage
-------------

from ask.common.task import Task
class NxosBgpGlobal(Task):
    ...
'''
from ask.common.common import Common

class Task(Common):
    def __init__(self, ansible_module, task_log):
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.task_properties_set = set()
        self.task_properties_set.add('register')
        self.task_properties_set.add('state')
        self.task_properties_set.add('task_name')
        self.init_task_properties()

    def init_task_properties(self):
        self.task_properties = dict()
        for p in self.task_properties_set:
            self.task_properties[p] = None

    def append_to_task_name(self, item):
        '''
        If self.task_name hasn't been set yet::

            - Append the ansible module name to self.task_name
        If item is not a key in self.properties::

            - Append item to self.task_name
            - This allows to append any value, for example, ansible_hostname, directly to self.task_name
        If item is a key in self.properties and item's value is not None::

            - Append item and item's value to self.task_name

        '''
        if self.task_name == None:
            self.task_name = "[{} : v.{}]".format(self.ansible_module, self.lib_version)
        if item not in self.scriptkit_properties:
            self.task_name += ", {}".format(item)
            return
        if item not in self.properties:
            return
        if self.properties[item] != None:
            self.task_name += ", {}: {}".format(item, self.properties[item])

    @property
    def register(self):
        return self.task_properties['register']
    @register.setter
    def register(self, x):
        parameter = 'register'
        if self.set_none(x, parameter):
            return
        self.task_properties[parameter] = x

    @property
    def state(self):
        return self.task_properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_state(x, parameter)
        self.task_properties[parameter] = x

    @property
    def task_name(self):
        return self.task_properties['task_name']
    @task_name.setter
    def task_name(self, x):
        parameter = 'task_name'
        if self.set_none(x, parameter):
            return
        self.task_properties[parameter] = x
