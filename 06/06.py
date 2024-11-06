# Task 1
# Напишіть програму, яка приймає рядок та виводить її перший та останній символ.
text = input('text - ')
print(f'first - {text[0]}, last - {text[-1]}')

# Task 2
# Напишіть програму, яка виводить рядок повністю у верхньому регістрі, а потім у нижньому.
text = input('text - ')
print(text.upper())
print(text.lower())

# Task 3
# Напишіть програму, яка перевіряє, чи міститься "Python" у даному рядку.
text = input('text - ')
print('Python in string' if 'Python' in text else 'Python not in string')

# Task 4
# Користувач вводить із клавіатури ім'я людини. Напишіть програму для перевірки введеного імені на валідність (мається на увазі, що, наприклад, ім'я не може містити цифр, воно повинно починатися з великої літери, за якою повинні йти маленькі).
name = input('name - ')
print('Valid name' if name.isalpha() and name.istitle() else 'Invalid name')

# Task 5
# Напишіть програму, яка приймає рядок та підраховує кількість слів у ній.
text = input('text - ')
print(len(text.split()))

# Task 6
# Напишіть програму, яка підраховує частоту кожного слова у рядку.
text = input('text - ')
for word in text.split():
    if word in text:
        print(f'{word} - {text.count(word)}')
        text = text.replace(word, '')

# Task 7
# Напишіть програму, яка приймає рядок і видаляє всі символи, окрім літер і цифр.
text = input('text - ')
text = ''.join(text.split())
for letter in text:
    if not letter.isalnum():
        text = text.replace(letter, '')
print(text)

# Task 8
# Напишіть програму, яка приймає рядок і виводить найдовше слово у ній.
text = input('text - ').split()
lengths = list(map(len, text))
print(text[lengths.index(max(lengths))])

# Task 9
# Напишіть програму, яка кодує рядок, замінюючи кожну літеру на її номер в алфавіті (тільки для латинського алфавіту, наприклад, A = 1, B = 2).
text = input('text - ')
for letter in text:
    if letter in text and letter.isalpha():
        text = text.replace(letter, str(ord(letter.lower()) - 96))
print(text)