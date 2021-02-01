# NxosBfdInterfaces() - cisco/nxos/nxos_bfd_interfaces.py
our_version = 102

from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_bfd_interfaces.py

Description:

NxosBfdInterfaces() generates Ansible Playbook tasks conformant with nxos_bfd_interfaces
which can be fed to Playbook().add_task()

Properties:
    bfd     - Enable/Disable Bidirectional Forwarding Detection (BFD) on the interface
                Valid values: enable, disable
    echo    - Enable/Disable BFD Echo functionality on the interface
                Valid values: enable, disable
    name    - Full name of interface, e.g. Ethernet1/1, port-channel10
    state   - see self.__init__().nxos_bfd_interfaces_valid_state

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_bfd_interfaces.py

'''

class NxosBfdInterfaces(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bfd_interfaces'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('bfd')
        self.properties_set.add('echo')
        self.properties_set.add('nane')
        self.properties_set.add('state')

        self.nxos_bfd_interfaces_valid_bfd = ['enable', 'disable']
        self.nxos_bfd_interfaces_valid_echo = ['enable', 'disable']
        self.nxos_bfd_interfaces_valid_state = ['merged', 'replaced', 'overridden', 'deleted', 'gathered', 'rendered', 'parsed']

        self.init_properties()

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
        populate and append dict() to self.ansible_task[self.ansible_module]['config']
        '''
        self.final_verification()

        d = dict()
        d['name'] = self.name
        if self.bfd != None:
            d['bfd'] = self.bfd
        if self.echo != None:
            d['echo'] = self.echo
        self.ansible_task = dict()
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['config'] = list()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module]['config'].append(d.copy())
        self.ansible_task[self.ansible_module]['state'] = self.state

        #self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None

    def verify_nxos_bfd_interfaces_state(self, x, parameter='state'):
        if x in self.nxos_bfd_interfaces_valid_state:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_interfaces_state'
        expectation = ','.join(self.nxos_bfd_interfaces_valid_state)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bfd_interfaces_bfd(self, x, parameter='bfd'):
        if x in self.nxos_bfd_interfaces_valid_bfd:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_interfaces_bfd'
        expectation = ','.join(self.nxos_bfd_interfaces_valid_bfd)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bfd_interfaces_echo(self, x, parameter='echo'):
        if x in self.nxos_bfd_interfaces_valid_echo:
            return
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_interfaces_echo'
        expectation = ','.join(self.nxos_bfd_interfaces_valid_echo)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def bfd(self):
        return self.properties['bfd']
    @bfd.setter
    def bfd(self, x):
        parameter = 'bfd'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_interfaces_bfd(x, parameter)
        self.properties[parameter] = x

    @property
    def echo(self):
        return self.properties['echo']
    @echo.setter
    def echo(self, x):
        parameter = 'echo'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_interfaces_echo(x, parameter)
        self.properties[parameter] = x

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.verify_interface(x, parameter) # inherited from AnsCommon()
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_interfaces_state(x, parameter)
        self.properties[parameter] = x
