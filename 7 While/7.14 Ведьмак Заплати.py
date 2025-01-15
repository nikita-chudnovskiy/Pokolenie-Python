n = int(input())
count = 0

while n != 0:
    if n >= 25:
        n -= 25
        count += 1
    elif n >= 10:
        n -= 10
        count += 1
    elif n >= 5:
        n -= 5
        count += 1
    elif n >= 1:
        n -= 1
        count += 1

print(count)

n = int(input())
k = 0
for i in (25, 10, 5, 1):
    while n // i > 0:
        k += 1
        n -= i
print(k)

n =49//25
print(n)