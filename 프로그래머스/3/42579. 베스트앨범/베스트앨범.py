def solution(genres, plays):
    arr = []
    for i in range(len(genres)):
        arr.append([genres[i], plays[i], i])
    
    m = {}
    for i in arr:
        if i[0] in m:
            m[i[0]] += i[1]
        else:
            m[i[0]] = i[1]
    m = sorted(m.items(), key = lambda x: x[1], reverse = True)

    t0 = []
    for i in m:
        tmp = []
        for j in arr:
            if j[0] == i[0]:
                tmp.append(j[1:])
        t0.append(tmp)
    
    ans = []
    for i in t0:
        i.sort(key = lambda x: (-x[0], x[1]))
        cnt = 0
        for j in i:
            if cnt < 2:
                ans.append(j[1])
                cnt += 1
    return ans
        
            