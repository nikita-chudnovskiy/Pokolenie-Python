mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break

   mult *= i
print(mult)

# #если 2.4.6.8.10 - не считаем
# если 9 заканчиваем
# 1.3.5.7
# число = число * i
# получаем
# 1*1=1
# 1*3=3
# 3*5=15
# 15*7=105