def solution(name):
    up_down = 0
    for char in name:
        up_down += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    n = len(name)
    left_right = n - 1
    
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        left_right = min(left_right, i * 2 + n - next_idx, (n - next_idx) * 2 + i)
        
    return up_down + left_right