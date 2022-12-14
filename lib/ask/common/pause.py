our_version = 102
from ask.common.task import Task
'''
***********************************
Pause()
***********************************

.. contents::
   :local:
   :depth: 1

Version
-------
102

ScriptKit Synopsis
------------------
- Pause() generates a task to pause playbook execution for X seconds.

ScriptKit Example
-----------------
- `unit_test/common/unit_test_pause.py <https://github.com/allenrobel/ask/blob/main/unit_test/common/unit_test_pause.py>`_

|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task::
                                - Type: function()
                                - Alias: update()
                                - Example:
                                    pb = Playbook(log)
                                    task = Pause(log)
                                    task.seconds = 10
                                    task.task_name = 'Pause 10 seconds'
                                    task.commit()
                                    pb.add_task(task)

========================    ============================================

|

============================    ==============================================
Property                        Description
============================    ==============================================
seconds                         Amount of time, in seconds, to pause playbook
                                execution::

                                    - Type: int()
                                    - Example:
                                        task.seconds = 10

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

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
