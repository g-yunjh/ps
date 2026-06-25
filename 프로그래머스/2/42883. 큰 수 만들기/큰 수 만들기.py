def solution(number, k):
    st = []
    n = list(number)
    st.append(n[0])
    cnt = k
    i = 1
    while cnt > 0 and i < len(n):
        if len(st) > 0 and st[-1] < n[i]:
            st.pop()
            cnt -= 1
        else:
            st.append(n[i])
            i += 1
    if cnt > 0:
        st = st[:-cnt]
    if i < len(n):
        st.extend(n[i:])
    return "".join(st)
        