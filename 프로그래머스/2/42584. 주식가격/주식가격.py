def solution(prices):
    arr = []
    arr.append([prices[0], 0])
    ans = [0] * len(prices)
    
    for i in range(1, len(prices)):
        while len(arr) > 0:
            if prices[i] < arr[-1][0]:
                ans[arr[-1][1]] = i - arr[-1][1]
                arr.pop()
            else:
                break
        arr.append([prices[i], i])
    
    for i in arr:
        ans[i[1]] = len(prices) - i[1] - 1
    
    return ans
        
        
        