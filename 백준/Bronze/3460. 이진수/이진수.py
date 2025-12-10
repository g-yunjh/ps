t = int(input())
for _ in range(t):
    n = int(input())
    pos = 0
    ans = []
    while n > 0:
        if n & 1:
            ans.append(pos)
        n >>= 1
        pos += 1
    print(" ".join(map(str, ans)))
