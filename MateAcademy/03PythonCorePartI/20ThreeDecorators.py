"""
Decorators pipeline for mixed lists:
1) number_filter: keep numeric items
2) round_dict: map rounded n -> n*2
3) arrow: format "n -> 2n"

like_numbers(...) returns:
"I like to filter, rounding, doubling, store and decorate numbers: ..."
"""

from typing import Callable, Any


def number_filter(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(items: list, *args, **kwargs) -> Any:
        numeric_items = [item for item in items if isinstance(item, (int, float))]
        return func(numeric_items, *args, **kwargs)

    return wrapper


def round_dict(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(items: list, *args, **kwargs) -> Any:
        rounded_dict = {round(item): round(item) * 2 for item in items}
        return func(rounded_dict, *args, **kwargs)

    return wrapper


def arrow(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(items: dict, *args, **kwargs) -> Any:
        arrow_list = [f"{key} -> {value}" for key, value in items.items()]
        return func(arrow_list, *args, **kwargs)

    return wrapper


@number_filter
@round_dict
@arrow
def like_numbers(items: list) -> str:
    return (
        "I like to filter, rounding, doubling, store and decorate numbers: "
        f"{', '.join(items)}!"
    )


items = ["35", 2.1, 4, 8.88, -123, "S", {"a", "b", 5}]

print(like_numbers(items))
