def solution(n):
    answer = 0
    
    a = n+1
    b = str(bin(n)).count('1')
    while True:
        if (str(bin(a)).count('1') == b):
            answer = a
            break
        else:
            a += 1
    
    return answer