import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

# input
n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    queue.append(i + 1)

count = 0
for i in arr:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        elif queue.index(i) <= len(queue)/2:
            queue.append(queue[0])
            queue.popleft()
            count += 1
        else:
            queue.insert(0, queue[-1])
            queue.pop()
            count += 1

print(count)
