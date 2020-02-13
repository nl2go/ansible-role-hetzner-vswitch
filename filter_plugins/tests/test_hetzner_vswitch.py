import unittest

from filter_plugins.hetzner_vswitch import *


class VSwitchTest(unittest.TestCase):

    def test_init(self):
        module = FilterModule()
        filters = module.filters()

        self.assertEqual(filters.get('hetzner_vswitch_pick'), pick.pick)
        self.assertEqual(filters.get('hetzner_vswitch_change_set'), change_set.change_set)
        self.assertEqual(filters.get('hetzner_vswitch_form_urlencode'), form_urlencode.form_urlencode)
        self.assertEqual(filters.get('hetzner_vswitch_group_by'), group_by.group_by)
        self.assertEqual(filters.get('hetzner_vswitch_list_to_dict'), helpers.array_to_dict)
