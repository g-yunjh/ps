def solution(n):
    n = str(n)
    leng = len(n)
    ans = [0] * leng
    for i in range(leng):
        ans[leng - i - 1] = int(n[i])
    return ans
        