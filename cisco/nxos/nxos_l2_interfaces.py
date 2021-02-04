# NxosL2Interfaces() - cisco/nxos/nxos_l2_interfaces.py
our_version = 106
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_l2_interfaces.py

Description:

NxosL2Interfaces() generates Ansible Playbook tasks conformant with nxos_l2_interfaces
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_l2_interfaces.py

Properties:

    allowed_vlans   -   Comma-separated list of allowed VLANs on trunk port
                        Example: 2-5,10,20
    mode            -   Mode in which interface needs to be configured.
                        Valid values: access, trunk, fex-fabric
    name            -   Full name of interface
                        Examples: Ethernet1/1, port-channel10
    native_vlan     -   Native VLAN configured on trunk port
                        Valid values: int() range: 1-3967
                        Example: 10
    state           -   see self._valid_state
    task_name       -   Name of the task
    vlan            -   Vlan configured on access port
                        Valid values: int() range: 1-3967
                        Example: 10

'''

class NxosL2Interfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_l2_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('allowed_vlans')
        self.properties_set.add('mode')
        self.properties_set.add('native_vlan')
        self.properties_set.add('vlan')
        self.properties_set.add('name')

        self.nxos_l2_interfaces_valid_mode = set()
        self.nxos_l2_interfaces_valid_mode.add('access')
        self.nxos_l2_interfaces_valid_mode.add('trunk')
        self.nxos_l2_interfaces_valid_mode.add('fex-fabric')

        self.nxos_l2_interfaces_valid_state = set()
        self.nxos_l2_interfaces_valid_state.add('merged')
        self.nxos_l2_interfaces_valid_state.add('replaced')
        self.nxos_l2_interfaces_valid_state.add('overridden')
        self.nxos_l2_interfaces_valid_state.add('deleted')

        self.nxos_l2_interfaces_native_vlan_min = 1
        self.nxos_l2_interfaces_native_vlan_max = 3967

        self.nxos_l2_interfaces_vlan_min = 1
        self.nxos_l2_interfaces_vlan_max = 3967

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['state'] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.update()')
            exit(1)
        if self.mode == None:
            self.task_log.error('exiting. call instance.mode before calling instance.update()')
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate and append dict() to self.ansible_task[self.ansible_module]['config']
        '''
        self.final_verification()

        d = dict()
        d['mode'] = self.mode
        d['name'] = self.name
        access = self.add_access()
        trunk = self.add_trunk()
        if access != False:
            d['access'] = access
        if trunk != False:
            d['trunk'] = trunk

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['config'] = list()
        self.ansible_task[self.ansible_module]['config'].append(deepcopy(d))
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_l2_interfaces_native_vlan(self, x, parameter='native_vlan'):
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interfaces_native_vlan'
        range_min = self.nxos_l2_interfaces_native_vlan_min
        range_max = self.nxos_l2_interfaces_native_vlan_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_l2_interfaces_vlan(self, x, parameter='vlan'):
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interfaces_vlan'
        range_min = self.nxos_l2_interfaces_vlan_min
        range_max = self.nxos_l2_interfaces_vlan_max
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_l2_interfaces_state(self, x, parameter='state'):
        verify_set = self.nxos_l2_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interfaces_state'
        expectation = ','.join(self.verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_l2_interfaces_mode(self, x, parameter='mode'):
        verify_set = self.nxos_l2_interfaces_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_l2_interfaces_mode'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def add_access(self):
        if self.vlan == None:
            return False
        d = dict()
        d['vlan'] = self.vlan
        return d.copy()

    def add_trunk(self):
        if self.allowed_vlans == None and self.native_vlan == None:
            return False
        d = dict()
        if self.allowed_vlans != None:
            d['allowed_vlans'] = self.allowed_vlans
        if self.native_vlan != None:
            d['native_vlan'] = self.native_vlan
        return d.copy()

    @property
    def allowed_vlans(self):
        return self.properties['allowed_vlans']
    @allowed_vlans.setter
    def allowed_vlans(self, x):
        parameter = 'allowed_vlans'
        if self.set_none(x, parameter):
            return
        self.verify_vlan_list(x)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interfaces_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def native_vlan(self):
        return self.properties['native_vlan']
    @native_vlan.setter
    def native_vlan(self, x):
        parameter = 'native_vlan'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interfaces_native_vlan(x, parameter)
        self.properties[parameter] = x

    @property
    def vlan(self):
        return self.properties['vlan']
    @vlan.setter
    def vlan(self, x):
        parameter = 'vlan'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interfaces_vlan(x, parameter)
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
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_l2_interfaces_state(x, parameter)
        self.properties[parameter] = x
