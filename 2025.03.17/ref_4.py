try:
    num = int(input('введите однозначное число: '))
    
except ValueError:
    print('не является числом')

else:
    if num == 1 or num == 2 or num == 4 or num == 8:
        print('да')
    else:
        print('нет')

