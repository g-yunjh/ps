import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < k:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        combined = first + second * 2
        
        heapq.heappush(scoville, combined)
        cnt += 1
    
    return cnt