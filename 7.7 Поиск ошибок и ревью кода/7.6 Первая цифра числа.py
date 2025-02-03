n = int(input())
while n > 9:
    n //= 10
print(n)

# ниже код переменную можно и не создавать
n = int(input())
while n > 0:
    last = n % 10
    n //= 10
print(last)
