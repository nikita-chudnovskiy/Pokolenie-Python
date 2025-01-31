# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


#
# num = int(input())
# flag = True
#
# for i in range(2, num//2+1):
#     if num % i == 0:
#         flag = False
#
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# Улучшили в 4000 раз
num = int(input())
flag = True

for i in range(2, int(num**0.5)+1): # num **0.5 # Улучшили в 4000 раз
    if num % i == 0:
        print(i)
        flag = False

if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')


num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):  # num **0.5 # Улучшили в 4000 раз
    if num % i == 0:
        print(i)
        flag = False
        break # В случае если число является составным и мы нашли его первый делитель
              # (отличный от 1), мы прерываем цикл с помощью оператора break:

if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')
