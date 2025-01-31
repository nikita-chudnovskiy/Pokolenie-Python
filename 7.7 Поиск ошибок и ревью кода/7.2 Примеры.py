i = 1
while i < 101:
    if i % 7 == 0:
        print(i)
    i += 1  # Правильный отступ

for i in range(7, 101, 7):
    if i % 7 == 0:
        print(i)

a = 0
for i in range(1, 1001):
    if i % 2 == 1:
        a = a + i
print(a)

total = 0  # name total
for i in range(1, 6, 2): # шаг убрали if
        print(i)
        total += i
print(total)
