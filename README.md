[![Travis (.org) branch](https://img.shields.io/travis/nl2go/ansible-role-hetzner-vswitch/master)](https://travis-ci.org/nl2go/ansible-role-hetzner-vswitch)
[![Ansible Galaxy](https://img.shields.io/badge/role-nl2go.hetzner_vswitch-blue.svg)](https://galaxy.ansible.com/nl2go/hetzner_vswitch/)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/nl2go/ansible-role-hetzner-vswitch)](https://galaxy.ansible.com/nl2go/hetzner_vswitch)
[![Ansible Galaxy Downloads](https://img.shields.io/ansible/role/d/45025.svg?color=blue)](https://galaxy.ansible.com/nl2go/hetzner_vswitch/)

# Ansible Role: Hetzner vSwitch

An Ansible Role that manages [Hetzner Robot vSwitch](https://wiki.hetzner.de/index.php/Vswitch/en).

## Requirements

- Existing [Hetzner Online GmbH Account](https://accounts.hetzner.com).
- Configured [Hetzner Robot Webservice Account](https://robot.your-server.de/preferences).

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    hetzner_vswitch_webservice_base_url: https://robot-ws.your-server.de
 
Base url that is pointing to the [Hetzner Robot API](https://robot.your-server.de/doc/webservice/de.html). The variable is mostly utilized for testing purposes, there
is no need to change the default.

    hetzner_vswitch_webservice_username: robot
    
Webservice login name. May be set/changed as described in the section [Change Access Data (Hetzner Wiki)](https://wiki.hetzner.de/index.php/KonsoleH:Zugangsdaten_aendern/en).

    hetzner_vswitch_webservice_password: secret
    
Webservice password. May be set/changed as described in the section [Change Access Data (Hetzner Wiki)](https://wiki.hetzner.de/index.php/KonsoleH:Zugangsdaten_aendern/en).

    hetzner_vswitch_instances:
      - name: New vSwitch
        vlan: 1234
    
Multiple vSwitch instances may be managed using `hetzner_vswitch_instances` variable. A vSwitch is 
identified by the `name` attribute. The name must be unique to omit collision/unexpected behavior. 
The `state` attribute for a vSwitch defaults to `present`.

    hetzner_vswitch_instances:
      - name: New vSwitch
        state: absent

To ensure the vSwitch is removed add `state: absent`. The `name` attribute remains mandatory to identify origin state.

    hetzner_vswitch_host:
      - name: New vSwitch

Every host can be bound to one or multiple vSwitches defined within `hetzner_vswitch_instances` using the `hetzner_vswitch_host` variable. vSwitches
are referenced by the `name` attribute.

Hosts with undefined `hetzner_vswitch_host` variable are ignored by the role.

    hetzner_vswitch_host:
      - name: New vSwitch
        state: absent

Add `state: absent` to detach a host from a vSwitch. 

    hetzner_vswitch_instances:
      - name: New vSwitch
        vlan: 4001
        ipv4_address: 192.168.100.0
        ipv4_netmask: 255.255.255.0
           
    hetzner_vswitch_host:
      - name: Existing vSwitch
        ipv4_address: 192.168.100.1
                   
To manage the underlying network configuration `ipv4_address` and `ipv4_netmask` must be present on the `hetzner_vswitch_instances`.
A dedicated host IP address must be specified as `ipv4_address` within `hetzner_vswitch_host` variable.

    hetzner_vswitch_webservice_concurrent_requests: 1
    hetzner_vswitch_webservice_concurrent_poll: 1
    
To speed up the role execution while handling the vSwitch configuration with multiple vSwitches, the number of parallel requests made to the Hetzner Robot API
can be controlled by `hetzner_vswitch_webservice_concurrent_requests` variable. The poll interval for asynchronous request
result processing is set using `hetzner_vswitch_webservice_concurrent_poll`. Check official documentation on
[Asynchronous Actions and Polling](https://docs.ansible.com/ansible/latest/user_guide/playbooks_async.html) for more explanation. 

## Dependencies

None.

## Example Playbook

    - hosts: all
      roles:
         - nl2go.hetzner-vswitch

## Development
Use [docker-molecule](https://github.com/nl2go/docker-molecule) following the instructions to run [Molecule](https://molecule.readthedocs.io/en/stable/)
or install [Molecule](https://molecule.readthedocs.io/en/stable/) locally (not recommended, version conflicts might appear).


Use following to run tests:

    molecule test --all

## Maintainers

- [pablo2go](https://github.com/pablo2go)
- [build-failure](https://github.com/build-failure)

## License

See the [LICENSE.md](LICENSE.md) file for details.

## Author Information

This role was created by in 2019 by [Newsletter2Go GmbH](https://www.newsletter2go.com/).
