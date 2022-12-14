# NxosVrfAf() - cisco/nxos/nxos_vrf_af.py
our_version = 101
from copy import deepcopy
from ask.common.task import Task
'''
*******************************************
NxosVrfAf()
*******************************************

.. contents::
   :local:
   :depth: 1

Version
-------
101

Caveats
-------
1. The ``evpn`` keyword for route-target is not currently supported by the Ansible module.  You will need to use NxosConfig module to configure this.

ScriptKit Synopsis
------------------
NxosVrfAf() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vrf_af <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vrf_af_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/interfaces/unit_test_nxos_vrf_af.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vrf_af.py>`_

Properties
----------

======================================  ==================================================
Properties / Methods                    Description
======================================  ==================================================
add_rt()                                Append the currently-configured route-target to 
                                        the RT list, and clear all RT-related properties
                                        so that another RT can be configured.  See
                                        ``ScriptKit Example`` above for usage within
                                        a script::

                                            - Type: method
                                            - Example:
                                                task = NxosVrfAf(log_instance)
                                                task.rt = '300:2000'
                                                task.rt_direction = 'export'
                                                task.rt_state = 'present'
                                                task.add_rt()
                                                task.rt = '300:2001'
                                                task.rt_direction = 'import'
                                                task.rt_state = 'present'
                                                task.add_rt()
                                                etc...

afi                                     Address Family::

                                            - Type: str()
                                            - Valid values:
                                                - ipv4
                                                - ipv6
                                            - Example:
                                                task.afi = 'ipv4'

route_target_both_auto_evpn             Enable/Disable the EVPN route-target 'auto' setting for both import and export target communities::

                                            - Type: bool()
                                            - Valid values:
                                                - False
                                                - True
                                            - Example:
                                                task.route_target_both_auto_evpn = False

rt                                      route-target::

                                            - Type: str()
                                            - Example:
                                                task.rt = '300:2000'

rt_direction                            Indicates the direction of the route-target::

                                            - Type: str()
                                            - Valid values:
                                                - both
                                                - export
                                                - import
                                            - Default: both
                                            - Example:
                                                task.rt_direction = 'import'

rt_state                                The state of this route-target::

                                            - Type: str()
                                            - Valid values:
                                                - absent
                                                - present
                                            - Default: present
                                            - Examples:
                                                task.rt_state = 'present'

state                                   Manages desired state of the resource::

                                            - Type: str()
                                            - Valid values:
                                                - absent
                                                - present
                                            - Examples:
                                                task.state = 'present'

task_name                               Freeform name for the task (ansible-playbook
                                        will print this when the task is run)::

                                            - Type: str()
                                            - Examples:
                                                task.task_name = 'configure route targets'

vrf                                     Name of the VRF to be managed::

                                            - Type: str()
                                            - Examples:
                                                - task.vrf = 'my_vrf'

======================================  ==================================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosVrfAf(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vrf_af'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.route_targets = list() # updated in add_rt()

        self.nxos_vrf_af_valid_afi = set()
        self.nxos_vrf_af_valid_afi.add('ipv4')
        self.nxos_vrf_af_valid_afi.add('ipv6')

        self.nxos_vrf_af_valid_state = set()
        self.nxos_vrf_af_valid_state.add('absent')
        self.nxos_vrf_af_valid_state.add('present')

        self.nxos_vrf_af_valid_rt_state = set()
        self.nxos_vrf_af_valid_rt_state.add('absent')
        self.nxos_vrf_af_valid_rt_state.add('present')

        self.nxos_vrf_af_valid_rt_direction = set()
        self.nxos_vrf_af_valid_rt_direction.add('both')
        self.nxos_vrf_af_valid_rt_direction.add('export')
        self.nxos_vrf_af_valid_rt_direction.add('import')

        self.properties_set = set()
        self.properties_set.add('afi')
        self.properties_set.add('rt_direction')
        self.properties_set.add('route_target_both_auto_evpn')
        self.properties_set.add('rt')
        self.properties_set.add('rt_state')
        self.properties_set.add('state')
        self.properties_set.add('vrf')

        self.properties_rt = set()
        self.properties_rt.add('rt_direction')
        self.properties_rt.add('rt')
        self.properties_rt.add('rt_state')

        self.properties_global = set()
        self.properties_global.add('afi')
        self.properties_global.add('route_target_both_auto_evpn')
        self.properties_global.add('state')
        self.properties_global.add('vrf')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_global)

        # used in commit() to resolve any disambiguated property
        # names back into the names used by the Ansible module.
        # In this case, rt_state is resolved into state
        self.property_map = dict()
        self.property_map['afi'] = 'afi'
        self.property_map['rt_direction'] = 'direction'
        self.property_map['route_target_both_auto_evpn'] = 'route_target_both_auto_evpn'
        self.property_map['rt'] = 'rt'
        self.property_map['rt_state'] = 'state'
        self.property_map['state'] = 'state'
        self.property_map['vrf'] = 'vrf'

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.afi == None:
            self.task_log.error('exiting. call instance.afi before calling instance.commit()')
            exit(1)
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.commit()')
            exit(1)
        if self.vrf == None:
            self.task_log.error('exiting. call instance.vrf before calling instance.commit()')
            exit(1)
        if len(self.route_targets) == 0:
            self.task_log.error('exiting. call instance.add_rt() at least once before calling instance.commit()')
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
        if len(self.route_targets) != 0:
            d['route_targets'] = deepcopy(self.route_targets)
        for p in self.properties_global:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def init_rt(self):
        for p in self.properties_rt:
            self.properties[p] = None
    def verify_rt(self):
        if self.rt == None:
            self.task_log.error('exiting. call instance.rt before calling instance.add_rt()')
            exit(1)
    def add_rt(self):
        self.verify_rt()
        d = dict()
        for p in self.properties_rt:
            if self.properties[p] != None:
                mapped_p = self.property_map[p]
                d[mapped_p] = self.properties[p]
        self.route_targets.append(deepcopy(d))
        self.init_rt()

    def verify_nxos_vrf_af_afi(self, x, parameter='afi'):
        verify_set = self.nxos_vrf_af_valid_afi
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_af_afi'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vrf_af_rt_direction(self, x, parameter='rt_direction'):
        verify_set = self.nxos_vrf_af_valid_rt_direction
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_af_rt_direction'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vrf_af_rt_state(self, x, parameter='rt_state'):
        verify_set = self.nxos_vrf_af_valid_rt_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_af_rt_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vrf_af_state(self, x, parameter='state'):
        verify_set = self.nxos_vrf_af_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vrf_af_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def afi(self):
        return self.properties['afi']
    @afi.setter
    def afi(self, x):
        parameter = 'afi'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_af_afi(x, parameter)
        self.properties[parameter] = x

    @property
    def rt_direction(self):
        return self.properties['rt_direction']
    @rt_direction.setter
    def rt_direction(self, x):
        parameter = 'rt_direction'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_af_rt_direction(x, parameter)
        self.properties[parameter] = x

    @property
    def route_target_both_auto_evpn(self):
        return self.properties['route_target_both_auto_evpn']
    @route_target_both_auto_evpn.setter
    def route_target_both_auto_evpn(self, x):
        parameter = 'route_target_both_auto_evpn'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def rt(self):
        return self.properties['rt']
    @rt.setter
    def rt(self, x):
        parameter = 'rt'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def rt_state(self):
        return self.properties['rt_state']
    @rt_state.setter
    def rt_state(self, x):
        parameter = 'rt_state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_af_rt_state(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vrf_af_state(x, parameter)
        self.properties[parameter] = x

    @property
    def vrf(self):
        return self.properties['vrf']
    @vrf.setter
    def vrf(self, x):
        parameter = 'vrf'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
