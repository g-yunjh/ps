def solution(prices):
    st = []
    ans = [0] * len(prices)
    
    for i in range(len(prices)):
        while st and st[-1][0] > prices[i]:
            ans[st[-1][1]] = i - st[-1][1]
            st.pop()
        st.append([prices[i], i])
        
    for i in range(len(ans)):
        if ans[i] == 0:
            ans[i] = len(ans) - i - 1
    return ans
            