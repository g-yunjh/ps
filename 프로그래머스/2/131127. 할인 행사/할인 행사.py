def solution(want, number, discount):
    arr = []
    for i in range(len(want)):
        arr += [want[i]] * number[i]

    cnt = 0
    for i in range(len(discount) - 9):
        tmp = arr.copy()
        for j in range(i, i+10):
            if discount[j] in tmp:
                tmp.remove(discount[j])
        if tmp == []:
            cnt += 1
    
    return cnt
            