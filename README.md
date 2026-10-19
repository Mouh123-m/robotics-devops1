
# Robotics DevOps Project

## 1. Project Overview

This project simulates a simple robot using Python.
The robot can move forward, detect obstacles, and stop
when an obstacle is detected.

The project demonstrates basic DevOps practices using
Git, GitHub, automated testing, and Docker (planned).

## 2. Project Objectives

- Simulate a robot using Python.
- Detect obstacles in a simulated environment.
- Stop the robot when an obstacle is detected.
- Test robot behavior automatically.
- Track source code changes with Git.
- Store and share the project on GitHub.
CI tests run automatically with GitHub Actions
- Add Docker support in a future stage.

## 3. Technologies

- Python
- Git
- GitHub
- unittest
- Docker (planned)

## 4. Project Structure

```text
robotics-devops/
├── src/
│   └── robot.py
├── tests/
│   └── test_robot.py
└── README.md
```

## 5. Run the Robot

Make sure Python is installed.

Run the following command from the project root:

```bash
python src/robot.py
```

## 6. Run Automated Tests

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

## 7. Expected Behavior

- The robot moves forward when the path is clear.
- The robot stops when an obstacle is detected.
- Automated tests verify the robot's behavior.

## 8. DevOps Workflow

1. Develop the robot using Python.
2. Test the code using unittest.
3. Track changes with Git.
4. Push the repository to GitHub.
5. Add Docker support later.

## 9. Future Improvements

- Add a graphical robot simulation.
- Add more obstacle detection scenarios.
- Automate testing with GitHub Actions.
- Containerize the application using Docker.

## 10. Author

Project developed as part of a DevOps course.
