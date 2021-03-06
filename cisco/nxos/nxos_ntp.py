# NxosNtp() - cisco/nxos/nxos_ntp.py
our_version = 110
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosNtp()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosNtp() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_ntp
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_ntp <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_ntp_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_ntp.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_ntp.py>`_


|

====================    ==============================================
Property                Description
====================    ==============================================
key_id                  Authentication key identifier to use with
                        given NTP server or peer, or keyword
                        ``default``::

                            - Type: int() or str()
                            - Valid values:
                                - int()
                                - keyword: default
                            - Examples:
                                task.key_id = 32
                                task.key_id = 'default'
                            - Required

peer                    Network address of NTP peer::

                            - Type: str()
                            - Valid values:
                                - ipv4 address
                                - ipv6 address
                            - Examples:
                                task.peer = '10.1.1.1'
                                task.peer = '2000:aaaa::2'

prefer                  Makes given NTP server or peer the
                        preferred NTP server or peer for the
                        device::

                            - Type: str()
                            - Valid values:
                                - disabled
                                - enabled
                            - Examples:
                                task.prefer = 'enabled'

server                  Network address of NTP server::

                            - Type: str()
                            - Valid values:
                                - ipv4 address
                                - ipv6 address
                            - Examples:
                                task.server = '10.1.1.1'
                                task.server = '2000:aaaa::2'

source_addr             Local source address from which NTP
                        messages are sent::

                            - Type: str()
                            - Valid values:
                                - ipv4 address
                                - ipv6 address
                            - Examples:
                                task.source_addr = '10.1.1.2'
                                task.source_addr = '2000:aaaa::3'

source_int              Local source interface from which NTP
                        messages are sent::

                            - Type: str()
                            - Valid values:
                                - interface name
                                - keyword: default
                            - Examples:
                                task.source_int = 'mgmt0'
                                task.source_int = 'Ethernet1/1'
                                task.source_int = 'default'

state                   The state of the configuration after
                        module completion::

                            - Type: str()
                            - Valid values:
                                - absent
                                - present
                            - Example:
                                task.state = 'present'
                            - Required

stratum                 If ``master`` is True, an optional stratum
                        can be supplied::

                            - Type: int()
                            - Valid values: range 1-15
                            - Default: 8
                            - Example:
                                task.stratum = 10

task_name               Name of the task. Ansible will display this
                        when the playbook is run::

                            - Type: str()
                            - Example:
                                - task.task_name = 'ntp config'

vrf_name                Makes the device communicate with the given
                        NTP server or peer over a specific VRF::

                            - Type: str()
                            - Valid values:
                                - VRF name
                                - keyword: default
                            - Examples:
                                task.vrf_name = 'management'
                                task.vrf_name = 'default'

====================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosNtp(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_ntp'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.nxos_ntp_valid_state = set()
        self.nxos_ntp_valid_state.add('absent')
        self.nxos_ntp_valid_state.add('present')

        self.properties_set = set()
        self.properties_set.add('key_id')
        self.properties_set.add('peer')
        self.properties_set.add('prefer')
        self.properties_set.add('server')
        self.properties_set.add('source_addr')
        self.properties_set.add('source_int')
        self.properties_set.add('state')
        self.properties_set.add('vrf_name')
        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.vrf_name == None:
            self.vrf_name = 'management'

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        d = dict()  
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_ntp_state(self, x, parameter='state'):
        verify_set = self.nxos_ntp_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_ntp_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def key_id(self):
        return self.properties['key_id']
    @key_id.setter
    def key_id(self, x):
        parameter = 'key_id'
        if self.set_none(x, parameter):
            return
        self.verify_digits_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def peer(self):
        return self.properties['peer']
    @peer.setter
    def peer(self, x):
        parameter = 'peer'
        if self.set_none(x, parameter):
            return
        self.verify_ipv4_ipv6_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def prefer(self):
        return self.properties['prefer']
    @prefer.setter
    def prefer(self, x):
        parameter = 'prefer'
        if self.set_none(x, parameter):
            return
        self.verify_enabled_disabled(x, parameter)
        self.properties[parameter] = x

    @property
    def server(self):
        return self.properties['server']
    @server.setter
    def server(self, x):
        parameter = 'server'
        if self.set_none(x, parameter):
            return
        self.verify_ipv4_ipv6_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def source_addr(self):
        return self.properties['source_addr']
    @source_addr.setter
    def source_addr(self, x):
        parameter = 'source_addr'
        if self.set_none(x, parameter):
            return
        self.verify_ipv4_ipv6(x, parameter)
        self.properties[parameter] = x

    @property
    def source_int(self):
        return self.properties['source_int']
    @source_int.setter
    def source_int(self, x):
        parameter = 'source_int'
        if self.set_none(x, parameter):
            return
        self.verify_interface_or_default(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_ntp_state(x, parameter)
        self.properties[parameter] = x

    @property
    def vrf_name(self):
        return self.properties['vrf_name']
    @vrf_name.setter
    def vrf_name(self, x):
        parameter = 'vrf_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = self.spaces_to_underscore(x)

