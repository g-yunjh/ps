def solution(numbers, target):
    arr = [[] for i in range(len(numbers))]
    arr[0].extend([-numbers[0], numbers[0]])
    for i in range(1, len(numbers)):
        for j in arr[i-1]:
            arr[i].append(j-numbers[i])
            arr[i].append(j+numbers[i])
    return arr[-1].count(target)

