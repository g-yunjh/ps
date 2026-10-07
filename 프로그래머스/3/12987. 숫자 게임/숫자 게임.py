def solution(A, B):
    a = sorted(A)
    b = sorted(B)
    
    ans = 0
    j = 0
    for i in range(len(a)):
        while j < len(b):
            if a[i] < b[j]:
                ans += 1
                j += 1
                break
            j += 1
    return ans
    