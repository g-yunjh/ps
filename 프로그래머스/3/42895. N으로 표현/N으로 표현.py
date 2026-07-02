def solution(N, number):
    if N == number:
        return 1
        
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
    # 1개부터 8개까지 N을 사용하는 경우를 계산
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        
        if number in dp[i]:
            return i
            
    # N을 8번 이하로 사용해서 표현할 수 없는 경우
    return -1
