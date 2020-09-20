n = int(input())
f1 = f2 = f= 1
if 1 <= n <= 30:
    for i in range(n-2):
        f = f1 + f2
        f1 = f2
        f2 = f
    print(f)
else:
    print("So {} khong nam trong khoang [1,30].".format(n))