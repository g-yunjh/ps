from functools import cmp_to_key

def solution(numbers):
    s = [str(n) for n in numbers]
    
    # 2. 커스텀 비교 함수 정의 (x+y 와 y+x 중 큰 것을 선택)
    def compare(x, y):
        if x + y > y + x:
            return -1  # x가 앞으로
        elif x + y < y + x:
            return 1   # y가 앞으로
        else:
            return 0
    
    s.sort(key=cmp_to_key(compare))
    
    answer = ''.join(s)
    answer = int(answer)
    answer = str(answer)
    
    return answer