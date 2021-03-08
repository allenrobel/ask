**************************************
NxosStaticRoutes()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosStaticRoutes() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_static_routes
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_static_routes <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_static_routes_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_static_routes.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_static_routes.py>`_

|

========================    ==============================================
Properties / Methods        Description
========================    ==============================================
add_next_hop()              Add a next hop to the curent ``dest``.  This
                            can be called multiple times for the same
                            ``dest``::

                                - Type: method
                                - Example:
                                    task = NxosStaticRoutes(log_instance)
                                    # set general route attributes
                                    task.dest = '1.1.0.0/16'
                                    task.afi = 'ipv4'
                                    task.admin_distance = 100
                                    # add a next hop for this route
                                    task.forward_router_address = '2.1.1.1'
                                    task.interface = 'Ethernet1/1'
                                    task.add_next_hop()
                                    # add a second next hop for this route
                                    task.forward_router_address = '2.2.1.1'
                                    task.interface = 'Ethernet1/2'
                                    task.add_next_hop()
                                    # update the task to store this route
                                    task.update()
                                    # add the task to the playbook
                                    # See ScriptKit Example above for how
                                    # to instantiate the Playbook() class
                                    pb.add_task(task)
                                    # Append this play with its single task
                                    pb.append_playbook()
                                    # write the playbook
                                    pb.write_playbook()

afi                         Specifies the top level address family 
                            indicator::

                                - Type: str()
                                - Valid values: ipv4, ipv6
                                - Example
                                    task.afi = 'ipv4'
                                - Required

dest                        Destination prefix of static route::

                                - Type: str()
                                - Valid values:
                                    - IPv4 address with prefixlen
                                        - prefixlen range: 0-32
                                    - IPv6 address with prefixlen
                                        - prefixlen range: 0-128
                                Examples:
                                    task.dest = '10.1.0.0/16'
                                    task.dest = '2001:aaaa:bbbb::/48'
                                - Required

admin_distance              Preference or administrative distance of
                            route::

                                - Type: int()
                                - Valid values: range 1-255
                                - Example:
                                    task.admin_distance = 100

dest_vrf                    VRF of the destination::

                                - Type: str()
                                - Example:
                                    task.dest_vrf = "ENG"

forward_router_address      IP address of the next hop router::

                                - Type: str()
                                - Valid values:
                                    - ip address in same address-family as dest/afi
                                - Examples:
                                    task.forward_router_address = '10.2.1.1'
                                    task.forward_router_address = '2001:aaaa::3'

interface                   Outgoing interface of next-hop::

                                - Type: str()
                                - Valid values:
                                    - Full interface name
                                    - Null0
                                - Examples:
                                    task.interface = 'Null0'
                                    task.interface = 'Ethernet1/1'

route_name                  Name of the static route::

                                - Type: str()
                                - Example:
                                    task.route_name = 'POD_2'

tag                         Route tag value::

                                - Type: int()
                                - Example:
                                    task.tag = 5000

track                       Track value::

                                - Type: int()
                                - Valid values: range 1-512
                                - Example:
                                    task.track = 100
                                - NOTES:
                                    - Track must already be configured on
                                      the device before adding the route.

vrf                         The VRF to which the static route(s) belong::

                                - Type: str()
                                - Example:
                                    task.vrf = 'ENG'

state                       Desired state after task has completed::

                                - Type: str()
                                - Valid values:
                                    - deleted
                                    - gathered
                                    - merged
                                    - overridden
                                    - parsed  (not currently supported by ScriptKit)
                                    - rendered
                                    - replaced

task_name                   Name of the task. Ansible will display this
                            when the playbook is run::

                                - Type: str()
                                - Example:
                                    - task.task_name = 'my task'

========================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
