# NxosLacpInterfaces() - cisco/nxos/nxos_lacp_interfaces.py
our_version = 103
import re
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_lacp_interfaces.py

Description:

NxosLacpInterfaces() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_lacp_interfaces
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_lacp_interfaces.py

Properties:
    graceful            -   port-channel lacp graceful convergence.
                            Disable this only with lacp ports connected to Non-Nexus peer.
                            Disabling this with Nexus peer can lead to port suspension.
                            Valid values: no, yes
    min                 -   Port-channel min members
    max                 -   Port-channel max members
    mode                -   LACP mode. Applicable only for Port-channel
                            Valid values: delay
    name                -   Name of the interface
    port_priority       -   LACP port priority for the interface. Applicable only for Ethernet
                            Valid values: int() range: 1-65535.
    rate                -   Rate at which PDUs are sent by LACP. Applicable only for Ethernet.
                            At fast rate LACP is transmitted once every 1 second. At normal rate
                            LACP is transmitted every 30 seconds after the link is bundled.
                            Valid values: fast, normal
    suspend_individual  -   port-channel lacp state. Disabling this will cause lacp
                            to put the port to individual state and not suspend the
                            port in case it does not get LACP BPDU from the peer ports
                            in the port-channel.
                            Valid values: no, yes
    state               -   The state of the configuration after module completion
                            Valid values: deleted, gathered, merged, overridden, parsed, rendered, replaced
    task_name           -   Freeform name for the task
    vpc                 -   Enable lacp convergence for vPC port channels
                            Valid values: no, yes
'''

class NxosLacpInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_lacp_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.re_lacp_interface = re.compile('^port-channel\d+$')

        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['state'] = None
        self.ansible_task[self.ansible_module]['config'] = list()

        self.nxos_lacp_interfaces_valid_state = set()
        self.nxos_lacp_interfaces_valid_state.add('deleted')
        self.nxos_lacp_interfaces_valid_state.add('gathered')
        self.nxos_lacp_interfaces_valid_state.add('merged')
        self.nxos_lacp_interfaces_valid_state.add('overridden')
        self.nxos_lacp_interfaces_valid_state.add('parsed')
        self.nxos_lacp_interfaces_valid_state.add('rendered')
        self.nxos_lacp_interfaces_valid_state.add('replaced')

        self.nxos_lacp_interfaces_valid_mode = set()
        self.nxos_lacp_interfaces_valid_mode.add('delay')

        self.nxos_lacp_interfaces_valid_rate = set()
        self.nxos_lacp_interfaces_valid_rate.add('fast')
        self.nxos_lacp_interfaces_valid_rate.add('normal')

        self.properties_set = set()
        self.properties_set.add('convergence')
        self.properties_set.add('graceful')
        self.properties_set.add('links')
        self.properties_set.add('min')
        self.properties_set.add('max')
        self.properties_set.add('mode')
        self.properties_set.add('name')
        self.properties_set.add('port_priority')
        self.properties_set.add('rate')
        self.properties_set.add('suspend_individual')
        self.properties_set.add('state')
        self.properties_set.add('vpc')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        if self.state == None:
            self.task_log.error('exiting. call instance.state before calling instance.update()')
            exit(1)
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.update()')
            exit(1)
        if self.graceful != None and self.is_ethernet_interface(self.name):
            self.task_log.error('exiting. instance.graceful is not applicable when instance.name is ethernet. Got instance.name: {}'.format(self.name))
            exit(1) 
        if self.vpc != None and self.is_ethernet_interface(self.name):
            self.task_log.error('exiting. instance.vpc is not applicable when instance.name is ethernet. Got instance.name: {}'.format(self.name))
            exit(1)
        if self.mode != None and self.is_ethernet_interface(self.name):
            self.task_log.error('exiting. instance.mode is not applicable when instance.name is ethernet. Got instance.name: {}'.format(self.name))
            exit(1)
        if self.rate != None and self.is_port_channel_interface(self.name):
            self.task_log.error('exiting. instance.rate is not applicable when instance.name is port-channel. Got instance.name: {}'.format(self.name))
            exit(1)
        if self.port_priority != None and self.is_port_channel_interface(self.name):
            self.task_log.error('exiting. instance.port_priority is not applicable when instance.name is port-channel. Got instance.name: {}'.format(self.name))
            exit(1)
        if self.suspend_individual != None and self.is_ethernet_interface(self.name):
            self.task_log.error('exiting. instance.suspend_individual is not applicable when instance.name is ethernet. Got instance.name: {}'.format(self.name))
            exit(1)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        convergence = None
        links = None

        d = dict()
        d['name'] = self.name
        if self.graceful != None:
            if convergence == None:
                convergence = dict()
            convergence['graceful'] = self.graceful
        if self.vpc != None:
            if convergence == None:
                convergence = dict()
            convergence['vpc'] = self.vpc
        if convergence != None:
            d['convergence'] = deepcopy(convergence)
            convergence = None

        if self.min != None:
            if links == None:
                links = dict()
            links['min'] = self.min
        if self.max != None:
            if links == None:
                links = dict()
            links['max'] = self.max
        if links != None:
            d['links'] = deepcopy(links)
            links = None

        if self.mode != None:
            d['mode'] = self.mode

        if self.rate != None:
            d['rate'] = self.rate

        if self.port_priority != None:
            d['port_priority'] = self.port_priority

        if self.suspend_individual != None:
            d['suspend_individual'] = self.suspend_individual
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['config'].append(deepcopy(d))
        self.ansible_task[self.ansible_module]['state'] = self.state

        self.init_properties()


    def verify_lacp_mode(self, x, parameter='mode'):
        verify_set = self.nxos_lacp_interfaces_valid_mode
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_lacp_mode'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lacp_interface(self, x, parameter='name'):
        if self.re_lacp_interface.search(x):
            return
        source_class = self.class_name
        source_method = 'verify_lacp_interface'
        expectation = 'valid LACP interface name e.g.: port-channel1000'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lacp_max(self, x, parameter='max'):
        expectation = 'integer in range 1-32'
        source_class = self.class_name
        source_method = 'verify_lacp_max'
        try:
            foo = int(x)
        except:
            self.fail(source_class, source_method, x, parameter, expectation)
        if foo < 1:
            self.fail(source_class, source_method, x, parameter, expectation)
        if foo > 32:
            self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lacp_min(self, x, parameter='max'):
        expectation = 'integer in range 1-32'
        source_class = self.class_name
        source_method = 'verify_lacp_min'
        try:
            foo = int(x)
        except:
            self.fail(source_class, source_method, x, parameter, expectation)
        if foo < 1:
            self.fail(source_class, source_method, x, parameter, expectation)
        if foo > 32:
            self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lacp_member(self, x, parameter='member'):
        if self.is_ethernet_interface(x):
            return
        source_class = self.class_name
        source_method = 'verify_lacp_member'
        expectation = 'valid LACP member interface name e.g.: Ethernet1/1, Ethernet1/2/1'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lacp_member_or_lacp_interface(self, x, parameter='member'):
        if self.is_ethernet_interface(x):
            return
        if self.re_lacp_interface.search(x):
            return
        source_class = self.class_name
        source_method = 'verify_lacp_member_or_lacp_interface'
        expectation = 'valid LACP member interface name or LACP interface name e.g.: Ethernet1/1, port-channel42'
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lacp_rate(self, x, parameter='rate'):
        verify_set = self.nxos_lacp_interfaces_valid_rate
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_lacp_rate'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lacp_port_priority(self, x, parameter='port_priority'):
        expectation = 'integer in range 1-65535'
        source_class = self.class_name
        source_method = 'verify_lacp_port_priority'
        try:
            foo = int(x)
        except:
            self.fail(source_class, source_method, x, parameter, expectation)
        if foo < 1:
            self.fail(source_class, source_method, x, parameter, expectation)
        if foo > 65535:
            self.fail(source_class, source_method, x, parameter, expectation)

    def verify_lacp_state(self, x, parameter='state'):
        verify_set = self.nxos_lacp_interfaces_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'verify_lacp_state'
        expectation = ','.join(sorted(verify_set))
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def graceful(self):
        return self.properties['graceful']
    @graceful.setter
    def graceful(self, x):
        parameter = 'graceful'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def max(self):
        return self.properties['max']
    @max.setter
    def max(self, x):
        parameter = 'max'
        if self.set_none(x, parameter):
            return
        self.verify_lacp_max(x, parameter)
        self.properties[parameter] = x

    @property
    def min(self):
        return self.properties['min']
    @min.setter
    def min(self, x):
        parameter = 'min'
        if self.set_none(x, parameter):
            return
        self.verify_lacp_min(x, parameter)
        self.properties[parameter] = x

    @property
    def mode(self):
        return self.properties['mode']
    @mode.setter
    def mode(self, x):
        parameter = 'mode'
        if self.set_none(x, parameter):
            return
        self.verify_lacp_mode(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        '''
        '''
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_lacp_member_or_lacp_interface(x, parameter)
        self.properties['name'] = x

    @property
    def port_priority(self):
        return self.properties['port_priority']
    @port_priority.setter
    def port_priority(self, x):
        parameter = 'port_priority'
        if self.set_none(x, parameter):
            return
        self.verify_lacp_port_priority(x, parameter)
        self.properties[parameter] = x

    @property
    def rate(self):
        return self.properties['rate']
    @rate.setter
    def rate(self, x):
        parameter = 'rate'
        if self.set_none(x, parameter):
            return
        self.verify_lacp_rate(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_lacp_state(x, parameter)
        self.properties[parameter] = x

    @property
    def suspend_individual(self):
        return self.properties['suspend_individual']
    @suspend_individual.setter
    def suspend_individual(self, x):
        parameter = 'suspend_individual'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

    @property
    def vpc(self):
        return self.properties['vpc']
    @vpc.setter
    def vpc(self, x):
        parameter = 'vpc'
        if self.set_none(x, parameter):
            return
        self.verify_toggle(x, parameter)
        self.properties[parameter] = x

