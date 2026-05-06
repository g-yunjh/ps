def gong(a,b):
    for i in range(1, b+1):
        tmp_a = a * i
        for j in range(1, a+1):
            tmp_b = b * j
            if tmp_a == tmp_b:
                return tmp_a

def solution(arr):
    tmp = gong(arr[0], arr[1])
    for i in range(2, len(arr)):
        tmp = gong(tmp, arr[i])
    
    return tmp