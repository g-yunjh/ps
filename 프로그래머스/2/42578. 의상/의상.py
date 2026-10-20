def solution(clothes):
    d = {}
    
    for c in clothes:
        if c[1] in d:
            d[c[1]] += 1
        else:
            d[c[1]] = 1
    
    cnt = 1
    for i in d:
        cnt *= d[i] + 1
    return cnt - 1