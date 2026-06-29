def solution(n, costs):
    costs.sort(key = lambda x: x[2], reverse = True)
    st = []
    st.append(costs[-1][0])
    st.append(costs[-1][1])
    cnt = costs[-1][2]
    costs.pop()
    i = 1
    while True:
        if costs[-i][0] in st and costs[-i][1] not in st:
            st.append(costs[-i][1])
            cnt += costs[-i][2]
            i = 1
        elif costs[-i][0] not in st and costs[-i][1] in st:
            st.append(costs[-i][0])
            cnt += costs[-i][2]
            i = 1
        else:
            i += 1
            if i > len(costs):
                break
    return cnt
    