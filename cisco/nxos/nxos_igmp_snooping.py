# NxosIgmpSnooping() - cisco/nxos/nxos_igmp_snooping.py
our_version = 104
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosIgmpSnooping()
**************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosIgmpSnooping() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_igmp_snooping
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_igmp_snooping <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_igmp_snooping_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_igmp_snooping.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_igmp_snooping.py>`_


|

================================    ==============================================
Property                            Description
================================    ==============================================
group_timeout                       Group membership timeout value for all VLANs 
                                    on the remote device::

                                        - Type: int() or str()
                                        - Units: minutes
                                        - Valid values:
                                            - int() range 1-10080 (minutes)
                                            - never : Never expire ports from group membership
                                            - default : Remove explicit group-timeout config
                                        Examples:
                                            task.group_timeout = 20
                                            task.group_timeout = 'never'
                                            task.group_timeout = 'default'

link_local_grp_supp                 Global link-local groups suppression::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.link_local_grp_supp = True

report_supp                         Global IGMPv1/IGMPv2 Report Suppression::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.report_supp = False

snooping                            Enables/disables IGMP snooping on the switch::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.snooping = False

state                               Desired state after task has run::

                                        - Type: str()
                                        - Valid values:
                                            - default
                                            - present
                                        - Example:
                                            task.state = 'default'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Example:
                                            - task.task_name = 'enable lacp'

v3_report_supp                      Global IGMPv3 Report Suppression and Proxy Reporting::

                                        - Type: bool()
                                        - Valid values: False, True
                                        Examples:
                                            task.v3_report_supp = False
                                        
================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosIgmpSnooping(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_igmp_snooping'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('group_timeout')
        self.properties_set.add('link_local_grp_supp')
        self.properties_set.add('report_supp')
        self.properties_set.add('snooping')
        self.properties_set.add('state')
        self.properties_set.add('v3_report_supp')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.nxos_igmp_snooping_valid_state = set()
        self.nxos_igmp_snooping_valid_state.add('default')
        self.nxos_igmp_snooping_valid_state.add('present')

        self.nxos_igmp_snooping_valid_group_timeout = set()
        self.nxos_igmp_snooping_valid_group_timeout.add('default')
        self.nxos_igmp_snooping_valid_group_timeout.add('never')
        self.nxos_igmp_snooping_min_group_timeout = 1
        self.nxos_igmp_snooping_max_group_timeout = 10080

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for item in self.properties_set:
            self.properties[item] = None

    def final_verification(self):
        if self.snooping == 'no' and self.group_timeout != None:
            self.task_log.error('exiting. instance.group_timeout cannot be set if self.snooping == no')
            exit(1)
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

    def nxos_igmp_snooping_verify_group_timeout(self, x, parameter='group_timeout'):
        verify_set = self.nxos_igmp_snooping_valid_group_timeout
        if x in verify_set:
            return
        if self.is_within_integer_range(x,
            self.nxos_igmp_snooping_min_group_timeout,
            self.nxos_igmp_snooping_max_group_timeout
            ):
            return
        source_class = self.class_name
        source_method = 'nxos_igmp_snooping_verify_group_timeout'
        expectation = ','.join(self.verify_set)
        expectation += ' , or int() within range {} - {}'.format(
            self.nxos_igmp_snooping_min_group_timeout,
            self.nxos_igmp_snooping_max_group_timeout)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_igmp_snooping_verify_state(self, x, parameter='state'):
        verify_set = self.nxos_igmp_snooping_valid_state
        if x in verify_set:
            return
        source_class = self.class_name
        source_method = 'nxos_igmp_snooping_verify_state'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    @property
    def group_timeout(self):
        return self.properties['group_timeout']
    @group_timeout.setter
    def group_timeout(self, x):
        parameter = 'group_timeout'
        if self.set_none(x, parameter):
            return
        self.nxos_igmp_snooping_verify_group_timeout(x, parameter)
        self.properties[parameter] = x

    @property
    def link_local_grp_supp(self):
        return self.properties['link_local_grp_supp']
    @link_local_grp_supp.setter
    def link_local_grp_supp(self, x):
        parameter = 'link_local_grp_supp'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def report_supp(self):
        return self.properties['report_supp']
    @report_supp.setter
    def report_supp(self, x):
        parameter = 'report_supp'
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
        self.nxos_igmp_snooping_verify_state(x, parameter)
        self.properties[parameter] = x

    @property
    def v3_report_supp(self):
        return self.properties['v3_report_supp']
    @v3_report_supp.setter
    def v3_report_supp(self, x):
        parameter = 'v3_report_supp'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x
