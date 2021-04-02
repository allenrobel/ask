# NxosPimRpAddress() - cisco/nxos/nxos_pim_rp_address.py
our_version = 103
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosPimRpAddress()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosPimRpAddress() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_pim_rp_address
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_pim_rp_address <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_pim_rp_address_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_pim_rp_address.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_pim_rp_address.py>`_

Dependencies
------------
The following must be enabled prior to applying nxos_pim_rp_address playbook::

  feature pim

NOTES
-----

   1. state=absent is currently not supported on all platforms


|

================    ==============================================
Property            Description
================    ==============================================
bidir               If True, ``group_list`` refers to a set of PIM
                    bidirectional mode multicast groups.
                    If False, ``group_list`` refers to a set of
                    PIM Sparse mode groups::

                        - Type: bool()  
                        - Valid values:
                            - False
                            - True
                        - Example:
                            task.bidir = False

group_list          Multicast groups for which ``rp_address`` will
                    act as the rendezvous point::

                        - Type: str()
                        - Valid values:
                            - ipv4 multicast address with prefixlen
                              - A.B.C.D/LEN
                        - Example:
                            task.group_list = '225.1.0.0/16'

prefix_list         Prefix list policy for static RP::

                        - Type: str()
                        - Valid values:
                            - ip prefix-list name
                        - Example:
                            task.prefix_list = 'ALLOW_SOURCES'

route_map           Route map policy for static RP::

                        - Type: str()
                        - Valid values:
                            route-map name
                        - Example:
                            task.route_map = 'ALLOW_SOURCES'

rp_address          Configures a Protocol Independent Multicast
                    (PIM) static rendezvous point (RP) address::

                        - Type: str()
                        - Valid values:
                            - ipv4 unicast address
                              - A.B.C.D
                        - Example:
                            task.rp_address = '10.1.1.3'

state               Desired state after task completion::

                        - Type: str()
                        - Valid values:
                            - absent
                            - present
                        - Example:
                            task.state = 'present'
                        - Required

task_name           Name of the task. Ansible will display this
                    when the playbook is run::

                        - Type: str()
                        - Example:
                            - task.task_name = 'my task'

================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''
class NxosPimRpAddress(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_pim_rp_address'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('bidir')
        self.properties_set.add('group_list')
        self.properties_set.add('prefix_list')
        self.properties_set.add('route_map')
        self.properties_set.add('rp_address')
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_pim_rp_address_valid_state = set()
        self.nxos_pim_rp_address_valid_state.add('absent')
        self.nxos_pim_rp_address_valid_state.add('present')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if self.rp_address == None:
            self.task_log.error('exiting. instance.rp_address must be set prior to calling instance.commit()')
            exit(1)
        if self.group_list != None and self.route_map != None:
            self.task_log.error('exiting. instance.group_list and instance_route_map are mutually-exclusive')
            exit(1)
        if self.group_list != None and self.prefix_list != None:
            self.task_log.error('exiting. instance.group_list and instance_prefix_list are mutually-exclusive')
            exit(1)
        if self.route_map != None and self.prefix_list != None:
            self.task_log.error('exiting. instance.route_map and instance_prefix_list are mutually-exclusive')
            exit(1)


    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        populate and append dict() to self.ansible_task[self.ansible_module]['config']

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

    def verify_nxos_pim_rp_address_rp_address(self, x, parameter='rp_address'):
        if self.is_ipv4_unicast_address(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_pim_rp_address_rp_address'
        expectation = 'ipv4 address without prefix e.g. 10.1.1.1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_pim_rp_address_state(self, x, parameter='state'):
        verify_set = self.nxos_pim_rp_address_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_pim_rp_address_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def bidir(self):
        return self.properties['bidir']
    @bidir.setter
    def bidir(self, x):
        parameter = 'bidir'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def group_list(self):
        return self.properties['group_list']
    @group_list.setter
    def group_list(self, x):
        parameter = 'group_list'
        if self.set_none(x, parameter):
            return
        self.verify_ipv4_multicast_address_with_prefix(x, parameter)
        self.properties[parameter] = x

    @property
    def prefix_list(self):
        return self.properties['prefix_list']
    @prefix_list.setter
    def prefix_list(self, x):
        parameter = 'prefix_list'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def route_map(self):
        return self.properties['route_map']
    @route_map.setter
    def route_map(self, x):
        parameter = 'route_map'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def rp_address(self):
        return self.properties['rp_address']
    @rp_address.setter
    def rp_address(self, x):
        parameter = 'rp_address'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_rp_address_rp_address(x)
        self.properties[parameter] = str(x)

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_pim_rp_address_state(x, parameter)
        self.properties[parameter] = x
