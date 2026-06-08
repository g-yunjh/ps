from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    cnt = 0
    
    while True:
        if q[0] == max(q):
            cnt += 1
            if location == 0:
                return cnt 
            q.popleft()
            location -= 1
        else:
            tmp = q[0]
            q.append(tmp)
            q.popleft()
            location -= 1
            if location < 0:
                location = len(q) + location
        
        