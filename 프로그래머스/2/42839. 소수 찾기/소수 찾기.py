import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    num_set = set()
    
    # 1. 모든 숫자 조합 만들기 (1글자부터 n글자까지)
    for i in range(1, len(numbers) + 1):
        # itertools.permutations는 튜플을 반환하므로 합쳐서 숫자로 변환
        perms = itertools.permutations(list(numbers), i)
        for p in perms:
            num_set.add(int("".join(p)))
    
    # 2. 생성된 숫자 중 소수의 개수 세기
    answer = 0
    for n in num_set:
        if is_prime(n):
            answer += 1
            
    return answer