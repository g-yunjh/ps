from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0
    
    while queue:
        curr = queue.popleft()
        # 현재 프로세스보다 우선순위가 높은 게 하나라도 있는지 확인
        if any(curr[0] < q[0] for q in queue):
            queue.append(curr)
        else:
            answer += 1
            if curr[1] == location:
                return answer