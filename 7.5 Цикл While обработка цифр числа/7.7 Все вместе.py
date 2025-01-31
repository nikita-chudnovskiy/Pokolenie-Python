n = int(input())
max_last = 0
min_last = 10
summa = 0
kol = 0
proizvedenie = 1
pervaya = 0
l_posl = n % 10

while n != 0:
    last = n % 10

    summa += last
    kol += 1
    proizvedenie *= last
    pervaya = n % 10

    if last > max_last:
        max_last = last

    if min_last > last:
        min_last = last

    n = n // 10
last = pervaya

print(summa)                    # print('Сумма', summa)
print(kol)                      # print('Количество', kol)
print(proizvedenie)             # print('Произведение', proizvedenie)
print(summa/kol)                # print('Среднее', summa / kol)
print(pervaya)                  # print('ПЕРВАЯ', pervaya)
print(pervaya+l_posl)           # print(pervaya+l_posl)
# print(max_last)                # print('Максимальная цифра равна', max_last)
# print(min_last)                # print('Минимальная цифра равна', min_last)


n,sm,kol,pr = int(input()),0,0,1
np = n % 10
while n != 0:
    sm += n % 10
    kol +=1
    pr *= n % 10
    n1 = n
    n = n // 10
print(sm,kol,pr,sm/kol,n1,n1+np,sep='\n')
