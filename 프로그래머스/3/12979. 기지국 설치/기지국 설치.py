def solution(n, stations, w):
    arr = []
    tmp = 0
    for i in range(len(stations)):  
        arr.append(stations[i] - w - tmp - 1)
        
        tmp = stations[i] + w
        
        if i == len(stations) - 1:
            arr.append(n - (stations[i] + w))
    
    cnt  = 0
    arr = [i for i in arr if i > 0]
    while len(arr) > 0:
        for i in range(len(arr)):
            arr[i] = arr[i] - 2 * w - 1
            cnt += 1
        arr = [i for i in arr if i > 0]
    return cnt
    
        