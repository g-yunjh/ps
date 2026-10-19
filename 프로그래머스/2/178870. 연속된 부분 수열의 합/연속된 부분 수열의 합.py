def solution(sequence, k):
    n = len(sequence)
    start = 0
    end = 0
    current_sum = sequence[0]
    
    min_len = float('inf')
    answer = []
    
    while end < n:
        if current_sum == k:
            current_len = end - start
            # 기존에 찾은 길이보다 더 짧은 구간을 발견한 경우에만 갱신
            if current_len < min_len:
                min_len = current_len
                answer = [start, end]
            
            # 다음 구간 탐색을 위해 start 이동
            current_sum -= sequence[start]
            start += 1
            
        elif current_sum < k:
            end += 1
            if end < n:
                current_sum += sequence[end]
                
        else: # current_sum > k
            current_sum -= sequence[start]
            start += 1
            
    return answer