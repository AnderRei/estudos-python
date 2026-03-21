# Write a function that takes a list of numbers
# and returns a new list with each number doubled.
# Using list comprehension to achieve this.


def double_list_items(ls: list) -> list:
    return [num * 2 for num in ls]


print(double_list_items([1, 2, 3, 4, 5]))
