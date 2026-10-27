import heapq

def solution(jobs):
    jobs.sort()
    heap = []
    now, total_time, i = 0, 0, 0
    n = len(jobs)

    while i < n or heap:
        while i < n and jobs[i][0] <= now:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if heap:
            duration, request_time = heapq.heappop(heap)
            now += duration
            total_time += (now - request_time)
        else:
            now = jobs[i][0]

    return total_time // n