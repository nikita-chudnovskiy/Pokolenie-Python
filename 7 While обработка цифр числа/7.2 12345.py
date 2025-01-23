# num = 12345
# print(num % 10)  # 5
# print((num // 10))  # 1234


num = 12345
product = 1
while num != 0:
    last_digit = num % 10
    print(last_digit)
    product = product * last_digit # 5 20 60 120 5*4  20*3 60*2 120*1
    print(product)

    num = num // 10
    print(num) # num в конце 0


print(product)