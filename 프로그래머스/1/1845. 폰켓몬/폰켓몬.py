def solution(nums):
    choose = len(nums) // 2
    kinds = len(set(nums))
    return min(choose, kinds)