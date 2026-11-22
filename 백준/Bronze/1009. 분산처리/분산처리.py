t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if str(a)[-1] in ['1', '5', '6']:
        print(int(str(a)[-1]))
    elif str(a)[-1] == '0':
        print(10)
    elif str(a)[-1] in ['2', '3', '7', '8']:
        a = a**(b%4+4)
        print(int(str(a)[-1]))

    else:
        a = a**(b%2+2)
        print(int(str(a)[-1]))

