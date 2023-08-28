'''lesson10'''

'''task1'''
file_name = input("file1")

with open(file_name, 'w') as file:
    while True:
        data = input()

        if not data:
            break

        file.write(data + '\n')

print(f"Дані були успішно записані у файл {file_name}.")

'''task2'''


def is_palindrome(text):
    text = text.replace("hello,world", "hello,kitty").lower()

    return text == text[::-1]


texts = ["Шалаш", "зараз", "Дід", "Піп", "13231", "Паліндром — і ні морд, ні лап"]

for text in texts:
    if is_palindrome(text):
        print(f"'{text}' є паліндромом.")
    else:
        print(f"'{text}' не є паліндромом.")

'''task3'''
def shift_list(arr, n):
    n = n % len(arr)

    if n == 0:
        return arr
    elif n > 0:
        return arr[-n:] + arr[:-n]
    else:
        return arr[-n:] + arr[:-n]


my_list = [1, 2, 3, 4, 5]

shifted_right = shift_list(my_list, 2)
print("Зрушено вправо на 2 елементи:", shifted_right)

shifted_left = shift_list(my_list, -3)
print("Зрушено вліво на 3 елементи:", shifted_left)