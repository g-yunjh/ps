def solution(genres, plays):
    g = {}
    for i in range(len(plays)):
        if genres[i] in g:
            g[genres[i]] += plays[i]
        else:
            g[genres[i]] = plays[i]
    g = sorted(g.items(), key = lambda x: -x[1])
    arr = []
    for i in g:
        tmp  = []
        for j in range(len(plays)):
            if genres[j] == i[0]:
                tmp.append([plays[j], j])
        arr.append(tmp)
    
    result = []
    for a in arr:
        a.sort(key = lambda x: -x[0])
        for i in range(len(a)):
            if i > 1:
                break
            result.append(a[i][1])
    return result