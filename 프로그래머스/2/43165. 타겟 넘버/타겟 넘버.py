def solution(numbers, target):
    d = [[-numbers[0], numbers[0]]]
    for i in range(len(numbers)-1):
        tmp = []
        for j in d[i]:
            tmp.append(j+numbers[i+1])
            tmp.append(j-numbers[i+1])
        d.append(tmp)
    return d[-1].count(target)
            