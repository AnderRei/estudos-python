class Robot:
    def __init__(self, name: str):
        self.name = name
        self.partner = None


def pair_robots(robots: list) -> tuple:
    robot_1 = Robot(robots[0])
    robot_2 = Robot(robots[1])

    robot_1.partner = robot_2
    robot_2.partner = robot_1

    return robot_1, robot_2


# LISTA COM OS NOMES
robots = ["Alex", "Tom"]

# CHAMA A FUNÇÃO
new_robots = pair_robots(robots)

# MOSTRA OS DADOS
print(new_robots)

print(new_robots[0].name)
print(new_robots[1].name)

print(new_robots[0].partner.name)
print(new_robots[1].partner.name)

print(new_robots[0].partner is new_robots[1])
print(new_robots[1].partner is new_robots[0])
