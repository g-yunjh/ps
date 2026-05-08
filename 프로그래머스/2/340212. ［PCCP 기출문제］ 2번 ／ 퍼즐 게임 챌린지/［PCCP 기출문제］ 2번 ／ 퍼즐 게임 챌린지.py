def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        total_time = times[0]
        
        for i in range(1, len(diffs)):
            if diffs[i] > mid:
                total_time += (diffs[i] - mid) * (times[i] + times[i-1]) + times[i]
            else:
                total_time += times[i]
            
            if total_time > limit:
                break
        
        if total_time <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer