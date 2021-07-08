# NxosVtpDomain() - cisco/nxos/nxos_vtp_domain.py
our_version = 100
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosVtpDomain()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
100

ScriptKit Synopsis
------------------
- NxosVtpDomain() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_vtp_domain
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_vtp_domain <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_vtp_domain_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_vtp_domain.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_vtp_domain.py>`_


|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task::

                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See ScriptKit Example above 

========================    ============================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
domain                              VTP domain name::

                                        - Type: str()
                                        - Examples:
                                            task.domain = 'domain1'
                                        - Required

task_name                           Name of the task. Ansible will display this
                                    when the playbook is run::

                                        - Type: str()
                                        - Examples:
                                            - task.task_name = 'my task'

================================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosVtpDomain(Task):
    '''
    Example usage:

    '''
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_vtp_domain'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()

        self.properties_set = set()
        self.properties_set.add('domain')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.mandatory_properties = set()
        self.mandatory_properties.add('domain')

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        for p in self.mandatory_properties:
            if self.properties[p] == None:
                self.task_log.error('exiting. instance.{} must be set before calling instance.commit()'.format(p))
                exit(1)

    def commit(self):
        self.update()
    def update(self):
        '''
        call final_verification()
        update ansible_task dict()
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
    def domain(self):
        return self.properties['domain']
    @domain.setter
    def domain(self, x):
        parameter = 'domain'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
