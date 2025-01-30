result = 0
for i in range(10):
    n = int(input())
    if n < 0:
        break
    result += n
print(result)

# Если встречается 7
n = int(input())
number = n
flag = True
while n != 0:
    last_num = n % 10
    if last_num == 7:
        flag = False
        break
    n = n // 10  # n//=10
if flag:
    print('В числе нет 7 ')
else:
    print('В чиле есть 7 ', number)

# Бесконечный цикл
# while True:
#     print(('***')*3)

a = 0
b = 0
while True:
    if a == 1:
        print(a)
        break

    if b < 5:
        b+=1
        print(b)
        continue

    if b ==5:
        print('b = 5')
        break
