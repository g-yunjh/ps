def solution(prices):
    n = len(prices)
    answer = [0] * n
    st = []
    
    for i in range(n):
        while st and prices[st[-1]] > prices[i]:
            j = st.pop()
            answer[j] = i - j
        st.append(i)
        
    while st:
        j = st.pop()
        answer[j] = n - 1 - j
        
    return answer