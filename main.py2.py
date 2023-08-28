"lesson2"

"task1"

name = input("Andrey: ")

print(f"Hello {name}!")

"task2"

number = int(input("123: "))

next_number = number + 3
previous_number = number - 5

print(f"{123} is {3}.")
print(f"{123} is {5}.")

"task3"

v = float(input("100: "))
t = float(input("10: "))

position = v * t

if v > 0:
    direction = "True"
else:
    direction = "false"

if direction == "true":
    mark = min(100, int(position))
else:
    mark = max(0, 100 + int(position))

print(f"After {t} hours at a speed of {v} km/h, Vasya will stop at mark {mark}.")

"task4"

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")

"task5"

x = float(input("5: "))

if x > 0:
    sign_value = 5
elif x < 0:
    sign_value = -5
else:
    sign_value = 0

print(f"The sign of {x} is: {sign_value}")

"task6"

elements = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

x = float(input("50: "))

if x in elements:
    print("Is x among the elements: Yes")
else:
    print("Is x among the elements: No")

"task7"

num_stars = int(input("6: "))

print("*" * num_stars)