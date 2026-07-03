def solution(money):
    # 첫집을 터는 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(dp1[0], money[1])
    for i in range(2,len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    # 첫집을 무조건 털지 않는 경우
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = max(dp2[0], money[1])
    for i in range(2,len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(dp1[-2], dp2[-1])