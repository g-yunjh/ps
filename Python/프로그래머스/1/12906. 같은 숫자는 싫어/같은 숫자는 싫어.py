def solution(arr):
    answer = []
    
    # solution
    temp = []
    temp.append(arr[0])
    for i in arr:
        if i != temp[-1]:
            temp.append(i)
    answer = temp
    
    return answer