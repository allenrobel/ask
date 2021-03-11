# NxosIgmp() - cisco/nxos/nxos_igmp.py
our_version = 102
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosIgmp()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosIgmp() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_igmp
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_igmp <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_igmp_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_igmp.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_igmp.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
enforce_rtr_alert                   Enables or disables the enforce router alert 
                                    option check for IGMPv2 and IGMPv3 packets::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.enforce_rtr_alert = False

flush_routes                        Removes routes when the IGMP process is 
                                    restarted. By default, routes are not 
                                    flushed::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.flush_routes = True

restart                             Restarts the igmp process (using an exec
                                    config command)::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.restart = True

snooping                            Enables/disables IGMP snooping on the switch::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.snooping = False

state                               Desired state after task has run::

                                        - Type: str()
                                        - Valid values:
                                            - absent
                                            - present
                                        - Example:
                                            task.state = 'present'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'enable lacp'
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosIgmp(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_igmp'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('enforce_rtr_alert')
        self.properties_set.add('flush_routes')
        self.properties_set.add('restart')
        self.properties_set.add('state')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_igmp_valid_state = set()
        self.nxos_igmp_valid_state.add('absent')
        self.nxos_igmp_valid_state.add('present')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for item in self.properties_set:
            self.properties[item] = None

    def final_verification(self):
        if self.state == None:
            self.state = 'present'

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

    def nxos_igmp_verify_state(self, x, parameter='state'):
        verify_set = self.nxos_igmp_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_igmp_verify_state'
        expectation = ','.join(self.verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def enforce_rtr_alert(self):
        return self.properties['enforce_rtr_alert']
    @enforce_rtr_alert.setter
    def enforce_rtr_alert(self, x):
        parameter = 'enforce_rtr_alert'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def flush_routes(self):
        return self.properties['flush_routes']
    @flush_routes.setter
    def flush_routes(self, x):
        parameter = 'flush_routes'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def restart(self):
        return self.properties['restart']
    @enforce_rtr_alert.setter
    def restart(self, x):
        parameter = 'restart'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def state(self):
        return self.properties['state']
    @state.setter
    def state(self, x):
        parameter = 'state'
        if self.set_none(x, parameter):
            return
        self.nxos_igmp_verify_state(x, parameter)
        self.properties[parameter] = x
