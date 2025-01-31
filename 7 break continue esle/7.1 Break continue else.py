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

# Возможно, вам может показаться, что бесконечные циклы лишены смысла, однако это не совсем так.
# Например, вы можете написать программу, которая запускается и работает, постоянно
# принимая запросы на обслуживание. Программный код такой программы может выглядеть так:
#
# while True:
#     query = get_new_query() #  получаем новый запрос на обработку
#     query.process()         #  обрабатываем запрос

# Напишем программу, которая выводит все числа от 1 до 100, кроме чисел 7, 17, 29 и 78.

for i in range(1, 10):
    if i == 3 or i == 5 or i == 7 or i == 0:
        continue  # переходим на следующую итерацию
    print(i)