[![Travis (.org) branch](https://img.shields.io/travis/nl2go/ansible-role-hetzner-vswitch/master)](https://travis-ci.org/nl2go/ansible-role-hetzner-vswitch)
[![Ansible Galaxy](https://img.shields.io/badge/role-nl2go.hetzner_vswitch-blue.svg)](https://galaxy.ansible.com/nl2go/hetzner_vswitch/)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/nl2go/ansible-role-hetzner-vswitch)](https://galaxy.ansible.com/nl2go/hetzner_vswitch)

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
        vlan: '1234'
    
Multiple vSwitch instances may be managed using `hetzner_vswitch_instances` variable. A vSwitch is 
identified by the `name` attribute. The name must be unique to omit collision/unexpected behavior. 
The `state` attribute for a vSwitch defaults to `present`.

    hetzner_vswitch_instances:
      - name: New vSwitch
        state: absent

To ensure the vSwitch is removed add `state: absent`. The `name` attribute remains mandatory to identify origin state.

## Dependencies

None.

## Example Playbook

Since the role is managing the communication with the [Hetzner Robot API](https://robot.your-server.de/doc/webservice/de.html)
only, it may be run on localhost.

    - hosts: localhost
      roles:
         - nl2go.hetzner-vswitch

## Maintainers

- [pablo2go](https://github.com/pablo2go)
- [build-failure](https://github.com/build-failure)

## License

See the [LICENSE.md](LICENSE.md) file for details.

## Author Information

This role was created by in 2019 by [Newsletter2Go GmbH](https://www.newsletter2go.com/).
