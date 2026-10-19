
import unittest
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from robot import Robot


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("Test-Robot")

    def test_initial_position(self):
        self.assertEqual(self.robot.position, 0)

    def test_robot_moves_forward(self):
        self.robot.move_forward()
        self.assertEqual(self.robot.position, 1)

    def test_robot_stops_when_obstacle_detected(self):
        self.robot.detect_obstacle(True)
        self.robot.move_forward()
        self.assertEqual(self.robot.position, 0)
        self.assertTrue(self.robot.stopped)

    def test_robot_moves_when_path_is_clear(self):
        self.robot.detect_obstacle(True)
        self.robot.detect_obstacle(False)
        self.robot.move_forward()
        self.assertEqual(self.robot.position, 1)
        
    def test_robot_turns_right_to_avoid_obstacle(self):
        self.robot.avoid_obstacle(
            front_obstacle=True,
            right_obstacle=False
        )
        self.assertEqual(self.robot.direction, "East")
        self.assertFalse(self.robot.stopped)
        self.assertEqual(self.robot.turns, 1)

    def test_robot_stays_stopped_when_both_paths_blocked(self):
        self.robot.avoid_obstacle(
            front_obstacle=True,
            right_obstacle=True
        )
        self.assertTrue(self.robot.stopped)
        self.assertEqual(self.robot.direction, "North")

    def test_robot_does_not_turn_when_path_is_clear(self):
        self.robot.avoid_obstacle(
            front_obstacle=False,
            right_obstacle=False
        )
        self.assertEqual(self.robot.direction, "North")
        self.assertEqual(self.robot.turns, 0)



if __name__ == "__main__":
    unittest.main()
