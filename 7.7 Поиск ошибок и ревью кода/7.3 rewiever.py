# 6
# 453
# 455623
# 25
# 0
# 65
# 112
# 44
# 3
# 90
from xml.sax.saxutils import escape

count = 0
mult = 1                        # 1: неправильно задана переменная (был 0), заодно переименовал
for _ in range(1, 11):          # 2: неправильно задана граница диапозона (было 10)
    num = int(input())
    if num >= 0:                # 3: неправильно установлено равенство (было > 0)
        mult *= num
        count += 1
if count > 0:
    print(count, mult, sep='\n') # 4: задан вывод не той переменной (был x)
else:
    print('NO')
