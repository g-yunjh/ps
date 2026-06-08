from collections import deque

def solution(progresses, speeds):
    q = deque(progresses)
    s = deque(speeds)
    arr = []
    cnt = 0
    while q:
        if q[0] >= 100:
            q.popleft()
            s.popleft()
            cnt += 1
        elif cnt > 0:
            arr.append(cnt)
            cnt = 0
        else:
            for i in range(len(q)):
                q[i] += s[i]    
    arr.append(cnt)
    return arr
            