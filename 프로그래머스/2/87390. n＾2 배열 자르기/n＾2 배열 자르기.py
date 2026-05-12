def solution(n, left, right):
    left_row = left // n
    right_row = right // n
    left_col = left % n
    right_col = right % n
    
    arr = []
    for i in range(left_row, right_row + 1):
        for j in range(i+1):
            arr.append(i+1)
        for j in range(i + 1, n):
            arr.append(j+1)
    return arr[left_col:len(arr) - n + right_col+1]
    
    