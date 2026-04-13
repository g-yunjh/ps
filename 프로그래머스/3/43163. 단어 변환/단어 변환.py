from collections import deque

def dif(n, m):
    cnt = 0
    for i in range(len(n)):
        if n[i] != m[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    queue = deque()
    queue.append([begin])
    while queue:
        i = queue.popleft()
        for word in words:
            if word not in i:
                if dif(i[-1], word):
                    if word == target:
                        return len(i)
                    else:
                        queue.append(i + [word])
    return 0
