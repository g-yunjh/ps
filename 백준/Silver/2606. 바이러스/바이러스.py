import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # the number of computers
m = int(input()) # the number of edges

# 인접 리스트
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)    # 무방향 그래프

# 방문 배열
visited = [False] * (n + 1)

# BFS로 1번에서 시작해 감염 확산
q = deque([1])
visited[1] = True
infected = 0  # 1번을 제외한 감염 수를 셀 것

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            infected += 1   # 새로 방문 = 새로 감염
            q.append(nxt)

print(infected)
