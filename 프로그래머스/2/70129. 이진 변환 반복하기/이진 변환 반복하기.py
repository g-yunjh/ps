def solution(s):
    cnt = 0
    ans = 0
    while  s != "1":
        tmp = 0
        for i in range(len(s)):
            if s[i] == "0":
                tmp += 1
        s = format(len(s) - tmp, 'b')
        cnt += tmp
        ans += 1
    return [ans, cnt]