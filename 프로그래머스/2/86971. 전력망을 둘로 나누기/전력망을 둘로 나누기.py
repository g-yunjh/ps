from collections import deque

def bfs(start, n, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 1  # 연결된 송전탑 개수
    
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    answer = n  # 최댓값으로 초기화 (차이의 최댓값은 n을 넘지 않음)
    
    # 1. 전선을 하나씩 끊어보며 완전탐색
    for i in range(len(wires)):
        # 그래프 초기화 (1번부터 n번까지 사용하므로 n+1 크기)
        graph = [[] for _ in range(n + 1)]
        
        # i번째 전선을 제외하고 그래프 구축
        for j, wire in enumerate(wires):
            if i == j:
                continue
            v1, v2 = wire
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        # 2. 끊어진 상태에서 한쪽 전력망의 송전탑 개수 파악
        visited = [False] * (n + 1)
        # 끊어진 전선의 한쪽 끝점인 wires[i][0]에서 탐색 시작
        v1_count = bfs(wires[i][0], n, graph, visited)
        
        # 3. 반대편 전력망 개수 계산 및 차이의 최솟값 갱신
        v2_count = n - v1_count
        diff = abs(v1_count - v2_count)
        
        answer = min(answer, diff)
        
    return answer