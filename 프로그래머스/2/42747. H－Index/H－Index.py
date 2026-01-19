def solution(citations):
    citations.sort(reverse = True)
    h = citations[0]
    while True:
        up = 0
        for citation in citations:
            if citation >= h:
                up += 1
            else:
                break
        if (up >= h) and (len(citations) - up <= h):
            return h
        else:
            h -= 1
        
            
        