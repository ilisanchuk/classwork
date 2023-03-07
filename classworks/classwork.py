n = int(input('Введите количесвто чисел в списке: '))
numbers = []
numbers_squared = []
for i in range(n):
    number = int(input())
    numbers.append(number)
    numbers_squared.append(number ** 2)
print('Список чисел: ', numbers)
print('Список квадратов чисел: ', numbers_squared)