
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.stopped = False

    def move_forward(self):
        if self.stopped:
            print(f"{self.name} is stopped and cannot move.")
        else:
            self.position += 1
            print(f"{self.name} moved forward to position {self.position}.")

    def detect_obstacle(self, obstacle):
        if obstacle:
            self.stopped = True
            print(f"{self.name} detected an obstacle and stopped!")
        else:
            self.stopped = False
            print(f"{self.name}: no obstacle detected.")

    def show_status(self):
        print(f"Robot: {self.name}")
        print(f"Position: {self.position}")
        print(f"Stopped: {self.stopped}")


robot = Robot("Robot-1")

robot.detect_obstacle(False)
robot.move_forward()

robot.detect_obstacle(False)
robot.move_forward()

robot.detect_obstacle(True)
robot.move_forward()

robot.show_status()
