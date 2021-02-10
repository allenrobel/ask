================================        ==================================================
Property                                Description
================================        ==================================================
description                             Description of the NVE interface::

                                            - Type: str()
                                            - Examples:
                                                - task.description = 'my nve'

global_ingress_replication_bgp          Configures ingress replication protocol as bgp for
                                        all VNIs.::

                                            - Type: str()
                                            - Valid values: no, yes
                                            - Examples:
                                                - task.global_ingress_replication_bgp = 'no'
                                            - Availability:
                                                - Platform: Nexus 9000
                                                - Software: NX-OS 9.2(x) or higher

global_mcast_group_L2                   Global multicast IP prefix for L2 VNIs or the
                                        keyword 'default'.::

                                            - Type: str()
                                            - Valid values: An ipv4 multicast ip address
                                            - Examples:
                                                - task.global_mcast_group_L2 = '225.1.2.3'
                                            - Availability:
                                                - Platform: Nexus 9000
                                                - Software: NX-OS 9.2(x) or higher

global_mcast_group_L2                   Global multicast IP prefix for L3 VNIs or the
                                        keyword 'default'.

                                            - Type: str()
                                            - Valid values: An ipv4 multicast ip address
                                            - Examples:
                                                - task.global_mcast_group_L2 = '225.1.2.3'
                                            - Availability:
                                                - Platform: Nexus 9000
                                                - Software: NX-OS 9.2(x) or higher

global_suppress_arp                     Enables ARP suppression for all VNIs.::

                                            - Type: str()
                                            - Valid values: no, yes
                                            - Examples:
                                                - task.global_suppress_arp = 'no'
                                            - Availability:
                                                - Platform: Nexus 9000
                                                - Software: NX-OS 9.2(x) or higher

host_reachability                       Specify mechanism for host reachability advertisement.::

                                            - 'yes' indicates that BGP will be used for host
                                              reachability advertisement.
                                            - 'no' indicates that no protocol is used for host
                                              reachability advertisement.
                                            - Other host reachability advertisement protocols 
                                              (e.g. OpenFlow, controller, etc.) are not
                                              supported.::

                                            - Type: str()
                                            - Valid values: no, yes
                                            - Examples:
                                                - task.host_reachability = 'yes'

interface                               Interface name for the VXLAN Network
                                        Virtualization Endpoint.::

                                            - Type: str()
                                            - Examples:
                                                - task.interface = 'nve1'
                                            - Required

multisite_border_gateway_interface      The loopback interface whose IP address should be
                                        used for the NVE Multisite Border-gateway Interface.::

                                            - Type: str()
                                            - Valid values:
                                                - A loopback interface name
                                                - The keyword 'default'
                                            - Examples:
                                                - task.multisite_border_gateway_interface = 'Loopback2'
                                                - task.multisite_border_gateway_interface = 'default'
                                            - Availability:
                                                - Platform: Subset of Nexus 9000
                                                - Software: NX-OS 7.0(3)I7(x) or higher

shutdown                                Administratively shutdown the NVE interface.::

                                            - Type: str()
                                            - Valid values: no, yes
                                            - Examples:
                                                - task.shutdown = 'yes'

source_interface                        The loopback interface whose IP address should be
                                        used for the NVE interface::

                                            - Type: str()
                                            - Valid values: A loopback interface name
                                            - Examples:
                                                - task.source_interface = 'loopback2'

source_interface_hold_down_time         Suppresses advertisement of the NVE loopback address
                                        until the overlay has converged.::

                                            - Type: int()
                                            - Valid values: int() range: 1-1500
                                            - Units: seconds
                                            - Examples:
                                                - task.source_interface_hold_down_time = 300

state                                   Determines whether the config should be present or 
                                        not on the device.::

                                            - Type: str()
                                            - Valid values: absent, present
                                            - Examples:
                                                - task.state = 'present'
                                            - Required

task_name                               Freeform name for the task (ansible-playbook will
                                        print this when the task is run)::

                                            - Type: str()
                                            - Examples:
                                                - task.task_name = 'configure vni'

================================    ==================================================
