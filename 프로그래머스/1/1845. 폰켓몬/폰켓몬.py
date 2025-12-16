def solution(nums):
    nums.sort()
    
    cnt = 0
    tmp = ''
    for i in nums:
        if (i != tmp):
            tmp = i
            cnt += 1

    if (cnt >= len(nums)/2):
        return len(nums)/2
    else:
        return cnt