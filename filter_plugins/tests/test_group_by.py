import unittest

from filter_plugins.group_by import *


class VSwitchMergeTest(unittest.TestCase):

    def test_group_by(self):
        lefts = [
            {
                'name': 'foo1',
                'foo': 'bar'
            },
            {
                'name': 'foo2',
                'foo': 'bar'
            }
        ]
        rights = [
            {
                'name': 'foo2',
                'foz': 'baz'
            },
            {
                'name': 'foo1',
                'foz': 'baz'
            }
        ]
        expected_results = [
            {
                'name': 'foo1',
                'group': [
                    {'foo': 'bar', 'name': 'foo1'},
                    {'foz': 'baz', 'name': 'foo1'}
                ]
            },
            {
                'name': 'foo2',
                'group': [
                    {'foo': 'bar', 'name': 'foo2'},
                    {'foz': 'baz', 'name': 'foo2'}
                ]
            }
        ]
        actual_results = group_by(lefts, rights)

        self.assertEqual(expected_results, actual_results)
