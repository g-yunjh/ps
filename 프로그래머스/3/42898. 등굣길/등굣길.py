def solution(m, n, puddles):
    MOD = 1000000007

    puddles = {(y-1, x-1) for x, y in puddles}

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if (i, j) in puddles:
                dp[i][j] = 0
                continue

            if i == 0 and j == 0:
                continue

            up = dp[i-1][j] if i > 0 else 0
            left = dp[i][j-1] if j > 0 else 0

            dp[i][j] = (up + left) % MOD

    return dp[-1][-1]