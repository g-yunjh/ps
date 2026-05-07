from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    lim = len(queue1) + len(queue2)
    cnt = 0
    while sum1 != sum2:
        if sum1 > sum2:
            tmp = q1[0]
            q1.popleft()
            sum1 -= tmp
            q2.append(tmp)
            sum2 += tmp
            cnt += 1
        else:
            tmp = q2[0]
            q2.popleft()
            sum2 -= tmp
            q1.append(tmp)
            sum1 += tmp
            cnt += 1
        if cnt > lim * 2:
            return -1
    return cnt
            
        