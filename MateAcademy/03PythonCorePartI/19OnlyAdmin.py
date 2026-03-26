# You are given a list of users, where each user is a dictionary with:
# - 'username': the user's name
# - 'is_admin': whether the user has admin privileges
#
# Create a decorator called only_admin.
# This decorator must filter the list, keeping only users with is_admin = True,
# and then pass this filtered list to the decorated function.


from typing import Callable


def only_admin(func: Callable) -> Callable:
    def wrapper(users_dict: list) -> None:
        new_users_dict = [user for user in users_dict if user["is_admin"] is True]
        func(new_users_dict)

    return wrapper


@only_admin
def create_permissions(users: list) -> None:
    for user in users:
        print(f'Creating permissions for {user["username"]}')


users = [
    {"username": "admin", "is_admin": True},
    {"username": "moderator_a11", "is_admin": True},
    {"username": "custom_user1", "is_admin": False},
    {"username": "custom_user2", "is_admin": False},
    {"username": "admin_2nd", "is_admin": True},
]

create_permissions(users)
