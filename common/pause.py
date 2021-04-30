our_version = 100
from ask.common.task import Task
'''
Name: pause.py
Author: Allen Robel
Email: arobel@cisco.com
Description:

Pause() generates Ansible Playbook tasks conformant with pause
which can be fed to Playbook().add_task()

Revision history: Use git log

Example usage:

    from ask.common.playbook import Playbook
    from ask.common.pause import Pause
    from ask.common.log import Log

    ansible_module = 'pause'
    log_level_console = 'INFO'
    log_level_file = 'DEBUG'
    log = Log('{}'.format(script_name), log_level_console, log_level_file)

    def playbook():
        pb = Playbook(log)
        pb.profile_local()
        pb.file = '/tmp/pause.yaml'
        pb.name = 'pause playbook'
        pb.add_host('labserver-2001') # from Ansible inventory
        return pb

    def pause_10(task):
        task.seconds = 10
        task.task_name = 'pause_10_seconds'
        task.update()
    def pause_20(task):
        task.seconds = 20
        task.task_name = 'pause_20_seconds'
        task.update()

    pb = playbook()
    task = Pause(log)
    pause_10(task)
    pause_20(task)

    pb.append_playbook()
    pb.write_playbook()
    log.info('wrote {}'.format(pb.file))

'''

class Pause(Task):
    def __init__(self, task_log):
        ansible_module = 'pause'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self._classname = __class__.__name__
        self.ansible_task = dict()

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        self.properties['seconds'] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.seconds == None:
            self.log.error('exiting. call instance.seconds before calling instance.commit()')
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
        if self.seconds != None:
            d['seconds'] = self.seconds
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = d.copy()

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

    @property
    def task_name(self):
        return self.properties['task_name']
    @task_name.setter
    def task_name(self, x):
        parameter = 'task_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
