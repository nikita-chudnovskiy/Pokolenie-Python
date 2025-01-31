# s = input()
# while s != 'КОНЕЦ':
#     print(s)
#     s =input()

s = input()
while s != 'КОНЕЦ' and s != 'конец':
    print(s)
    s = input()

word = input()
while not (word == "КОНЕЦ" or word == "конец"):
    print(word)
    word = input()

word = input()
while 'КОНЕЦ' != word != 'конец':
    print(word)
    word = input()

# 3.10 python
while (word := input()).upper() != 'КОНЕЦ':
    print(word)
