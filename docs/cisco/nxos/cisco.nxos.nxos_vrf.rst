*******************************************
NxosVrf() - nxos_vrf.py
*******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVrf() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vrf <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vrf_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vrf.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vrf.py>`_

Properties
----------

======================================  ==================================================
Property                                Description
======================================  ==================================================
admin_state                             Administrative state of the VRF::

                                            - Type: str()
                                            - Valid values: down, up
                                            - Examples:
                                                - task.admin_state = 'up'

aggregate                               list() of VRF definitions::

                                            This property is not accessed directly.
                                            Use ScriptKit's add_vrf() method to populate the aggregate list().
                                            If add_vrf() is not called prior to update(), then the task will contain
                                            a single vrf and aggregate is not used.  See ScriptKit Example above for 
                                            example usage in a script.

associated_interfaces                   This is an intent option and checks the operational state
                                        of the interfaces for the given vrf name.  If the value
                                        in the associated_interfaces list() does not match the operational
                                        state of vrf interfaces on device the module will report a
                                        failure::

                                            - Type: list()
                                            - Valid values: list() of interface names, or the keyword 'default'
                                            - Examples:
                                                - task.associated_interfaces = ['Ethernet1/1', 'port-channel44']
                                                - task.associated_interfaces = 'default'

delay                                   Time in seconds to wait before checking for the operational state
                                        on the remote device::

                                            - Type: int()
                                            - Default: 10
                                            - Examples:
                                                - task.delay = 20

description                             Description of the VRF::

                                            - Type: str()
                                            - Valid values: Freeform vrf description, or keyword 'default'
                                            - Examples:
                                                - task.description = 'no offsite access'
                                                - task.description = 'default'

interfaces                              List of interfaces on which to configure VRF membership::

                                            - Type: list()
                                            - Valid values: list() of interface names, or the keyword 'default'
                                            - Examples:
                                                - task.interfaces = ['Ethernet1/1', 'port-channel44']
                                                - task.interfaces = 'default'

name                                    Name of the VRF to be managed::

                                            - Type: str()
                                            - Examples:
                                                - task.name = 'my_vrf'

purge                                   Purge VRFs not defined in the aggregate parameter::

                                            - Type: str()
                                            - Valid values: no, yes
                                            - NOTE: purge is recognized only when NxosVrf().add_vrf() is used.
                                                    For example, the following purges all vrfs configured on 
                                                    the remote device, except for vrf_1 and vrf_2::

                                                        task.name = 'vrf_1'
                                                        task.state = 'present'
                                                        task.add_vrf()
                                                        task.name = 'vrf_2'
                                                        task.state = 'present'
                                                        task.add_vrf()
                                                        task.purge = 'yes'
                                                        task.update()

rd                                      VPN Route Distinguisher (RD)::

                                            - Type: str()
                                            - Valid values: str() in one of the following formats, or keywords: 'auto' or 'default':
                                                - ASN2:NN
                                                - ASN4:NN
                                                - IPV4:NN
                                            - Examples:
                                                - task.rd = 'auto'
                                                - task.rd = 'default'
                                                - task.rd = '65230:200'
                                                - task.rd = '29123312:65000'
                                                - task.rd = '10.1.1.1:65200'

state                                   Manages desired state of the resource::

                                            - Type: str()
                                            - Valid values: absent, present
                                            - Examples:
                                                - task.state = 'present'

task_name                               Freeform name for the task (ansible-playbook will
                                        print this when the task is run)::

                                            - Type: str()
                                            - Examples:
                                                - task.task_name = 'configure vrf {}'.format(task.name)

vni                                     Virtual network identifier::

                                            - Type: int()
                                            - Valid values: int(), or the keyword 'default'
                                            - Examples:
                                                - task.vni = 10200
                                                - task.vni = 'default'

======================================  ==================================================

