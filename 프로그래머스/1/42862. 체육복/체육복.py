def solution(n, lost, reserve):
    arr = [1]*(n+2)
    arr[0] = 0
    arr[-1] = 0
    for i in lost:
        arr[i] -= 1
    for i in reserve:
        arr[i] += 1
    for i in range(1, n+1):
        if arr[i] == 0:
            if arr[i-1] > 1:
                arr[i-1] -= 1
                arr[i] += 1
            elif arr[i+1] > 1:
                arr[i+1] -= 1
                arr[i] += 1
    cnt = 0
    for i in arr:
        if i > 0:
            cnt += 1
    return cnt
            
        