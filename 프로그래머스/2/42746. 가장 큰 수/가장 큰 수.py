def solution(numbers):
    # 1. 모든 숫자를 문자열로 변환 (정렬 비교를 위해)
    str_numbers = list(map(str, numbers))
    
    # 2. 커스텀 정렬 (람다 함수 이용)
    # 두 문자열 a와 b를 비교할 때, (a + b)와 (b + a)의 크기를 비교하여 정렬합니다.
    # key=lambda x: x * 3 : 
    #   파이썬에서는 key에 문자열을 전달하면, 문자열을 기준으로 비교합니다.
    #   '3' * 3 = '333', '30' * 3 = '303030' 처럼 문자열을 반복하여
    #   길이가 다른 숫자(예: 3과 30)를 공평하게 비교할 수 있게 합니다.
    #   (numbers 원소의 최대값이 1000이므로 3자리까지 반복하면 충분합니다.)
    
    str_numbers.sort(key=lambda x: x * 3, reverse=True)
    
    # 3. 정렬된 문자열 리스트를 하나의 문자열로 합침
    answer = "".join(str_numbers)
    
    # 4. 특수 예외 처리: [0, 0, 0]과 같이 모두 0인 경우
    # 결과가 '000'이 아닌 '0'이 되도록 처리합니다.
    if answer[0] == '0':
        return '0'
        
    return answer