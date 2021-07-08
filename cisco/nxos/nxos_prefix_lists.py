# NxosPrefixLists() - cisco/nxos/nxos_prefix_lists.py
our_version = 100
from copy import deepcopy
import re
from ask.common.task import Task
'''
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
'''
class NxosPrefixLists(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_prefix_lists'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()

        self.config = list()

        self.properties_afi = set()
        self.properties_afi.add('afi')
        self.properties_afi.add('state')

        self.properties_prefix_list_entry = set()
        self.properties_prefix_list_entry.add('action')
        self.properties_prefix_list_entry.add('eq')
        self.properties_prefix_list_entry.add('ge')
        self.properties_prefix_list_entry.add('le')
        self.properties_prefix_list_entry.add('mask')
        self.properties_prefix_list_entry.add('prefix')
        self.properties_prefix_list_entry.add('sequence')


        self.properties_prefix_list = set()
        self.properties_prefix_list.add('name')
        self.properties_prefix_list.add('description')

        self.properties = set()
        self.properties.update(self.properties_afi)
        self.properties.update(self.properties_prefix_list_entry)
        self.properties.update(self.properties_prefix_list)

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties)

        # property_map is used to map between disambiguated property names
        # and the ambiguous Ansible property names used in the Ansible playbook.
        #  There are current no ambiguous property names, so this equals
        # self.properties
        self.property_map = dict()
        for p in self.properties:
            self.property_map[p] = p

        self.nxos_prefix_lists_valid_action = set()
        self.nxos_prefix_lists_valid_action.add('deny')
        self.nxos_prefix_lists_valid_action.add('permit')

        self.nxos_prefix_lists_valid_afi = set()
        self.nxos_prefix_lists_valid_afi.add('ipv4')
        self.nxos_prefix_lists_valid_afi.add('ipv6')

        self.nxos_prefix_lists_valid_state = set()
        self.nxos_prefix_lists_valid_state.add('merged')
        self.nxos_prefix_lists_valid_state.add('replaced')
        self.nxos_prefix_lists_valid_state.add('overridden')
        self.nxos_prefix_lists_valid_state.add('deleted')
        self.nxos_prefix_lists_valid_state.add('gathered')
        self.nxos_prefix_lists_valid_state.add('rendered')
        self.nxos_prefix_lists_valid_state.add('parsed')

        self.verify_cmp = dict()
        self.verify_cmp['ipv4'] = dict()
        self.verify_cmp['ipv4']['eq_min'] = 1
        self.verify_cmp['ipv4']['eq_max'] = 32
        self.verify_cmp['ipv4']['ge_min'] = 1
        self.verify_cmp['ipv4']['ge_max'] = 32
        self.verify_cmp['ipv4']['le_min'] = 1
        self.verify_cmp['ipv4']['le_max'] = 32
        self.verify_cmp['ipv6'] = dict()
        self.verify_cmp['ipv6']['eq_min'] = 1
        self.verify_cmp['ipv6']['eq_max'] = 128
        self.verify_cmp['ipv6']['ge_min'] = 1
        self.verify_cmp['ipv6']['ge_max'] = 128
        self.verify_cmp['ipv6']['le_min'] = 1
        self.verify_cmp['ipv6']['le_max'] = 128

        self.mutex_prefix_list_entry = dict()
        self.mutex_prefix_list_entry['eq'] = set()
        self.mutex_prefix_list_entry['eq'].add('le')
        self.mutex_prefix_list_entry['eq'].add('ge')
        self.mutex_prefix_list_entry['ge'] = set()
        self.mutex_prefix_list_entry['ge'].add('eq')
        self.mutex_prefix_list_entry['ge'].add('le')
        self.mutex_prefix_list_entry['le'] = set()
        self.mutex_prefix_list_entry['le'].add('eq')
        self.mutex_prefix_list_entry['le'].add('ge')

        self.init_properties()

    def get_mapped_property(self, x):
        '''
        return either a mapped property, if one exists, or x
        '''
        if x in self.property_map:
            return self.property_map[x]
        return x

    def init_prefix_list_entry(self):
        '''
        '''
        for p in self.properties_prefix_list_entry:
            self.properties[p] = None

    def init_prefix_list(self):
        '''
        '''
        self.init_prefix_list_entry()
        self.prefix_list_entries = list()
        for p in self.properties_prefix_list:
            self.properties[p] = None

    def init_afi(self):
        '''
        '''
        self.prefix_lists = list()
        self.init_prefix_list()
        for p in self.properties_afi:
            self.properties[p] = None

    def init_properties(self):
        self.properties = dict()
        self.init_afi()
        self.properties['task_name'] = None
        self.properties['state'] = None

    def verify_prefix_list_entry(self):
        if self.action == None:
            self.task_log.error('exiting. instance.action must be set before calling instance.add_prefix_list_entry()')
            exit(1)
        if self.prefix == None:
            self.task_log.error('exiting. instance.prefix must be set before calling instance.add_prefix_list_entry()')
            exit(1)
        if self.sequence == None:
            self.task_log.error('exiting. instance.sequence must be set before calling instance.add_prefix_list_entry()')
            exit(1)
        for p in self.mutex_prefix_list_entry:
            for mp in self.mutex_prefix_list_entry[p]:
                if self.properties[p] != None and self.properties[mp] != None:
                    self.task_log.error('exiting. {} and {} are mutually-exclusive'.format(p, mp))
                    exit(1)
    def add_prefix_list_entry(self):
        self.verify_prefix_list_entry()
        d = dict()
        for p in self.properties_prefix_list_entry:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                d[mapped_p] = self.properties[p]
        if len(d) == 0:
            self.task_log.error('exiting. No prefix_list_entry properties are set')
            exit(1)
        self.prefix_list_entries.append(deepcopy(d))
        self.init_prefix_list_entry()

    def verify_prefix_list(self):
        if len(self.prefix_list_entries) == 0:
            self.task_log.error('exiting. call instance.add_prefix_list_entry() at least once before calling instance.add_prefix_list()')
            exit(1)
        if self.name == None:
            self.task_log.error('exiting. instance.name must be set before calling instance.add_prefix_list()')
            exit(1)
    def add_prefix_list(self):
        self.verify_prefix_list()
        d = dict()
        for p in self.properties_prefix_list:
            if self.properties[p] != None:
                mapped_p = self.get_mapped_property(p)
                d[mapped_p] = self.properties[p]
        if len(d) == 0:
            self.task_log.error('exiting. No prefix_list properties are set')
            exit(1)
        d['entries'] = deepcopy(self.prefix_list_entries)
        self.prefix_lists.append(deepcopy(d))
        self.init_prefix_list()

    def verify_nxos_prefix_lists_eq(self, x, parameter='eq'):
        self.verify_nxos_prefix_lists_afi(self.afi)
        source_class = self.class_name
        range_min = self.verify_cmp[self.afi]['eq_min']
        range_max = self.verify_cmp[self.afi]['eq_max']
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)
    def verify_nxos_prefix_lists_ge(self, x, parameter='ge'):
        self.verify_nxos_prefix_lists_afi(self.afi)
        source_class = self.class_name
        range_min = self.verify_cmp[self.afi]['ge_min']
        range_max = self.verify_cmp[self.afi]['ge_max']
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)
    def verify_nxos_prefix_lists_le(self, x, parameter='le'):
        self.verify_nxos_prefix_lists_afi(self.afi)
        source_class = self.class_name
        range_min = self.verify_cmp[self.afi]['le_min']
        range_max = self.verify_cmp[self.afi]['le_max']
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)
    def verify_nxos_prefix_lists_mask(self, x, parameter='mask'):
        self.verify_nxos_prefix_lists_afi(self.afi)
        # TODO: Add verification
        pass

    def verify_add_afi(self):
        if self.afi == None:
            self.task_log.error('exiting. instance.afi must be set prior to calling instance.add_afi()')
            exit(1)
        if len(self.prefix_lists) == 0:
            self.task_log.error('exiting. Call add_prefix_list at least once before calling instance.add_afi()')
            exit(1)
        for prefix_list in self.prefix_lists:
            for prefix_list_entry in prefix_list['entries']:
                if 'eq' in prefix_list_entry:
                    self.verify_nxos_prefix_lists_eq(prefix_list_entry['eq'])
                if 'ge' in prefix_list_entry:
                    self.verify_nxos_prefix_lists_ge(prefix_list_entry['ge'])
                if 'le' in prefix_list_entry:
                    self.verify_nxos_prefix_lists_le(prefix_list_entry['le'])
                if 'mask' in prefix_list_entry:
                    self.verify_nxos_prefix_lists_mask(prefix_list_entry['mask'])
    def add_afi(self):
        self.verify_add_afi()
        d = dict()
        d['afi'] = self.afi
        d['prefix_lists'] = deepcopy(self.prefix_lists)
        self.config.append(deepcopy(d))
        self.init_afi()

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if len(self.config) == 0:
            self.task_log.error('exiting. call instance.add_afi() at least once before calling instance.commit()')
            exit(1)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        update self.ansible_task
        '''
        self.final_verification()

        self.ansible_task[self.ansible_module]['config'] = deepcopy(self.config)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['state'] = self.state

    def verify_nxos_prefix_lists_action(self, x, parameter='afi'):
        verify_set = self.nxos_prefix_lists_valid_action
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_prefix_lists_action'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_prefix_lists_afi(self, x, parameter='afi'):
        verify_set = self.nxos_prefix_lists_valid_afi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_prefix_lists_afi'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_prefix_lists_prefix(self, x, parameter='prefix'):
        source_class = self.class_name
        source_method = 'verify_nxos_prefix_lists_prefix'
        expectation = 'ipv4 or ipv6 prefix <= 32 (ipv4) and <= 128 (ipv6) e.g. 1.1.1.0/30, 2001::0/126'
        if self.is_ipv4_network(x):
            return
        if self.is_ipv6_network(x):
            return
        self.fail(source_class, source_method, x, parameter, expectation)            

    def verify_nxos_prefix_lists_state(self, x, parameter='state'):
        verify_set = self.nxos_prefix_lists_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_prefix_lists_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)


    @property
    def action(self):
        return self.properties['action']
    @action.setter
    def action(self, x):
        parameter = 'action'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_prefix_lists_action(x, parameter)
        self.properties[parameter] = x

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_prefix_lists_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def description(self):
        return self.properties['description']
    @description.setter
    def description(self, x):
        parameter = 'description'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def eq(self):
        return self.properties['eq']
    @eq.setter
    def eq(self, x):
        parameter = 'eq'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def ge(self):
        return self.properties['ge']
    @ge.setter
    def ge(self, x):
        parameter = 'ge'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def le(self):
        return self.properties['le']
    @le.setter
    def le(self, x):
        parameter = 'le'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def mask(self):
        return self.properties['mask']
    @mask.setter
    def mask(self, x):
        parameter = 'mask'
        if self.set_none(x, parameter):
            return
        # TODO add verification
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def prefix(self):
        return self.properties['prefix']
    @prefix.setter
    def prefix(self, x):
        parameter = 'prefix'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_prefix_lists_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def sequence(self):
        return self.properties['sequence']
    @sequence.setter
    def sequence(self, x):
        parameter = 'sequence'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_prefix_lists_state(x, parameter)
        self.properties[parameter] = x
