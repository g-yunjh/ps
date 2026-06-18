import heapq

def solution(jobs):
    answer = 0
    start = -1          # 바로 이전에 완료된 작업의 종료 시간
    now = 0             # 현재 시간
    i = 0               # 처리 완료된 작업의 개수
    heap = []           # 현재 대기 중인 작업들을 담을 우선순위 큐
    
    # 모든 작업을 처리할 때까지 반복
    while i < len(jobs):
        # 1. 현재 시점(now)까지 요청된 모든 작업을 힙에 삽입
        for job in jobs:
            if start < job[0] <= now:
                # 힙은 첫 번째 원소를 기준으로 정렬하므로 (소요시간, 요청시간) 순으로 넣음
                heapq.heappush(heap, [job[1], job[0]])
        
        # 2. 대기 중인 작업이 있는 경우
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]  # 현재 시간에 소요 시간을 더함
            answer += (now - current[1]) # (종료시간 - 요청시간)을 누적
            i += 1             # 처리된 작업 개수 증가
        else:
            # 3. 대기 중인 작업이 없다면 시간이 흘러야 함 (다음 작업의 요청 시간으로 점프)
            now += 1
            
    return answer // len(jobs)