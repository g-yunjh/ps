def solution(n, words):
    arr = []
    arr.append(words[0])
    t = 0
    for i in range(1, len(words)):
        if words[i] in arr or arr[-1][-1] != words[i][0]:
            t = i + 1
            break
        else:
            arr.append(words[i])
    if arr == words:
        return [0,0]
    
    num = t % n
    if num == 0:
        num = n
        cnt = t // n
        return [num, cnt]
    else:
        return [num, t // n + 1]
    
    