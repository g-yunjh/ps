import heapq

def solution(jobs):
    jobs.sort() # 요청 시간 순으로 정렬
    n = len(jobs)
    time, i, answer = 0, 0, 0
    wait_list = [] # 처리 대기 중인 작업을 담는 힙
    
    while i < n or wait_list:
        # 현재 시간 이전에 요청된 모든 작업을 힙에 삽입
        while i < n and jobs[i][0] <= time:
            heapq.heappush(wait_list, (jobs[i][1], jobs[i][0])) # (소요시간, 요청시간)
            i += 1
            
        if wait_list:
            duration, start = heapq.heappop(wait_list)
            time += duration
            answer += (time - start)
        else:
            # 처리할 작업이 없으면 다음 작업 요청 시간으로 점프
            time = jobs[i][0]
            
    return answer // n