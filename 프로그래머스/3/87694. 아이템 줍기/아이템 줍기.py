from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]

    # 1. 모든 좌표를 2배로 하여 사각형을 채운다.
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

    # 2. 사각형 내부 제거
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0

    # 시작점과 도착점도 2배
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    visited = [[False] * 102 for _ in range(102)]
    q = deque()
    q.append((characterX, characterY, 0))
    visited[characterX][characterY] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, dist = q.popleft()

        if x == itemX and y == itemY:
            return dist // 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 102 and 0 <= ny < 102:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))