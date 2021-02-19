# StcStreamblock() - spirent/stc_streamblock.py
our_version = 105
from copy import deepcopy
from ask.common.task import Task
'''
*****************************************************************************
StcStreamblock() - spirent/stc_streamblock.py
*****************************************************************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
StcStreamblock() facilitates generation of Ansible playbooks to create
Spirent StreamBlocks to send traffic between Spirent emulated devices.

See StcStreamblockBgpRoutes() for creating StreamBlocks to send traffic
between BGP routes.

StcStreamblock() generate Ansible task instances conformant with
Spirent Ansible implementation for their LabServer + TestCenter products.
These task instances can then be passed to Playbook().add_task()

Caveats
-------

1.  The following throws an error.  We are working with Spirent on this:

        action = 'delete'

2.  Spirent Ansible currently does not perform error-checking to 
    ensure that the value of traffic_pattern is appropriate for 
    the defined endpoints.  For example, if traffic_pattern = 'PAIR',
    but the number of source and destination endpoints is unequal,
    Spirent will accept this as a valid configuration (i.e.
    the Playbook will succeed). Later, when the user tries to
    start ArpNd, or tries to start traffic, Spirent will then throw
    an error.

3.  Spirent Ansible currently does not perform error-checking to
    ensure that the "under" property value is appropriate for the
    set of SrcBinding-targets the user has defined.  So, for 
    example, if the user set port_name = 'POD1_TOR2_PORT10', ScriptKit
    will translate this into:

        under: ref:/Port[@Name='POD1_TOR2_PORT10']

    If there are SrcBinding-targets hosted on other ports, for
    this StreamBlock, this will be an invalid configuration.  The
    correct configuration in this case would be for the user NOT
    to set port_name, which would result in the correct:

        under: ref:/project

    Spirent will not detect this invalid configuration and will accept
    the StreamBlock (and configure it).  Later, when the user tries 
    to start ArpNd, and/or start traffic, an error will be thrown.


Ansible Module Documentation
----------------------------

    - `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_

Prerequisites
-------------

    1.  To run playbooks generated by StcStreamBlock()
        `Spirent stc-ansible <https://github.com/Spirent/stc-ansible>`_ 
        and its dependencies (e.g. paramiko) must be installed.

ScriptKit Example
-----------------

    - `unit_test/spirent/unit_test_stc_streamblock.py <https://github.com/allenrobel/ask/blob/main/unit_test/spirent/unit_test_stc_streamblock.py>`_

Properties
----------

====================================    ==================================================
Property                                Description
====================================    ==================================================
action                                  create or delete the StreamBlock::

                                            - Type: str()
                                            - Spirent name: action
                                            - Valid values: create, delete
                                            - Default: create

count                                   Increments Ansible var $item from 1 to count.
                                        This can be used to increment something in the
                                        playbook::

                                            - Type: int()
                                            - Spirent name: count
                                            - Default: 1

load                                    In conjunction with load_unit, determines
                                        the rate at which traffic is sent.::

                                            - Type: int() or float()
                                            - Spirent name: Load
                                            - Examples:
                                                - task.load = 99.2
                                                - task.load = 50000
                                            - See also: load_unit
                                            - Required if action is create

load_unit                               The unit of measure for the traffic rate.
                                        For example, if load_unit is PERCENT_LINE_RATE
                                        and load is 24.4, then the interface speed is
                                        taken into account to determine the actual
                                        rate.  If load_unit is FRAMES_PER_SECOND, and
                                        load is 100, then traffic will be sent at an
                                        absolute rate of 100 packets per second.::

                                            - Type: str()
                                            - Spirent name: LoadUnit
                                            - Valid values:
                                                - BITS_PER_SECOND
                                                - FRAMES_PER_SECOND
                                                - INTER_BURST_GAP
                                                - INTER_BURST_GAP_IN_MILLISECONDS
                                                - INTER_BURST_GAP_IN_NANOSECONDS
                                                - KILOBITS_PER_SECOND
                                                - L2_RATE
                                                - MEGABITS_PER_SECOND
                                                - PERCENT_LINE_RATE
                                            - Examples:
                                                - task.load_unit = 'BITS_PER_SECOND'
                                            - See also: load
                                            - Required if action is create

name                                    Name of the StreamBlock.::

                                            - Type: str()
                                            - Spirent name: Name
                                            - Examples:
                                                - task.name = 'my_streamblock'
                                            - Required

port_name                               The name of the port under which to create
                                        the StreamBlock.  If not set, the StreamBlock
                                        will be created under ref:/project.  If set,
                                        use the name you gave to the port when you
                                        created the port.::

                                            - Type: str()
                                            - Spirent name: under
                                            - Default: ref:/project
                                            - NOTES:

                                            1.  If tx_device is set to a partial device name that
                                                expands to devices that exist on multiple ports,
                                                port_name must NOT be set.  For example, the following
                                                is invalid (assuming a device named Device511 lives on 
                                                MyPort1 and a device named Device512 lives on, say, 
                                                MyPort2.

                                                task.tx_name = 'Device51'
                                                task.tx_type = 'device'
                                                task.tx_selector = 'STARTS_WITH'
                                                task.tx_protocol = 'ipv4'
                                                task.port_name = 'MyPort1'

                                                Spirent Ansible will accept the above without,
                                                error, but it will generate an error later when
                                                you try to start traffic and/or start ArpNd.

                                            Examples:

                                            
                                                task.port_name = 'MyPort5'

                                                The above results in the 'under' property being 
                                                set as follows:

                                                under: ref:/Port[@Name='MyPort5']

                                                task.port_name = None (or, omitting task.port_name)

                                                The above results in the 'under' property being set 
                                                as follows:

                                                under: ref:/project

rx_name                                 The name of the rx entity.  If rx_type is
                                        device, then rx_name should be the name of an
                                        emulated device.  This is used, along with
                                        rx_type, and rx_protocol, to construct the
                                        Spirent DstBinding-targets value::

                                            - Type: str()
                                            - Spirent name: none
                                            - Examples:
                                                - task.rx_name = 'my_rx_device'
                                            - Required if action is create

rx_protocol                             The protocol of the rx entity.  This is used, 
                                        along with rx, and rx_type, to construct
                                        the Spirent DstBinding-targets value::

                                            - Type: str()
                                            - Valid values: ipv4, ipv6
                                            - Spirent name: none
                                            - Examples:
                                                - task.rx_protocol = 'ipv4'
                                            - Required if action is create

rx_type                                 The type of the rx entity.  This currently
                                        allows for a single value: device. This is used, 
                                        along with rx, and rx_protocol, to construct
                                        the Spirent DstBinding-targets value::

                                            - Type: str()
                                            - Valid values: device
                                            - Spirent name: none
                                            - Examples:
                                                - task.rx_type = 'device'
                                            - Required if action is create

rx_selector                             An optional selector that determines how
                                        rx_name is interpreted.::

                                            - Type: str()
                                            - Valid values:
                                              - EQUAL        "=": Selector.equal
                                              - NOT_EQUAL    "!=" Selector.different
                                              - CONTAINS     "~=" Selector.contains
                                              - STARTS_WITH  "^=" Selector.startswith
                                            - DEFAULT: EQUAL
                                            - Examples:

                                            If rx_name is set to "rx_host", then the following hold:

                                            - rx_selector = 'EQUAL'

                                                "rx_host" is selected (single device)

                                            - rx_selector = 'NOT_EQUAL'

                                                Multiple devices would be selected, if their
                                                name (rx_name) does not contain "rx_host" e.g.:

                                                "tx_host"
                                                "rx_host_45"
                                                "foobar_server"

                                            - rx_selector = 'CONTAINS'

                                                Multiple devices would be selected, if their
                                                name (rx_name) contains "rx_host" e.g.:

                                                "my_rx_host"
                                                "rx_host_45"
                                                "rx_host"

                                            - rx_selector = 'STARTS_WITH'

                                                Multiple devices would be selected, if their
                                                name (rx_name) starts with "rx_host" e.g.:

                                                "rx_host_44"
                                                "rx_host_EAST"
                                                "rx_host"

stream_only_generation                  Set to True to use streams rather than VFDs 
                                        (Variable Field Definitions) to generate traffic
                                        between endpoints.::

                                            - Type: bool()
                                            - Valid values: False, True
                                            - Default: True
                                            - Spirent name: EnableStreamOnlyGeneration
                                            - Examples:
                                                - task.stream_only_generation = False

traffic_pattern                         Determines the pattern used between sources
                                        and destinations.::

                                            - Type: str()
                                            - Valid values: BACKBONE, MESH, PAIR
                                            - Spirent name: TrafficPattern
                                            - Required if action is create

tx_name                                 The name of the tx entity.  If tx_type is
                                        device, then tx_name should be the name of an
                                        emulated device.  This is used, along with
                                        tx_type, and tx_protocol, to construct the
                                        Spirent SrcBinding-targets value::

                                            - Type: str()
                                            - Spirent name: none
                                            - Examples:
                                                - task.tx_name = 'my_tx_device'
                                            - Required if action is create

tx_protocol                             The protocol of the tx entity.  This is used, 
                                        along with tx, and tx_type, to construct
                                        the Spirent SrcBinding-targets value::

                                            - Type: str()
                                            - Valid values: ipv4, ipv6
                                            - Spirent name: none
                                            - Examples:
                                                - task.tx_protocol = 'ipv4'
                                            - Required if action is create

tx_selector                             An optional selector that determines how
                                        tx_name is interpreted.::

                                            - Type: str()
                                            - Valid values:
                                              - EQUAL        "=": Selector.equal
                                              - NOT_EQUAL    "!=" Selector.different
                                              - CONTAINS     "~=" Selector.contains
                                              - STARTS_WITH  "^=" Selector.startswith
                                            - DEFAULT: EQUAL
                                            - Examples:

                                            If tx_name is set to "tx_host", then the following hold:

                                            - tx_selector = 'EQUAL'
                                            
                                                "tx_host" is selected (single device)

                                            - tx_selector = 'NOT_EQUAL'
                                            
                                                Multiple devices would be selected, if their
                                                name (tx_name) does not contain "tx_host" e.g.:

                                                "rx_host"
                                                "rx_host_45"
                                                "foobar_server"

                                            - tx_selector = 'CONTAINS'
                                            
                                                Multiple devices would be selected, if their
                                                name (tx_name) contains "tx_host" e.g.:

                                                "my_tx_host"
                                                "tx_host_45"
                                                "tx_host"

                                            - rx_selector = 'STARTS_WITH'
                                            
                                                Multiple devices would be selected, if their
                                                name (tx_name) starts with "tx_host" e.g.:

                                                "tx_host_44"
                                                "tx_host_EAST"
                                                "tx_host"

tx_type                                 The type of the tx entity.  This currently
                                        allows for a single value: device. This is used, 
                                        along with tx, and tx_protocol, to construct
                                        the Spirent SrcBinding-targets value::

                                            - Type: str()
                                            - Valid values: device
                                            - Spirent name: none
                                            - Examples:
                                                - task.tx_type = 'device'
                                            - Required if action is create

====================================    ==================================================

'''
class StcStreamblock(Task):
    def __init__(self, task_log):
        ansible_module = 'stc'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('action')
        self.properties_set.add('count')
        self.properties_set.add('port_name')
        self.properties_set.add('stream_only_generation')
        self.properties_set.add('traffic_pattern')
        self.properties_set.add('name')
        self.properties_set.add('load')
        self.properties_set.add('load_unit')
        self.properties_set.add('rx_name')
        self.properties_set.add('tx_name')
        self.properties_set.add('rx_protocol')
        self.properties_set.add('tx_protocol')
        self.properties_set.add('rx_selector')
        self.properties_set.add('tx_selector')
        self.properties_set.add('rx_type')
        self.properties_set.add('tx_type')
        self.properties_set.add('task_name')

        self.selector_set = set()
        self.selector_set.add('EQUAL')
        self.selector_set.add('NOT_EQUAL')
        self.selector_set.add('CONTAINS')
        self.selector_set.add('STARTS_WITH')

        self.selector_map = dict()
        self.selector_map['EQUAL']          = '='
        self.selector_map['NOT_EQUAL']      = '!='
        self.selector_map['CONTAINS']       = '~='
        self.selector_map['STARTS_WITH']    = '^='

        self.load_profile_set = set()
        self.load_profile_set.add('load')
        self.load_profile_set.add('load_unit')

        self.streamblock_set = set()
        self.streamblock_set.add('name')
        self.streamblock_set.add('stream_only_generation')
        self.streamblock_set.add('traffic_pattern')

        # maps between properties in this class and Spirent playbook properties
        # May also contain internally-used properties
        self.property_map = dict()
        self.property_map['action']                 = 'action'
        self.property_map['count']                  = 'count'
        self.property_map['port_name']              = 'port_name'
        self.property_map['stream_only_generation'] = 'EnableStreamOnlyGeneration'
        self.property_map['traffic_pattern']        = 'TrafficPattern'
        self.property_map['name']                   = 'Name'
        self.property_map['load']                   = 'Load'
        self.property_map['load_unit']              = 'LoadUnit'
        self.property_map['rx_name']                = 'rx_name'
        self.property_map['tx_name']                = 'tx_name'
        self.property_map['rx_type']                = 'rx_type'
        self.property_map['tx_type']                = 'tx_type'
        self.property_map['rx_protocol']            = 'rx_protocol'
        self.property_map['tx_protocol']            = 'tx_protocol'
        self.property_map['task_name']              = 'task_name'

        # Used in build_srcbinding_targets() and build_dstbinding_targets()
        # Also used to build stc_streamblock_valid_tx_type and stc_streamblock_valid_rx_type
        self.binding_target_types = dict()
        self.binding_target_types['device'] = 'EmulatedDevice'
        # Used in build_srcbinding_targets() and build_dstbinding_targets()
        # Also used to build stc_streamblock_valid_tx_protocol and stc_streamblock_valid_rx_protocol
        self.binding_target_protocols = dict()
        self.binding_target_protocols['ipv4'] = 'Ipv4If'
        self.binding_target_protocols['ipv6'] = 'Ipv6If'

        self.stc_streamblock_valid_action = set()
        self.stc_streamblock_valid_action.add('create')
        self.stc_streamblock_valid_action.add('delete')

        self.stc_streamblock_valid_load_unit = set()
        self.stc_streamblock_valid_load_unit.add('BITS_PER_SECOND')
        self.stc_streamblock_valid_load_unit.add('FRAMES_PER_SECOND')
        self.stc_streamblock_valid_load_unit.add('INTER_BURST_GAP')
        self.stc_streamblock_valid_load_unit.add('INTER_BURST_GAP_IN_MILLISECONDS')
        self.stc_streamblock_valid_load_unit.add('INTER_BURST_GAP_IN_NANOSECONDS')
        self.stc_streamblock_valid_load_unit.add('KILOBITS_PER_SECOND')
        self.stc_streamblock_valid_load_unit.add('L2_RATE')
        self.stc_streamblock_valid_load_unit.add('MEGABITS_PER_SECOND')
        self.stc_streamblock_valid_load_unit.add('PERCENT_LINE_RATE')

        self.stc_streamblock_valid_traffic_pattern = set()
        self.stc_streamblock_valid_traffic_pattern.add('PAIR')
        self.stc_streamblock_valid_traffic_pattern.add('MESH')
        self.stc_streamblock_valid_traffic_pattern.add('BACKBONE')

        self.stc_streamblock_valid_rx_type = set()
        for p in self.binding_target_types:
            self.stc_streamblock_valid_rx_type.add(p)

        self.stc_streamblock_valid_tx_type = set()
        for p in self.binding_target_types:
            self.stc_streamblock_valid_tx_type.add(p)

        self.stc_streamblock_valid_rx_protocol = set()
        for p in self.binding_target_protocols:
            self.stc_streamblock_valid_rx_protocol.add(p)

        self.stc_streamblock_valid_tx_protocol = set()
        for p in self.binding_target_protocols:
            self.stc_streamblock_valid_tx_protocol.add(p)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None

    def final_verification(self):
        if self.action == 'delete':
            if self.name == None:
                self.task_log.error('exiting. call instance.name before calling instance.update()')
                exit(1)
            return

        if self.tx_name == None:
            self.task_log.error('exiting. call instance.tx_name before calling instance.update()')
            exit(1)
        if self.tx_type == None:
            self.task_log.error('exiting. call instance.tx_type before calling instance.update()')
            exit(1)
        if self.tx_protocol == None:
            self.task_log.error('exiting. call instance.tx_protocol before calling instance.update()')
            exit(1)
        if self.rx_name == None:
            self.task_log.error('exiting. call instance.rx_name before calling instance.update()')
            exit(1)
        if self.rx_type == None:
            self.task_log.error('exiting. call instance.rx_type before calling instance.update()')
            exit(1)
        if self.rx_protocol == None:
            self.task_log.error('exiting. call instance.rx_protocol before calling instance.update()')
            exit(1)
        if self.name == None:
            self.task_log.error('exiting. call instance.name before calling instance.update()')
            exit(1)
        if self.load == None:
            self.task_log.error('exiting. call instance.load before calling instance.update()')
            exit(1)
        if self.load_unit == None:
            self.task_log.error('exiting. call instance.load_unit before calling instance.update()')
            exit(1)
        if self.traffic_pattern == None:
            self.task_log.error('exiting. call instance.traffic_pattern before calling instance.update()')
            exit(1)

        if self.action == None:
            self.action = 'create'
        if self.count == None:
            self.count = 1
        if self.rx_selector == None:
            self.rx_selector = 'EQUAL'
        if self.tx_selector == None:
            self.tx_selector = 'EQUAL'
        if self.stream_only_generation == None:
            self.stream_only_generation = True

    def update_delete(self):
        self.streamblock_properties = dict()
        d = dict()
        d['Name'] = self.name
        streamblock = dict()
        streamblock['Streamblock'] = deepcopy(d)

        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['objects'] = list()
        self.ansible_task[self.ansible_module]['objects'].append(deepcopy(streamblock))
        self.ansible_task[self.ansible_module]['action'] = self.action

    def update(self):
        '''
        Call self.final_verification()
        Populate self.ansible_task dict() which is required by Playbook()
        '''
        self.final_verification()
        if self.action == 'delete':
            self.update_delete()
            return

        self.streamblock_properties = dict()
        d = dict()

        load = dict()
        for key in self.load_profile_set:
            if self.properties[key] != None:
                mapped_key = self.property_map[key]
                load[mapped_key] = self.properties[key]
        if len(load) != 0:
            d['AffiliationStreamBlockLoadProfile'] = deepcopy(load)

        for key in self.streamblock_set:
            if self.properties[key] != None:
                mapped_key = self.property_map[key]
                d[mapped_key] = self.properties[key]
        d['DstBinding-targets'] = self.build_dstbinding_targets()
        d['SrcBinding-targets'] = self.build_srcbinding_targets()

        streamblock = dict()
        streamblock['Streamblock'] = deepcopy(d)

        self.ansible_task = dict()
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = dict()
        self.ansible_task[self.ansible_module]['objects'] = list()
        self.ansible_task[self.ansible_module]['objects'].append(deepcopy(streamblock))
        self.ansible_task[self.ansible_module]['action'] = self.action
        self.ansible_task[self.ansible_module]['count'] = self.count
        if self.port_name == None:
            self.ansible_task[self.ansible_module]['under'] = self.build_ref_project()
        else:
            self.ansible_task[self.ansible_module]['under'] = self.build_ref_port()

    def build_ref_project(self):
        return 'ref:/project'
    def build_ref_port(self):
        return "ref:/Port[@Name='{}']".format(self.port_name)

    def build_dstbinding_targets(self):
        '''
        Build the following from rx_name, rx_selector, rx_type, rx_protocol

        ref:/EmulatedDevice[@Name='401_ipv4_device']/Ipv4If
        '''
        return "ref:/{}[@Name{}'{}']/{}".format(
            self.binding_target_types[self.rx_type],
            self.selector_map[self.rx_selector],
            self.rx_name,
            self.binding_target_protocols[self.rx_protocol])

    def build_srcbinding_targets(self):
        '''
        Build the following from tx, tx_type, tx_protocol

        ref:/EmulatedDevice[@Name='401_ipv4_device']/Ipv4If
        '''
        return "ref:/{}[@Name{}'{}']/{}".format(
            self.binding_target_types[self.tx_type],
            self.selector_map[self.tx_selector],
            self.tx_name,
            self.binding_target_protocols[self.tx_protocol])

    def verify_stc_streamblock_action(self, x, parameter='action'):
        verify_set = self.stc_streamblock_valid_action
        if x in verify_set:
            return
        source_method = 'verify_stc_streamblock_action'
        expectation = '{}'.format(', '.join(verify_set))
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_streamblock_count(self, x, parameter='count'):
        if self.is_digits(x):
            return
        source_method = 'verify_stc_streamblock_count'
        expectation = 'int()'
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_streamblock_load_unit(self, x, parameter='load_unit'):
        verify_set = self.stc_streamblock_valid_load_unit
        if x in verify_set:
            return
        source_method = 'verify_stc_streamblock_load_unit'
        expectation = '{}'.format(', '.join(verify_set))
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_streamblock_traffic_pattern(self, x, parameter='traffic_pattern'):
        verify_set = self.stc_streamblock_valid_traffic_pattern
        if x in verify_set:
            return
        source_method = 'verify_stc_streamblock_traffic_pattern'
        expectation = '{}'.format(', '.join(verify_set))
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_streamblock_rx_type(self, x, parameter='rx_type'):
        verify_set = self.stc_streamblock_valid_rx_type
        if x in verify_set:
            return
        source_method = 'verify_stc_streamblock_rx_type'
        expectation = '{}'.format(', '.join(verify_set))
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_streamblock_tx_type(self, x, parameter='tx_type'):
        verify_set = self.stc_streamblock_valid_tx_type
        if x in verify_set:
            return
        source_method = 'verify_stc_streamblock_tx_type'
        expectation = '{}'.format(', '.join(verify_set))
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_streamblock_rx_protocol(self, x, parameter='rx_protocol'):
        verify_set = self.stc_streamblock_valid_rx_protocol
        if x in verify_set:
            return
        source_method = 'verify_stc_streamblock_rx_protocol'
        expectation = '{}'.format(', '.join(verify_set))
        self.fail(self.class_name, source_method, x, parameter, expectation)

    def verify_stc_streamblock_tx_protocol(self, x, parameter='tx_protocol'):
        verify_set = self.stc_streamblock_valid_tx_protocol
        if x in verify_set:
            return
        source_method = 'verify_stc_streamblock_tx_protocol'
        expectation = '{}'.format(', '.join(verify_set))
        self.fail(self.class_name, source_method, x, parameter, expectation)

    #-----------------------------------------------------------------
    # top_level properties
    #-----------------------------------------------------------------

    @property
    def action(self):
        return self.properties['action']
    @action.setter
    def action(self, x):
        parameter = 'action'
        if self.set_none(x, parameter):
            return
        self.verify_stc_streamblock_action(x, parameter)
        self.properties[parameter] = x

    @property
    def count(self):
        return self.properties['count']
    @count.setter
    def count(self, x):
        parameter = 'count'
        if self.set_none(x, parameter):
            return
        self.verify_stc_streamblock_count(x, parameter)
        self.properties[parameter] = x

    @property
    def port_name(self):
        return self.properties['port_name']
    @port_name.setter
    def port_name(self, x):
        parameter = 'port_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    #-----------------------------------------------------------------
    # streamblock properties
    #-----------------------------------------------------------------

    @property
    def name(self):
        return self.properties['name']
    @name.setter
    def name(self, x):
        parameter = 'name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def stream_only_generation(self):
        return self.properties['stream_only_generation']
    @stream_only_generation.setter
    def stream_only_generation(self, x):
        parameter = 'stream_only_generation'
        if self.set_none(x, parameter):
            return
        self.verify_boolean(x, parameter)
        self.properties[parameter] = x

    @property
    def traffic_pattern(self):
        return self.properties['traffic_pattern']
    @traffic_pattern.setter
    def traffic_pattern(self, x):
        parameter = 'traffic_pattern'
        if self.set_none(x, parameter):
            return
        self.verify_stc_streamblock_traffic_pattern(x, parameter)
        self.properties[parameter] = x

    #-----------------------------------------------------------------
    # streamblock_config properties
    # See:
    #    build_dstbinding_targets()
    #    build_srcbinding_targets()
    #-----------------------------------------------------------------

    @property
    def rx_name(self):
        return self.properties['rx_name']
    @rx_name.setter
    def rx_name(self, x):
        parameter = 'rx_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def tx_name(self):
        return self.properties['tx_name']
    @tx_name.setter
    def tx_name(self, x):
        parameter = 'tx_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def rx_selector(self):
        return self.properties['rx_selector']
    @rx_selector.setter
    def rx_selector(self, x):
        parameter = 'rx_selector'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def tx_selector(self):
        return self.properties['tx_selector']
    @tx_selector.setter
    def tx_selector(self, x):
        parameter = 'tx_selector'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def rx_type(self):
        return self.properties['rx_type']
    @rx_type.setter
    def rx_type(self, x):
        parameter = 'rx_type'
        if self.set_none(x, parameter):
            return
        self.verify_stc_streamblock_rx_type(x, parameter)
        self.properties[parameter] = x

    @property
    def tx_type(self):
        return self.properties['tx_type']
    @tx_type.setter
    def tx_type(self, x):
        parameter = 'tx_type'
        if self.set_none(x, parameter):
            return
        self.verify_stc_streamblock_tx_type(x, parameter)
        self.properties[parameter] = x

    @property
    def rx_protocol(self):
        return self.properties['rx_protocol']
    @rx_protocol.setter
    def rx_protocol(self, x):
        parameter = 'rx_protocol'
        if self.set_none(x, parameter):
            return
        self.verify_stc_streamblock_rx_protocol(x, parameter)
        self.properties[parameter] = x

    @property
    def tx_protocol(self):
        return self.properties['tx_protocol']
    @tx_protocol.setter
    def tx_protocol(self, x):
        parameter = 'tx_protocol'
        if self.set_none(x, parameter):
            return
        self.verify_stc_streamblock_tx_protocol(x, parameter)
        self.properties[parameter] = x


    #-----------------------------------------------------------------
    # Load properties
    #-----------------------------------------------------------------

    @property
    def load(self):
        return self.properties['load']
    @load.setter
    def load(self, x):
        parameter = 'load'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def load_unit(self):
        return self.properties['load_unit']
    @load_unit.setter
    def load_unit(self, x):
        parameter = 'load_unit'
        if self.set_none(x, parameter):
            return
        self.verify_stc_streamblock_load_unit(x, parameter)
        self.properties[parameter] = x

    @property
    def task_name(self):
        return self.properties['task_name']
    @task_name.setter
    def task_name(self, x):
        parameter = 'task_name'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
