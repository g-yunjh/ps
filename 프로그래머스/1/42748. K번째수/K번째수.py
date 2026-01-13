def solution(array, commands):   
    answer = []
    for cmd in commands:
        arr = []
        for i in range(cmd[0] - 1, cmd[1]):
            arr.append(array[i])
        arr.sort()
        answer.append(arr[cmd[2] - 1])
    
    return answer
        