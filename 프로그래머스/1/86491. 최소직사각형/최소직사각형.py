def solution(sizes):
    x = []
    y = []
    for s in sizes:
        s.sort()
        x.append(s[0])
        y.append(s[1])
    return max(x) * max(y)
    