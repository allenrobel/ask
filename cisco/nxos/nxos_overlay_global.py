# NxosOverlayGlobal() - cisco/nxos/nxos_overlay_global.py
our_version = 101
from copy import deepcopy
from ask.common.task import Task
'''
nxos_overlay_global.py
----------------------

Description
-----------

NxosOverlayGlobal() generates Ansible Playbook tasks conformant with nxos_overlay_global
which can be fed to Playbook().add_task()

Example usage
-------------

unit_test/cisco/nxos/unit_test_nxos_overlay_global.py

Dependencies
------------

The following must be enabled prior to applying nxos_overlay_global playbook::

    nv overlay evpn

Properties
----------

======================================  ==================================================
Property                                Description
======================================  ==================================================
anycast_gateway_mac                     Anycast gateway mac of the switch::

                                             Type: str()
                                             Valid values:
                                                - default
                                                - EEEE.EEEE.EEEE
                                                - EE:EE:EE:EE:EE:EE
                                                - EE-EE-EE-EE-EE-EE
                                             Required
======================================  ==================================================

'''
class NxosOverlayGlobal(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_overlay_global'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('anycast_gateway_mac')

        self.nxos_overlay_global_valid_state = set()
        self.nxos_overlay_global_valid_state.add('absent')
        self.nxos_overlay_global_valid_state.add('present')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name']    = None

    def final_verification(self):
        if self.anycast_gateway_mac == None:
            self.task_log.error('exiting. instance.anycast_gateway_mac must be set prior to calling instance.update()')
            exit(1)

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
        self.ansible_task[self.ansible_module] = deepcopy(d)
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_overlay_global_state(self, x, parameter='state'):
        verify_set = self.nxos_overlay_global_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_overlay_global_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_overlay_global_anycast_gateway_mac(self, x, parameter='anycast_gateway_mac'):
        if self.is_default(x):
            return
        if self.is_mac_address(x):  # inherited from AnsCommon via Ask
            return
        source_class = self.class_name
        source_method = 'verify_nxos_overlay_global_anycast_gateway_mac'
        expectation = 'keyword "default" or a mac address with any of the following formats: x.x.x, xxxx.xxxx.xxxx, xx:xx:xx:xx:xx:xx, xx-xx-xx-xx-xx-xx'
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def anycast_gateway_mac(self):
        return self.properties['anycast_gateway_mac']
    @anycast_gateway_mac.setter
    def anycast_gateway_mac(self, x):
        parameter = 'anycast_gateway_mac'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_overlay_global_anycast_gateway_mac(x, parameter)
        self.properties[parameter] = x
