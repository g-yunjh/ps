def solution(s):
    answer = ''
    
    # solution
    arr = list(map(int, s.split()))
    max_num = arr[0]
    min_num = arr[0]
    for i in arr:
        if max_num < i:
            max_num = i
        if min_num > i:
            min_num = i
    answer = str(min_num) + " " + str(max_num)
        
    return answer