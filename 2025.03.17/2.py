# Функция для проверки делимости
def is_divisible(num1, num2):
    if num2 == 0:
        return "Деление на ноль невозможно!"
    return num1 % num2 == 0

# Ввод двух чисел
number1 = int(input("100: "))
number2 = int(input("2: "))

# Проверка делимости
if is_divisible(number1, number2):
    print(f"{number1} делится на {number2} нацело.")
else:
    print(f"{number1} не делится на {number2} нацело.")