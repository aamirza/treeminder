import unittest
from unittest import mock

import treeminder
from goaltype import GoalType


class TreeMinderTests(unittest.TestCase):
    def test_yaml_getter_gets_params(self):
        self.assertIsNotNone(treeminder.get_yaml_data()['GOAL_TYPE'])

    @mock.patch('treeminder.get_yaml_data')
    def test_validate_goal_type_raises_error(self, mock_yaml):
        mock_yaml.return_value = {"GOAL_TYPE": "bodges"}
        user_data = treeminder.get_yaml_data()
        with self.assertRaises(treeminder.InvalidGoalType):
            treeminder.validate_goal_type(user_data['GOAL_TYPE'])

    def test_validate_goal_type_returns_goal_type(self):
        self.assertEqual(treeminder.validate_goal_type('badges'), GoalType.BADGES)


if __name__ == '__main__':
    unittest.main()
