from logging import getHandlerByName

n = 0

while n<5:
    n+=1
    if n ==4:
        break
    print(n)
else:
    print('Цикл завершен')

print()


# Напишем 2 кода
num = 666
n = num
flag = False
while n != 0:
    last = n % 10
    if last == 7:
        flag = True
        break        # прерываем цикл, так как число гарантированно содержит цифру 7
    n //= 10

if flag == True:
    print('Число', num, 'содержит цифру 7')
else:
    print('Число', num, 'не содержит цифру 7')

print()
n = 757
while n!=0:
    l=n%10
    if l ==7:
        print('Содержит', n, 'число',l)
        break
    n=n//10
else:
    print('Не содержит 7')