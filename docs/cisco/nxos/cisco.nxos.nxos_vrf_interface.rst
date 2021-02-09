*******************************************
NxosVrfInterface() - nxos_vrf_interface.py
*******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVrfInterface() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vrf_interface <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vrf_interface_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vrf_interface.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vrf_interface.py>`_

Properties
----------

======================================  ==================================================
Property                                Description
======================================  ==================================================
interface                               Full name of interface to be managed::

                                            - Type: str()
                                            - Examples:
                                                - task.interface = 'Ethernet1/1' 
                                                - task.interface = 'Vlan10'
                                                - task.interface = 'port-channel200'

state                                   Manages desired state of the resource::

                                            - Type: str()
                                            - Valid values: absent, present
                                            - Examples:
                                                - task.state = 'present'

vrf                                     Name of VRF to be managed::

                                            - Type: str()
                                            - Examples:
                                                - task.vrf = 'my_vrf'

======================================  ==================================================
