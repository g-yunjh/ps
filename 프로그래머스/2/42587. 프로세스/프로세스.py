from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque()
    for i in range(len(priorities)):
        queue.append([i, priorities[i]])
    
    cnt = 0
    while queue:
        if (queue[0][1] == max(queue, key=lambda x: x[1])[1]):
            if (queue[0][0] == location):
                answer = cnt + 1
                break
            else:
                cnt += 1
                queue.popleft()
        else:
            queue.append(queue[0])
            queue.popleft()
    return answer