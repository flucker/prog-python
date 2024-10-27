# Task 1
# Написати скрипт, який виводить задане число на екран, лише якщо введене число від’ємне.
n = int(input('number = '))
n < 0 and print(n)
# Task 2
# Написати скрипт, який перевіряє, чи введене користувачем цілочисельне значення менше 20 чи ні.
n = int(input('number = '))
n < 20 and print('lower than 20')
n >= 20 and print('greater than 20 or equal')
# Task 3
# Написати скрипт, який перевіряє, чи введене користувачем цілочисельне значення дорівнює нулю чи ні.
n = int(input('number = '))
n == 0 and print('zero')
n and print('not zero')
# Task 4
# Написати скрипт, який перевіряє, чи введене користувачем цілочисельне значення є парним чи непарним.
n = int(input('number = '))
n % 2 == 0 and print('Even')
n % 2 and print('Odd')
# Task 5
# Написати скрипт, який повертає найбільше число серед трьох, які введені користувачем.
n1 = int(input('number1 = '))
n2 = int(input('number2 = '))
n3 = int(input('number3 = '))
print(max(n1, n2, n3))