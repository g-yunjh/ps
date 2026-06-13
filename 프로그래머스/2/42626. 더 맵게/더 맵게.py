import heapq

def solution(s, k):
    heapq.heapify(s)
    
    cnt = 0
    while s[0] < k:
        if len(s) == 1:
            return -1
        
        t0 = heapq.heappop(s)
        t1 = heapq.heappop(s)
        heapq.heappush(s, t0 + t1 * 2)
        cnt += 1
    return cnt