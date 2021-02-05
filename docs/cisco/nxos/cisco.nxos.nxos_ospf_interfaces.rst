
*************************************************
NxosOspfInterfaces() - cisco.nxos.nxos_interfaces
*************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosOspfInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_ospf_interfaces
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_ospf_interfaces <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_ospf_interfaces_module.rst>`_

Properties
----------
Properties which differ from the Ansible Module Documentation are noted in the table below:


================    ==============================
Ansible Module      ScriptKit
================    ==============================
enable              authentication_enable
key_chain           authentication_key_chain
message_digest      authentication_message_digest
null_auth           authentication_null_auth
key_encryption      authentication_key_encryption
key                 authentication_key
key_encryption      message_digest_key_encryption
key                 message_digest_key
key_id              message_digest_key_id
area_id             process_area_id
area_secondaries    process_area_secondaries
multi_areas         process_multi_areas
multi_areas         multi_areas
================    ==============================


- multi_areas
    - Appears under both address_family and processes
    - Use task.process_multi_areas when adding to a process
    - Use task.multi_areas when adding to an address_family 


ScriptKit Example
-----------------
    unit_test/cisco/nxos/unit_test_nxos_ospf_interfaces.py

Authors
~~~~~~~

- Allen Robel (@PacketCalc)
