**************************************
NxosSnmpLocation()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosSnmpLocation() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_snmp_location
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_snmp_location <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_snmp_location_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_snmp_location.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_snmp_location.py>`_

|

============    ==============================================
Property        Description
============    ==============================================
location        Location information::

                    - Type: str()
                    - Example:
                        task.location = 'Row: 7, Rack: 10'
                    - Required

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
