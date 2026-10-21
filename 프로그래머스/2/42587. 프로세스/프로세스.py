from collections import deque

def solution(priorities, location):
    idx = location
    p = deque(priorities)
    m = max(p)
    cnt = 1
    while True:
        if p[0] == m:
            if idx == 0:
                return cnt
            else:
                idx -= 1
                cnt += 1
                p.popleft()
                m = max(p)
        else:
            if idx == 0:
                p.append(p[0])
                p.popleft()
                idx = len(p) - 1
            else:
                p.append(p[0])
                p.popleft()
                idx -= 1
    
            
        