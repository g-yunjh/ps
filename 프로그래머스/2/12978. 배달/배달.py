import heapq

def solution(N, road, K):
    # 1. 인접 리스트 만들기
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    # 2. 거리 배열 초기화
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    
    
    # 3. 우선순위 큐 준비 (거리, 마을번호)
    queue = [(0, 1)]
    
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        
        # 이미 처리된 적 있는 거리라면 무시
        if dist[current_node] < current_dist:
            continue
            
        # 주변 마을 확인
        for next_node, weight in graph[current_node]:
            new_dist = current_dist + weight
            
            # 더 짧은 경로를 발견했다면?
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(queue, (new_dist, next_node))
                
    # 4. K 이하인 마을 개수 세기
    return len([d for d in dist if d <= K])