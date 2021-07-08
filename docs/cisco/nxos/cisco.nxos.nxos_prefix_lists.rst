******************************************
NxosPrefixLists()
******************************************

.. contents::
   :local:
   :depth: 1

Version
-------
100

Status
------

- BETA

- This library is in development and not yet complete, nor fully-tested.
- See TODO below for missing functionality.

TODO
----

- 20210707: Add verification for mask
- 20210707: Add verifications for values of eq, ge, le relative to prefix/LEN

ScriptKit Synopsis
------------------
NxosPrefixLists() generates Ansible task instances conformant with cisco.nxos.nxos_prefix_lists.
These task instances can then be passed to Playbook().add_task()

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_prefix_lists.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_prefix_lists.py>`_

Caveats
-------

Ansible Module Documentation
----------------------------
- `nxos_prefix_lists <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_prefix_lists_module.rst>`_

|

========================    ==============================================
Method                      Description
========================    ==============================================
add_afi()                   Add an address-family identifier to the config
                            list()::

                                - Type: function()
                                - Example:
                                    See ScriptKit Example link above

add_prefix_list_entry()     Add an entry to the current prefix_list::

                                - Type: function()
                                - Example:
                                    See ScriptKit Example link above

add_prefix_list()           Add a prefix_list using the current afi::

                                - Type: function()
                                - Example:
                                    See ScriptKit Example link above

commit()                    Perform final verification and commit the 
                            current task::

                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See ScriptKit Example link above

========================    ==============================================

|

============================    ==============================================
Property                        Description
============================    ==============================================
action                          Prefix-List permit or deny.::

                                    - Type: str()
                                    - Valid values:
                                        - deny
                                        - permit
                                    - Examples:
                                        task.action = 'permit'

afi                             The Address Family Identifier (AFI) 
                                for the prefix-lists.::

                                    - Type: str()
                                    - Valid values:
                                        - ipv4
                                        - ipv6
                                    - Examples:
                                        task.afi = 'ipv4'

description                     Description of the prefix-list::

                                    - Type: str()
                                    - Examples:
                                        task.description = 'filter outside networks'

eq                              Exact prefix length to be matched.::

                                    - Type: int()
                                    - Valid values:
                                        - ipv4 afi: range 0-32
                                        - ipv6 afi: range 0-128
                                    - Example:
                                        task.eq = 32
                                    - NOTES:
                                        1. mutually-exclusive with ge, le

ge                              Minimum prefix length to be matched.::

                                    - Type: int()
                                    - Valid values:
                                        - ipv4 afi: range 0-32
                                        - ipv6 afi: range 0-128
                                    - Example:
                                        task.ge = 32
                                    - NOTES:
                                        1. mutually-exclusive with eq, le

le                              Maximum prefix length to be matched.::

                                    - Type: int()
                                    - Valid values:
                                        - ipv4 afi: range 0-32
                                        - ipv6 afi: range 0-128
                                    - Example:
                                        task.le = 32
                                    - NOTES:
                                        1. mutually-exclusive with eq, ge

mask                            Explicit match mask.::

                                    - Type: str()
                                    - Example:
                                        task.mask = '255.255.0.0'

name                            Name of the prefix-list::

                                    - Type: str()
                                    - Examples:
                                        task.name = 'PL_OUTSIDE'

prefix                          IP or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format.::

                                    - Type: str()
                                    - Example:
                                        task.prefix = '10.0.1.0/24'
                                        task.prefix = '2001::0/16'

sequence                        Sequence Number of the current entry.::

                                    - Type: int()
                                    - Valid values:
                                        - range 1-4294967294
                                    - Example:
                                        task.sequence = 40

============================    ==============================================

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
