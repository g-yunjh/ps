from collections import deque
def solution(skill, skill_trees):
    ans = 0
    arr = []
    for s in skill_trees:
        tmp = deque(skill)
        t = True
        for i in s:
            if len(tmp) > 0  and i in tmp:
                if tmp[0] == i:
                    tmp.popleft()
                else:
                    t = False
                    break
        if t == True:
            # arr.append(s)
            ans += 1
                    
    return ans