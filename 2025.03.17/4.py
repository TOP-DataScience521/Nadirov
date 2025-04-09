def is_single_digit_power_of_two(num):
    """
    Проверяет, является ли однозначное число степенью двойки.

    Args:
        num (int): Число для проверки.

    Returns:
        bool: True, если число является степенью двойки, иначе False.
    """
    return num in [1, 2, 4, 8]

# Получение пользовательского ввода
user_input = input("Введите однозначное целое число: ")

try:
    # Преобразование ввода в целое число
    number = int(user_input)
    
    # Проверка на однозначное число
    if 0 <= number < 10:
        if is_single_digit_power_of_two(number):
            print("да")
        else:
            print("нет")
    else:
        print("Введите однозначное целое число.")
except ValueError:
    print("Ошибка: введено не число.")

