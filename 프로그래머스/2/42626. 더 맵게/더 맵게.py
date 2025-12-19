import heapq

def solution(s, k):
    heap = []
    for i in s:
        heapq.heappush(heap, i)
        
    cnt = 0
    while (heap[0] < k):
        if (len(heap) == 1):
            return -1
        else:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
            cnt += 1
        
    return cnt
        
            