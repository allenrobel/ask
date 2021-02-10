*******************************************
NxosVxlanVtepVni() - nxos_vxlan_vtep_vni.py
*******************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
NxosVxlanVtepVni() generates Ansible task instances conformant with cisco.nxos.nxos_vxlan_vtep_vni.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vrf <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vxlan_vtep_vni_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vxlan_vtep_vni.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vxlan_vtep_vni.py>`_

Properties
----------

================================    ==================================================
Property                            Description
================================    ==================================================
assoc_vrf                           Used to identify and separate processing VNIs that 
                                    are associated with a VRF and used for routing.
                                    The VRF and VNI specified with this command must
                                    match the configuration of the VNI under the VRF.::

                                        - Type: str()
                                        - Valid values: no, yes
                                        - Examples:
                                            - task.assoc_vrf = 'no'

ingress_replication                 Specifies mechanism for host reachability
                                    advertisement.::

                                        - Type: str()
                                        - Valid values: bgp, static, default
                                        - Examples:
                                            - task.ingress_replication = 'bgp'

interface                           Interface name for the VXLAN Network
                                    Virtualization Endpoint.::

                                        - Type: str()
                                        - Examples:
                                            - task.interface = 'nve1'
                                        - Required

multicast_group                     The multicast group (range) of the VNI.::

                                        - Type: str()
                                        - Valid values: A multicast group address,
                                          or the keyword 'default'
                                        - Examples:
                                            - task.multicast_group = '225.1.2.3'
                                            - task.multicast_group = 'default'

multisite_ingress_replication       Enables multisite ingress replication.::

                                        - Type: str()
                                        - Valid values: disable, enable, optimized
                                        - Examples:
                                            - task.multisite_ingress_replication = 'disable'
                                            - task.multisite_ingress_replication = 'optimized'

peer_list                           Set the ingress-replication static peer list.::

                                        - Type: list()
                                        - Valid values: A python list() of ipv4 addresses
                                        - Examples:
                                            - task.peer_list = ['1.1.2.1', '10.2.3.4']

state                               Determines whether the config should be present or 
                                    not on the device.::

                                        - Type: str()
                                        - Valid values: absent, present
                                        - Examples:
                                            - task.state = 'present'
                                        - Required

suppress_arp                        Suppress arp under layer 2 VNI.::

                                        - Type: str()
                                        - Valid values: no, yes
                                        - Examples:
                                            - task.suppress_arp = 'yes'

suppress_arp_disable                Overrides the global ARP suppression config. 
                                    Available on NX-OS 9K series running 9.2.x 
                                    or higher.::

                                        - Type: str()
                                        - Valid values: no, yes
                                        - Examples:
                                            - task.suppress_arp_disable = 'no'

task_name                           Freeform name for the task (ansible-playbook will
                                    print this when the task is run)::

                                        - Type: str()
                                        - Examples:
                                            - task.task_name = 'configure vni'

vni                                 Virtual Network Identifier.::

                                        - Type: int()
                                        - Valid values: int() range: 1-16777214
                                        - Examples:
                                            - task.vni = 10111
                                        - Required

================================    ==================================================
