n = int(input())
for i in range(1, n + 1):
    if i >= 5 and i <= 9 or i >= 17 and i <= 37 or i >= 78 and i <= 87:  # 5-9 17-37 78-87
        continue
    print(i)

# Диапазон использовать это (5 <= i <= 9)
n = int(input())
for i in range(1, n + 1):
    if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
        continue

    print(i)
