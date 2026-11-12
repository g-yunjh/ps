def solution(citations):
    citations.sort(reverse = True)
    h = citations[0]
    while True:
        cnt = 0
        for i in citations:
            if i >= h:
                cnt += 1
            else:
                break
        if cnt >= h:
            if len(citations) - cnt <= h:
                return h
            else:
                h -= 1
        else:
            h -= 1