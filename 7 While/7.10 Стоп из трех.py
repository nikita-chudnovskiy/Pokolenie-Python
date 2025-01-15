word = input()
count = 0
while word not in ('стоп', 'хватит', 'достаточно'):
    count += 1
    word = input()
print(count)

count = 0
while (world := input()) not in ('стоп', 'хватит', 'достаточно'):
    count += 1
print(count)
