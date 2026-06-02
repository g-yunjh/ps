def solution(n):
    ans = 0
    for i in range(n):
        if n % (i+1) == 0:
            ans += (i+1)
    return ans
            