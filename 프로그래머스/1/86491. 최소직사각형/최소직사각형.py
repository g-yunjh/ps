def solution(s):
    ga = 0
    se = 0
    for i in range(len(s)):
        ga = max(ga, max(s[i][0], s[i][1]))
        se = max(se, min(s[i][0], s[i][1]))
        
    return ga * se
            