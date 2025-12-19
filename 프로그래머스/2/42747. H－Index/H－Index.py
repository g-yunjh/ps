def solution(citations):
    citations.sort()
    
    h = citations[-1]
    while True:
        up = []
        under = []
        
        for i in citations:
            if (i >= h):
                up.append(i)
            else:
                under.append(i)
        
        if (len(up) >= h) & (len(under) <= h):
            return h
        else:
            h -= 1