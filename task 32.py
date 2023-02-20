# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input('введите размер массива - '))
array1 = list()
for i in range(n):
    array1.append(int(input(f'Введите {i + 1} элементы массива - ')))
print(f'Изначальный массив {array1}')

min_range = int(input('Задайте минимальный диапазон - '))
max_range = int(input('Задайте максимальный диапазон - '))
array2 = list()

for i in range(len(array1)):
    if min_range <= array1[i] <= max_range:
        array2.append(array1[i])
print(f'Элементы, попавшие в диапазон {array2}')