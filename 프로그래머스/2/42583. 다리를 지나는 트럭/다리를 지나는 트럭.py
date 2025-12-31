from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque()
    cnt = 0
    while (len(bridge) + len(trucks) != 0):
        if (len(trucks) > 0):
            if (sum([w for w, t in bridge]) + trucks[0] <= weight):
                bridge.append([trucks[0], 0])
                trucks.popleft()
        
        for i in bridge:
            i[1] += 1
        
        if (bridge[0][1] == bridge_length):
            bridge.popleft()
        
        cnt += 1
    
    return cnt + 1
            