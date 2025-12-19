def solution(array, commands):
    answer = []
    for c in commands:
        tmp = []
        for i in range(c[0] - 1, c[1]):
            tmp.append(array[i])
        tmp.sort()
        answer.append(tmp[c[2] - 1])
            
    return answer