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

