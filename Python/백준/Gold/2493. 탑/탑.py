import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = []              # (height, index)
res = [0] * n

for i in range(n):
    h = arr[i]
    while stack and stack[-1][0] <= h:
        stack.pop()
    res[i] = stack[-1][1] if stack else 0
    stack.append((h, i + 1))   # 인덱스는 1-based

print(*res)
