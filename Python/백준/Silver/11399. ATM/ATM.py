import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
tmp = 0
for i in arr:
    ans += i
    ans += tmp
    tmp += i

print(ans)
