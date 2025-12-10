import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

lo, hi = 1, max(arr)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0
    for x in arr:
        cnt += x // mid

    if cnt >= n:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
