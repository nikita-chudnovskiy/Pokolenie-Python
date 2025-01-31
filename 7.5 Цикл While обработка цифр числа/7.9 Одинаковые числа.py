n = int(input())
flag = 'YES'
last = n % 10
while n != 0:
    first = n % 10
    if last != first:
        flag = 'NO'
    n = n // 10
print(flag)
