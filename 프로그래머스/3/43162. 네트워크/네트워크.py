def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def dfs(v):
        visited[v] = True
        for neighbor in range(n):
            if computers[v][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer