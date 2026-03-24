#A decorator that validates the 'is_admin' attribute in the user dictionary. 
#It executes the wrapped function only for admin users; 
#otherwise, it blocks access and prints a permission denial message.

from typing import Callable
from functools import wraps


def admin_required(func: Callable) -> None:
    @wraps(func)
    def wrapper(user: dict) -> None:
        if user.get("is_admin"):
            return func(user)
        else:
            print("You are not allowed to see this information!")
    return wrapper


@admin_required
def send_secure_information(user: dict) -> None:
    print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")

send_secure_information({'name': 'Administrator', 'is_admin': True})
send_secure_information({'name': 'User1234', 'is_admin': False})
