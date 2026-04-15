import sys
input = sys.stdin.readline

n = int(input())

score = [0] * 301
for i in range(1, n + 1):
    score[i] = int(input())

dp = [0] * 301

# 1. 초기값 설정 (1~3번째 계단)
dp[1] = score[1]
if n >= 2:
    dp[2] = score[1] + score[2]
if n >= 3:
    # 3번째 계단은 (1+3번째) 또는 (2+3번째) 중 큰 것
    dp[3] = max(score[1] + score[3], score[2] + score[3])

# 2. 바텀업 반복문 (4번째 계단부터 끝까지)
for i in range(4, n + 1):
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

print(dp[n])