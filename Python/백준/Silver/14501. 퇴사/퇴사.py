import sys
input = sys.stdin.readline

n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)

for i in range(1, n+1):
    ti, pi = map(int, input().split())
    t[i] = ti
    p[i] = pi

dp = [0] * (n+2)  # n+1일까지 보기 위해 n+2 크기로 준비

# 뒤에서부터 거꾸로 채움
for i in range(n, 0, -1):
    if i + t[i] <= n + 1:  # 상담 가능
        dp[i] = max(p[i] + dp[i + t[i]], dp[i+1])
    else:  # 상담 불가능
        dp[i] = dp[i+1]

print(dp[1])
