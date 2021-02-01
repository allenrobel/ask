# NxosBfdGlobal() - cisco/nxos/nxos_bfd_global.py
our_version = 108
from copy import deepcopy
from ask.common.task import Task
'''
Name: nxos_bfd_global.py

Description:

NxosBfdGlobal() generates Ansible Playbook tasks conformant with nxos_bfd_global
which can be fed to Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_bfd_global.py
'''

class NxosBfdGlobal(Task):
    def __init__(self, task_log):
        ansible_module = 'cisco.nxos.nxos_bfd_global'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self._classname = __class__.__name__
        self.ansible_task = dict()

        self.init_properties()

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


        self.bfd_fabricpath_interval_min = 50    # guessing fabricpath is the same as ipv4
        self.bfd_fabricpath_interval_max = 999   # fabricpath isn't available on n9k as AFAIK

        #-------------------------------------------------------------------------------------------
        # combined into the following dict() in self.update()
        # self.properties['fabricpath_interval'] = {"tx": bfd_fabricpath_interval, "min_rx": bfd_fabricpath_min_rx, "multiplier": bfd_fabricpath_multiplier}
        # see properties bfd_fabricpath_interval, bfd_fabricpath_min_rx, and bfd_fabricpath_multiplier
        self.bfd_fabricpath_interval_min = 50    # guessing fabricpath is the same as ipv4
        self.bfd_fabricpath_interval_max = 999   # fabricpath isn't available on n9k as AFAIK

        self.bfd_fabricpath_min_rx_min = 50
        self.bfd_fabricpath_min_rx_max = 999

        self.bfd_fabricpath_multiplier_min = 1
        self.bfd_fabricpath_multiplier_max = 50
        #-------------------------------------------------------------------------------------------

        #-------------------------------------------------------------------------------------------
        # combined into the following dict() in self.update()
        # self.properties['interval'] = {"tx": bfd_interval, "min_rx": bfd_min_rx, "multiplier": bfd_multiplier}
        # see properties bfd_interval, bfd_min_rx, and bfd_multiplier
        self.bfd_interval_min = 50   # This is BFD tx interval (naming it 'interval' for consistency
        self.bfd_interval_max = 999  # with Ansible and our CLI)

        self.bfd_min_rx_min = 50
        self.bfd_min_rx_max = 999

        self.bfd_multiplier_min = 1
        self.bfd_multiplier_max = 50
        #-------------------------------------------------------------------------------------------

        #-------------------------------------------------------------------------------------------
        # combined into the following dict() in self.update()
        # self.properties['ipv4_interval'] = {"tx": bfd_ipv4_interval, "min_rx": bfd_ipv4_min_rx, "multiplier": bfd_ipv4_multiplier}
        # see properties bfd_ipv4_interval, bfd_ipv4_min_rx, and bfd_ipv4_multiplier
        self.bfd_ipv4_interval_min = 50   # This is BFD ipv4 tx interval (naming it 'bfd_ipv4_interval' for consistency
        self.bfd_ipv4_interval_max = 999  # with Ansible and our CLI)

        self.bfd_ipv4_min_rx_min = 50
        self.bfd_ipv4_min_rx_max = 999

        self.bfd_ipv4_multiplier_min = 1
        self.bfd_ipv4_multiplier_max = 50
        #-------------------------------------------------------------------------------------------

        #-------------------------------------------------------------------------------------------
        # combined into the following dict() in self.update()
        # self.properties['ipv6_interval'] = {"tx": bfd_ipv6_interval, "min_rx": bfd_ipv6_min_rx, "multiplier": bfd_ipv6_multiplier}
        # see properties bfd_ipv6_interval, bfd_ipv6_min_rx, and bfd_ipv6_multiplier
        self.bfd_ipv6_interval_min = 50   # This is BFD ipv6 tx interval (naming it 'bfd_ipv6_interval' for consistency
        self.bfd_ipv6_interval_max = 999  # with Ansible and our CLI)

        self.bfd_ipv6_min_rx_min = 50
        self.bfd_ipv6_min_rx_max = 999

        self.bfd_ipv6_multiplier_min = 1
        self.bfd_ipv6_multiplier_max = 50
        #-------------------------------------------------------------------------------------------


        self.echo_rx_interval_min = 50
        self.echo_rx_interval_max = 999

        self.slow_timer_min = 1000
        self.slow_timer_max = 30000

        self.startup_timer_min = 0
        self.startup_timer_max = 30

        self.nxos_bfd_global_valid_echo_interface = ['Loopback', 'deleted']

    def init_properties(self):
        self.properties = dict()
        self.properties['echo_interface'] = None                    # str() LoopbackX, or 'deleted'
        self.properties['echo_rx_interval'] = None                  # int() in milliseconds
        self.properties['fabricpath_interval'] = None               # dict() {tx: ms, min_rx: ms, multiplier: x}
        self.properties['fabricpath_slow_timer'] = None             # int() milliseconds
        self.properties['fabricpath_vlan'] = None                   # int() vlan ID
        self.properties['interval'] = None                          # dict() {tx: ms, min_rx: ms, multiplier: x} BFD interval timer values
        self.properties['ipv4_echo_rx_interval'] = None             # int() milliseconds
        self.properties['ipv4_interval'] = None                     # dict() {tx: ms, min_rx: ms, multiplier: x} BFD IPv4 interval timer values
        self.properties['ipv4_slow_timer'] = None                   # int() milliseconds BFD IPv4 slow rate timer
        self.properties['ipv6_echo_rx_interval'] = None             # int() milliseconds
        self.properties['ipv6_interval'] = None                     # dict() {tx: ms, min_rx: ms, multiplier: x} BFD IPv6 interval timer values
        self.properties['ipv6_slow_timer'] = None                   # int() milliseconds BFD IPv6 slow rate timer
        self.properties['slow_timer'] = None                        # int() milliseconds BFD slow rate timer
        self.properties['startup_timer'] = None                     # int() seconds BFD delayed startup timer

        self._bfd_interval = None
        self._bfd_min_rx = None
        self._bfd_multiplier = None

        self._bfd_ipv4_interval = None
        self._bfd_ipv4_min_rx = None
        self._bfd_ipv4_multiplier = None

        self._bfd_ipv6_interval = None
        self._bfd_ipv6_min_rx = None
        self._bfd_ipv6_multiplier = None

        self._bfd_fabricpath_interval = None
        self._bfd_fabricpath_min_rx = None
        self._bfd_fabricpath_multiplier = None

    def update(self):
        '''
        update verifies that mandatory module-specific parameters are set prior to
        calling self.update_topo()

        self.update_topo() is inherited from AnsJson()
        '''
        self.final_verification()

        d = dict()
        if self.echo_interface != None:
            d['echo_interface'] = self.echo_interface
        if self.echo_rx_interval != None:
            d['echo_rx_interval'] = self.echo_rx_interval
        if self.properties['fabricpath_interval'] != None:
            d['fabricpath_interval'] = self.properties['fabricpath_interval']
        if self.fabricpath_slow_timer != None:
            d['fabricpath_slow_timer'] = self.fabricpath_slow_timer
        if self.fabricpath_vlan != None:
            d['fabricpath_vlan'] = self.fabricpath_vlan
        if self.properties['interval'] != None:
            d['interval'] = self.properties['interval']
        if self.ipv4_echo_rx_interval != None:
            d['ipv4_echo_rx_interval'] = self.ipv4_echo_rx_interval
        if self.properties['ipv4_interval'] != None:
            d['ipv4_interval'] = self.properties['ipv4_interval']
        if self.ipv4_slow_timer != None:
            d['ipv4_slow_timer'] = self.ipv4_slow_timer
        if self.ipv6_echo_rx_interval != None:
            d['ipv6_echo_rx_interval'] = self.ipv6_echo_rx_interval
        if self.properties['ipv6_interval'] != None:
            d['ipv6_interval'] = self.properties['ipv6_interval']
        if self.ipv6_slow_timer != None:
            d['ipv6_slow_timer'] = self.ipv6_slow_timer
        if self.slow_timer != None:
            d['slow_timer'] = self.slow_timer
        if self.startup_timer != None:
            d['startup_timer'] = self.startup_timer

        if self.state != None:
            d['state'] = self.state
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name

        self.ansible_task[self.ansible_module] = d.copy()

        self.init_properties()

    def final_verification(self):
        self.nxos_bfd_global_verify_bfd_sets(self.bfd_interval, self.bfd_min_rx, self.bfd_multiplier, 'bfd')
        self.nxos_bfd_global_verify_bfd_sets(self.bfd_ipv4_interval, self.bfd_ipv4_min_rx, self.bfd_ipv4_multiplier, 'bfd_ipv4')
        self.nxos_bfd_global_verify_bfd_sets(self.bfd_ipv6_interval, self.bfd_ipv6_min_rx, self.bfd_ipv6_multiplier, 'bfd_ipv6')
        self.nxos_bfd_global_verify_bfd_sets(self.bfd_fabricpath_interval, self.bfd_fabricpath_min_rx, self.bfd_fabricpath_multiplier, 'bfd_fabricpath')

        if self.bfd_interval != None:
            self.properties['interval'] = self.make_bfd_dict(self.bfd_interval, self.bfd_min_rx, self.bfd_multiplier)

        if self.bfd_ipv4_interval != None:
            self.properties['ipv4_interval'] = self.make_bfd_dict(self.bfd_ipv4_interval, self.bfd_ipv4_min_rx, self.bfd_ipv4_multiplier)

        if self.bfd_ipv6_interval != None:
            self.properties['ipv6_interval'] = self.make_bfd_dict(self.bfd_ipv6_interval, self.bfd_ipv6_min_rx, self.bfd_ipv6_multiplier)

        if self.bfd_fabricpath_interval != None:
            self.properties['fabricpath_interval'] = self.make_bfd_dict(self.bfd_fabricpath_interval, self.bfd_fabricpath_min_rx, self.bfd_fabricpath_multiplier)

        # uuid is required and is used to ensure uniqueness of entries
        # uuid is used internally and is not related to Ansible.
        # For nxos_bfd_global, which is a global config without the need to ensure uniqueness, we use the ansible module name as the UUID
        self.properties['UUID'] = self.ansible_module


    def nxos_bfd_global_verify_echo_interface(self, x, parameter='unspecified'):
        for item in self.nxos_bfd_global_valid_echo_interface:
            if item in x:
                return
        source_class = self._classname
        source_method = 'nxos_bfd_global_verify_echo_interface'
        expectation = ','.join(self.nxos_bfd_global_valid_echo_interface)
        self.fail(source_class, source_method, x, parameter, expectation)

    def nxos_bfd_global_verify_bfd_sets(self, interval, min_rx, multiplier, feature=None):
        valid_bfd_features = ['bfd', 'bfd_ipv4', 'bfd_ipv6', 'bfd_fabricpath']
        if feature not in valid_bfd_features:
            self.task_log.error('exiting. feature must be one of {}'.format(','.join(valid_bfd_features)))
            exit(1)
        bfd_set = set([interval, min_rx, multiplier])
        if None in bfd_set and len(bfd_set) != 1:
            self.task_log.error('exiting. if any of {0}_interval, {0}_min_rx, {0}_multiplier are None, they all must be None'.format(feature))
            exit(1)
        # we have already checked for is_digits and for valid ranges within the properties for each of these

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
        self.nxos_bfd_global_verify_echo_interface(x, parameter)
        self.properties[parameter] = x

    @property
    def echo_rx_interval(self):
        return self.properties['echo_rx_interval']
    @echo_rx_interval.setter
    def echo_rx_interval(self, x):
        parameter = 'echo_rx_interval'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(
            x,
            self.echo_rx_interval_min,
            self.echo_rx_interval_max,
            self._classname,
            'echo_rx_interval')
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
        self.verify_integer_range(
            x,
            self.fabricpath_slow_timer_min,
            self.fabricpath_slow_timer_max,
            self._classname,
            parameter)
        self.properties[parameter] = x

    @property
    def bfd_fabricpath_interval(self):
        return self._bfd_fabricpath_interval
    @bfd_fabricpath_interval.setter
    def bfd_fabricpath_interval(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['fabricpath_interval'] = {"tx": bfd_fabricpath_interval, "min_rx": bfd_fabricpath_min_rx, "multiplier": bfd_fabricpath_multiplier}
        '''
        parameter = 'bfd_fabricpath_interval'
        if x == None:
            self._bfd_fabricpath_interval = None
            return
        self.verify_integer_range(
            x,
            self.bfd_fabricpath_interval_min,
            self.bfd_fabricpath_interval_max,
            self._classname,
            parameter)
        self._bfd_fabricpath_interval = x

    @property
    def bfd_fabricpath_min_rx(self):
        return self._bfd_fabricpath_min_rx
    @bfd_fabricpath_min_rx.setter
    def bfd_fabricpath_min_rx(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['fabricpath_interval'] = {"tx": bfd_fabricpath_interval, "min_rx": bfd_fabricpath_min_rx, "multiplier": bfd_fabricpath_multiplier}
        '''
        parameter = 'bfd_fabricpath_min_rx'
        if x == None:
            self._bfd_fabricpath_min_rx = None
            return
        self.verify_integer_range(
            x,
            self.bfd_fabricpath_min_rx_min,
            self.bfd_fabricpath_min_rx_max,
            self._classname,
            parameter)
        self._bfd_fabricpath_min_rx = x

    @property
    def bfd_fabricpath_multiplier(self):
        return self._bfd_fabricpath_multiplier
    @bfd_fabricpath_multiplier.setter
    def bfd_fabricpath_multiplier(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['fabricpath_interval'] = {"tx": bfd_fabricpath_interval, "min_rx": bfd_fabricpath_min_rx, "multiplier": bfd_fabricpath_multiplier}
        '''
        parameter = 'bfd_fabricpath_multiplier'
        if x == None:
            self._bfd_fabricpath_multiplier = None
            return
        self.verify_integer_range(
            x,
            self.bfd_fabricpath_multiplier_min,
            self.bfd_fabricpath_multiplier_max,
            self._classname,
            parameter)
        self._bfd_fabricpath_multiplier = x

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
        return self._bfd_interval
    @bfd_interval.setter
    def bfd_interval(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['interval'] = {"tx": bfd_interval, "min_rx": bfd_min_rx, "multiplier": bfd_multiplier}
        '''
        parameter = 'bfd_interval'
        if x == None:
            self._bfd_interval = None
            return
        self.verify_integer_range(
            x,
            self.bfd_interval_min,
            self.bfd_interval_max,
            self._classname,
            parameter)
        self._bfd_interval = x

    @property
    def bfd_min_rx(self):
        return self._bfd_min_rx
    @bfd_min_rx.setter
    def bfd_min_rx(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['interval'] = {"tx": bfd_interval, "min_rx": bfd_min_rx, "multiplier": bfd_multiplier}
        '''
        parameter = 'bfd_min_rx'
        if x == None:
            self._bfd_min_rx = None
            return
        self.verify_integer_range(
            x,
            self.bfd_interval_min,
            self.bfd_interval_max,
            self._classname,
            parameter)
        self._bfd_min_rx = x

    @property
    def bfd_multiplier(self):
        return self._bfd_multiplier
    @bfd_multiplier.setter
    def bfd_multiplier(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['interval'] = {"tx": bfd_interval, "min_rx": bfd_min_rx, "multiplier": bfd_multiplier}
        '''
        parameter = 'bfd_multiplier'
        if x == None:
            self._bfd_multiplier = None
            return
        self.verify_integer_range(
            x,
            self.bfd_multiplier_min,
            self.bfd_multiplier_max,
            self._classname,
            parameter)
        self._bfd_multiplier = x


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
        self.verify_integer_range(
            x,
            self.ipv4_echo_rx_interval_min,
            self.ipv4_echo_rx_interval_max,
            self._classname,
            parameter)
        self.properties[parameter] = x

    @property
    def ipv4_slow_timer(self):
        return self.properties['ipv4_slow_timer']
    @ipv4_slow_timer.setter
    def ipv4_slow_timer(self, x):
        parameter = 'ipv4_slow_timer'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(
            x,
            self.ipv4_slow_timer_min,
            self.ipv4_slow_timer_max,
            self._classname,
            parameter)
        self.properties[parameter] = x

    @property
    def bfd_ipv4_interval(self):
        return self._bfd_ipv4_interval
    @bfd_ipv4_interval.setter
    def bfd_ipv4_interval(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['ipv4_interval'] = {"tx": bfd_ipv4_interval, "min_rx": bfd_ipv4_min_rx, "multiplier": bfd_ipv4_multiplier}
        '''
        parameter = 'bfd_ipv4_interval'
        if x == None:
            self._bfd_ipv4_interval = None
            return
        self.verify_integer_range(
            x,
            self.bfd_ipv4_interval_min,
            self.bfd_ipv4_interval_max,
            self._classname,
            parameter)
        self._bfd_ipv4_interval = x

    @property
    def bfd_ipv4_min_rx(self):
        return self._bfd_ipv4_min_rx
    @bfd_ipv4_min_rx.setter
    def bfd_ipv4_min_rx(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['ipv4_interval'] = {"tx": bfd_ipv4_interval, "min_rx": bfd_ipv4_min_rx, "multiplier": bfd_ipv4_multiplier}
        '''
        parameter = 'bfd_ipv4_min_rx'
        if x == None:
            self._bfd_ipv4_min_rx = None
            return
        self.verify_integer_range(
            x,
            self.bfd_ipv4_min_rx_min,
            self.bfd_ipv4_min_rx_max,
            self._classname,
            parameter)
        self._bfd_ipv4_min_rx = x

    @property
    def bfd_ipv4_multiplier(self):
        return self._bfd_ipv4_multiplier
    @bfd_ipv4_multiplier.setter
    def bfd_ipv4_multiplier(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['ipv4_interval'] = {"tx": bfd_ipv4_interval, "min_rx": bfd_ipv4_min_rx, "multiplier": bfd_ipv4_multiplier}
        '''
        parameter = 'bfd_ipv4_multiplier'
        if x == None:
            self._bfd_ipv4_multiplier = None
            return
        self.verify_integer_range(
            x,
            self.bfd_ipv4_multiplier_min,
            self.bfd_ipv4_multiplier_max,
            self._classname,
            parameter)
        self._bfd_ipv4_multiplier = x

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
        self.verify_integer_range(
            x,
            self.ipv6_echo_rx_interval_min,
            self.ipv6_echo_rx_interval_max,
            self._classname,
            parameter)
        self.properties[parameter] = x

    @property
    def ipv6_slow_timer(self):
        return self.properties['ipv6_slow_timer']
    @ipv6_slow_timer.setter
    def ipv6_slow_timer(self, x):
        parameter = 'ipv6_slow_timer'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(
            x,
            self.ipv6_slow_timer_min,
            self.ipv6_slow_timer_max,
            self._classname,
            parameter)
        self.properties[parameter] = x

    @property
    def bfd_ipv6_interval(self):
        return self._bfd_ipv6_interval
    @bfd_ipv6_interval.setter
    def bfd_ipv6_interval(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['ipv6_interval'] = {"tx": bfd_ipv6_interval, "min_rx": bfd_ipv6_min_rx, "multiplier": bfd_ipv6_multiplier}
        '''
        parameter = 'bfd_ipv6_interval'
        if x == None:
            self._bfd_ipv6_interval = None
            return
        self.verify_integer_range(
            x,
            self.bfd_ipv6_interval_min,
            self.bfd_ipv6_interval_max,
            self._classname,
            parameter)
        self._bfd_ipv6_interval = x

    @property
    def bfd_ipv6_min_rx(self):
        return self._bfd_ipv6_min_rx
    @bfd_ipv6_min_rx.setter
    def bfd_ipv6_min_rx(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['ipv6_interval'] = {"tx": bfd_ipv6_interval, "min_rx": bfd_ipv6_min_rx, "multiplier": bfd_ipv6_multiplier}
        '''
        parameter = 'bfd_ipv6_min_rx'
        if x == None:
            self._bfd_ipv6_min_rx = None
            return
        self.verify_integer_range(
            x,
            self.bfd_ipv6_min_rx_min,
            self.bfd_ipv6_min_rx_max,
            self._classname,
            parameter)
        self._bfd_ipv6_min_rx = x

    @property
    def bfd_ipv6_multiplier(self):
        return self._bfd_ipv6_multiplier
    @bfd_ipv6_multiplier.setter
    def bfd_ipv6_multiplier(self, x):
        '''
        Not added to feature_dict. This is combined into the following dict() in self.update():

        self.properties['ipv6_interval'] = {"tx": bfd_ipv6_interval, "min_rx": bfd_ipv6_min_rx, "multiplier": bfd_ipv6_multiplier}
        '''
        parameter = 'bfd_ipv6_multiplier'
        if x == None:
            self._bfd_ipv6_multiplier = None
            return
        self.verify_integer_range(
            x,
            self.bfd_ipv6_multiplier_min,
            self.bfd_ipv6_multiplier_max,
            self._classname,
            parameter)
        self._bfd_ipv6_multiplier = x


    @property
    def slow_timer(self):
        return self.properties['slow_timer']
    @slow_timer.setter
    def slow_timer(self, x):
        parameter = 'slow_timer'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(
            x,
            self.slow_timer_min,
            self.slow_timer_max,
            self._classname,
            parameter)
        self.properties[parameter] = x

    @property
    def startup_timer(self):
        return self.properties['startup_timer']
    @startup_timer.setter
    def startup_timer(self, x):
        parameter = 'startup_timer'
        if self.set_none(x, parameter):
            return
        self.verify_integer_range(
            x,
            self.startup_timer_min,
            self.startup_timer_max,
            self._classname,
            parameter)
        self.properties[parameter] = x

    @property
    def _interval(self):
        return self.properties['interval']
    @property
    def _ipv4_interval(self):
        return self.properties['ipv4_interval']
    @property
    def _ipv6_interval(self):
        return self.properties['ipv6_interval']

    @property
    def _fabricpath_interval(self):
        return self.properties['fabricpath_interval']
