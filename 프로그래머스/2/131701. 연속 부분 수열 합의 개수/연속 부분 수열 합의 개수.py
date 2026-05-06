def solution(elements):
    extend = elements * 2
    arr = []
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            arr.append(sum(extend[j:j+i]))
    arr = set(arr)
    return len(arr)