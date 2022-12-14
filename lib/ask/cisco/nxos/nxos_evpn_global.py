# NxosEvpnGlobal() - cisco/nxos/nxos_evpn_global.py
our_version = 107
from copy import deepcopy
from ask.common.task import Task
'''
**************************************
NxosEvpnGlobal()
**************************************

.. contents::
   :local:
   :depth: 1

Version
-------
107

ScriptKit Synopsis
------------------
- NxosEvpnGlobal() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_evpn_global
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_evpn_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_evpn_global_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_evpn_global.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_evpn_global.py>`_


|

========================    ============================================
Method                      Description
========================    ============================================
commit()                    Perform final verification and commit the 
                            current task::
                                - Type: function()
                                - Alias: update()
                                - Example:
                                    See also: ScriptKit Example above 

                                    #!/usr/bin/env python3
                                    # enable nv overlay evpn
                                    from ask.common.playbook import Playbook
                                    from ask.common.log import Log
                                    from ask.cisco.nxos.nxos_evpn_global import NxosEvpnGlobal

                                    log_level_console = 'INFO'
                                    log_level_file = 'DEBUG'
                                    log = Log('my_log', log_level_console, log_level_file)

                                    pb = Playbook(log)
                                    pb.profile_nxos()
                                    pb.ansible_password = 'mypassword'
                                    pb.name = 'nxos_evpn_global example'
                                    pb.add_host('dc-101')
                                    pb.file = '/tmp/nxos_evpn_global.yaml'

                                    task = NxosEvpnGlobal(log)
                                    task.nv_overlay_evpn = True
                                    task.task_name = 'configure nv overlay evpn'
                                    task.commit()

                                    pb.add_task(task)
                                    pb.append_playbook()
                                    pb.write_playbook()
                                    log.info('wrote {}'.format(pb.file))

                                - Resulting tasks:

                                    hosts: dc-101
                                    name: nxos_evpn_global example
                                    tasks:
                                    -   cisco.nxos.nxos_evpn_global:
                                            nv_overlay_evpn: true
                                        name: configure nv overlay evpn

                                - Resulting config:

                                    nv overlay evpn

========================    ============================================

|

================================    ==============================================
Property                            Description
================================    ==============================================
nv_overlay_evpn                     Enable ``True`` / Disable ``False`` EVPN 
                                    control plane::

                                        - Type: bool()
                                        - Valid values: False, True
                                        - Examples:
                                            task.nv_overlay_evpn = True
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
        if self.nv_overlay_evpn == None:
            self.task_log.error('exiting. instance.nv_overlay_evpn must be set before calling instance.commit()')
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
    def nv_overlay_evpn(self):
        return self.properties['nv_overlay_evpn']
    @nv_overlay_evpn.setter
    def nv_overlay_evpn(self, x):
        parameter = 'nv_overlay_evpn'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

