def solution(info, edges):
    g = [[] for _ in range(len(info))]
    for u, v in edges:
        g[u].append(v)
    
    max_sheep = 0

    def dfs(curr, sheep, wolf, possible):
        nonlocal max_sheep
        
        if info[curr] == 0:
            sheep += 1
        else:
            wolf += 1
            
        if wolf >= sheep:
            return
        
        max_sheep = max(max_sheep, sheep)
        
        next_possible = possible.copy()
        next_possible.remove(curr)
        next_possible.extend(g[curr])
        
        for nxt in next_possible:
            dfs(nxt, sheep, wolf, next_possible)


    dfs(0, 0, 0, [0])
    
    return max_sheep