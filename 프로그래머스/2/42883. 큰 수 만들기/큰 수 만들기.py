def solution(number, k):
    st = []
    
    for num in number:
        # 스택에 값이 있고, 지울 수 있는 횟수(k)가 남아있으며,
        # 스택의 마지막 값이 현재 들어올 숫자(num)보다 작을 동안 반복해서 빼냅니다.
        while st and k > 0 and st[-1] < num:
            st.pop()
            k -= 1
        
        # 조건을 만족하게 빼낸 후 (또는 뺄 필요가 없다면) 현재 숫자를 스택에 넣습니다.
        st.append(num)
        
    # 만약 k를 다 소진하지 못하고 반복문이 끝났다면 (예: "9876"처럼 이미 내림차순인 경우)
    # 뒤에서부터 남은 k개만큼 잘라냅니다.
    if k > 0:
        st = st[:-k]
        
    # 리스트를 문자열로 합쳐서 반환합니다.
    return "".join(st)