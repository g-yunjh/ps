def solution(array, commands):
    answer = []
    
    # solution
    for arr in commands:
        temp_arr = []
        for i in range(arr[0] - 1, arr[1]):
            temp_arr.append(array[i])
        temp_arr.sort()
        answer.append(temp_arr[arr[2] - 1])
    
    return answer