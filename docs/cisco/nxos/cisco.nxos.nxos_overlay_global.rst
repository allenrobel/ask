**************************************
NxosOverlayGlobal()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosOverlayGlobal() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_overlay_global
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_overlay_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_overlay_global_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_overlay_global.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_overlay_global.py>`_

Dependencies
------------
The following must be enabled prior to applying nxos_overlay_global playbook::

    nv overlay evpn

|

======================================  ==================================================
Property                                Description
======================================  ==================================================
anycast_gateway_mac                     Anycast gateway mac of the switch::

                                             - Type: str()
                                             - Valid values:
                                                - default
                                                - EEEE.EEEE.EEEE
                                                - EE:EE:EE:EE:EE:EE
                                                - EE-EE-EE-EE-EE-EE
                                            - Examples:
                                                task.anycast_gateway_mac = 'default'
                                                task.anycast_gateway_mac = '00a0.2100.01ab'
                                                task.anycast_gateway_mac = '00:a0:21:00:01:ab'
                                                task.anycast_gateway_mac = '00-a0-21-00-01-ab'
                                            - Required

======================================  ==================================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
