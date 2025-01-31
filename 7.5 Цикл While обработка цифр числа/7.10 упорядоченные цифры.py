n = int(input())
flag = True

while n >= 10:
    last = n % 10
    pred_last = n % 100 // 10
    if last > pred_last:
        flag = False
        break
    n = n // 10

if flag:
    print('YES')
else:
    print('NO')

# n=int(input())
# f='YES'
# while n>9:
#     if n%10>(n%100//10): # флаг меняется если посл больше предыдущего
#         f='NO'
#     n=n//10
# print(f)