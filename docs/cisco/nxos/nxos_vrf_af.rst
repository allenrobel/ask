*******************************************
NxosVrfAf()
*******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVrfAf() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vrf_af <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vrf_af_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vrf_af.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vrf_af.py>`_

Properties
----------

======================================  ==================================================
Properties / Methods                    Description
======================================  ==================================================
add_rt()                                Append the currently-configured route-target to 
                                        the RT list, and clear all RT-related properties
                                        so that another RT can be configured.  See
                                        ``ScriptKit Example`` above for usage within
                                        a script::

                                            - Type: method
                                            - Example:
                                                task = NxosVrfAf(log_instance)
                                                task.rt = '300:2000'
                                                task.rt_direction = 'export'
                                                task.rt_state = 'present'
                                                task.add_rt()
                                                task.rt = '300:2001'
                                                task.rt_direction = 'import'
                                                task.rt_state = 'present'
                                                task.add_rt()
                                                etc...

afi                                     Address Family::

                                            - Type: str()
                                            - Valid values:
                                                - ipv4
                                                - ipv6
                                            - Example:
                                                task.afi = 'ipv4'

route_target_both_auto_evpn             Enable/Disable the EVPN route-target 'auto' setting for both import and export target communities::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.route_target_both_auto_evpn = False

rt                                      route-target::

                                            - Type: str()
                                            - Example:
                                                task.rt = '300:2000'

rt_direction                            Indicates the direction of the route-target::

                                            - Type: str()
                                            - Valid values:
                                                - both
                                                - export
                                                - import
                                            - Default: both
                                            - Example:
                                                task.rt_direction = 'import'

rt_state                                The state of this route-target::

                                            - Type: str()
                                            - Valid values:
                                                - absent
                                                - present
                                            - Default: present
                                            - Examples:
                                                task.rt_state = 'present'

state                                   Manages desired state of the resource::

                                            - Type: str()
                                            - Valid values:
                                                - absent
                                                - present
                                            - Examples:
                                                task.state = 'present'

task_name                               Freeform name for the task (ansible-playbook
                                        will print this when the task is run)::

                                            - Type: str()
                                            - Examples:
                                                task.task_name = 'configure route targets'

vrf                                     Name of the VRF to be managed::

                                            - Type: str()
                                            - Examples:
                                                - task.vrf = 'my_vrf'

======================================  ==================================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

