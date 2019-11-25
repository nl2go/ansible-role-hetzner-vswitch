Role Name
=========

This roles sets up a Hetzner vSwitch.

Requirements
------------

The vSwitches are set up just with API calls, so you don't need any
extra requirements.

Role Variables
--------------

  * hetzner_vswitch_hetzner_robot_api_url: URL for the Hetzner Robot API (or the mock).
  * hetzner_vswitch_hetzner_robot_api_user: Credentials for the Hetzner Robot API.
  * hetzner_vswitch_hetzner_robot_api_pass: Credentials for the Hetzner Robot API.
  * hetzner_vswitch_webservice_mock: Image to mock the Hetzner API, e.j.: ``nl2go/hetzner-robot-api-mock:1.2.3``.
  * hetzner_vswitch_vlan_name: Name for the VLAN.
  * hetzner_vswitch_vlan_id: Identifier for the VLAN, a "string", between 4000 and 4019.

Dependencies
------------

No other roles are needed.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: hetzner_vswitch }

License
-------

MIT

Author Information
------------------

[Newsletter2go GbmH. - A sendinblue company](https://www.newsletter2go.com/jobs/)
