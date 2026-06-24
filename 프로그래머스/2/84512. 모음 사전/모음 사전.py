from itertools import product
def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    dic = []
    for i in range(1,6):
        tmp = product(arr, repeat = i)
        for j in tmp:
            dic.append("".join(j))
    dic.sort()
    return dic.index(word) + 1