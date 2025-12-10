import sys
input = sys.stdin.readline

n = int(input())

ans = []
for i in range(n):
    arr = list(map(int, list(str(i))))
    arr.append(i)
    if (sum(arr) == n):
        ans.append(i)

if (len(ans) == 0):
    print(0)
else:
    print(min(ans))