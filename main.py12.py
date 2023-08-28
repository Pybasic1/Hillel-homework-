'''lesson12'''
import random
from tabulate import tabulate


class Building:
    def __init__(self, number):
        self.number = number
        self.population = random.randint(1, 100)


class Street:
    def __init__(self, number):
        self.number = number
        self.buildings = [Building(i) for i in range(1, random.randint(5, 20) + 1)]


class City:
    def __init__(self):
        self.streets = []

    def populate_city(self):
        self.streets = [Street(i) for i in range(1, random.randint(2, 5) + 1)]

    def get_total_population(self):
        total_population = sum(building.population for street in self.streets for building in street.buildings)
        return total_population

    def print_city_table(self):
        table_data = []
        for street in self.streets:
            for building in street.buildings:
                table_data.append([street.number, building.number, building.population])

        print(tabulate(table_data, headers=["Вулиця", "Будинок", "Населення"]))


if __name__ == "__main__":
    city = City()
    city.populate_city()

    total_population = city.get_total_population()
    print(f"Загальне населення міста: {total_population} осіб\n")

    city.print_city_table()