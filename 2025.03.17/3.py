def is_leap_year(year):
    """
    Определяет, является ли год високосным.

    Год является високосным, если:
    - Он делится на 4, но не делится на 100, или
    - Он делится на 400.

    Args:
        year (int): Год для проверки.

    Returns:
        bool: True, если год високосный, иначе False.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


# Получение пользовательского ввода (номер года)
year = int(input())

# Проверка на високосность
if is_leap_year(year):
    print("да")
else:
    print("нет")