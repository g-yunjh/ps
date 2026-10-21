def solution(s):
    st = []
    for i in s:
        if i == "(":
            st.append(1)
        else:
            if len(st) == 0:
                return False
            else:
                st.pop()
    if len(st) == 0:
        return True
    else:
        return False
            