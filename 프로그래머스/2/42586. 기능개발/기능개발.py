from collections import deque

def solution(progresses, speeds):
    answer = []
    
    # solution
    progresses = deque(progresses)
    speeds = deque(speeds)
    while True:
        cnt = 0
        for i in range(0, len(progresses)):
            progresses[i] += speeds[i]
        for i in list(progresses):
            if i < 100:
                break
            else:
                cnt += 1
                progresses.popleft()
                speeds.popleft()
        if cnt != 0:
            answer.append(cnt)
        cnt = 0
        if len(progresses) == 0:
            break
    
    return answer