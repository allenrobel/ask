# ask - Ansible ScriptKit

Ansible ScriptKit is a set of classes and example scripts that can be used to generate playbooks.  We use this internally for some of our customer proof of concepts and thought we'd open-source it for anyone else to use and to contribute to.

Goals:
   - Remove the need to understand/remember the YAML structure for each of the supported modules
   - Allow for programatic construction of playbooks using familiar python logic constructs

Hence, creating an nxos_ospfv2 playbook looks and feels the same as creating a nxos_feature playbook.

Most NX-OS Ansible modules are supported, but not all have been added to the repo yet.  We will be adding them over the next several days and hope to be finished with the initial set by 2021.02.07.

Also, we've developed a set of classes that can be used to generate Spirent Ansible playbooks (e.g. reserve ports, create emulated devices (including BGP), create StreamBlocks, and start/stop devices and traffic).  These are not comprehensive, but get the job done for most simple ipv4/ipv6 traffic use-cases.  These, too, will be added by 2021.02.07.

We hope to add support for ACI, DCNM, etc, over time and welcome contributions in these and other areas.

Suggestions and bug reports very much appreciated!

## Reaching us

1. Post questions and suggestions in the Discussion forum.
2. Email us at [Ansible ScriptKit](mailto:info@scriptkit.org?subject=[GitHub]ScriptKit)


## Installing Ansible ScriptKit

If you are using a virtual env, activate it first, then:

Look at your current python module path:

```
python3
import sys
sys.path
```

cd into one of the directories in sys.path (or add a new directory to the path and cd into that)

clone the repo

```
git clone https://github.com/allenrobel/ask.git
```

Now you should be able to run the unit-test / example scripts.  For example:

```
(ansible-latest) arobel repos % cd ask/unit_test/cisco/nxos 
(ansible-latest) arobel nxos % ./unit_test_nxos_banner.py 
2021-02-01 11:48:16,785 INFO 19.65 unit_test_nxos_banner.<module> wrote playbook /tmp/playbook_nxos_banner.yaml
(ansible-latest) arobel nxos % 
```