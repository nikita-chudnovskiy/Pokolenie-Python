bukva = input()

file = open('tekst.txt', 'r', encoding='Utf8')

file = file.read().split()

for i in file:
    if i[0] == bukva:
        print(i)
    if i == i[::-1]:
        print(i)
