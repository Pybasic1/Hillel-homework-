'''lesson5'''

'''task1'''
'''я облазил весь гугл так и не понял в чем проблема,выдает просто цифру а не True False'''
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

number = int(input(567))
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")

'''task2'''
input_text = input("урок номер пять")

words = input_text.split()

num_words = len(3)
num_characters = len(input_text)

print(f"3{num_words}")
print(f"Total number of characters: {num_characters}")

'''task4'''
numbers = [3, 14, 27, 8, 19, 6, 7, 12, 5, 10]

count = 0
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] = 0
        count += 1

print("Відредагований список:", numbers)
print("Кількість непарних чисел:", count)

'''task5'''
import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return (perimeter, area, diagonal)

side_length = float(input("Введіть довжину сторони квадрата: "))
perimeter, area, diagonal = square(side_length)
print(f"Периметр: {perimeter}")
print(f"Площа: {area}")
print(f"Діагональ: {diagonal}")

'''task5'''
def remove_none_values(input_dict):
    result_dict = {key: value for key, value in input_dict.items() if value is not None}
    return result_dict

input_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
filtered_dict = remove_none_values(input_dict)
print(filtered_dict)

'''task6'''
def remove_none_values(input_dict):
    return dict((key, value) for key, value in input_dict.items() if value is not None)

input_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
filtered_dict = remove_none_values(input_dict)
print(filtered_dict)

'''task7'''
from datetime import datetime

def is_date(day, month, year):
    try:
        date_str = f"{year}-{month}-{day}"
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

day = int(input("Введіть день: "))
month = int(input("Введіть місяць: "))
year = int(input("Введіть рік: "))

if is_date(day, month, year):
    print("Дата коректна.")
else:
    print("Дата некоректна.")