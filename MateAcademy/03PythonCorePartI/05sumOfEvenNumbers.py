# Given a list of integers, return the sum of all even numbers in the list.


def sum_of_even_numbers(numbers: list) -> int:
    
    return sum([number for number in numbers if number % 2 == 0])

print(sum_of_even_numbers([1, 2, 3, 4, 5, 6]))
