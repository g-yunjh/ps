from collections import deque

def solution(progresses, speeds):
    cnt = 0
    p = deque(progresses)
    s = deque(speeds)
    ans = []
    while len(p) != 0:
        cnt += 1
        tmp = 0
        if p[0] + s[0] * cnt >= 100:
            while p[0] + s[0] * cnt >= 100:
                p.popleft()
                s.popleft()
                tmp += 1
                if len(p) == 0:
                    break
        if tmp != 0:
            ans.append(tmp)
    return ans
                
        
        
        