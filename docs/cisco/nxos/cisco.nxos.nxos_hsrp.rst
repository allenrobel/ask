**************************************
NxosHsrp()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosHsrp() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_hsrp
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_hsrp <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_hsrp_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_hsrp.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_hsrp.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
auth_string                         Authentication string. If this needs to be 
                                    hidden(for md5 type), the string should be 7
                                    followed by the key string. Otherwise, it can
                                    be 0 followed by key string or just key string
                                    (for backward compatibility). For text type,
                                    this should be just be a key string. if this
                                    is 'default', authentication is removed.::

                                        - Type: str()
                                        - Valid values:
                                            - An authentication string
                                            - keyword: default
                                        - Examples:
                                            task.auth_string = '7 asdeir123'
                                            task.auth_string = '0 foobar'
                                            task.auth_string = 'foobar'
                                            task.auth_string = 'default'

auth_type                           Authentication type::

                                        - Type: str()
                                        - Valid values:
                                            - md5
                                            - text
                                        - Examples:
                                            task.auth_type = 'md5'
                                            task.auth_type = 'text'

group                               HSRP group number::

                                        - Type: int()
                                        - Valid values:
                                            - range 0-255 (version 1)
                                            - range 0-4095 (version 2)
                                        - Example:
                                            task.group = 10
                                        - Required

interface                           Full name of interface that is being managed for HSRP::

                                        - Type: str()
                                        - Examples:
                                            task.interface = 'Vlan10'
                                            task.interface = 'Ethernet1/1'
                                        - Required

preempt                             Enable/Disable HSRP preempt::

                                        - Type: str()
                                        - Valid values:
                                            - disabled
                                            - enabled
                                        - Example:
                                            task.preempt = 'disabled'

priority                            HSRP priority or keyword ``default``::

                                        - Type: int() or str()
                                        - Valid values:
                                            - range 0-255
                                            - keyword: default
                                        - Example:
                                            task.priority = 150
                                            task.priority = 'default'

state                               Desired state of ``hsrp`` attributes::

                                        - Type: str()
                                        - Valid values:
                                            - absent
                                            - present
                                        - Example:
                                            task.state = 'present'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'configure HSRP'

version                             HSRP version::

                                        - Type: int()
                                        - Valid values:
                                            - 1
                                            - 2
                                        - Default: 1
                                        - Example:
                                            task.version = 2

vip                                 HSRP virtual IP address or keyword ``default``::

                                        - Type: str()
                                        - Valid values:
                                            - An ip address with prefixlen
                                            - keyword: default
                                        - Examples:
                                            task.vip = '10.1.1.3/24'
                                            task.vip = 'default'

================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
