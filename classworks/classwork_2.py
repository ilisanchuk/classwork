n = int(input('Введите количесвто чисел в списке: '))
numbers = []
numbers_2 = []
for i in range(n):
    number = int(input())
    numbers.append(number)
    if number % 2 == 0:
        numbers_2.append(number)
print('Список чисел: ', numbers)
print('Четные числа из списка: ', numbers_2)