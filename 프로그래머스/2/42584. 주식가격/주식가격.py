def solution(prices):
    answer = []
    
    # solution
    n = len(prices)
    # 1. 결과를 저장할 배열. 초기값은 0
    answer = [0] * n
    # 2. 가격 하락을 경험하지 않은 시점의 인덱스를 저장할 스택
    stack = []

    # prices 배열을 처음부터 끝까지 순회합니다. (O(n))
    for i in range(n):
        
        # 3. 가격 하락 체크:
        # 스택이 비어있지 않고, 현재 가격(prices[i])이
        # 스택 top의 가격(prices[stack[-1]])보다 작다면 (하락 발생)
        while stack and prices[i] < prices[stack[-1]]:
            
            # 가격이 떨어진 시점의 인덱스를 스택에서 꺼냅니다.
            top_index = stack.pop()
            
            # 가격이 유지된 기간을 계산하여 answer에 저장합니다.
            # 기간 = 현재 시간 i - 가격이 떨어진 top_index
            answer[top_index] = i - top_index
        
        # 4. 현재 인덱스를 스택에 추가합니다. (다음 하락 체크 대상이 됨)
        stack.append(i)

    # 5. 모든 순회가 끝난 후, 스택에 남아있는 인덱스 처리
    # 스택에 남아있는 인덱스들은 배열의 끝까지 가격이 떨어지지 않은 시점들입니다.
    # 즉, 마지막 시점 (n-1)까지 유지된 것입니다.
    while stack:
        final_index = stack.pop()
        # 가격이 유지된 기간 = 배열의 마지막 인덱스(n-1) - 해당 시점 인덱스
        answer[final_index] = (n - 1) - final_index
        
    return answer