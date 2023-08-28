'''lesson3'''

'''task1'''
number = int(input(335))

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

digit_sum = digit1 + digit2 + digit3

print(f"{digit_sum}")

'''task2'''
x = float(input(2,15))

decimal_part = int((x * 100) % 10)

print(f"2 {decimal_part}")

'''task3'''
list_ten = [10, 20, 30, 40, 50]

for item in reversed(list_ten):
    print(item)

'''task4'''
list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]

for num in list_of_six:
    if num % 5 == 0 and num <= 150:
        print(num)

'''task5'''
import random


random_number = random.randint(1, 10)

attempts = 3

for attempt in range(attempts):
    user_guess = int(input(f"Attempt {attempt + 1}/{attempts}: Enter a number from 1 to 10: "))

    if user_guess == random_number:
        print("You won!")
        break
    else:
        print("You lose!")

if user_guess != random_number:
    print(f"The correct number was: {random_number}")

'''task7'''
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}")
'''написал так потому что в математике не силен,не хочу науптать'''