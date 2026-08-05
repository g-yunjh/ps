from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)
            
    path = []
    
    def dfs(now):
        while graph[now]:
            dfs(graph[now].pop())
        path.append(now)
        
    dfs("ICN")
    return path[::-1]