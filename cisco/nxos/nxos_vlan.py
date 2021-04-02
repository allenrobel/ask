# NxosVlan() - cisco/nxos/nxos_vlan.py
our_version = 110
from copy import deepcopy
from ask.common.task import Task
'''
=========================
NxosVlan() - nxos_vlan.py
=========================

Description
-----------
NxosVlan() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Deprecation
-----------
NxosVlan() is deprecated and will be removed after 2022-06-01.  Use NxosVlans() instead.


Example usage
-------------
unit_test/cisco/nxos/unit_test_nxos_vlan.py

Properties
----------

- Property names are identical to the nxos_vlan module.
- aggregate is not accessed directly by the user when using ScriptKit.
    - Rather, use the NxosVlan().add_vlan() method to add vlans to the aggregate list.  Then call NxosVlan().update()
    - See the unit-test script at the path above for an example of this.

========================    ===========
Property                    Description
========================    ===========
admin_state                 Manage the VLAN administrative state of the VLAN.
                            Equivalent to shut/no shut in VLAN config mode::

                                - Type: str()
                                - Valid values: up, down
aggregate                   List of VLAN definitions.
                            This property is not accessed directly.
                            Use ScriptKit's add_vlan() method to populate the aggregate list().
                            If add_vlan() is not called prior to update(), then the task will contain
                            a single vlan and aggregate is not used.
associated_interfaces       This is a intent option and checks the operational state of the
                            or given vlan name for associated interfaces. If the value in the
                            associated_interfaces does not match with the operational state of
                            vlan interfaces on device it will result in failure::

                                - Type: list() of interface names
delay                       Time in seconds to wait before checking for the opertational state
                            on remove device::

                                - Type: int()
                                - Default: 10
interfaces                  Interfaces associated with vlan_id::

                                - Type: list() or str()
                                - Valid values: list() of interface names, or keyword 'default'
mapped_vni                  The Virtual Network Identifier (VNI) ID that is mapped to the VLAN::

                                - Type: int() or str()
                                - Valid values: int() range: 4096-16773119 or keyword 'default'
mode                        Set VLAN mode to classical ethernet or fabricpath.
                            This is a valid option for Nexus 5000::

                                - Type: str()
                                - Valid values: ce, fabricpath 
name                        Name of VLAN::

                                - Type: str()
                                - Valid values: str() or keyword 'default'
state                       Manage the state of the resource::

                                - Type: str()
                                - Valid values: absent, present
vlan_id                     Single VLAN ID::

                                - Type: int()
                                - Valid values: int() range: 1-4094
                                - Required
vlan_range                  Range of VLANs::

                                - Type: str()
                                - Valid values: NX-OS vlan range string e.g. 2-10 or 2,5,10-15
vlan_state                  Manage the vlan operational state of the VLAN::

                                - Type: str()
                                - Valid values: active, suspend
========================    ===========
'''

class NxosVlan(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vlan'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.aggregate_list = list() # updated in add_vlan()
        self.ansible_task = dict()

        self._min_vlan_id = 2
        self._max_vlan_id = 3967
        self._min_vni = 1
        self._max_vni = 16777214
        self._valid_admin_state = ['up', 'down']
        self._valid_associated_interfaces = ['Ethernet', 'port-channel', 'Vlan']
        self._valid_interfaces = ['Ethernet', 'port-channel', 'default']
        self._valid_mode = ['ce', 'fabricpath']
        self._valid_vlan_state = ['active', 'suspend']
        self.nxos_vlan_valid_state = set()
        self.nxos_vlan_valid_state.add('present')
        self.nxos_vlan_valid_state.add('absent')

        self.properties_set = set()
        self.properties_set.add('admin_state')
        self.properties_set.add('associated_interfaces')
        self.properties_set.add('delay')
        self.properties_set.add('interfaces')
        self.properties_set.add('mapped_vni')
        self.properties_set.add('mode')
        self.properties_set.add('name')
        self.properties_set.add('purge')
        self.properties_set.add('state')
        self.properties_set.add('vlan_id')
        self.properties_set.add('vlan_range')
        self.properties_set.add('vlan_state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. Set instance.state before calling instance.update()')
            exit(1)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()
        d = dict()
        if len(self.aggregate_list) != 0:
            d['aggregate'] = deepcopy(self.aggregate_list)
        else:
            for p in self.properties_set:
                if self.properties[p] != None:
                    d[p] = self.properties[p]
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)
        self.init_properties()

    def add_vlan(self):
        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.aggregate_list.append(deepcopy(d))

    def verify_admin_state(self, x, parameter='admin_state'):
        if x in self._valid_admin_state:
            return
        source_class = self.class_name
        source_method = 'verify_admin_state'
        expectation = ','.join(self._valid_admin_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_associated_interfaces(self, x, parameter='associated_interfaces'):
        source_class = self.class_name
        source_method = 'verify_associated_interfaces'
        expectation = '[list() of interfaces]'
        if type(x) != type(list()):
            self.fail(source_class, source_method, x, parameter, expectation)
        for interface in x:
            found = False
            for valid in self._valid_associated_interfaces:
                if valid in interface:
                    found = True
            if found == False:
                self.fail(source_class, source_method, x, parameter, expectation)

    def verify_interfaces(self, x, parameter='interfaces'):
        if x == 'default':
            return
        source_class = self.class_name
        source_method = 'verify_interfaces'
        expectation = '[list() of interfaces, or the keyword default]'
        if type(x) != type(list()):
            self.fail(source_class, source_method, x, parameter, expectation)
        for interface in x:
            found = False
            for valid in self._valid_interfaces:
                if valid in interface:
                    found = True
            if found == False:
                self.fail(source_class, source_method, x, parameter, expectation)

    def verify_mode(self, x, parameter='mode'):
        if x in self._valid_mode:
            return
        source_class = self.class_name
        source_method = 'verify_mode'
        expectation = ','.join(self._valid_mode)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vlan_state(self, x, parameter='state'):
        verify_set = self.nxos_vlan_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vlan_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_vlan_state(self, x, parameter='vlan_state'):
        if x in self._valid_vlan_state:
            return
        source_class = self.class_name
        source_method = 'verify_vlan_state'
        expectation = ','.join(self._valid_vlan_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_mapped_vni(self, x, parameter='mapped_vni'):
        self.verify_integer_range(x, self._min_vni, self._max_vni, self.class_name, 'verify_mapped_vni')

    @property
    def admin_state(self):
        return self.properties['admin_state']
    @admin_state.setter
    def admin_state(self, x):
        parameter = 'admin_state'
        if self.set_none(x, parameter):
            return
        self.verify_admin_state(x, parameter)
        self.properties[parameter] = x

    @property
    def associated_interfaces(self):
        return self.properties['associated_interfaces']
    @associated_interfaces.setter
    def associated_interfaces(self, x):
        parameter = 'associated_interfaces'
        if self.set_none(x, parameter):
            return
        self.verify_associated_interfaces(x, parameter)
        self.properties[parameter] = x

    @property
    def delay(self):
        return self.properties['delay']
    @delay.setter
    def delay(self, x):
        source_class = self.class_name
        source_method = 'delay'
        expectation = 'digits'
        parameter = 'delay'
        if self.set_none(x, parameter):
            return
        if not self.is_digits(x):
            self.fail(source_class, source_method, x, parameter, expectation)
        self.properties[parameter] = x

    @property
    def interfaces(self):
        return self.properties['interfaces']
    @interfaces.setter
    def interfaces(self, x):
        parameter = 'interfaces'
        if self.set_none(x, parameter):
            return
        self.verify_interfaces(x, parameter)
        self.properties[parameter] = x

    @property
    def mapped_vni(self):
        return self.properties['mapped_vni']
    @mapped_vni.setter
    def mapped_vni(self, x):
        parameter = 'mapped_vni'
        if self.set_none(x, parameter):
            return
        self.verify_mapped_vni(x, parameter)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = self.spaces_to_underscore(x)

    @property
    def purge(self):
        return self.properties['purge']
    @purge.setter
    def purge(self, x):
        parameter = 'purge'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vlan_state(x, parameter)
        self.properties[parameter] = x

    @property
    def vlan_id(self):
        return self.properties['vlan_id']
    @vlan_id.setter
    def vlan_id(self, x):
        parameter = 'vlan_id'
        if self.set_none(x, parameter):
            return
        expectation = 'int() within 2-4094 inclusive'
        self.verify_vlan(x, expectation, parameter)
        self.properties[parameter] = x

    @property
    def vlan_range(self):
        return self.properties['vlan_range']
    @vlan_range.setter
    def vlan_range(self, x):
        parameter = 'vlan_range'
        if self.set_none(x, parameter):
            return
        self.verify_vlan_list(x, parameter)
        self.properties[parameter] = x

    @property
    def vlan_state(self):
        return self.properties['vlan_state']
    @vlan_state.setter
    def vlan_state(self, x):
        parameter = 'vlan_state'
        if self.set_none(x, parameter):
            return
        self.verify_vlan_state(x, parameter)
        self.properties[parameter] = x

