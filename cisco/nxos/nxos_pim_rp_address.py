# NxosPimRpAddress() - cisco/nxos/nxos_pim_rp_address.py
our_version = 101
from copy import deepcopy
from ask.common.task import Task
'''
===========================================
NxosPimRpAddress() - nxos_pim_rp_address.py
===========================================

Description
-----------
NxosPimRpAddress() generates Ansible Playbook tasks conformant with nxos_pim_rp_address
which can be fed to Playbook().add_task()

Example usage
-------------
unit_test/cisco/nxos/unit_test_nxos_pim_rp_address.py

Dependencies
------------
The following must be enabled prior to applying nxos_pim_rp_address playbook

- feature pim

Properties
----------

Valid values for all bool() types are: no, yes

=========== ===========
Property    Description
=========== ===========
bidir       Group range is treated in PIM bidirectional mode::

                - Type: bool()  
group_list  Group range for static RP::

                - Type: str()
                - Valid values: multicast addresses
prefix_list Prefix list policy for static RP::

                - Type: str()
                - Valid values: prefix-list policy names
route_map   Route map policy for static RP::

                - Type: str()
                - Valid values: route-map policy names
rp_address  Configures a Protocol Independent Multicast (PIM) static rendezvous point (RP) address::

                - Type: str()
                - Valid values: unicast addresses
state       Specify desired state of the resource::

                - Type: str()
                - Valid values: absent, present
                - Default: present
=========== ===========

NOTES
-----

   1. state=absent is currently not supported on all platforms

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
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.rp_address == None:
            self.task_log.error('exiting. instance.rp_address must be set prior to calling instance.update()')
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
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def group_list(self):
        return self.properties['group_list']
    @group_list.setter
    def group_list(self, x):
        parameter = 'group_list'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = str(x)

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
