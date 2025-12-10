"""
- 여러 개의 익은 토마토가 동시에 영향을 주므로 BFS(너비 우선 탐색)를 사용한다.
- 처음에 익은 토마토(1)의 좌표를 모두 큐에 넣고, 안 익은 토마토(0)의 개수를 센다.
- 큐에서 하나씩 꺼내며 상하좌우를 확인해 안 익은 토마토를 익히고, 날짜(day)를 +1 하여 큐에 넣는다.
- BFS가 끝났을 때 안 익은 토마토가 남아 있으면 -1, 그렇지 않으면 마지막 day를 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dq = deque()
unripe = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            dq.append((i, j, 0))
        elif box[i][j] == 0:
            unripe += 1

if unripe == 0:
    print(0)
    sys.exit(0)

dirs = [(-1,0), (1,0), (0,-1), (0,1)]
max_day = 0

while dq:
    x, y, d = dq.popleft()
    max_day = max(max_day, d)
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = 1
            unripe -= 1
            dq.append((nx, ny, d+1))

print(-1 if unripe > 0 else max_day)
