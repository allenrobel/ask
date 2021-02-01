# NxosHsrpInterfaces() - python/lib3/nxos_hsrp_interfaces.py
our_version = 102
# standard library
from copy import deepcopy
# scriptkit library
from ask.common.task import Task
'''
Name: nxos_hsrp_interfaces.py

Description:

NxosHsrpInterfaces() generates Ansible Playbook tasks conformant with nxos_hsrp_interfaces
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/nxos_hsrp_interfaces.py

Properties:

    name        Full name of interface, e.g. Ethernet1/1
                Required
    bfd         Enable/Disable HSRP Bidirectional Forwarding Detection (BFD) on the interface
                Valid values: disable, enable
    state       Valid values: see __init__().nxos_hsrp_interfaces_valid_state

'''

class NxosHsrpInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_hsrp_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self._classname = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('name')
        self.properties_set.add('bfd')

        self.nxos_hsrp_interfaces_valid_bfd = set()
        self.nxos_hsrp_interfaces_valid_bfd.add('disable')
        self.nxos_hsrp_interfaces_valid_bfd.add('enable')

        self.nxos_hsrp_interfaces_valid_state = set()
        self.nxos_hsrp_interfaces_valid_state.add('merged')
        self.nxos_hsrp_interfaces_valid_state.add('replaced')
        self.nxos_hsrp_interfaces_valid_state.add('overridden')
        self.nxos_hsrp_interfaces_valid_state.add('deleted')
        self.nxos_hsrp_interfaces_valid_state.add('gathered')
        self.nxos_hsrp_interfaces_valid_state.add('rendered')
        self.nxos_hsrp_interfaces_valid_state.add('parsed')

        self.nxos_hsrp_interfaces_valid_interface_examples = set()
        self.nxos_hsrp_interfaces_valid_interface_examples.add('EthernetX/Y')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('EthernetX/Y/Z')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('EthernetX/Y.S')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('EthernetX/Y/Z.S')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('port-channelX')
        self.nxos_hsrp_interfaces_valid_interface_examples.add('VlanX')

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
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['config'] = list()
        self.ansible_task[self.ansible_module]['config'].append(deepcopy(d))
        self.ansible_task[self.ansible_module]['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

    def verify_nxos_hsrp_interfaces_bfd(self, x, parameter='bfd'):
        if x in self.nxos_hsrp_interfaces_valid_bfd:
            return
        source_class = self._classname
        source_method = 'verify_nxos_hsrp_interfaces_bfd'
        expectation = ','.join(self.nxos_hsrp_interfaces_valid_bfd)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_hsrp_interfaces_interface(self, x, parameter='interface'):
        if self.is_ethernet_interface(x):
            return
        if self.is_ethernet_subinterface(x):
            return
        if self.is_port_channel_interface(x):
            return
        if self.is_vlan_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_nxos_hsrp_interfaces_interface'
        expectation = ','.join(sorted(self.nxos_hsrp_interfaces_valid_interface_examples))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_hsrp_interfaces_state(self, x, parameter='state'):
        if x in self.nxos_hsrp_interfaces_valid_state:
            return
        source_class = self._classname
        source_method = 'verify_nxos_hsrp_interfaces_state'
        expectation = ','.join(self.nxos_hsrp_interfaces_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def bfd(self):
        return self.properties['bfd']
    @bfd.setter
    def bfd(self, x):
        parameter = 'bfd'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_interfaces_bfd(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_interfaces_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_hsrp_interfaces_state(x, parameter)
        self.properties[parameter] = x

