def solution(arr):
    st = []
    st.append(arr[0])
    for a in arr:
        if st[-1] != a:
            st.append(a)
    return st