from itertools import permutations

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def solution(numbers):
    nums = set()
    for i in range(1, len(numbers) + 1):
        # 1글자부터 n글자까지 모든 순열 생성
        for p in permutations(numbers, i):
            nums.add(int(''.join(p)))
    
    count = 0
    for n in nums:
        if is_prime(n): count += 1
    return count