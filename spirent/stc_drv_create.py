# StcDrvCreate() - spirent/stc_drv_create.py
our_version = 104
from copy import deepcopy
from ask.common.task import Task
'''
**************************************************
StcDrvCreate() - spirent/stc_drv_create.py
**************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcDrvCreate() creates a Dynamic Result View (DRV) on a 
set of Spirent ports.

It generates Ansible task instances conformant with Spirent's
Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run the playbook generated by StcDrvCreate(),
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_drv_create.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_drv_create.py>`_

Properties
----------

====================================    ==================================================
Property                                Description
====================================    ==================================================
disable_auto_grouping                   Disable grouping of results::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Default: True
                                            - Spirent name: DisableAutoGrouping
                                            - Examples:
                                                - task.disable_auto_grouping = True

drv_name                                Name of the Dynamic Result View::

                                            - Type: str()
                                            - Spirent name: ['DynamicResultView']['name']
                                            - Default: "Dropped Frames DRV"
                                            - Examples:
                                                - task.drv_name = 'RxResults'

from_objects                            The set of Spirent objects to query for results::

                                            - Type: str()
                                            - Default: ref:/project/port
                                            - Spirent name: FromObjects
                                            - Examples:
                                                - task.from_objects = 'ref:/project/port'

limit_size                              Limit the size of the collected results to X entries::

                                            - Type: int()
                                            - Spirent name: LimitSize
                                            - Default: 20000
                                            - Examples:
                                                - task.limit_size = 15000

reset_existing                          Reset any existing results::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Default: False
                                            - Spirent name: ResetExisting
                                            - Examples:
                                                - task.reset_existing = True


select_properties                       Add one or more property filters which determine what
                                        results are collected. This is additive, so each time
                                        it is called, the filter is added to the filters that 
                                        have previously been added.::

                                            - Type: str()
                                            - Spirent name: SelectProperties
                                            - Default:  If select_properties is not set, the following 
                                                        results are collected:
                                                - StreamBlock.DroppedFrameCount
                                                - StreamBlock.DroppedFrameDuration
                                                - StreamBlock.Name
                                                - StreamBlock.RxSigFrameRate

                                            - Example (collect results for these three filters)
                                                - task.select_properties = 'StreamBlock.ActualRxPortName'
                                                - task.select_properties = 'StreamBlock.RxSigFrameCount'
                                                - task.select_properties = 'StreamBlock.RxSigFrameRate'
                                            - Example filters
                                                - Port.Name
                                                - StreamBlock.StreamId
                                                - StreamBlock.ActualRxPortName
                                                - StreamBlock.DroppedFrameCount
                                                - StreamBlock.DroppedFrameDuration
                                                - StreamBlock.DuplicateFrameCount
                                                - StreamBlock.FrameConfig.ipv4:IPv4.1.sourceAddr
                                                - StreamBlock.FrameConfig.ipv4:IPv4.1.destAddr
                                                - StreamBlock.FrameConfig.ethernet:EthernetII.1.srcMac
                                                - StreamBlock.FrameConfig.ethernet:EthernetII.vlans.Vlan.1.id
                                                - StreamBlock.IsExpected
                                                - StreamBlock.AvgLatency
                                                - StreamBlock.MaxLatency
                                                - StreamBlock.MinLatency
                                                - StreamBlock.Name
                                                - StreamBlock.RxSigFrameCount
                                                - StreamBlock.RxSigFrameRate
                                                - StreamBlock.TxFrameCount
                                                - StreamBlock.TxFrameRate

sort_by                                 Filter by which to sort the result.::

                                            - Type: str()
                                            - Spirent name: SortBy
                                            - Default: results are not sorted
                                            - Example
                                                - task.sort_by = 'StreamBlock.RxSigFrameCount'

sort_direction                          Direction in which to sort the results.::

                                            - Type: str()
                                            - Spirent name: none
                                            - Valid values: ASCENDING, DESCENDING
                                            - Default: ASCENDING
                                            - Example
                                                - task.sort_direction = 'DESCENDING'

where_conditions                        Determines if a given result should be added based on
                                        the result value. Conditions are composed of the following,
                                        may be joined with AND/OR, and are enclosed in curly-brackets.::

                                            select_property [ > | < | >= | <= | != | == ] <value>

                                            Example:

                                            StreamBlock.DroppedFrameCount > 0

                                            - Type: str()
                                            - Spirent name: WhereConditions
                                            - Default: No conditions are used to filter results
                                            - Example:
                                                - task.where_conditions = "{StreamBlock.DroppedFrameCount > 0 AND StreamBlock.IsExpected = 1}"

====================================    ==================================================

'''
class StcDrvCreate(Task):
    def __init__(self, task_log):
        ansible_module = 'stc'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.stc_drv_create_valid_sort_direction = set()
        self.stc_drv_create_valid_sort_direction.add('ASCENDING')
        self.stc_drv_create_valid_sort_direction.add('DESCENDING')

        self.init_properties()
        self.init_presentation_result_query()

    def init_properties(self):
        self.properties = dict()
        self.properties['drv_name']         = None
        self.properties['reset_existing']   = None
        self.properties['sort_direction']   = None

    def init_presentation_result_query(self):
        self.select_properties_set = set()
        self.presentation_result_query = dict()
        self.presentation_result_query['DisableAutoGrouping'] = True
        self.presentation_result_query['FromObjects'] = None
        self.presentation_result_query['LimitSize'] = None
        self.presentation_result_query['SelectProperties'] = None
        self.presentation_result_query['SortBy'] = None
        self.presentation_result_query['WhereConditions'] = None

        self.valid_select_properties = set()
        self.valid_select_properties.add('StreamBlock.StreamId')
        self.valid_select_properties.add('StreamBlock.Name')
        self.valid_select_properties.add('Port.Name')
        self.valid_select_properties.add('StreamBlock.ActualRxPortName')
        self.valid_select_properties.add('StreamBlock.FrameConfig.ipv4:IPv4.1.sourceAddr')
        self.valid_select_properties.add('StreamBlock.FrameConfig.ipv4:IPv4.1.destAddr')
        self.valid_select_properties.add('StreamBlock.FrameConfig.ethernet:EthernetII.1.srcMac')
        self.valid_select_properties.add('StreamBlock.FrameConfig.ethernet:EthernetII.vlans.Vlan.1.id')
        self.valid_select_properties.add('StreamBlock.TxFrameCount')
        self.valid_select_properties.add('StreamBlock.TxFrameRate')
        self.valid_select_properties.add('StreamBlock.RxSigFrameCount')
        self.valid_select_properties.add('StreamBlock.RxSigFrameRate')
        self.valid_select_properties.add('StreamBlock.DuplicateFrameCount')
        self.valid_select_properties.add('StreamBlock.DroppedFrameCount')
        self.valid_select_properties.add('StreamBlock.DroppedFrameDuration')
        self.valid_select_properties.add('StreamBlock.MinLatency')
        self.valid_select_properties.add('StreamBlock.MaxLatency')
        self.valid_select_properties.add('StreamBlock.AvgLatency')
        self.valid_select_properties.add('StreamBlock.IsExpected')

    def verify_stc_drv_create_select_properties(self, x, parameter='select_properties'):
        verify_set = self.valid_select_properties
        if x not in verify_set:
            parameter = 'select_properties'
            source_class = self.class_name
            source_method = 'verify_stc_drv_create_select_properties'
            expectation = '{}'.format(', '.join(verify_set))
            self.fail(source_class, source_method, x, parameter, expectation)

    def verify_stc_drv_create_sort_by(self, x, parameter='sort_by'):
        verify_set = self.valid_select_properties
        if x not in verify_set:
            source_class = self.class_name
            source_method = 'verify_stc_drv_create_sort_by'
            expectation = '{}'.format(', '.join(verify_set))
            self.fail(source_class, source_method, x, parameter, expectation)

    def verify_stc_drv_create_sort_direction(self, x, parameter='sort_direction'):
        verify_set = self.stc_drv_create_valid_sort_direction
        if x not in verify_set:
            parameter = 'select_properties'
            source_class = self.class_name
            source_method = 'verify_stc_drv_create_sort_direction'
            expectation = '{}'.format(', '.join(verify_set))
            self.fail(source_class, source_method, x, parameter, expectation)

    def final_verification(self):
        if self.reset_existing == None:
            self.reset_existing = False
        if self.drv_name == None:
            self.drv_name = "Dropped Frames DRV"
        if self.disable_auto_grouping == None:
            self.disable_auto_grouping = True
        if self.from_objects == None:
            self.from_objects = 'ref:/project/port'
        if self.limit_size == None:
            self.limit_size = 20000
        if len(self.select_properties_set) == 0:
            self.select_properties_set.add("StreamBlock.Name")
            self.select_properties_set.add("StreamBlock.ActualRxPortName")
            self.select_properties_set.add("StreamBlock.DroppedFrameCount")
            self.select_properties_set.add("StreamBlock.DroppedFrameDuration")
            self.select_properties_set.add("StreamBlock.RxSigFrameRate")
 
        if self.sort_by != None:
            if self.sort_by not in self.select_properties_set:
                self.task_log.error('exiting. instance.sort_by not found in instance.select_properties. Add it before calling instance.update()')
                self.task_log.error('instance.sort_by: {}'.format(self.sort_by))
                self.task_log.error('instance.select_properties: {}'.format(self.select_properties))
                exit(1)

    def add_config(self):
        d = dict()
        d['action'] = 'create'
        d['under'] = 'ref:/project'
        d['reset_existing'] = self.reset_existing
        d['objects'] = list()
        drv = dict()
        drv['DynamicResultView'] = dict()
        drv['DynamicResultView']['name'] = self.drv_name
        drv['DynamicResultView']['PresentationResultQuery'] = dict()
        drv['DynamicResultView']['PresentationResultQuery']['DisableAutoGrouping'] = self.disable_auto_grouping
        drv['DynamicResultView']['PresentationResultQuery']['FromObjects'] = self.from_objects
        drv['DynamicResultView']['PresentationResultQuery']['LimitSize'] = self.limit_size
        drv['DynamicResultView']['PresentationResultQuery']['SelectProperties'] = self.select_properties
        sort_by = self.make_sort_by()
        if sort_by != False:
            drv['DynamicResultView']['PresentationResultQuery']['SortBy'] = sort_by
        if self.where_conditions != None:
            drv['DynamicResultView']['PresentationResultQuery']['WhereConditions'] = self.where_conditions
        d['objects'].append(deepcopy(drv))
        return deepcopy(d)

    def update(self):
        '''
        Call self.final_verification()
        Populate self.ansible_task dict()
        '''
        self.final_verification()
        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = self.add_config()

    def make_sort_by(self):
        '''
        Example: "{StreamBlock.DroppedFrameCount DESCENDING}"
        '''
        if self.sort_by == None:
            return False
        if self.sort_direction == None:
            sort_direction = 'ASCENDING'
        else:
            sort_direction = self.sort_direction
        return "{" + self.sort_by + " " + sort_direction + "}"

    #-----------------------------------------------------------------------
    # stc_module properties
    #-----------------------------------------------------------------------

    @property
    def drv_name(self):
        return self.properties['drv_name']
    @drv_name.setter
    def drv_name(self, x):
        parameter = 'drv_name'
        self.properties[parameter] = x

    @property
    def reset_existing(self):
        return self.properties['reset_existing']
    @reset_existing.setter
    def reset_existing(self, x):
        parameter = 'reset_existing'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    #-----------------------------------------------------------
    # presentation_result_query properties
    #-----------------------------------------------------------
    @property
    def disable_auto_grouping(self):
        return self.presentation_result_query['DisableAutoGrouping']
    @disable_auto_grouping.setter
    def disable_auto_grouping(self, x):
        self.verify_boolean(x)
        parameter = 'DisableAutoGrouping'
        self.presentation_result_query[parameter] = x

    @property
    def from_objects(self):
        return self.presentation_result_query['FromObjects']
    @from_objects.setter
    def from_objects(self, x):
        parameter = 'FromObjects'
        self.presentation_result_query[parameter] = x

    @property
    def limit_size(self):
        return self.presentation_result_query['LimitSize']
    @limit_size.setter
    def limit_size(self, x):
        self.verify_digits(x)
        parameter = 'LimitSize'
        self.presentation_result_query[parameter] = x

    @property
    def select_properties(self):
        return "{}".format(' '.join(sorted(self.select_properties_set)))
    @select_properties.setter
    def select_properties(self, x):
        self.verify_stc_drv_create_select_properties(x)
        self.select_properties_set.add(x)

    @property
    def sort_by(self):
        return self.presentation_result_query['SortBy']
    @sort_by.setter
    def sort_by(self, x):
        parameter = 'SortBy'
        self.verify_stc_drv_create_sort_by(x)
        self.presentation_result_query[parameter] = x

    @property
    def sort_direction(self):
        return self.properties['sort_direction']
    @sort_direction.setter
    def sort_direction(self, x):
        parameter = 'sort_direction'
        self.verify_stc_drv_create_sort_direction(x, parameter)
        self.properties[parameter] = x

    @property
    def where_conditions(self):
        return self.presentation_result_query['WhereConditions']
    @where_conditions.setter
    def where_conditions(self, x):
        parameter = 'WhereConditions'
        self.presentation_result_query[parameter] = x
