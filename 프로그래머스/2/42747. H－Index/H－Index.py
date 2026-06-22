def solution(citations):
    citations.sort()
    cnt = len(citations)
    
    h = citations[-1]
    c = citations.index(h)
    while True:
        if cnt - c >= h:
            return h
        elif (h - 1) in citations:
            h -= 1
            c = citations.index(h)
        else:
            h -= 1
