mx = -10**6 -1
s = 0
for _ in range(10):
    num = int(input())
    if num <= 0:
        s += num
    if num > mx and num < 0:
        mx = num
if s < 0:
    print(s)
    print(mx)
else:
    print("NO")


