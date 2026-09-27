def solution(dirs):
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    
    x, y = 0, 0
    visited = set()
    
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        
        # 좌표평면 경계(-5 ~ 5)를 벗어나는 경우 무시
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
        
        visited.add((x, y, nx, ny))
        visited.add((nx, ny, x, y))
        
        x, y = nx, ny
        
    return len(visited) // 2