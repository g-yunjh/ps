from collections import deque

queue = deque()

n = int(input())
for i in range(n):
    queue.append(i+1)

while True:
    if (len(queue) == 1):
        print(queue[0])
        break
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()
