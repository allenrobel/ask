# NxosEvpnVni() - cisco/nxos/nxos_evpn_vni.py
our_version = 103
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosEvpnVni()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosEvpnVni() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_evpn_vni
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_evpn_vni <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_evpn_vni_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_evpn_vni.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_evpn_vni.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
route_distinguisher                 VPN Route Distinguisher (RD).  RD is combined
                                    with the IPv4 or IPv6 prefix learned by the PE
                                    router to create a globally unique address::

                                        - Type: str()
                                        - Valid values:
                                            - auto
                                            - default
                                            - y.y.y.y:x
                                                - where y.y.y.y is dotted-decimal address
                                                - where x is int()
                                            - x:x 
                                                - where x is int()
                                        - Examples:
                                            task.route_distinguisher = 'auto'
                                            task.route_distinguisher = 'default'
                                            task.route_distinguisher = '10.3.1.1:34000'
                                            task.route_distinguisher = '12229:14177'

route_target_both                   Enables/Disables route-target settings for both 
                                    import and export target communities using a single
                                    property::

                                        - Type: str() or list()
                                        - Valid values:
                                            - auto
                                            - default
                                            - list() with str() elements in the following
                                              formats:
                                                - y.y.y.y:x
                                                    - where y.y.y.y is dotted-decimal address
                                                    - where x is int()
                                                - x:x 
                                                    - where x is int()
                                        - Examples:
                                            task.route_target_both = 'auto'
                                            task.route_target_both = 'default'
                                            rt = list()
                                            rt.append('10.1.1.3:12001')
                                            rt.append('12227:12001')
                                            task.route_target_both = rt.copy()

route_target_export                 Sets the route-target 'export' extended communities::

                                        - Type: str() or list()
                                        - Valid values:
                                            - auto
                                            - default
                                            - list() with str() elements in the following
                                              formats:
                                                - y.y.y.y:x
                                                    - where y.y.y.y is dotted-decimal address
                                                    - where x is int()
                                                - x:x 
                                                    - where x is int()
                                        - Examples:
                                            task.route_target_both = 'auto'
                                            task.route_target_both = 'default'
                                            rt = list()
                                            rt.append('10.1.1.3:12001')
                                            rt.append('12227:12001')
                                            task.route_target_both = rt.copy()

route_target_import                 Sets the route-target 'import' extended communities::

                                        - Type: str() or list()
                                        - Valid values:
                                            - auto
                                            - default
                                            - list() with str() elements in the following
                                              formats:
                                                - y.y.y.y:x
                                                    - where y.y.y.y is dotted-decimal address
                                                    - where x is int()
                                                - x:x 
                                                    - where x is int()
                                        - Examples:
                                            task.route_target_both = 'auto'
                                            task.route_target_both = 'default'
                                            rt = list()
                                            rt.append('10.1.1.3:12001')
                                            rt.append('12227:12001')
                                            task.route_target_both = rt.copy()

state                               Determines whether the config should be present
                                    or not on the remote device::

                                        - Type: str()
                                        - Valid values:
                                            - absent
                                            - present
                                        - Default: present

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Examples:
                                            - task.task_name = 'my task'

vni                                 The EVPN VXLAN Network Identifier::

                                        - Type: int()
                                        - Examples:
                                            - task.vni = 32020
                                        
================================    ==============================================

NOTES
-----

1.  ``feature nv overlay`` must be enabled before using this library
2.  RD override is not permitted. You should set it to the default values first and then reconfigure it
3.  ``route_target_both``, ``route_target_import`` and ``route_target_export`` valid values are a list of extended communities
    (e.g. ['1.2.3.4:5', '33:55']) or the keywords ``auto`` or ``default``.
4.  ``route_target_both`` property is discouraged due to the inconsistent behavior of the property across Nexus platforms
    and image versions. For this reason it is recommended to use explicit ``route_target_export`` and
    ``route_target_import`` properties instead of ``route_target_both``
5.  RD valid values are a string in one of the route-distinguisher formats, the keyword ``auto``, or the keyword ``default``

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)


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

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_evpn_vni_valid_state = set()
        self.nxos_evpn_vni_valid_state.add('absent')
        self.nxos_evpn_vni_valid_state.add('present')

        self.init_properties()

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
        self.properties[parameter] = str(x)
