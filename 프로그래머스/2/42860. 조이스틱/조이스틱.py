def solution(name):
    up_down_moves = 0
    for char in name:
        up_down_moves += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
    n = len(name)
    min_left_right = n - 1  
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        path1 = min_left_right
        path2 = i * 2 + (n - next_idx)
        path3 = (n - next_idx) * 2 + i
        
        min_left_right = min(path1, path2, path3)
        
    return up_down_moves + min_left_right