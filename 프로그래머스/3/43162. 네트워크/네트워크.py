def solution(n, computers):
    answer = 0
    visited = [False] * n  # 방문 여부를 체크할 리스트

    def dfs(v):
        visited[v] = True  # 현재 컴퓨터 방문 처리
        for neighbor in range(n):
            # 연결되어 있고 + 아직 방문하지 않은 컴퓨터라면 탐색 계속
            if computers[v][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    for i in range(n):
        if not visited[i]:  # 아직 어떤 네트워크에도 속하지 않은 컴퓨터 발견!
            dfs(i)          # 이 컴퓨터와 연결된 모든 노드를 방문 처리
            answer += 1     # 네트워크 개수 증가
            
    return answer