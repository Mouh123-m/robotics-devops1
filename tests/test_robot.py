
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


if __name__ == "__main__":
    unittest.main()
