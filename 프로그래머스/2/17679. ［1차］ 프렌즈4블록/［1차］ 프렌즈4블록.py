def solution(m, n, board):
    d = [[] for i in range(n)]
    board.reverse()
    for i in range(m):
        for j in range(n):
            d[j].append(board[i][j])
    cnt = 0
    while True:
        arr = []
        for i in range(n-1):
            for j in range(m-1):
                if d[i][j] not in ['#', '.'] and d[i][j] == d[i][j+1] == d[i+1][j] == d[i+1][j+1]:
                    arr.append([i, j])
        if arr == []:
            return cnt
        for a in arr:
            d[a[0]][a[1]] = '#'
            d[a[0]][a[1] + 1] = '#'
            d[a[0] + 1][a[1]] = '#'
            d[a[0] + 1][a[1] + 1] = '#'
        arr = []
        for i in range(n):
            d[i] = [j for j in d[i] if j != '#']
            tmp = m - len(d[i])
            for j in range(tmp):
                d[i].append('.')    
            cnt += tmp 
            