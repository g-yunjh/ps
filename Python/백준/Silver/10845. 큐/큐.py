from collections import deque

queue = deque()
out = []

n = int(input())
for i in range(n):
    com  = input()
    if com == "pop":
        if len(queue) == 0:
            out.append(-1)
        else:
            out.append(queue[0])
            queue.popleft()
    elif com == "size":
        out.append(len(queue))
    elif com == "empty":
        if len(queue) == 0:
            out.append(1)
        else:
            out.append(0)
    elif com == "front":
        if len(queue) == 0:
            out.append(-1)
        else:
            out.append(queue[0])
    elif com == "back":
        if len(queue) == 0:
            out.append(-1)
        else:
            out.append(queue[-1])
    else:
        queue.append(com.split(" ")[1])

for i in out:
    print(i)