**************************************
NxosSnmpCommunity()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosSnmpCommunity() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_snmp_community
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_snmp_community <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_snmp_community_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_snmp_community.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_snmp_community.py>`_

|

============    ==============================================
Property        Description
============    ==============================================
access          Access type for community.  ro (read-only),
                rw (read-write)::

                    - Type: str()
                    - Valid values:
                        - ro
                        - rw
                    - Example:
                        - task.access = 'ro'

acl             ACL name to filter snmp requests::

                    - Type: str()
                    - Value values:
                        - ip access-list name
                        - keyword: default
                    - Example:
                        - task.acl = 'default'
                        - task.acl = 'SNMP_ACL'

community       Case-sensitive community string::

                    - Type: str()
                    - Value values:
                        - An SNMP community name
                    - Required
                    - Example:
                        - task.community = 'management_geeks'

group           Group to which the community belongs::

                    - Type: str()
                    - Example:
                        - task.group = 'geek_group'

state           Manage the state of the resource::

                    - Type: str()
                    - Value values:
                        - absent
                        - present
                    - Example:
                        - task.state = 'present'

task_name       Name of the task. Ansible will display this
                when the playbook is run::

                    - Type: str()
                    - Example:
                        - task.task_name = 'my task'

============    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

