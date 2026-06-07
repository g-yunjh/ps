def solution(arr):
    st = []
    st.append(arr[0])
    
    for i in arr:
        if i != st[-1]:
            st.append(i)
    
    return st
            