# NxosVpcInterface() - cisco/nxos/nxos_vpc_interface.py
our_version = 109
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosVpcInterface()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosVpcInterface() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_vpc_interface
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vpc_interface <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vpc_interface_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vpc_interface.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vpc_interface.py>`_


|

========================    ==============================================
Property                    Description
========================    ==============================================
peer_link                   Set to True (enable) or False (disable) to
                            configure VPC Peer Link on the associated
                            portchannel interface::

                                - Type: bool()
                                - Valid values:
                                    - False
                                    - True
                                - Example:
                                    task.peer_link = False

portchannel                 Group number of the portchannel that will be
                            configured::

                                - Type: int()
                                - Valid values:
                                    - range: 1-4096
                                - Example:
                                    task.portchannel = 10
                                - Required


vpc                         VPC group/id that will be configured on associated portchannel::

                                - Type: int()
                                - Valid values:
                                    - range: 1-4096
                                - Example:
                                    task.vpc = 10

state                       Desired state after task completion::

                                - Type: str()
                                - Valid values:
                                    - absent
                                    - present
                                - Example:
                                    task.state = 'present'
                                - Required

task_name                   Name of the task. Ansible will display this
                            when the playbook is run::

                                - Type: str()
                                - Example:
                                    - task.task_name = 'my task'
                                        
========================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

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
        if self.portchannel == None:
            self.task_log.error('exiting. call instance.portchannel before calling instance.update()')
            exit(1)
        if self.peer_link != None and self.vpc != None:
            self.task_log.error('exiting. instance.peer_link ({}) and instance.vpc ({}) are mutually exclusive. Unset one or the other.'.format(self.peer_link, self.vpc))
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
        self.verify_boolean(x, parameter)
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
