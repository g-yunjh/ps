import math

def solution(n, k):
    # k진수 변환
    arr1 = []
    while (n > 0):
        if (n % k == 0):
            arr1.append("0")
        else:
            arr1.append(str(n%k))
            n -= (n % k)
        n //= k
    arr1.reverse()
    tmp = "".join(arr1)
    
    # 0을 기준으로 자르기
    arr2 = list(tmp.split("0"))
    
    # 소수인지 확인하기
    cnt = 0
    for i in arr2:
        if (i != ""):
            i = int(i)
            if i < 2:
                continue
            else:
                t_c = 0
                for j in range(2, int(math.sqrt(i))+1):
                    if i % j == 0:
                        t_c += 1
                if t_c == 0:
                    cnt += 1
                
    return cnt
    
    