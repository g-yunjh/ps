def solution(s):
    st = []
    for i in s:
        if (i == "("):
            st.append(1)
        elif (not st):
            return False
        else:
            st.pop()
    if (st):
        return False
    else:
        return True
        