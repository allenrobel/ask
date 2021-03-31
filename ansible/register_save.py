# RegisterSave() - ansible/register_save.py
our_version = 105
from ask.common.task import Task
'''
Name: register_save.py

Description:

RegisterSave() generates Ansible Playbook task, using module 'local_action',
to save a previously-set register to a file.  RegisterSave() can be fed to
Playbook().add_task()

Example usage:
    unit_test/cisco/nxos/unit_test_nxos_command.py
'''

class RegisterSave(Task):
    def __init__(self, task_log):
        ansible_module = 'local_action'
        super().__init__(ansible_module, task_log)
        self.lib_version = our_version
        self.class_name = __class__.__name__

        self.properties_set = set()
        self.properties_set.add('filename')
        self.properties_set.add('var')

        # scriptkit_properties can be used by scripts when
        # setting task_name. See Task().append_to_task_name()
        self.scriptkit_properties = set()
        self.scriptkit_properties.update(self.properties_set)

        self.init_properties()

    def init_properties(self):
        self.properties = dict()
        for p in self.properties_set:
            self.properties[p] = None
        self.properties['name'] = None

    def final_verification(self):
        if self.var == None:
            self.task_log.error('exiting. call instance.var before calling update()')
            exit(1)
        if self.filename == None:
            self.task_log.error('exiting. call instance.filename before calling update()')
            exit(1)

    def commit(self):
        self.update()
    def update(self):
        '''
        '''
        self.final_verification()
        self.ansible_task = dict()
        self.ansible_task['vars'] = dict()
        self.ansible_task['vars']['ansible_connection'] = 'local'
        if self.task_name != None:
            self.ansible_task['name'] = self.task_name
        save_results = 'copy content="{' + '{ ' + self.var + ' }' + '}"' + ' dest="' + self.filename + '"'
        self.ansible_task[self.ansible_module] = save_results

    @property
    def filename(self):
        return self.properties['filename']
    @filename.setter
    def filename(self, x):
        parameter = 'filename'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x

    @property
    def var(self):
        return self.properties['var']
    @var.setter
    def var(self, x):
        parameter = 'var'
        if self.set_none(x, parameter):
            return
        self.properties[parameter] = x
