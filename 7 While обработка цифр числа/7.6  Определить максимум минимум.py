n = int(input())
max_last = 0
min_last = 10
while n != 0:
    last = n % 10
    if last > max_last:
        max_last = last

    if min_last > last:
        min_last = last

    n = n // 10
print('Максимальная цифра равна', max_last)
print('Минимальная цифра равна', min_last)
