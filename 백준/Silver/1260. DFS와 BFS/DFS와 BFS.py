from collections import deque

n, m, v = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호 작은 것부터 방문
for i in range(1, n+1):
    graph[i].sort()

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

def dfs(v):
    dfs_visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    bfs_visited[v] = True
    
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        
        for i in graph[cur]:
            if not bfs_visited[i]:
                bfs_visited[i] = True
                queue.append(i)

dfs(v)
print()
bfs(v)