n = int(input())
total = 0
while n >= 0:
    total += n
    n = int(input())
print(total)

total = 0
while (n := int(input())) >= 0:
    total += n
print(total)
