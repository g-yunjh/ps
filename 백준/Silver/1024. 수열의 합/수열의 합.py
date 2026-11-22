n, l = map(int, input().split())

while l <= 100:
    if l % 2 == 0:
        if n % l == l // 2:
            tmp = (n // l) - (l // 2) + 1
            if tmp < 0:
                print(-1)
                break
            for i in range(l):
                print(tmp + i, end=" ")
            break
        else:
            l += 1
    else:
        if n % l == 0:
            tmp = (n // l) - (l // 2)
            if tmp < 0:
                print(-1)
                break
            for i in range(l):
                print(tmp + i, end=" ")
            break
        else:
            l += 1

if l > 100:
    print(-1)