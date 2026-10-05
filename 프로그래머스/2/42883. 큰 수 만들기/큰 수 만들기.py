def solution(number, k):
    st = [number[0]]
    i = 1
    while k > 0 and i < len(number):
        while k > 0:
            if len(st) == 0 or int(st[-1]) >= int(number[i]):
                st.append(number[i])
                i += 1
                break
            else:
                st.pop()
                k -= 1
    if i < len(number):
        for i in range(i, len(number)):
            st.append(number[i])
    if k > 0:
        for i in range(k):
            st.pop()
    return "".join(st)
        