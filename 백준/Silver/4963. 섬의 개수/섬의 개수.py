import sys
from collections import deque

input = sys.stdin.readline

dirs = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)]

def bfs(start_r, start_c, h, w, graph):
    queue = deque([(start_r, start_c)])
    graph[start_r][start_c] = 0

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and graph[nr][nc] == 1:
                graph[nr][nc] = 0
                queue.append((nr, nc))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    count = 0

    for r in range(h):
        for c in range(w):
            if graph[r][c] == 1:
                count += 1
                bfs(r, c, h, w, graph)

    print(count)