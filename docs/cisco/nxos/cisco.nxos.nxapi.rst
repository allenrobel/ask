.. _cisco.nxos.nxos_nxapi_module:


*********************
cisco.nxos.nxos_nxapi
*********************

**Manage NXAPI configuration on an NXOS device.**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- NxosNxapi() generates Ansible Playbook tasks conformant with nxos_nxapi which can be fed to Playbook().add_task()


Usage example
-------------
    unit_test/cisco/nxos/unit_test_nxos_nxapi.py

Parameters
----------
.. raw:: html
    
    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Valid Values</th>
            <th width="100%">Description</th>
        </tr>
        <tr>
            <td>http</td>
            <td>
                <ul>
                    <li>no</li>
                    <li>yes<li>
                </ul>
            </td>
            <td>
                <div>
                Controls the operating state of the HTTP protocol as one of the underlying transports for NXAPI. By default, NXAPI will enable the HTTP transport when the feature is first configured. To disable the use of the HTTP transport, set the value of this argument to False.
                </div>
            </td>
        </tr>
    </table>


Authors
~~~~~~~

- Allen Robel (@PacketCalc)
