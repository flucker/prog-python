# Task 1
# Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
# Примітка: щасливим квитком називається число, у якому, при парній кількості цифр, сума цифр його лівої половини дорівнює сумі цифр його правої половини.
# Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.
number = input('number - ')
number = list(map(int, number))
half_index = int(len(number) / 2)
print('Lucky number' if sum(number[:half_index]) == sum(number[half_index:]) else 'Try another number')

# Task 2
# З клавіатури вводиться число (шестизначне). Перевірити, чи воно є паліндромом.
# Примітка: Паліндром називається число, слово або текст, які однаково читаються зліва направо і справа наліво.
# Наприклад, це числа 143341, 5555, 7117 і т.д.
number = input('number - ')
number = list(number)
number_reversed = number[:]
number_reversed.reverse()
print('Palindrome' if number == number_reversed else 'Try another number')

# Task 3
# Дано коло з центром на початку координат та радіусом 4. Користувач вводить з клавіатури координати точки x та y. Написати програму, яка визначить, лежить ця точка всередині кола чи ні
x = int(input('x - '))
y = int(input('y - '))
radius = 4
print('Point inside circle' if radius ** 2 >= x ** 2 + y ** 2 else 'Point outside circle')