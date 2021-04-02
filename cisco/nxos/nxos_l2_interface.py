# NxosL2Interface() - cisco/nxos/nxos_l2_interface.py
our_version = 105
from copy import deepcopy
from ask.common.task import Task
'''
Name: ask_task_nxos_l2_interface.py

DEPRECATED  Will be removed after 2022-06-01.
            Alternative: cisco/nxos/nxos_l2_interfaces.py

Description:

NxosL2Interface() generates Ansible Playbook tasks conformant with nxos_l2_interface
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_l2_interface.py

Properties:
    access_vlan             If mode=access, used as the access VLAN ID.
                            Valid values: int() range: 1-3967
    aggregate               list() of dict()
    mode                    Valid values: access, trunk
    name                    full name of interface e.g. Ethernet1/1, port-channel10
    native_vlan             If mode=trunk, used as the trunk native VLAN ID.
    state                   Valid values: present, absent, unconfigured
    trunk_allowed_vlans     If mode=trunk, these are the only VLANs that will be configured on the trunk.
                            Valid values: str() e.g. '10, 20-30'.  
    trunk_vlans             If mode=trunk, used as the VLAN range to ADD or REMOVE from the trunk.
                            Valid values: str() e.g. '10, 20-30'
'''

class NxosL2Interface(Task):
    def __init__(self, task_log):
        ansible_module = 'nxos_l2_interface'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.task_log.warning('*******************************************************************************************')
        self.task_log.warning('NxosL2Interface() is DEPRECATED as its Ansible module nxos_ls_interface is DEPRECATED.')
        self.task_log.warning('NxosL2Interface() will be removed after 2022-06-01')
        self.task_log.warning('Use NxosL2Interfaces() (cisco/nxos/nxos_l2_interfaces.py) instead.')
        self.task_log.warning('*******************************************************************************************')

        self.nxos_l2_interface_valid_state = set()
        self.nxos_l2_interface_valid_state.add('present')
        self.nxos_l2_interface_valid_state.add('absent')
        self.nxos_l2_interface_valid_state.add('unconfigured')

        self.nxos_l2_interface_valid_mode = set()
        self.nxos_l2_interface_valid_mode.add('access')
        self.nxos_l2_interface_valid_mode.add('trunk')

        self.nxos_l2_interface_access_vlan_min = 1
        self.nxos_l2_interface_access_vlan_max = 3967

        self.nxos_l2_interface_native_vlan_min = 1
        self.nxos_l2_interface_native_vlan_max = 3967

        self.properties_set = set()
        self.properties_set.add('access_vlan')
        self.properties_set.add('aggregate')
        self.properties_set.add('mode')
        self.properties_set.add('name')
        self.properties_set.add('native_vlan')
        self.properties_set.add('state')
        self.properties_set.add('trunk_allowed_vlans')
        self.properties_set.add('trunk_vlans')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None

    def final_verification(self):
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.update()')
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
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def verify_nxos_l2_interface_mode(self, x, parameter='mode'):
        verify_set = self.nxos_l2_interface_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interface_mode'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_l2_interface_access_vlan(self, x, parameter='access_vlan'):
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interface_access_vlan'
        range_min = self.nxos_l2_interface_access_vlan_min
        range_max = self.nxos_l2_interface_access_vlan_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_l2_interface_native_vlan(self, x, parameter='native_vlan'):
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interface_native_vlan'
        range_min = self.nxos_l2_interface_native_vlan_min
        range_max = self.nxos_l2_interface_native_vlan_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_l2_interface_state(self, x, parameter='state'):
        verify_set = self.nxos_l2_interface_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interface_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def access_vlan(self):
        return self.properties['access_vlan']
    @access_vlan.setter
    def access_vlan(self, x):
        parameter = 'access_vlan'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interface_access_vlan(x, parameter)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interface_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def native_vlan(self):
        return self.properties['native_vlan']
    @native_vlan.setter
    def native_vlan(self, x):
        parameter = 'native_vlan'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interface_native_vlan(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interface_state(x, parameter)
        self.properties[parameter] = x

    @property
    def trunk_allowed_vlans(self):
        return self.properties['trunk_allowed_vlans']
    @trunk_allowed_vlans.setter
    def trunk_allowed_vlans(self, x):
        parameter = 'trunk_allowed_vlans'
        if self.set_none(x, parameter):
            return
        if type(x) == type(int()):
            x = str(x)
        self.verify_vlan_list(str(x), parameter)
        self.properties[parameter] = x

    @property
    def trunk_vlans(self):
        return self.properties['trunk_vlans']
    @trunk_vlans.setter
    def trunk_vlans(self, x):
        parameter = 'trunk_vlans'
        if self.set_none(x, parameter):
            return
        self.verify_vlan_list(x, parameter)
        self.properties[parameter] = x
