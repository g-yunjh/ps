from itertools import permutations
def solution(k, dungeons):
    arr = permutations(dungeons, len(dungeons))
    arr = list(arr)
    max_cnt = 0
    for i in arr:
        h = k
        cnt = 0
        for j in i:
            if j[0] > h:
                break
            else:
                h -= j[1]
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt
        
    