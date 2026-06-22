from itertools import permutations
import math

def is_prime(n):
    # 1과 그 이하의 수는 소수가 아님
    if n <= 1:
        return False
    
    # 2부터 n의 제곱근까지의 숫자만 확인
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False  # 나누어 떨어지면 소수가 아님
            
    return True  # 루프를 무사히 통과하면 소수

def solution(numbers):
    n = list(numbers)
    
    arr0 = []
    for i in range(1, len(n) + 1):
        tmp = permutations(n,i)
        for j in tmp:
            arr0 .append(int("".join(j)))
            
    arr1 = []
    for i in arr0:
        if is_prime(i) == True:
            arr1.append(i)
    arr1 = set(arr1)
    return len(arr1)