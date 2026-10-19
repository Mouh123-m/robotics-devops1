
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.stopped = False
        self.direction = "North"
        self.turns = 0

    def move_forward(self):
        if self.stopped:
            print(f"{self.name} is stopped and cannot move.")
        else:
            self.position += 1
            print(
                f"{self.name} moved forward to position "
                f"{self.position}, facing {self.direction}."
            )

    def detect_obstacle(self, obstacle):
        if obstacle:
            self.stopped = True
            print(f"{self.name} detected an obstacle and stopped!")
        else:
            self.stopped = False
            print(f"{self.name}: no obstacle detected.")

    def turn_right(self):
        directions = ["North", "East", "South", "West"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        self.turns += 1
        print(f"{self.name} turned right. Now facing {self.direction}.")

    def avoid_obstacle(self, front_obstacle, right_obstacle):
        if not front_obstacle:
            self.stopped = False
            print(f"{self.name}: path is clear.")
            return

        self.stopped = True
        print(f"{self.name} stopped because of an obstacle ahead.")

        if not right_obstacle:
            self.turn_right()
            self.stopped = False
            print(f"{self.name} avoided the obstacle.")
        else:
            print(f"{self.name}: right path is blocked. Staying stopped.")

    def show_status(self):
        print(f"Robot: {self.name}")
        print(f"Position: {self.position}")
        print(f"Direction: {self.direction}")
        print(f"Stopped: {self.stopped}")
        print(f"Turns: {self.turns}")


if __name__ == "__main__":
    robot = Robot("Robot-1")

    robot.move_forward()

    robot.avoid_obstacle(
        front_obstacle=True,
        right_obstacle=False
    )
    robot.move_forward()

    robot.show_status()
