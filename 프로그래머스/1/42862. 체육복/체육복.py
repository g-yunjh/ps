def solution(n, lost, reserve):
    answer = 0
    
    # solution
    dual = []
    temp = []
    for i in lost:
        if i in reserve:
            dual.append(i)
        else:
            temp.append(i)

    dual.sort()
    temp.sort()
    lost = dual + temp
        
    
    arr = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            arr.append(i)
        elif i - 1 in reserve:
            reserve.remove(i - 1)
            arr.append(i)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            arr.append(i)
        
    answer = n - len(lost) + len(arr)

    return answer