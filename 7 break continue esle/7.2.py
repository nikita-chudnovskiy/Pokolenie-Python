# при i = 7 условие не верно, но print произошел раньше проверки и вывел ее на печать.
for i in range(10):
    print(i, end='*')
    if i > 6:
        break
print()
print(1,2,3,sep='@' ,end='finish')