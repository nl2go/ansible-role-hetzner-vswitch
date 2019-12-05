import unittest

from filter_plugins.pick import *


class PickTest(unittest.TestCase):

    def test_pick(self):
        obj = [{'foo': 'a', 'bar': 'b'}]
        expected_obj = [{'foo': 'a'}]

        actual_obj = pick(obj, ['foo'])

        self.assertEqual(actual_obj, expected_obj)
