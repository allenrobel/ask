***********************************************
StcPortControl() - spirent/stc_port_control.py
***********************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcPortControl() provides commands to attach to, and detach from, Spirent
ports.

StcPortControl() generates Ansible task instances conformant with Spirent's
Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run the playbook generated by StcPortControl(),
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_port_control.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_port_control.py>`_

NOTES
-----

    1. If no ports are specified (see add_port_by_*() methods below), then command
       (attach or detach) will be executed for ALL ports.

Properties
----------

====================================    ==================================================
Property / Method                       Description
====================================    ==================================================
add_port_by_standard_name()             This adds a port, by port name, using 
                                        ScriptKit-assigned names in Chassis/Module/Port
                                        format, e.g. Stc1/1/5.  As such, this method
                                        requires that the chassis, module, and port
                                        properties are called first.::

                                            Example:

                                            chassis = 1
                                            module = 1
                                            for port in [1, 5]:
                                                task.chassis = chassis
                                                task.module = module
                                                task.port = port
                                                task.add_port_by_standard_name()

add_port_by_custom_name()               This adds a port, by port name, using custom
                                        user-assigned names.::

                                            Example:

                                            port_names = ['MyPort1', 'MyPort2']
                                            for name in port_names:
                                                task.add_port_by_custom_name(name)

auto_connect                            Automatically connect to the ports in port_list::

                                            - Type: bool()
                                            - Spirent name: AutoConnect
                                            - Valid values: False, True
                                            - Default: True
                                            - Examples:
                                                - task.auto_connect = False

chassis                                 Chassis number, starting with 1.  For
                                        single-chassis, use 1.::

                                            - Type: int()
                                            - Spirent name: location
                                            - Examples:
                                                - task.chassis = 1
                                            - Required

module                                  Module number::

                                            - Type: int()
                                            - Spirent name: location
                                            - Examples:
                                                - task.module = 2
                                            - Required

port                                    Port number::

                                            - Type: int()
                                            - Spirent name: location
                                            - Examples:
                                                - task.port = 1
                                            - Required

command                                 Attach to, or detach from the ports in port_list::

                                            - Type: str()
                                            - Spirent name: command
                                            - Valid values: attach, detach
                                            - Examples:
                                                - task.command = 'attach'
                                            - Required

revoke_owner                            Forcefully reserve all ports in port_list. If the 
                                        port(s) are reserved by another user, force a 
                                        change in ownership.  This will disrupt whatever
                                        the other user may be doing with the port(s)::

                                            - Type: bool()
                                            - Spirent name: RevokeOwner
                                            - Valid values: False, True
                                            - Default: False
                                            - Examples:
                                                - task.revoke_owner = True

====================================    ==================================================
