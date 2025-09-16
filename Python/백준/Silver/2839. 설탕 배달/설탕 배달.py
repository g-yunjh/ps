import sys
input = sys.stdin.readline

n = int(input())

ans = []

# 5킬로그램 봉지를 기준으로 하나씩 늘려가면서
for i in range((n // 5) + 1):
    tmp = n
    tmp -= i*5
    if tmp % 3 == 0:
        ans.append(tmp//3 + i)

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
