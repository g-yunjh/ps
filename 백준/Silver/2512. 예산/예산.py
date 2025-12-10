import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

if sum(arr) <= m:
    print(max(arr))
else:
    lo, hi = 0, max(arr)
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        total = sum(x if x <= mid else mid for x in arr)
        if total <= m:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)
