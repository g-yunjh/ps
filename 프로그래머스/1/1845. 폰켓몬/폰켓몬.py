def solution(nums):
    n = len(nums)
    k = len(set(nums))
    
    if k > n / 2:
        return n//2
    else:
        return k
    