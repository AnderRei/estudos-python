# You have a list of robots, each represented as a dictionary with a "core_version" key.
# Find the indices of all robots that have a core version less than a given new version.


def get_outdated_robots(robots: list, new_version: int) -> list:
    return [indice for indice, robo in enumerate(robots) if robo
            ["core_version"] < new_version]


robots = [
  {'core_version': 9},
  {'core_version': 13},
  {'core_version': 16},
  {'core_version': 9},
  {'core_version': 14},
]

print(get_outdated_robots(robots, 10))
