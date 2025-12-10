import sys
input = sys.stdin.readline

n = int(input())
ans = n
for i in range(n):
    w = input()
    prev = ''
    arr = []
    for j in w:
        if j == prev:
            continue
        elif j not in arr:
            arr.append(j)
            prev = j
        elif j in arr:
            prev = j
            ans -= 1
            break

print(ans)
