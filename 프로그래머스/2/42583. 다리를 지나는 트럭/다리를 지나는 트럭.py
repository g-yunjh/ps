from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0    
    q = deque([0] * bridge_length)
    t = deque(truck_weights)
    w = 0
    
    while w != 0 or len(t) != 0:
        cnt += 1
        if len(t) > 0 and w - q[0] + t[0] <= weight:
            w -= q[0]
            q.popleft()
            q.append(t[0])
            w += t[0]
            t.popleft()
        else:
            w -= q[0]
            q.popleft()
            q.append(0)
    
    return cnt