def solution(numbers):
    stack = []
    ans = [-1] * len(numbers)
    
    for i in range(len(numbers)):
        # 스택에 있는 인덱스들과 비교하여 현재 값이 더 크면 그 인덱스의 정답을 갱신
        while stack and numbers[stack[-1]] < numbers[i]:
            ans[stack.pop()] = numbers[i]
        stack.append(i)
        
    return ans