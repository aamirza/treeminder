import unittest

from goaltype import GoalType


class GoalTypeTests(unittest.TestCase):
    def test_goal_type_contains_valid_goal_types(self):
        self.assertIn('badges', GoalType, "Badges not found in GoalType")
        self.assertIn('points', GoalType, "Points not found in GoalType")



if __name__ == '__main__':
    unittest.main()
