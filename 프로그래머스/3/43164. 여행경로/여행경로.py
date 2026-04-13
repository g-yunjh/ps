def solution(o_t):
    # 1. 알파벳 순으로 정렬 (경로가 여러 개일 경우 사전 순 앞서는 것 선택)
    tickets = sorted(o_t, key=lambda x: x[1])
    visited = [False] * len(tickets)
    
    def dfs(current, path):
        # 모든 티켓을 다 사용했다면 성공!
        if len(path) == len(tickets) + 1:
            return path
        
        for i, ticket in enumerate(tickets):
            # 출발지가 일치하고 아직 사용하지 않은 티켓이라면
            if ticket[0] == current and not visited[i]:
                visited[i] = True
                # 다음 도시로 이동 시도
                result = dfs(ticket[1], path + [ticket[1]])
                if result: return result # 경로를 찾았다면 즉시 반환
                
                # 만약 이 경로가 막다른 길이라면 티켓 사용 취소 (백트래킹)
                visited[i] = False
        
        return None

    return dfs("ICN", ["ICN"])