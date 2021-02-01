# NxosEvpnGlobal() - cisco/nxos/nxos_evpn_global.py
our_version = 104
# standard library
from copy import deepcopy
import re
# scriptkit library
from ask.common.task import Task
'''
Name: nxos_evpn_global.py

Description:

NxosEvpnGlobal() generates Ansible Playbook tasks conformant with nxos_evpn_global
which can be fed to Playbook().add_task()

Example usage:
    cisco/nxos/unit_test_nxos_evpn_global.py

Properties:

    nv_overlay_evpn         Enable/disable EVPN control plane
                            Valid values: no, yes. 

'''

class NxosEvpnGlobal(Task):
    '''
    Example usage:

    '''
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_evpn_global'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.properties_set = set()
        self.properties_set.add('nv_overlay_evpn')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.nv_overlay_evpn == None:
            self.task_log.error('exiting. instance.nv_overlay_evpn must be set before calling instance.update()')
            exit(1)

    def update(self):
        '''
        verify mandatory module-specific parameters are set
        update ansible_task dict()
        call init_properties()
        '''
        self.final_verification()

        d = dict()
        for p in self.properties_set:
            if self.properties[p] != None:
                d[p] = self.properties[p]
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    @property
    def nv_overlay_evpn(self):
        return self.properties['nv_overlay_evpn']
    @nv_overlay_evpn.setter
    def nv_overlay_evpn(self, x):
        parameter = 'nv_overlay_evpn'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

