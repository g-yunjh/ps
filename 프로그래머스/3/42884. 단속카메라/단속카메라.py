def solution(routes):
    routes.sort(key = lambda x: x[1])
    q = []
    q.append(routes[0][1])
    ans = 1
    for i in range(1, len(routes)):
        if q[0] >= routes[i][0]:
            q.append(routes[i][1])
        else:
            ans += 1
            q = []
            q.append(routes[i][1])
            
    return ans