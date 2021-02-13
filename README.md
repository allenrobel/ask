# ask - Ansible ScriptKit README version 102

Ansible ScriptKit is a set of classes and example scripts that can be used to generate playbooks.  We use this internally for some of our customer proof of concepts and thought we'd open-source it for anyone else to use and to contribute to.

Goals:
   - Remove the need to understand/remember the YAML structure for each of the supported modules
   - Allow for programatic construction of playbooks using familiar python logic constructs
   - Fail quickly. Catch many errors without having to run the playbook against a device
   - Fail clearly. Provide detailed error messages for:
        - Parameters that are mutually-exclusive
        - Parameter values that are out of valid range
        - Missing mandatory parameters

Hence, creating an nxos_ospfv2 playbook looks and feels the same as creating a nxos_feature playbook.

We have completed the initial commit for all NX-OS Ansible modules supported to date.  We will be adding support for the remaining modules over the coming weeks/months.  We actively monitor the NX-OS Ansible Collections repo and will strive for quick turnaround on additions/changes to the modules that ScriptKit supports.

Also, we've developed a set of classes that can be used to generate Spirent Ansible playbooks (e.g. reserve ports, create emulated devices (including BGP), create StreamBlocks, and start/stop devices and traffic).  These are NOT comprehensive.  Rather, they focus on our (perhaps relatively simple) use-cases.  These get the job done for us for things like ipv4/ipv6 traffic, and convergence test cases.  We have added about 50% of what we have, and will try to add the remaining by 2021.02.21.  At that time, we will also add a few complete convergence test case playbook generation scripts (configure DUT(s), configure Spirent, start traffic, initiate perturbance, stop traffic, collect statistics).

Over time (longer-term roadmap) we hope to add support for ACI, DCNM, etc.  We welcome contributions in these and other areas.

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