def solution(s):
    st = []
    s = list(s)
    for i in s:
        if i == "(":
            st.append(1)
        elif st == []:
            return False
        else:
            st.pop()
    
    if st == []:
        return True
    else:
        return False