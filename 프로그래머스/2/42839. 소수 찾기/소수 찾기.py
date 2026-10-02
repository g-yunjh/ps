from itertools import permutations
from math import sqrt

def solution(numbers):
    arr1 = list(numbers)
    arr2 = []
    for i in range(len(numbers)):
        arr2.append(list(permutations(arr1, i + 1)))
    arr3 = []
    for i in arr2:
        for j in i:
            arr3.append(int("".join(j)))
    arr3 = list(set(arr3))
    
    # 소수인지 확인하기
    arr4 = []
    for i in arr3:
        if i > 1:
            n = True
            for j in range(2, int(sqrt(i)) + 1):
                if i % j  == 0:
                    n = False
            if n == True:
                arr4.append(i)
    return len(arr4)
