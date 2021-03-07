**************************************
NxosFeature()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosFeature() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_feature
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_feature <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_feature_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_feature.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_feature.py>`_

Dependencies
------------

The following must be enabled prior to applying nxos_pim_interface playbook::

    feature pim

|

====================    ==============================================
Property                Description
====================    ==============================================
bfd                     Enables BFD for PIM at the interface level.
                        This overrides the bfd variable set at the
                        pim global level::

                            - Type: str()
                            - Valid values:
                                - enable
                                - disable
                                - default
                            - Dependencies: feature bfd
                            - Example:
                                task.bfd = 'enable'

border                  Configures interface to be a boundary of a
                        PIM domain::

                            - Type: bool()
                            - Valid values:
                                - False
                                - True
                            - Example:
                                task.border = True

dr_prio                 Configures priority for PIM DR election on
                        the interface::

                            - Type: int()
                            - Valid values:
                                - range: 1-4294967295
                            - Example:
                                task.dr_prio = 3000

hello_auth_key          Authentication for PIM hellos on this interface::

                            - Type: str()
                            - Example:
                                task.hello_auth_key = 'zippofinetic'

hello_interval          Hello interval in milliseconds or seconds for this
                        interface. Use the option ``hello_interval_ms`` to
                        specify if the given value is in milliseconds or
                        seconds. The default is seconds.::

                            - Type: int()
                            - Valid values:
                                - range: 1-18724286
                            - Example (set pim hello interval to 100ms):
                                task.hello_interval_ms = True
                                task.hello_interval = 100
                            - Example (set pim hello interval to 1 second):
                                task.hello_interval_ms = False
                                task.hello_interval = 1

hello_interval_ms       Specifies that the hello_interval is in milliseconds.
                        If set to True, the value of ``hello_interval`` will
                        be interpreted as milliseconds.  If set to False,
                        the value of ``hello_interval`` will be interpreted
                        as seconds.::

                            - Type: bool()
                            - Valid values:
                                - False
                                - True
                            - Version added: 2.0.0
                            - Example:
                                task.hello_interval_ms = True

interface               Full name of the PIM interface::

                            - Type: str()
                            - Example:
                                task.interface = 'Ethernet1/33'
                            - Required

jp_policy_in            Inbound policy for join-prune messages::

                            - Type: str()
                            - Example:
                                task.jp_policy_in = 'PIM_JP_IN'

jp_policy_out           Outbound policy for join-prune messages::

                            - Type: str()
                            - Example:
                                task.jp_policy_out = 'PIM_JP_OUT'

jp_type_in              Type of policy mapped to jp_policy_in::

                            - Type: str()
                            - Valid values:
                                - prefix
                                - routemap
                            - Example:
                                task.jp_type_in = 'routemap'

jp_type_out             Type of policy mapped to jp_policy_out::

                            - Type: str()
                            - Valid values:
                                - prefix
                                - routemap
                            - Example:
                                task.jp_type_out = 'routemap'

neighbor_policy         Configures a neighbor policy for filtering
                        adjacencies::

                            - Type: str()
                            - Example:
                                task.neighbor_policy = 'PIM_POLICY'

neighbor_type           Type of policy mapped to neighbor_policy::

                            - Type: str()
                            - Valid values:
                                - prefix
                                - routemap
                            - Example:
                                task.neighbor_type = 'prefix'

sparse                  Enable/disable sparse-mode on the interface::

                            - Type: bool()
                            - Valid values:
                                - False
                                - True
                            - Example:
                                task.sparse = True

state                   Desired state after task has completed::

                            - Type: str()
                            - Valid values:
                                - absent
                                - default
                                - present
                            - Example:
                                task.state = 'present'
                            - Required

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'my task'
                                        
====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
