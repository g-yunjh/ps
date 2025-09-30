import sys
import math
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
b, c = map(int, input().split())

ans = n # 일단 총감독관 한명씩 넣어놓기

for a in a_list:
    a -= b
    if (a > 0):
        ans += math.ceil(a/c)

print(ans)