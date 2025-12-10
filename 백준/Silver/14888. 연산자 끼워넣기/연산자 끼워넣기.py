import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
plus, minus, mul, divi = map(int, input().split())

MAX = -10**18
MIN =  10**18

def tzero_div(a, b):
    # C++14와 동일: 0을 향해 버림
    return int(a / b)

def dfs(idx, cur, p, m, mu, d):
    global MAX, MIN
    if idx == N:
        if cur > MAX: MAX = cur
        if cur < MIN: MIN = cur
        return
    x = A[idx]
    if p:
        dfs(idx + 1, cur + x, p - 1, m, mu, d)
    if m:
        dfs(idx + 1, cur - x, p, m - 1, mu, d)
    if mu:
        dfs(idx + 1, cur * x, p, m, mu - 1, d)
    if d:
        dfs(idx + 1, tzero_div(cur, x), p, m, mu, d - 1)

dfs(1, A[0], plus, minus, mul, divi)
print(MAX)
print(MIN)
