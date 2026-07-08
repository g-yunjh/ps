from collections import deque

def solution(begin, target, words):
    l = len(words[0])
    q = deque()
    for w in words:
        c = 0
        for i in range(l):
            if begin[i] != w[i]:
                c += 1
            if c > 1:
                break
        if c == 1:
            q.append([w, 1])
    if len(q) == 0:
        return 0
    for i in q:
        if i[0] in words:
            words.remove(i[0])
    
    while len(q) > 0:
        if q[0][0] == target:
            return q[0][1]
        for w in words:
            c = 0
            for i in range(l):
                if q[0][0][i] != w[i]:
                    c += 1
                if c > 1:
                    break
            if c == 1:
                q.append([w,q[0][1] + 1])
        for i in q:
            if i[0] in words:
                words.remove(i[0])
        q.popleft()
    
    return 0