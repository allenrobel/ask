# NxosVpcInterface() - cisco/nxos/nxos_vpc_interface.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
==========================================
NxosVpcInterface() - nxos_vpc_interface.py
==========================================

Description
-----------
NxosVpcInterface() generates Ansible task instances conformant with its identically-named Ansible module.
These task instances can then be passed to Playbook().add_task()

Example usage
-------------
unit_test/cisco/nxos/unit_test_nxos_vpc_interface.py

Properties
----------

- Property names are identical to the nxos_vpc_interface module.

Properties
----------

- Property names are identical to the cisco.nxos.nxos_vpc_interface module.

========================    ===========
Property                    Description
========================    ===========
peer_link                   Set to true/false for peer link config on associated portchannel.::

                                - Type: str()
                                - Valid values: no, yes
                                - Example: task.peer_link = 'no'
portchannel                 Group number of the portchannel that will be configured::

                                - Type: str()
                                - Valid values: int() range: 1-4096
                                - Example: task.portchannel = 10
                                - Required
state                       The state of the configuration after module completion. The state overridden would 
                            override the configuration of all the VLANs on the device (including VLAN 1) with
                            the provided configuration in the task. Use caution with this state.::

                                - Type: str()
                                - Valid values: deleted, gathered, merged, overridden, parsed, rendered, replaced
                                - Example: task.state = 'merged'

vpc                         VPC group/id that will be configured on associated portchannel::

                                - Type: int()
                                - Valid values: int() range: 1-4096
                                - Example: task.vpc = 10
========================    ===========
'''

class NxosVpcInterface(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vpc_interface'
        super().__init__(ansible_module, task_log)
        self._version = our_version
        self.class_name = __class__.__name__

        self.portchannel_min = 1
        self.portchannel_max = 4096

        self.vpc_min = 1
        self.vpc_max = 4096

        self.nxos_vpc_interface_valid_state = ['present', 'absent']

        self.properties_set = set()
        self.properties_set.add('peer_link')
        self.properties_set.add('portchannel')
        self.properties_set.add('state')
        self.properties_set.add('vpc')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.portchannel == None:
            self.task_log.error('exiting. call instance.portchannel before calling instance.update()')
            exit(1)
        if self.peer_link != None and self.vpc != None:
            self.task_log.error('exiting. instance.peer_link ({}) and instance.vpc ({}) are mutually exclusive. Unset one or the other.'.format(self.peer_link, self.vpc))
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

    def verify_nxos_vpc_interface_port_channel(self, x, parameter='port_channel'):
        source_class = self.class_name
        range_min = self.portchannel_min
        range_max = self.portchannel_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    def verify_nxos_vpc_interface_state(self, x, parameter='state'):
        verify_set = self.nxos_vpc_interface_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_vpc_interface_state'
        expectation = ','.join(self.verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_vpc_interface_vpc(self, x, parameter='vpc'):
        source_class = self.class_name
        range_min = self.vpc_min
        range_max = self.vpc_max
        self.verify_integer_range(x, range_min, range_max, source_class, parameter)

    @property
    def peer_link(self):
        return self.properties['peer_link']
    @peer_link.setter
    def peer_link(self, x):
        parameter = 'peer_link'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def portchannel(self):
        return self.properties['portchannel']
    @portchannel.setter
    def portchannel(self, x):
        parameter = 'portchannel'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_interface_port_channel(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_interface_state(x, parameter)
        self.properties[parameter] = x

    @property
    def vpc(self):
        return self.properties['vpc']
    @vpc.setter
    def vpc(self, x):
        parameter = 'vpc'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_vpc_interface_vpc(x, parameter)
        self.properties[parameter] = x
