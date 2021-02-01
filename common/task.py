# Task() - common/task.py
our_version = 101
'''
Description: Task() is the base class for Ansible Playbook Task classes

Synopsis:

from ask.common.task import Task
class NxosBgpGlobal(Task):
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
