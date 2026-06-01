import heapq

def solution(n, works):
    # 1. 모든 작업량을 음수로 변환하여 힙에 저장 (최대 힙 구현)
    heap = [-w for w in works]
    heapq.heapify(heap)
    
    # 2. n번 동안 가장 큰 값을 꺼내서 1 감소 후 다시 넣기
    for _ in range(n):
        max_val = heapq.heappop(heap)
        if max_val == 0:  # 작업량이 이미 0이면 더 이상 뺄 것이 없음
            return 0
        max_val += 1  # 음수이므로 +1을 해야 실제로는 -1 감소됨
        heapq.heappush(heap, max_val)
        
    # 3. 야근 지수(제곱의 합) 계산
    return sum(w ** 2 for w in heap)