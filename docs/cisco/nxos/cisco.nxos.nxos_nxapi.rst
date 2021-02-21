***********************************
NxosNxapi() - cisco.nxos.nxos_nxapi
***********************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosNxapi() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_nxapi
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_nxapi <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_nxapi_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_nxapi.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_nxapi.py>`_


|

============================    ==============================================
Property                        Description
============================    ==============================================
http                            Controls the operating state of the HTTP protocol
                                as one of the underlying transports for NXAPI.
                                When NXAPI is configured, HTTP transport is 
                                enabled by default.::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Default: True

http_port                       Port on which the HTTP server will listen for requests::

                                    - Type: int()
                                    - Valid values: range 1-65535
                                    - Default: 80

https                           Controls the operating state of the HTTPS protocol as one of
                                the underlying transports for NXAPI.
                                By default, NXAPI will disable the HTTPS transport when the
                                feature is first configured::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Default: False

https_port                      Port on which the HTTPS server will listen for requests::

                                    - Type: int()
                                    - Valid values: range 1-65535
                                    - Default: 443

sandbox                         The NXAPI feature provides a web base UI for developers for entering
                                commands.  This feature is initially disabled when the NXAPI feature
                                is configured for the first time::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Default: False
                                    - NOTES:
                                        - sandbox not currently supported on N9K as of NXOS version 9.3(6)

ssl_strong_ciphers              Use strong (True) or weak (False) ciphers::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Default: False

state                           The state argument controls whether or not the NXAPI feature is
                                configured on the remote device. When the value is ``present`` the
                                NXAPI feature configuration is present in the device running-config.
                                When the value is ``absent`` the feature configuration is removed 
                                from the running-config.::

                                    - Type: str()
                                    - Valid values: absent, present
                                    - Default: present

tlsv1_0                         Use Transport Layer Security version 1.0::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Default: True

tlsv1_1                         Use Transport Layer Security version 1.1::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Default: False

tlsv1_2                         Use Transport Layer Security version 1.2::

                                    - Type: bool()
                                    - Valid values: False, True
                                    - Default: False

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)