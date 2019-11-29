import os
import requests
import unittest

from requests.auth import HTTPBasicAuth


class DefaultTest(unittest.TestCase):
    hetzner_robot_base_url = os.getenv(
        'HETZNER_ROBOT_BASE_URL', 'http://localhost:3000'
    )
    auth = HTTPBasicAuth('robot', 'secret')

    def test_vswitches_changed(self):
        response = requests.get(self.hetzner_robot_base_url +
                                "/vswitch", auth=self.auth)
        self.assertEqual(len(response.json()), 1)
        self.assertDictEqual(response.json()[0], {
                    "cancelled": 'false',
                    "id": 1,
                    "name": "Existing vSwitch",
                    "vlan": '1234'
                })
