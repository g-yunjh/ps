def solution(k, tangerine):
    tangerine.sort()
    tmp = 0
    cnt = 0
    arr = []
    for t in tangerine:
        if t != tmp and cnt != 0:
            arr.append([tmp, cnt])
            tmp = t
            cnt = 1
        elif cnt == 0:
            tmp = t
            cnt = 1
        else:
            cnt += 1
    arr.append([tmp, cnt])
    
    arr.sort(key = lambda x : x[1], reverse = True)
        
    for i in range(len(arr)):
        if k - arr[i][1] <= 0:
            return i + 1
        else:
            k -= arr[i][1]
            
        