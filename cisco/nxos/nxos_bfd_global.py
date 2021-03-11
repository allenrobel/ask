# NxosBfdGlobal() - cisco/nxos/nxos_bfd_global.py
our_version = 112
from copy import deepcopy
from ask.common.task import Task
'''
***********************************
NxosBfdGlobal()
***********************************

.. contents::
   :local:
   :depth: 1

ScriptKit Synopsis
------------------
- NxosBfdGlobal() generates Ansible Playbook tasks conformant with cisco.nxos.nxos_bfd_global
- These can then be passed to Playbook().add_task()

Ansible Module Documentation
----------------------------
- `nxos_bfd_global <https://github.com/ansible-collections/cisco.nxos/blob/main/docs/cisco.nxos.nxos_bfd_global_module.rst>`_

ScriptKit Example
-----------------
- `unit_test/cisco/nxos/unit_test_nxos_bfd_global.py <https://github.com/allenrobel/ask/blob/main/unit_test/cisco/nxos/unit_test_nxos_bfd_global.py>`_

Notes
-----
This class deviates from the Ansible module for certain property
names to disambiguate them. See the table below for details.

|

============================    ==============================================
Property                        Description
============================    ==============================================
bfd_fabricpath_interval         BFD fabricpath session interval::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999
                                    - Example:
                                        task.bfd_fabricpath_interval = 999

bfd_fabricpath_min_rx           Minimum RX interval for fabricpath sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999
                                    - Example:
                                        task.bfd_fabricpath_min_rx = 50


bfd_fabricpath_multiplier       Detect multiplier for fabricpath bfd sessions::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.bfd_fabricpath_multiplier = 3

bfd_interval                    TX interval::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_interval = 999

bfd_min_rx                      Minimum RX interval::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values: range: 50-999  
                                    - Example:
                                        task.bfd_min_rx = 50

bfd_multiplier                  Detect multiplier for bfd sessions::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.bfd_multiplier = 3

bfd_ipv4_interval               TX interval for ipv4 sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_ipv4_interval = 999

bfd_ipv4_min_rx                 Minimum RX interval for ipv4 sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_ipv4_min_rx = 50

bfd_ipv4_multiplier             Detect multiplier for ipv4 bfd sessions::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.bfd_ipv4_multiplier = 3

bfd_ipv6_interval               TX interval for ipv6 sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_ipv6_interval = 999

bfd_ipv6_min_rx                 Minimum RX interval for ipv6 sessions::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999  
                                    - Example:
                                        task.bfd_ipv6_min_rx = 50

bfd_ipv6_multiplier             Detect multiplier for ipv6 bfd sessions::

                                    - Type: int()
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.bfd_ipv6_multiplier = 3

echo_interface                  Interface used for bfd echo frames::

                                    - Type: str()
                                    - Valid values:
                                        - A loopback interface
                                        - The keyword 'deleted'
                                    - Examples:
                                        - task.echo_interface = 'Loopback2'
                                        - task.echo_interface = 'deleted'

echo_rx_interval                BFD session echo rx interval::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.echo_rx_interval = 3

fabricpath_slow_timer           BFD fabricpath slow rate timer::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1-50
                                    - Example:
                                        task.fabricpath_slow_timer = 10

fabricpath_vlan                 BFD fabricpath control vlan::

                                    - Type: int()
                                    - Unit: vlan ID
                                    - Example:
                                        task.fabricpath_vlan = 2002

ipv4_echo_rx_interval           Echo rx-interval for ipv4 BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999
                                    - Example:
                                        task.ipv4_echo_rx_interval = 50

ipv4_slow_timer                 Slow mode timer for ipv4 BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1000-30000
                                    - Example:
                                        task.ipv4_slow_timer = 2000

ipv6_echo_rx_interval           Echo rx-interval for ipv6 BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 50-999
                                    - Example:
                                        task.ipv6_echo_rx_interval = 50

ipv6_slow_timer                 Slow mode timer for ipv6 BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1000-30000
                                    - Example:
                                        task.ipv6_slow_timer = 2000

slow_timer                      Slow mode timer for BFD session::

                                    - Type: int()
                                    - Unit: milliseconds
                                    - Valid values:
                                        - range: 1000-30000
                                    - Example:
                                        task.slow_timer = 2000

startup_timer                   Delayed Start Up timer for BFD sessions::

                                    - Type: int()
                                    - Unit: seconds
                                    - Valid values:
                                        - range: 0-30
                                    - Example:
                                        task.startup_timer = 20

============================    ==============================================

|

Authors
~~~~~~~

- Allen Robel (@PacketCalc)

'''

class NxosBfdGlobal(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bfd_global'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__
        self.ansible_task = dict()


        # interval_properties_set is used to disambiguate properties
        # in Ansible module nxos_bfd_global which have the same name,
        # but are not ambiguous in the Ansible module since they appear
        # as keys in different dictionaries.
        #
        # Specifically, the following keys:
        #
        # tx, min_rx, multiplier
        #
        # Which appear in the following Ansible dictionaries:
        #
        # fabricpath_interval
        # interval
        # ipv4_interval
        # ipv6_interval
        #
        # The user of this class will use the below property names, and
        # these will be used to construct the dictionaries that Ansible
        # expects.
        self.interval_properties_set = set()
        self.interval_properties_set.add('bfd_fabricpath_interval')
        self.interval_properties_set.add('bfd_fabricpath_min_rx')
        self.interval_properties_set.add('bfd_fabricpath_multiplier')
        self.interval_properties_set.add('bfd_interval')
        self.interval_properties_set.add('bfd_min_rx')
        self.interval_properties_set.add('bfd_multiplier')
        self.interval_properties_set.add('bfd_ipv4_interval')
        self.interval_properties_set.add('bfd_ipv4_min_rx')
        self.interval_properties_set.add('bfd_ipv4_multiplier')
        self.interval_properties_set.add('bfd_ipv6_interval')
        self.interval_properties_set.add('bfd_ipv6_min_rx')
        self.interval_properties_set.add('bfd_ipv6_multiplier')

        self.properties_set = set()
        self.properties_set.add('echo_interface')
        self.properties_set.add('echo_rx_interval')
        self.properties_set.add('fabricpath_interval')
        self.properties_set.add('fabricpath_slow_timer')
        self.properties_set.add('fabricpath_vlan')
        self.properties_set.add('interval')
        self.properties_set.add('ipv4_echo_rx_interval')
        self.properties_set.add('ipv4_interval')
        self.properties_set.add('ipv4_slow_timer')
        self.properties_set.add('ipv6_echo_rx_interval')
        self.properties_set.add('ipv6_interval')
        self.properties_set.add('ipv6_slow_timer')
        self.properties_set.add('slow_timer')
        self.properties_set.add('startup_timer')
        self.properties_set.update(self.interval_properties_set)

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.fabricpath_slow_timer_min = 1000  # guessing fabricpath is the same as ipv4
        self.fabricpath_slow_timer_max = 30000 # fabricpath isn't available on n9k as AFAIK

        self.ipv4_echo_rx_interval_min = 50
        self.ipv4_echo_rx_interval_max = 999

        self.ipv4_slow_timer_min = 1000
        self.ipv4_slow_timer_max = 30000

        self.ipv6_echo_rx_interval_min = 50
        self.ipv6_echo_rx_interval_max = 999

        self.ipv6_slow_timer_min = 1000
        self.ipv6_slow_timer_max = 30000


        # combined into the following dict() in self.final_verification()/self.make_bfd_dict()
        # self.properties['fabricpath_interval'] = {"tx": bfd_fabricpath_interval, "min_rx": bfd_fabricpath_min_rx, "multiplier": bfd_fabricpath_multiplier}
        # see properties bfd_fabricpath_interval, bfd_fabricpath_min_rx, and bfd_fabricpath_multiplier
        self.bfd_fabricpath_interval_min = 50    # guessing fabricpath is the same as ipv4
        self.bfd_fabricpath_interval_max = 999   # fabricpath isn't available on n9k as AFAIK

        self.bfd_fabricpath_min_rx_min = 50
        self.bfd_fabricpath_min_rx_max = 999

        self.bfd_fabricpath_multiplier_min = 1
        self.bfd_fabricpath_multiplier_max = 50

        self.bfd_interval_min = 50 
        self.bfd_interval_max = 999

        self.bfd_min_rx_min = 50
        self.bfd_min_rx_max = 999

        self.bfd_multiplier_min = 1
        self.bfd_multiplier_max = 50

        self.bfd_ipv4_interval_min = 50
        self.bfd_ipv4_interval_max = 999

        self.bfd_ipv4_min_rx_min = 50
        self.bfd_ipv4_min_rx_max = 999

        self.bfd_ipv4_multiplier_min = 1
        self.bfd_ipv4_multiplier_max = 50

        self.bfd_ipv6_interval_min = 50 
        self.bfd_ipv6_interval_max = 999

        self.bfd_ipv6_min_rx_min = 50
        self.bfd_ipv6_min_rx_max = 999

        self.bfd_ipv6_multiplier_min = 1
        self.bfd_ipv6_multiplier_max = 50


        self.echo_rx_interval_min = 50
        self.echo_rx_interval_max = 999

        self.slow_timer_min = 1000
        self.slow_timer_max = 30000

        self.startup_timer_min = 0
        self.startup_timer_max = 30

        self.nxos_bfd_global_valid_echo_interface = ['Loopback', 'deleted']

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['task_name'] = None

    def final_verification(self):
        self.verify_nxos_bfd_global_bfd_sets(
            self.bfd_interval,
            self.bfd_min_rx,
            self.bfd_multiplier,
            'bfd')
        self.verify_nxos_bfd_global_bfd_sets(
            self.bfd_ipv4_interval,
            self.bfd_ipv4_min_rx,
            self.bfd_ipv4_multiplier,
            'bfd_ipv4')
        self.verify_nxos_bfd_global_bfd_sets(
            self.bfd_ipv6_interval,
            self.bfd_ipv6_min_rx,
            self.bfd_ipv6_multiplier,
            'bfd_ipv6')
        self.verify_nxos_bfd_global_bfd_sets(
            self.bfd_fabricpath_interval,
            self.bfd_fabricpath_min_rx,
            self.bfd_fabricpath_multiplier,
            'bfd_fabricpath')

        if self.bfd_fabricpath_interval != None:
            self.properties['fabricpath_interval'] = self.make_bfd_dict(
                self.bfd_fabricpath_interval,
                self.bfd_fabricpath_min_rx,
                self.bfd_fabricpath_multiplier)

        if self.bfd_interval != None:
            self.properties['interval'] = self.make_bfd_dict(
                self.bfd_interval,
                self.bfd_min_rx,
                self.bfd_multiplier)

        if self.bfd_ipv4_interval != None:
            self.properties['ipv4_interval'] = self.make_bfd_dict(
                self.bfd_ipv4_interval,
                self.bfd_ipv4_min_rx,
                self.bfd_ipv4_multiplier)

        if self.bfd_ipv6_interval != None:
            self.properties['ipv6_interval'] = self.make_bfd_dict(
                self.bfd_ipv6_interval,
                self.bfd_ipv6_min_rx,
                self.bfd_ipv6_multiplier)

    def update(self):
        '''
        call final_verification()
        populate ansible_task dict()
        '''
        self.final_verification()

        d = dict()
        for p in self.properties_set:
            # interval_properties are not added to
            # the playbook directly. See final_verification()
            if p in self.interval_properties_set:
                continue
            if self.properties[p] != None:
                d[p] = self.properties[p]
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        self.ansible_task[self.ansible_module] = deepcopy(d)

    def verify_nxos_bfd_global_echo_interface(self, x, parameter='echo_interface'):
        verify_set = self.nxos_bfd_global_valid_echo_interface
        for item in verify_set:
            if item in x:
                return
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_echo_interface'
        expectation = ','.join(verify_set)
        self.fail(source_class, source_method, x, parameter, expectation)

    def verify_nxos_bfd_global_bfd_sets(self, interval, min_rx, multiplier, feature=None):
        valid_bfd_features = ['bfd', 'bfd_ipv4', 'bfd_ipv6', 'bfd_fabricpath']
        if feature not in valid_bfd_features:
            self.task_log.error('exiting. feature must be one of {}'.format(','.join(valid_bfd_features)))
            exit(1)
        bfd_set = set([interval, min_rx, multiplier])
        if None in bfd_set and len(bfd_set) != 1:
            self.task_log.error('exiting. if any of {0}_interval, {0}_min_rx, {0}_multiplier are None, they all must be None'.format(feature))
            exit(1)

    def verify_nxos_bfd_global_echo_rx_interval(self, x):
        range_min = self.echo_rx_interval_min
        range_max = self.echo_rx_interval_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_echo_rx_interval'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_fabricpath_slow_timer(self, x):
        range_min = self.fabricpath_slow_timer_min
        range_max = self.fabricpath_slow_timer_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_fabricpath_slow_timer'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_fabricpath_interval(self, x):
        range_min = self.bfd_fabricpath_interval_min
        range_max = self.bfd_fabricpath_interval_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_fabricpath_interval'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_fabricpath_min_rx(self, x):
        range_min = self.bfd_fabricpath_min_rx_min
        range_max = self.bfd_fabricpath_min_rx_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_fabricpath_min_rx'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_fabricpath_multiplier(self, x):
        range_min = self.bfd_fabricpath_multiplier_min
        range_max = self.bfd_fabricpath_multiplier_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_fabricpath_multiplier'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_interval(self, x):
        range_min = self.bfd_interval_min
        range_max = self.bfd_interval_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_interval'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_min_rx(self, x):
        range_min = self.bfd_min_rx_min
        range_max = self.bfd_min_rx_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_min_rx'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_multiplier(self, x):
        range_min = self.bfd_multiplier_min
        range_max = self.bfd_multiplier_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_multiplier'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv4_interval(self, x):
        range_min = self.bfd_ipv4_interval_min
        range_max = self.bfd_ipv4_interval_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv4_interval'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv4_min_rx(self, x):
        range_min = self.bfd_ipv4_min_rx_min
        range_max = self.bfd_ipv4_min_rx_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv4_min_rx'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv4_multiplier(self, x):
        range_min = self.bfd_ipv4_multiplier_min
        range_max = self.bfd_ipv4_multiplier_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv4_multiplier'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv6_interval(self, x):
        range_min = self.bfd_ipv6_interval_min
        range_max = self.bfd_ipv6_interval_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv6_interval'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv6_min_rx(self, x):
        range_min = self.bfd_ipv6_min_rx_min
        range_max = self.bfd_ipv6_min_rx_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv6_min_rx'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv6_multiplier(self, x):
        range_min = self.bfd_ipv6_multiplier_min
        range_max = self.bfd_ipv6_multiplier_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv6_multiplier'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_slow_timer(self, x):
        range_min = self.slow_timer_min
        range_max = self.slow_timer_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_slow_timer'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_startup_timer(self, x):
        range_min = self.startup_timer_min
        range_max = self.startup_timer_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_startup_timer'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv4_echo_rx_interval(self, x):
        range_min = self.ipv4_echo_rx_interval_min
        range_max = self.ipv4_echo_rx_interval_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv4_echo_rx_interval'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv4_slow_timer(self, x):
        range_min = self.ipv4_slow_timer_min
        range_max = self.ipv4_slow_timer_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv4_slow_timer'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv6_echo_rx_interval(self, x):
        range_min = self.ipv6_echo_rx_interval_min
        range_max = self.ipv6_echo_rx_interval_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv6_echo_rx_interval'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def verify_nxos_bfd_global_bfd_ipv6_slow_timer(self, x):
        range_min = self.ipv6_slow_timer_min
        range_max = self.ipv6_slow_timer_max
        source_class = self.class_name
        source_method = 'verify_nxos_bfd_global_bfd_ipv6_slow_timer'
        self.verify_integer_range(x, range_min, range_max, source_class, source_method)

    def make_bfd_dict(self, interval, min_rx, multiplier):
        d = dict()
        d['tx'] = interval
        d['min_rx'] = min_rx
        d['multiplier'] = multiplier
        return d

    @property
    def echo_interface(self):
        return self.properties['echo_interface']
    @echo_interface.setter
    def echo_interface(self, x):
        parameter = 'echo_interface'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_global_echo_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def echo_rx_interval(self):
        return self.properties['echo_rx_interval']
    @echo_rx_interval.setter
    def echo_rx_interval(self, x):
        parameter = 'echo_rx_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_global_echo_rx_interval(x)
        self.properties[parameter] = x


    #---------------------------
    # FABRICPATH properties
    #---------------------------

    # fabricpath does not have an echo_rx_interval property
    @property
    def fabricpath_slow_timer(self):
        return self.properties['fabricpath_slow_timer']
    @fabricpath_slow_timer.setter
    def fabricpath_slow_timer(self, x):
        parameter = 'fabricpath_slow_timer'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_global_fabricpath_slow_timer(x)
        self.properties[parameter] = x

    @property
    def bfd_fabricpath_interval(self):
        return self.properties['bfd_fabricpath_interval']
    @bfd_fabricpath_interval.setter
    def bfd_fabricpath_interval(self, x):
        parameter = 'bfd_fabricpath_interval'
        if x == None:
            self.properties['bfd_fabricpath_interval'] = None
            return
        self.verify_nxos_bfd_global_fabricpath_interval(x)
        self.properties['bfd_fabricpath_interval'] = x

    @property
    def bfd_fabricpath_min_rx(self):
        return self.properties['bfd_fabricpath_min_rx']
    @bfd_fabricpath_min_rx.setter
    def bfd_fabricpath_min_rx(self, x):
        parameter = 'bfd_fabricpath_min_rx'
        if x == None:
            self.properties['bfd_fabricpath_min_rx'] = None
            return
        self.verify_nxos_bfd_global_fabricpath_min_rx(x)
        self.properties['bfd_fabricpath_min_rx'] = x

    @property
    def bfd_fabricpath_multiplier(self):
        return self.properties['bfd_fabricpath_multiplier']
    @bfd_fabricpath_multiplier.setter
    def bfd_fabricpath_multiplier(self, x):
        parameter = 'bfd_fabricpath_multiplier'
        if x == None:
            self.properties['bfd_fabricpath_multiplier'] = None
            return
        self.verify_nxos_bfd_global_fabricpath_multiplier(x)
        self.properties['bfd_fabricpath_multiplier'] = x

    @property
    def fabricpath_vlan(self):
        return self.properties['fabricpath_vlan']
    @fabricpath_vlan.setter
    def fabricpath_vlan(self, x):
        parameter = 'fabricpath_vlan'
        if self.set_none(x, parameter):
            return
        self.verify_digits(x, parameter)
        self.properties[parameter] = x


    #---------------------------
    # BFD properties
    #---------------------------

    @property
    def bfd_interval(self):
        return self.properties['bfd_interval']
    @bfd_interval.setter
    def bfd_interval(self, x):
        parameter = 'bfd_interval'
        if x == None:
            self.properties['bfd_interval'] = None
            return
        self.verify_nxos_bfd_global_bfd_interval(x)
        self.properties['bfd_interval'] = x

    @property
    def bfd_min_rx(self):
        return self.properties['bfd_min_rx']
    @bfd_min_rx.setter
    def bfd_min_rx(self, x):
        parameter = 'bfd_min_rx'
        if x == None:
            self.properties['bfd_min_rx'] = None
            return
        self.verify_nxos_bfd_global_bfd_min_rx(x)
        self.properties['bfd_min_rx'] = x

    @property
    def bfd_multiplier(self):
        return self.properties['bfd_multiplier']
    @bfd_multiplier.setter
    def bfd_multiplier(self, x):
        parameter = 'bfd_multiplier'
        if x == None:
            self.properties['bfd_multiplier'] = None
            return
        self.verify_nxos_bfd_global_bfd_multiplier(x)
        self.properties['bfd_multiplier'] = x


    #---------------------------
    # IPV4 properties
    #---------------------------

    @property
    def ipv4_echo_rx_interval(self):
        return self.properties['ipv4_echo_rx_interval']
    @ipv4_echo_rx_interval.setter
    def ipv4_echo_rx_interval(self, x):
        parameter = 'ipv4_echo_rx_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_global_bfd_ipv4_echo_rx_interval(x)
        self.properties[parameter] = x

    @property
    def ipv4_slow_timer(self):
        return self.properties['ipv4_slow_timer']
    @ipv4_slow_timer.setter
    def ipv4_slow_timer(self, x):
        parameter = 'ipv4_slow_timer'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_global_bfd_ipv4_slow_timer(x)
        self.properties[parameter] = x

    @property
    def bfd_ipv4_interval(self):
        return self.properties['bfd_ipv4_interval']
    @bfd_ipv4_interval.setter
    def bfd_ipv4_interval(self, x):
        parameter = 'bfd_ipv4_interval'
        if x == None:
            self.properties['bfd_ipv4_interval'] = None
            return
        self.verify_nxos_bfd_global_bfd_ipv4_interval(x)
        self.properties['bfd_ipv4_interval'] = x

    @property
    def bfd_ipv4_min_rx(self):
        return self.properties['bfd_ipv4_min_rx']
    @bfd_ipv4_min_rx.setter
    def bfd_ipv4_min_rx(self, x):
        parameter = 'bfd_ipv4_min_rx'
        if x == None:
            self.properties['bfd_ipv4_min_rx'] = None
            return
        self.verify_nxos_bfd_global_bfd_ipv4_min_rx(x)
        self.properties['bfd_ipv4_min_rx'] = x

    @property
    def bfd_ipv4_multiplier(self):
        return self.properties['bfd_ipv4_multiplier']
    @bfd_ipv4_multiplier.setter
    def bfd_ipv4_multiplier(self, x):
        parameter = 'bfd_ipv4_multiplier'
        if x == None:
            self.properties['bfd_ipv4_multiplier'] = None
            return
        self.verify_nxos_bfd_global_bfd_ipv4_multiplier(x)
        self.properties['bfd_ipv4_multiplier'] = x

    #---------------------------
    # IPV6 properties
    #---------------------------

    @property
    def ipv6_echo_rx_interval(self):
        return self.properties['ipv6_echo_rx_interval']
    @ipv6_echo_rx_interval.setter
    def ipv6_echo_rx_interval(self, x):
        parameter = 'ipv6_echo_rx_interval'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_global_bfd_ipv6_echo_rx_interval(x)
        self.properties[parameter] = x

    @property
    def ipv6_slow_timer(self):
        return self.properties['ipv6_slow_timer']
    @ipv6_slow_timer.setter
    def ipv6_slow_timer(self, x):
        parameter = 'ipv6_slow_timer'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_global_bfd_ipv6_slow_timer(x)
        self.properties[parameter] = x

    @property
    def bfd_ipv6_interval(self):
        return self.properties['bfd_ipv6_interval']
    @bfd_ipv6_interval.setter
    def bfd_ipv6_interval(self, x):
        parameter = 'bfd_ipv6_interval'
        if x == None:
            self.properties['bfd_ipv6_interval'] = None
            return
        self.verify_nxos_bfd_global_bfd_ipv6_interval(x)
        self.properties['bfd_ipv6_interval'] = x

    @property
    def bfd_ipv6_min_rx(self):
        return self.properties['bfd_ipv6_min_rx']
    @bfd_ipv6_min_rx.setter
    def bfd_ipv6_min_rx(self, x):
        parameter = 'bfd_ipv6_min_rx'
        if x == None:
            self.properties['bfd_ipv6_min_rx'] = None
            return
        self.verify_nxos_bfd_global_bfd_ipv6_min_rx(x)
        self.properties['bfd_ipv6_min_rx'] = x

    @property
    def bfd_ipv6_multiplier(self):
        return self.properties['bfd_ipv6_multiplier']
    @bfd_ipv6_multiplier.setter
    def bfd_ipv6_multiplier(self, x):
        parameter = 'bfd_ipv6_multiplier'
        if x == None:
            self.properties['bfd_ipv6_multiplier'] = None
            return
        self.verify_nxos_bfd_global_bfd_ipv6_multiplier(x)
        self.properties['bfd_ipv6_multiplier'] = x


    @property
    def slow_timer(self):
        return self.properties['slow_timer']
    @slow_timer.setter
    def slow_timer(self, x):
        parameter = 'slow_timer'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_global_bfd_slow_timer(x)
        self.properties[parameter] = x

    @property
    def startup_timer(self):
        return self.properties['startup_timer']
    @startup_timer.setter
    def startup_timer(self, x):
        parameter = 'startup_timer'
        if self.set_none(x, parameter):
            return
        self.verify_nxos_bfd_global_bfd_startup_timer(x)
        self.properties[parameter] = x
