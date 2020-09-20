n = int(input())
s = 0
for i in range(1,n//2 + 1):
    if not n%i:
        s = s + i
print(s)