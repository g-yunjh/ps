def solution(n, s):
    if n > s:
        return [-1]
    arr = [s//n for i in range(n)]
    for i in range(s%n):
        arr[i] += 1
    arr.sort()
    return arr
    