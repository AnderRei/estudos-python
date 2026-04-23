# You have a list of cars grouped by their brands. Each car is represented as a dictionary with its name and horsepower (HP).
# Your task is to create a function that takes this list and a minimum HP value, and returns a new list containing only the
# cars that have HP greater than or equal to the specified minimum.


def powerful_cars(brand_cars: list, minimal_hp: int) -> list:
    return [[car for car in marca if car["HP"] >= minimal_hp] for marca in brand_cars]


brand_cars = [
    [
        {"name": "Ferrari_F430", "HP": 483},
        {"name": "Ferrari_360", "HP": 395},
        {"name": "Ferrari_488", "HP": 661},
    ],
    [
        {"name": "Lamborghini_Aventador", "HP": 690},
        {"name": "Lamborghini_Gallardo", "HP": 560},
    ],
]

minimal_hp = 661

print(powerful_cars(brand_cars, minimal_hp))
