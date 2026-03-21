# Function checks if all targets were hit at least once.
# Each attempt is represented as a list of booleans,
# where True indicates a hit and False indicates a miss.
# The function returns True if all targets were hit at least once,
# and False otherwise.


def all_targets_hit_upgrade(attempts: list) -> bool:
    return all([any(alvo) for alvo in attempts])


attempts = [
    [True, False, True],  # Shots at target 1
    [False, True, False, True],  # Shots at target 2
    [False, True],  # Shots at target 3
]
print(all_targets_hit_upgrade(attempts))  # all targets were hit at least once

attempts = [
    [True, False, True],  # Shots at target 1
    [False, False, True],  # Shots at target 2
    [False, False],  # Shots at target 3
]
print(all_targets_hit_upgrade(attempts))  # not all targets were hit at least once
