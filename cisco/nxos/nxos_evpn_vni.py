# NxosEvpnVni() - cisco/nxos/nxos_evpn_vni.py
our_version = 101
# standard library
from copy import deepcopy
# scriptkit library
from ask.common.task import Task
'''
Name: nxos_evpn_vni.py

Description:

NxosEvpnVni() generates Ansible Playbook tasks conformant with nxos_evpn_vni
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_evpn_vni.py

Properties:

    route_distinguisher -   str()   VPN Route Distinguisher (RD).  RD is combined with the IPv4 or IPv6
                                    prefix learned by the PE router to create a globally unique address.
    route_target_both   -   str()   Enables/Disables route-target settings for both import and export
                                    target communities using a single property.
    route_target_export -   str()   Sets the route-target 'export' extended communities
    route_target_import -   str()   Sets the route-target 'import' extended communities
    state               -   str()   Determines whether the config should be present or not on the device
                                    Valid values: absent, present
                                    Default: present
    vni                 -   str()   The EVPN VXLAN Network Identifier

    NOTES:

    1.  feature nv overlay must be enabled before using this library
    2.  RD override is not permitted. You should set it to the default values first and then reconfigure it
    3.  route_target_both, route_target_import and route_target_export valid values are a list of extended communities
        (e.g. ['1.2.3.4:5', '33:55']) or the keywords 'auto' or 'default'.
    4.  route_target_both property is discouraged due to the inconsistent behavior of the property across Nexus platforms
        and image versions. For this reason it is recommended to use explicit route_target_export and
        route_target_import properties instead of route_target_both
    5.  RD valid values are a string in one of the route-distinguisher formats, the keyword 'auto', or the keyword 'default'

'''

class NxosEvpnVni(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_evpn_vni'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('route_distinguisher')  
        self.properties_set.add('route_target_both')
        self.properties_set.add('route_target_export')
        self.properties_set.add('route_target_import')
        self.properties_set.add('state')
        self.properties_set.add('vni')
        self.init_properties()

        self.nxos_evpn_vni_valid_state = set()
        self.nxos_evpn_vni_valid_state.add('absent')
        self.nxos_evpn_vni_valid_state.add('present')

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None

    def final_verification(self):
        if self.vni == None:
            self.task_log.error('exiting. instance.vni must be set before calling instance.update()')
            exit(1)

    def update(self):
        '''
        verify mandatory module-specific parameters are set
        update ansible_task dict()
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

    def verify_nxos_evpn_vni_state(self, x, parameter='state'):
        verify_set = self.nxos_evpn_vni_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_evpn_vni_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def route_distinguisher(self):
        return self.properties['route_distinguisher']
    @route_distinguisher.setter
    def route_distinguisher(self, x):
        parameter = 'route_distinguisher'
        if self.set_none(x, parameter):
            return
        self.verify_rd(x, parameter) # inherited from Common() via Task()
        self.properties[parameter] = x

    @property
    def route_target_both(self):
        return self.properties['route_target_both']
    @route_target_both.setter
    def route_target_both(self, x):
        parameter = 'route_target_both'
        if self.set_none(x, parameter):
            return
        self.verify_rt(x, parameter) # inherited from Common() via Task()
        self.properties[parameter] = x

    @property
    def route_target_export(self):
        return self.properties['route_target_export']
    @route_target_export.setter
    def route_target_export(self, x):
        parameter = 'route_target_export'
        if self.set_none(x, parameter):
            return
        self.verify_rt(x, parameter) # inherited from Common() via Task()
        self.properties[parameter] = x

    @property
    def route_target_import(self):
        return self.properties['route_target_import']
    @route_target_import.setter
    def route_target_import(self, x):
        parameter = 'route_target_import'
        if self.set_none(x, parameter):
            return
        self.verify_rt(x, parameter) # inherited from Common() via Task()
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_evpn_vni_state(x, parameter)
        self.properties[parameter] = x

    @property
    def vni(self):
        return self.properties['vni']
    @vni.setter
    def vni(self, x):
        parameter = 'vni'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter) # inherited from Common() via Task()
        self.properties[parameter] = x
