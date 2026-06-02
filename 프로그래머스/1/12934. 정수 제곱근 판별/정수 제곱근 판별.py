def solution(n):
    tmp = n ** 0.5
    if int(tmp) == tmp:
        return (tmp + 1) ** 2
    else:
        return -1