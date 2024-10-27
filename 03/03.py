# Task 1
# Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці. На одному поверсі - 4 квартири. Напишіть програму, яка від користувача отримує номер квартири та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі. Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це.
room = int(input('room - '))
floors = 9
entrances = 4
rooms_on_floor = 4
if room < 1 or room > rooms_on_floor * floors * entrances:
    print('Invalid room')
else:
    entrance = room // (floors * rooms_on_floor)
    if room % (floors * rooms_on_floor):
        entrance += 1

    floor = (room - (floors*rooms_on_floor * (entrance - 1))) // rooms_on_floor
    if (room - (floors*rooms_on_floor * (entrance - 1))) % rooms_on_floor:
        floor += 1

    room_number_on_floor = room % rooms_on_floor
    if not room_number_on_floor:
        room_number_on_floor = rooms_on_floor
    print('entrance -', entrance)
    print('floor -', floor)
    print('room_number_on_floor -', room_number_on_floor)
# Task 2
# Написати програму, яка буде повертати для заданого року кількість днів. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400
year = int(input('year - '))
if year < 0:
    print('Invalid year')
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('leap year')
# Task 3
# Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої. Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує такий трикутник.
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a <= 0 or b <= 0 or c <= 0:
    print('Invalid values')
elif a + b > c and a + c > b and b + c > a:
    print('Valid triangle')
else:
    print('Invalid triangle')