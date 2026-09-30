def solution(x, y, n):
    d = [[x]]
    while True:
        if y in d[-1]:
            return len(d) - 1
        tmp = []
        for i in d[-1]:
            tmp.append(i+n)
            tmp.append(i*2)
            tmp.append(i*3)
        if (min(tmp) > y):
            return -1
        d.append(list(set(tmp)))
        
