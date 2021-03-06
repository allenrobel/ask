**************************************************
StcDrvClear() - spirent/stc_drv_clear.py
**************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcDrvClear() clears Dynamic Result View (DRV) results on a 
set of Spirent ports.

It generates Ansible task instances conformant with Spirent's
Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run the playbook generated by StcDrvClear(),
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_drv_clear.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_drv_clear.py>`_

Properties
----------

====================================    ==================================================
Property                                Description
====================================    ==================================================
port_list                               List of Spirent port references on which to clear
                                        Dynamic Result View results::

                                            - Type: str()
                                            - Spirent name: PortList
                                            - Default: ref:/port
                                            - Examples:
                                                - task.port_list = 'ref:/port'

====================================    ==================================================
