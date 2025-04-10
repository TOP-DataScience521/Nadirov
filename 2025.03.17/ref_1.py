num1 = int(input('введите первое число: '))
num2 = int(input('введите второе число: '))
num3 = int(input('введите третье число: '))

total = 0
if num1 > 0:
    total += num1
if num2 > 0:
    total += num2
if num3 > 0:
    total += num3

# альтернативно
# total = (
#       (num1 if num1 > 0 else 0)
#     + (num2 if num2 > 0 else 0)
#     + (num3 if num3 > 0 else 0)
# )

print(total)

