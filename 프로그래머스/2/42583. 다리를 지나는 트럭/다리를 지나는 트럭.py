from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    w = 0
    q = deque()
    t = deque(truck_weights)
    for i in range(bridge_length):
        q.append(0)
    while sum(t) + w != 0:
        cnt += 1
        if len(t) == 0:
            w -= q[0]
            q.popleft()
        else:
            w -= q[0]
            q.popleft()
            if w + t[0] > weight:
                q.append(0)
            else:
                q.append(t[0])
                w += t[0]
                t.popleft()
    return cnt
        
            