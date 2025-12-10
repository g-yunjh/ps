import sys
from collections import deque
input = sys.stdin.readline
arr = deque()

# input
n = int(input())

# for
answer = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push_front":
        arr.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        arr.append(cmd[1])
    elif cmd[0] == "pop_front":
        if len(arr) == 0:
            answer.append(-1)
        else:
            answer.append(arr[0])
            arr.popleft()
    elif cmd[0] == "pop_back":
        if len(arr) == 0:
            answer.append(-1)
        else:
            answer.append(arr[-1])
            arr.pop()
    elif cmd[0] == "size":
        answer.append(len(arr))
    elif cmd[0] == "empty":
        if len(arr) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif cmd[0] == "front":
        if len(arr) == 0:
            answer.append(-1)
        else:
            answer.append(arr[0])
    elif cmd[0] == "back":
        if len(arr) == 0:
            answer.append(-1)
        else:
            answer.append(arr[-1])
    else:
        answer.append("error")

for i in answer:
    print(i)
