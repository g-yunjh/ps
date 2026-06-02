def solution(n):
    n = str(n)
    n = list(n)
    n.sort(reverse = True)
    ans = ""
    for i in n:
        ans += i
    return int(ans)