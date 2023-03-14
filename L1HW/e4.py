a = int(input("Input positive integer number:"))

max_num = a % 10

a_left = a // 10

# Разбираем введенное число на цифры и ищем максимальное. Цикл заканчивается, когда остается последняя цифра справа.

while a_left // 10 > 0:
    max_num1 = a_left % 10
    if max_num1 > max_num:
        max_num = max_num1
    a_left = a_left // 10

# Сравниваем последнюю цифру справа с максимальным значением, полученным в результате цикла.
# Если последняя цифра больше, то она и будет максимальной.

if a_left > max_num:
    max_num = a_left

print("Max number:", max_num)
