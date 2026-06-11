def solution(clothes):
    m = {}
    
    for c in clothes:
        if c[1] in m:
            m[c[1]] += 1
        else:
            m[c[1]] = 2
    
    ans = 1
    for i in m.items():
        ans *= i[1]
    return ans - 1