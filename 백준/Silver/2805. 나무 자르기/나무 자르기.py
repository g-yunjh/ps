def search(arr, m):
    start = 0
    end = arr[0] - 1
    ans = 0
    while start <= end:
        h = (start + end) // 2
        cnt = 0
        for i in arr:
            if (i > h):
                cnt += i - h
        if cnt >= m:
            start = h + 1
            ans = h
        else:
            end = h - 1
    return ans


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

print(search(arr, m))