# Task 1
# Виведіть на екран 10 рядків із значенням числа Pi. У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.
import math
for i in range(2, 11):
    print(f'{math.pi:.{i}f}')

# Task 2
# Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери). Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту. Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"
text = input('text - ')
for i in range(1, len(text) + 1):
    pattern = text[:i]
    if text.count(pattern) * len(pattern) == len(text):
        print(pattern)
        break

# Task 3
# Напишіть скрипт для очищення тексту від HTML-тегів.
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, а другий закриває.
# - тег у собі може містити купу додаткової інформації. Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">
html = """
<ul class="menu" role="tree">
    <li class="python-meta current_item selectedcurrent_branch selected">
        <a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>
    </li>
    <li class="psf-meta ">
        <a href="https://www.python.org/psf/" title="The Python Software Foundation" >PSF</a>
    </li>
    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>
    </li>
    <li class="pypi-meta ">
        <a href="https://pypi.org/" title="Python Package Index" >PyPI</a>
    </li>
    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board" >Jobs</a>
    </li>
    <li class="shop-meta ">
        <a href="/community/"  >Community</a>
    </li>
</ul>
"""
while '<' in html:
    start = html.find('<')
    end = html.find('>')
    pattern = html[start:end + 1]
    html = html.replace(pattern, '')
else:
    res = html.split()
    res = '\n'.join(res)
    print(res)

# Task 4
# Напишіть програму, яка приймає рядок тексту і повертає словник, де ключами є слова, а значеннями - кількість входжень кожного слова в тексті.
import string
text = 'Python,python:python,awesome awesome language'
text = text.lower()

for i in string.punctuation:
    text = text.replace(i, ' ')

words = text.split()
counter = {}
for word in words:
    if word not in counter:
        counter[word] = words.count(word)
print(counter)

# Task 5
# Реалізуйте простий перекладач, який використовує словник для збереження пар слів. Користувач може вводити слово, а програма повертає його переклад. У цьому випадку, словник може використовуватись для збереження відповідностей між словами у різних мовах.
# Приклад:
# translations = {
#     'hello': 'привіт',
#     'goodbye': 'до побачення',
#     'cat': 'кіт',
#     'dog': 'собака'
# }
translations = {
    'cat': 'кот',
    'dog': 'собака',
    'mouse': 'мышь',
    'parrot': 'попугай'
}


word = input('word>>').lower().strip()
if word in translations:
    print(translations[word])
else:
    for key, value in translations.items():
        if value == word:
            print(key)
            break
    else:
        print('Такого слова нет в словаре')

# Task 6
# Реалізуйте просту програму для збереження контактів. Кожен контакт може мати ім'я як ключ та номер телефону як значення. Дозвольте користувачу додавати нові контакти, видаляти існуючі та отримувати номер телефону за ім'ям.
prompt = 'add - add contact\n' \
         'remove - remove contact\n' \
         'show - show all contacts\n' \
         'exit - exit\n' \
         '>>'

contacts = {}

while (ans := input(prompt).lower().strip()) != 'exit':
    if ans == 'add':
        name = input('name>>')
        phone = input('phone>>')
        contacts[name] = phone
    elif ans == 'remove':
        name = input('name>>')
        if name in contacts:
            del contacts[name]
        else:
            print('Contact not found')
    elif ans == 'show':
        for name, phone in contacts.items():
            print(f'{name}: {phone}')
    else:
        print('Invalid command')

# Task 7
# Напишіть програму, яка конвертуватиме суму з однієї валюти в іншу, використовуючи словник з курсами обміну.
currency = {
    'usd': {
        'sell': 42.50,
        'buy': 41.50
    },
    'eur': {
        'sell': 50.50,
        'buy': 49.50
    }
}

while True:
    currency_name = input('currency (USD, EUR)>>').lower().strip()
    if currency_name not in currency:
        print('Invalid currency')
        continue

    action = input('action (sell, buy)>>').lower().strip()
    if action not in currency[currency_name]:
        print('Invalid action')
        continue

    amount = float(input('amount>>'))
    money = amount / currency[currency_name][action] if action == 'sell' else amount * currency[currency_name][action]
    return_currency = currency_name if action == 'sell' else 'UAH'

    print(f'You will receive {money:.2f} {return_currency}')