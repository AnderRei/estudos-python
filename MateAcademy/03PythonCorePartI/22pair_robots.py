class Robot:
    def __init__(self, name: str) -> str:
        self.name = name
        self.partner = None


def pair_robots(robots: list) -> tuple:
    robot_1 = Robot(robots[0])
    robot_2 = Robot(robots[1])

    robot_1.partner = robot_2
    robot_2.partner = robot_1

    return robot_1, robot_2


r1, r2 = pair_robots(["Robo A", "Robo B"])

print(r1.name)  # Robo A
print(r1.partner.name)  # Robo B
print(r2.partner.name)  # Robo A
