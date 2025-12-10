import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort(reverse=True)

cnt = 0
for i in arr:
    if k == 0:
        break
    elif i <= k:
        cnt += k//i
        k = k % i

print(cnt)
