class Robot:
    def __init__(self, model: str, constructor: str, serial_no: int) -> None:
        self.model = model
        self.constructor = constructor
        self.serial_no = serial_no


def copy_robot(robot: Robot) -> Robot:
    return Robot(robot.model, robot.constructor, robot.serial_no + 1)
  

robot = Robot('g135', 'Alex', 1664)
robot_copy = copy_robot(robot)

print(robot_copy is robot)
print(robot_copy.model)
print(robot.serial_no)
print(robot_copy.serial_no)
