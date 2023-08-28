'''lesson7'''

'''task1'''
def common_numbers_count(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_numbers = set1 & set2
    return len(common_numbers)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

count = common_numbers_count(list1, list2)
print(f"Кількість спільних чисел: {count}")

'''task2'''
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

temperature = float(input("Введіть температуру: "))
unit = input("Введіть одиницю температури (C/F/K): ").upper()

if unit == 'C':
    celsius = temperature
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
elif unit == 'F':
    fahrenheit = temperature
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = fahrenheit_to_kelvin(fahrenheit)
elif unit == 'K':
    kelvin = temperature
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = kelvin_to_fahrenheit(kelvin)
else:
    print("Невірний тип температури!")

print(f"Температура у Цельсіях: {celsius:.2f} °C")
print(f"Температура у Фаренгейтах: {fahrenheit:.2f} °F")
print(f"Температура у Кельвінах: {kelvin:.2f} K")

'''task3'''
