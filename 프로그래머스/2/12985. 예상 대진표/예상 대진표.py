def solution(n,a,b):
    ans = 0
    while a!= b:
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        ans += 1
    return ans