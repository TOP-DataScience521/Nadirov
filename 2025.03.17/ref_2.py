num1 = int(input('введите первое число: '))
num2 = int(input('введите второе число: '))

quot = num1 // num2
rem = num1 % num2

# альтернативно
# quot, rem = divmod(num1, num2)

if rem:
    print(
        f'{num1} не делится на {num2} нацело',
        f'неполное частное: {quot}',
        f'остаток: {rem}',
        sep='\n'
    )
else:
    print(
        f'{num1} делится на {num2} нацело',
        f'частное: {quot}',
        sep='\n'
    )

