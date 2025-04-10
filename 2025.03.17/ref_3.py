year = int(input('введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
# альтернативно
# if not year % 4 and year % 100 or not year % 400:
    print('да')
else:
    print('нет')

