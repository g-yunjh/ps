from itertools import permutations

def solution(k, dungeons):
    max_num = 0
    iter = []
    for i in range(len(dungeons)):
        iter.append(i)
    for i in permutations(iter):
        cnt = 0
        h = k
        for j in i:
            if h >= dungeons[j][0]:
                h -= dungeons[j][1]
                cnt += 1
        if cnt > max_num:
            max_num = cnt
    
    return max_num
       