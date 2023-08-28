'''lesson9'''

'''task1'''
def count_points(win, draw, loss):
    return (win * 3) + draw - loss

win = int(input("Введіть кількість перемог: "))
draw = int(input("Введіть кількість нічиїх: "))
loss = int(input("Введіть кількість поразок: "))

points = count_points(win, draw, loss)
print(f"Кількість очок: {points}")

'''task2'''


def hide_email(email):
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]

    if len(username) > 2:
        username = username[:2] + '*' * (len(username) - 2)

    if len(domain) > 3:
        domain = '*' * (len(domain) - 3) + domain[-3:]

    return f"{username}@{domain}"


email = input("Введіть електронну адресу: ")
hidden_email = hide_email(email)
print(f"Прихована адреса: {hidden_email}")

'''task3'''
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


sentence = input("Введіть рядок: ")
result = longest_word(sentence)
print(f"Найдовше слово: {result}")

'''task4'''
def fake_string(initial_string, old_word, new_word, count):
    return initial_string.replace(old_word, new_word, count)

input_string = input("Введіть рядок: ")
old_word = input("Введіть слово для заміни: ")
new_word = input("Введіть нове слово: ")
count = int(input("Введіть кількість замін: "))

result = fake_string(input_string, old_word, new_word, count)
print(f"Змінений рядок: {result}")