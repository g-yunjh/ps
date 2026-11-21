a, b = input().split()

a = a[2]+a[1]+a[0]
b = b[2]+b[1]+b[0]
a = int(a)
b = int(b)

if a < b:
    print(b)
else:
    print(a)
