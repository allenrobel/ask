**************************************
NxosEvpnVni()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosEvpnVni() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_evpn_vni
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_evpn_vni <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_evpn_vni_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_evpn_vni.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_evpn_vni.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
route_distinguisher                 VPN Route Distinguisher (RD).  RD is combined
                                    with the IPv4 or IPv6 prefix learned by the PE
                                    router to create a globally unique address::

                                        - Type: str()
                                        - Valid values:
                                            - auto
                                            - default
                                            - y.y.y.y:x
                                                - where y.y.y.y is dotted-decimal address
                                                - where x is int()
                                            - x:x 
                                                - where x is int()
                                        - Examples:
                                            task.route_distinguisher = 'auto'
                                            task.route_distinguisher = 'default'
                                            task.route_distinguisher = '10.3.1.1:34000'
                                            task.route_distinguisher = '12229:14177'

route_target_both                   Enables/Disables route-target settings for both 
                                    import and export target communities using a single
                                    property::

                                        - Type: str() or list()
                                        - Valid values:
                                            - auto
                                            - default
                                            - list() with str() elements in the following
                                              formats:
                                                - y.y.y.y:x
                                                    - where y.y.y.y is dotted-decimal address
                                                    - where x is int()
                                                - x:x 
                                                    - where x is int()
                                        - Examples:
                                            task.route_target_both = 'auto'
                                            task.route_target_both = 'default'
                                            rt = list()
                                            rt.append('10.1.1.3:12001')
                                            rt.append('12227:12001')
                                            task.route_target_both = rt.copy()

route_target_export                 Sets the route-target 'export' extended communities::

                                        - Type: str() or list()
                                        - Valid values:
                                            - auto
                                            - default
                                            - list() with str() elements in the following
                                              formats:
                                                - y.y.y.y:x
                                                    - where y.y.y.y is dotted-decimal address
                                                    - where x is int()
                                                - x:x 
                                                    - where x is int()
                                        - Examples:
                                            task.route_target_both = 'auto'
                                            task.route_target_both = 'default'
                                            rt = list()
                                            rt.append('10.1.1.3:12001')
                                            rt.append('12227:12001')
                                            task.route_target_both = rt.copy()

route_target_import                 Sets the route-target 'import' extended communities::

                                        - Type: str() or list()
                                        - Valid values:
                                            - auto
                                            - default
                                            - list() with str() elements in the following
                                              formats:
                                                - y.y.y.y:x
                                                    - where y.y.y.y is dotted-decimal address
                                                    - where x is int()
                                                - x:x 
                                                    - where x is int()
                                        - Examples:
                                            task.route_target_both = 'auto'
                                            task.route_target_both = 'default'
                                            rt = list()
                                            rt.append('10.1.1.3:12001')
                                            rt.append('12227:12001')
                                            task.route_target_both = rt.copy()

state                               Determines whether the config should be present
                                    or not on the remote device::

                                        - Type: str()
                                        - Valid values:
                                            - absent
                                            - present
                                        - Default: present

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Examples:
                                            - task.task_name = 'my task'

vni                                 The EVPN VXLAN Network Identifier::

                                        - Type: int()
                                        - Examples:
                                            - task.vni = 32020
                                        
================================    ==============================================

NOTES
-----

1.  ``feature nv overlay`` must be enabled before using this library
2.  RD override is not permitted. You should set it to the default values first and then reconfigure it
3.  ``route_target_both``, ``route_target_import`` and ``route_target_export`` valid values are a list of extended communities
    (e.g. ['1.2.3.4:5', '33:55']) or the keywords ``auto`` or ``default``.
4.  ``route_target_both`` property is discouraged due to the inconsistent behavior of the property across Nexus platforms
    and image versions. For this reason it is recommended to use explicit ``route_target_export`` and
    ``route_target_import`` properties instead of ``route_target_both``
5.  RD valid values are a string in one of the route-distinguisher formats, the keyword ``auto``, or the keyword ``default``

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
