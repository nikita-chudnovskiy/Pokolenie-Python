# функции range(), которая позволяет генерировать последовательность чисел

for i in range(1,6,1): # старт стоп шаг
    print(i,end=' ')
print()
for i in range(5,0,-1): # старт стоп шаг
    print(i, end=" ")
print('Взлетаем')
for i in range(100, 150):  # перебираем числа от 100 до 999
    if i % 10 == 7:        # используем остаток от деления на 10, для получения последней цифры
        print(i)