# ask - Ansible ScriptKit

Ansible ScriptKit is a set of classes and example scripts that can be used to generate playbooks.  We use this internally for some of our customer proof of concepts and thought we'd open-source it for anyone else to use and to contribute to.

Goals:
   - Remove the need to understand/remember the YAML structure for each of the supported modules
   - Allow for programatic construction of playbooks using familiar python logic constructs

Hence, creating an nxos_ospfv2 playbook looks and feels the same as creating a nxos_feature playbook.

Most NX-OS Ansible modules are supported, but not all have been added to the repo yet.  We will be adding them over the next several days and hope to be finished with the initial set by 2021.02.05 (end of this current week).

Also, we've developed a set of classes that can be used to generate Spirent Ansible playbooks (e.g. reserve ports, create emulated devices (including BGP), create StreamBlocks, and start/stop devices and traffic).  These are not comprehensive, but get the job done for most simple ipv4/ipv6 traffic use-cases.  These, too, will be added by the end of this week (2021.02.05).

We hope to add support for ACI, DCNM, etc, over time and welcome contributions in these and other areas.

Suggestions and bug reports very much appreciated!
