# ask - Ansible ScriptKit

*README version 103*

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

## Supported Modules

Status | Description
------ | -----------
B      | Beta (under development)
D      | Deprecated
S      | Supported

Platform    | Status  | Name
----------- | ------- | ------------------------------------------------------
NX-OS       |    S    | [cisco.nxos.nxos_aaa_server][nxos_aaa_server]
NX-OS       |    S    | [cisco.nxos.nxos_aaa_server_host][nxos_aaa_server_host]
NX-OS       |    S    | [cisco.nxos.nxos_acl_interfaces][nxos_acl_interfaces]
NX-OS       |    B    | [cisco.nxos.nxos_acls][nxos_acls]
NX-OS       |    S    | [cisco.nxos.nxos_banner][nxos_banner]
NX-OS       |    S    | [cisco.nxos.nxos_bfd_global][nxos_bfd_global]
NX-OS       |    S    | [cisco.nxos.nxos_bfd_interfaces][nxos_bfd_interfaces]
NX-OS       |    D    | [cisco.nxos.nxos_bgp][nxos_bgp]
NX-OS       |    B    | [cisco.nxos.nxos_bgp_address_family][nxos_bgp_address_family]
NX-OS       |    D    | [cisco.nxos.nxos_bgp_af][nxos_bgp_af]
NX-OS       |    B    | [cisco.nxos.nxos_bgp_global][nxos_bgp_global]
NX-OS       |    D    | [cisco.nxos.nxos_bgp_neighbor][nxos_bgp_neighbor]
NX-OS       |    B    | [cisco.nxos.nxos_bgp_neighbor_address_family][nxos_bgp_neighbor_address_family]
NX-OS       |    D    | [cisco.nxos.nxos_bgp_neighbor_af][nxos_bgp_neighbor_af]
NX-OS       |    S    | [cisco.nxos.nxos_command][nxos_command]
NX-OS       |    S    | [cisco.nxos.nxos_config][nxos_config]
NX-OS       |    S    | [cisco.nxos.nxos_evpn_global][nxos_evpn_global]
NX-OS       |    S    | [cisco.nxos.nxos_evpn_vni][nxos_evpn_vni]
NX-OS       |    S    | [cisco.nxos.nxos_feature][nxos_feature]
NX-OS       |    B    | [cisco.nxos.nxos_gir][nxos_gir]
NX-OS       |    B    | [cisco.nxos.nxos_gir_profile_management][nxos_gir_profile_management]
NX-OS       |    S    | [cisco.nxos.nxos_hsrp][nxos_hsrp]
NX-OS       |    S    | [cisco.nxos.nxos_hsrp_interfaces][nxos_hsrp_interfaces]
NX-OS       |    S    | [cisco.nxos.nxos_igmp][nxos_igmp]
NX-OS       |    S    | [cisco.nxos.nxos_igmp_snooping][nxos_igmp_snooping]
NX-OS       |    S    | [cisco.nxos.nxos_interfaces][nxos_interfaces]
NX-OS       |    S    | [cisco.nxos.nxos_l2_interfaces][nxos_l2_interfaces]
NX-OS       |    S    | [cisco.nxos.nxos_l3_interfaces][nxos_l3_interfaces]
NX-OS       |    S    | [cisco.nxos.nxos_lacp_interfaces][nxos_lacp_interfaces]
NX-OS       |    S    | [cisco.nxos.nxos_lag_interfaces][nxos_lag_interfaces]
NX-OS       |    S    | [cisco.nxos.nxos_lldp_global][nxos_lldp_global]
NX-OS       |    S    | [cisco.nxos.nxos_lldp_interfaces][nxos_lldp_interfaces]
NX-OS       |    S    | [cisco.nxos.nxos_logging][nxos_logging]
NX-OS       |    S    | [cisco.nxos.nxos_ntp][nxos_ntp]
NX-OS       |    S    | [cisco.nxos.nxos_ntp_auth][nxos_ntp_auth]
NX-OS       |    S    | [cisco.nxos.nxos_ntp_options][nxos_ntp_options]
NX-OS       |    S    | [cisco.nxos.nxos_nxapi][nxos_nxapi]
NX-OS       |    S    | [cisco.nxos.nxos_ospf_interfaces][nxos_ospf_interfaces]
NX-OS       |    S    | [cisco.nxos.nxos_ospfv2][nxos_ospfv2]
NX-OS       |    S    | [cisco.nxos.nxos_overlay_global][nxos_overlay_global]
NX-OS       |    S    | [cisco.nxos.nxos_pim][nxos_pim]
NX-OS       |    S    | [cisco.nxos.nxos_pim_interface][nxos_pim_interface]
NX-OS       |    S    | [cisco.nxos.nxos_pim_rp_address][nxos_pim_rp_address]
NX-OS       |    B    | [cisco.nxos.nxos_prefix_lists][nxos_prefix_lists]
NX-OS       |    S    | [cisco.nxos.nxos_reboot][nxos_reboot]
NX-OS       |    S    | [cisco.nxos.nxos_snmp_community][nxos_snmp_community]
NX-OS       |    S    | [cisco.nxos.nxos_snmp_contact][nxos_snmp_contact]
NX-OS       |    S    | [cisco.nxos.nxos_snmp_host][nxos_snmp_host]
NX-OS       |    S    | [cisco.nxos.nxos_snmp_location][nxos_snmp_location]
NX-OS       |    S    | [cisco.nxos.nxos_static_routes][nxos_static_routes]
NX-OS       |    S    | [cisco.nxos.nxos_system][nxos_system]
NX-OS       |    D    | [cisco.nxos.nxos_vlan][nxos_vlan]
NX-OS       |    S    | [cisco.nxos.nxos_vlans][nxos_vlans]
NX-OS       |    S    | [cisco.nxos.nxos_vpc][nxos_vpc]
NX-OS       |    S    | [cisco.nxos.nxos_vpc_interface][nxos_vpc_interface]
NX-OS       |    S    | [cisco.nxos.nxos_vrf][nxos_vrf]
NX-OS       |    S    | [cisco.nxos.nxos_vrf_af][nxos_vrf_af]
NX-OS       |    S    | [cisco.nxos.nxos_vrf_interface][nxos_vrf_interface]
NX-OS       |    S    | [cisco.nxos.nxos_vtp_domain][nxos_vtp_domain]
NX-OS       |    S    | [cisco.nxos.nxos_vtp_password][nxos_vtp_password]
NX-OS       |    S    | [cisco.nxos.nxos_vtp_version][nxos_vtp_version]
NX-OS       |    S    | [cisco.nxos.nxos_vxlan_vtep][nxos_vxlan_vtep]
NX-OS       |    S    | [cisco.nxos.nxos_vxlan_vtep_vni][nxos_vxlan_vtep_vni]

## ScriptKit Classes

Status  | Name
------- | ------------------------------------------------------
   S    | [Pause()][pause]
   S    | [Playbook()][playbook]

[nxos_aaa_server]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_aaa_server.rst
[nxos_aaa_server_host]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_aaa_server_host.rst
[nxos_acl_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_acl_interfaces.rst
[nxos_acls]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_acls.rst
[nxos_banner]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_banner.rst
[nxos_bfd_global]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_bfd_global.rst
[nxos_bfd_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_bfd_interfaces.rst
[nxos_bgp]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_bgp.rst
[nxos_bgp_address_family]:https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_bgp_address_family.rst
[nxos_bgp_af]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_bgp_af.rst
[nxos_bgp_global]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_bgp_global.rst
[nxos_bgp_neighbor]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_bgp_neighbor.rst
[nxos_bgp_neighbor_address_family]:https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_bgp_neighbor_address_family.rst
[nxos_bgp_neighbor_af]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_bgp_neighbor_af.rst
[nxos_command]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_command.rst
[nxos_config]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_config.rst
[nxos_evpn_global]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_evpn_global.rst
[nxos_evpn_vni]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_evpn_vni.rst
[nxos_feature]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_feature.rst
[nxos_gir]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_gir.rst
[nxos_gir_profile_management]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_gir_profile_management.rst
[nxos_hsrp]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_hsrp.rst
[nxos_hsrp_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_hsrp_interfaces.rst
[nxos_igmp]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_igmp.rst
[nxos_igmp_snooping]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_igmp_snooping.rst
[nxos_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_interfaces.rst
[nxos_l2_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_l2_interfaces.rst
[nxos_l3_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_l3_interfaces.rst
[nxos_lacp_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_lacp_interfaces.rst
[nxos_lag_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_lag_interfaces.rst
[nxos_lldp_global]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_lldp_global.rst
[nxos_lldp_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_lldp_interfaces.rst
[nxos_logging]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_logging.rst
[nxos_ntp]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_ntp.rst
[nxos_ntp_auth]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_ntp_auth.rst
[nxos_ntp_options]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_ntp_options.rst
[nxos_nxapi]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_nxapi.rst
[nxos_ospf_interfaces]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_ospf_interfaces.rst
[nxos_ospfv2]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_ospfv2.rst
[nxos_overlay_global]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_overlay_global.rst
[nxos_pim]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_pim.rst
[nxos_pim_interface]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_pim_interface.rst
[nxos_pim_rp_address]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_pim_rp_address.rst
[nxos_prefix_lists]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_prefix_lists.rst
[nxos_reboot]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_reboot.rst
[nxos_snmp_community]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_snmp_community.rst
[nxos_snmp_contact]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_snmp_contact.rst
[nxos_snmp_host]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_snmp_host.rst
[nxos_snmp_location]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_snmp_location.rst
[nxos_static_routes]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_static_routes.rst
[nxos_system]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_system.rst
[nxos_vlan]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vlan.rst
[nxos_vlans]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vlans.rst
[nxos_vpc]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vpc.rst
[nxos_vpc_interface]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vpc_interface.rst
[nxos_vrf]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vrf.rst
[nxos_vrf_af]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vrf_af.rst
[nxos_vrf_interface]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vrf_interface.rst
[nxos_vtp_domain]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vtp_domain.rst
[nxos_vtp_password]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vtp_password.rst
[nxos_vtp_version]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vtp_version.rst
[nxos_vxlan_vtep]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vxlan_vtep.rst
[nxos_vxlan_vtep_vni]: https://github.com/allenrobel/ask/blob/main/docs/cisco/nxos/cisco.nxos.nxos_vxlan_vtep_vni.rst
[pause]: https://github.com/allenrobel/ask/blob/main/docs/common/pause.rst
[playbook]: https://github.com/allenrobel/ask/blob/main/docs/common/playbook.rst
