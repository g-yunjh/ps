def solution(n, t, m, p):
    txt = "0123456789ABCDEF"
    
    arr = "0"
    j = 1
    while len(arr) < t * m:
        i = j
        tmp = []
        while i > 0:
            tmp.append(txt[i % n])
            i //= n
        tmp.reverse()
        tmp = "".join(tmp)
        arr += tmp
        j += 1
    
    result = ""
    for i in range(len(arr)):
        if m == p:
            if (i+1) % m == 0 and (i+1-p) //m < t:
                result += arr[i]
        else:
            if (i+1) % m == p and (i+1-p) // m < t:
                result += arr[i]
    return result