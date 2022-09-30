#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input('Введите число: '))
fibo = []
a, b = 0, 1
for i in range(n):
    fibo.insert(0, a)
    a, b = b, a - b
a, b = 1, 1
for i in range(n-1):
    fibo.append(a)
    a, b = b, a + b
print(fibo)