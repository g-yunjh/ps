def solution(clothes):
    clothes.sort(key = lambda x: x[1])
    
    cnt = 0
    tmp = clothes[0][1]
    arr = []
    for i in clothes:
        if (i[1] == tmp):
            cnt += 1
        else:
            tmp = i[1]
            arr.append(cnt)
            cnt = 1
    
    arr.append(cnt)
    
    answer = 1
    for i in arr:
        answer = answer * (i+1)
    
    return answer - 1
        
        